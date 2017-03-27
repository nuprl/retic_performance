#lang racket/base

(require
  "benchmark-info.rkt"
  "performance-info.rkt" ;; TODO remove this import
  "util.rkt"
  racket/set
  (only-in racket/list
    make-list))

(module+ test
  (require rackunit))

;; =============================================================================

(define *sample-rate* (make-parameter 10))
(define *num-trials* (make-parameter 5))
(define *output* (make-parameter #f))
(define *verbose* (make-parameter #t))

(define (debug msg . arg*)
  (when (*verbose*)
    (printf "[DEBUG] ")
    (apply printf msg arg*)
    (newline)))

;; -----------------------------------------------------------------------------

(define (parse-int v field-name)
  (let ([s (string->number v)])
    (if (and s (exact-integer? s) (positive? s))
      s
      (raise-arguments-error 'sample "expected positive integer" field-name v))))

(define (get-output-directory bm-name)
  (define dirname (or (*output*) (format "~a-sample" bm-name)))
  (ensure-directory dirname)
  dirname)

(define (make-sample-index** population-size sample-size trials)
  (for/list ([_i (in-range trials)])
    (let loop ([acc (set)])
      (if (= sample-size (set-count acc))
        acc
        (loop (set-add acc (random population-size)))))))

(define (num-configurations->sample-size nc rate)
  (let ([nm (log2 nc)])
    (* rate nm)))

(define (performance-info->sample* pi rate trials)
  (define nc (num-configurations pi))
  (define sample-size (num-configurations->sample-size nc rate))
  (define index-to-sample*
    (make-sample-index** nc sample-size trials))
  (with-input-from-file (performance-info-src pi)
    (lambda ()
      (for/fold ([c** (make-list trials '())])
                ([ln (in-lines)]
                 [i (in-naturals)])
        (if (for/or ([i* (in-list index-to-sample*)])
              (set-member? i* i))
          (let ([cfg (line->configuration-string ln)])
            (for/list ([c* (in-list c**)]
                       [i* (in-list index-to-sample*)])
              (if (set-member? i* i)
                (cons cfg c*)
                c*)))
          c**)))))

(define (benchmark-info->sample* bm sample-rate num-trials)
  (define nc (benchmark->num-configurations bm))
  (define sample-size (num-configurations->sample-size nc sample-rate))
  (define index-to-sample*
    (make-sample-index** nc sample-size num-trials))
  (for/list ([i* (in-list index-to-sample*)])
    (for/list ([i (in-set i*)])
      (configuration->string (natural->configuration bm i)))))

(define (generate-samples bm-name)
  (define bm (->benchmark-info bm-name))
  (define sample*
    (cond
     [(benchmark->karst-data bm)
      (let ([pi (benchmark->performance-info bm)])
        (performance-info->sample* pi (*sample-rate*) (*num-trials*)))]
     [else
      (benchmark-info->sample* bm (*sample-rate*) (*num-trials*))]))
  (define o (get-output-directory bm-name))
  (debug "Storing output in ~a/" o)
  (for ([s (in-list sample*)]
        [i (in-naturals)])
    (with-output-to-file (build-path o (format "~a-samples.txt~a" bm-name i))
      #:exists 'replace
      (lambda ()
        (for-each displayln  s)))))

;; =============================================================================

(module+ main
  (require racket/cmdline)
  (command-line
   #:program "sample"
   #:once-each
   [("-r" "--rate") sp "sample rate" (*sample-rate* (parse-int sp "--rate"))]
   [("-t" "--trials") tp "num. trials" (*num-trials* (parse-int tp "--trials"))]
   [("-o" "--output") op "file (or directory) to store output" (*output* op)]
   [("-q" "--quiet") "run quietly" (*verbose* #f)]
   #:args benchmark-name*
   (cond
    [(null? benchmark-name*)
     (printf "usage: raco rp-sample <benchmark-name> ...~n")]
    [(null? (cdr benchmark-name*))
     (generate-samples (car benchmark-name*))]
    [else
     (for ((bm (in-list benchmark-name*)))
       (with-handlers ((exn:fail? (lambda (e) (printf "Error processing ~a, run 'raco rp-sample ~a' to debug~n" bm bm))))
         (generate-samples bm)))])))

;; =============================================================================

(module+ test
  (require rackunit rackunit-abbrevs)

  (test-case "parse-int"
    (define dummy-name "yolo")
    (check-equal? (parse-int "4" dummy-name) 4)
    (check-exn* exn:fail:contract? parse-int
      ["" dummy-name]
      ["3.14" dummy-name]
      ["()" dummy-name]
      ["hello" dummy-name]))

  (test-case "make-sample-index**"
    (define (random-check-sample-index** pop-size samp-size trials)
      (let ([i** (make-sample-index** pop-size samp-size trials)])
        (check-equal? (length i**) trials)
        (for ([i* (in-list i**)])
          (check-equal? (set-count i*) samp-size)
          (check-true (for/and ([i (in-set (car i**))]) (<= 0 i (- pop-size 1)))))))
      (random-check-sample-index** 50 5 0)
      (random-check-sample-index** 50 5 1)
      (random-check-sample-index** 100 9 3)
      (void))

  (test-case "num-configurations->sample-size"
    (check-apply* num-configurations->sample-size
     [2 1
      ==> 1]
     [1024 1
      ==> 10]
     [2048 1
      ==> 11]
     [2048 2
      ==> 22]
     [2048 10
      ==> 110]))

  (test-case "->sample*"
    (define (check->sample bm-name)
      (define bm (->benchmark-info bm-name))
      (define pi (benchmark->performance-info bm))
      (define sample-rate 10)
      (define num-trials 2)
      (define mc (benchmark->max-configuration bm))
      (define nc (benchmark->num-configurations bm))
      (define sample-size (num-configurations->sample-size nc sample-rate))
      (define s1 (benchmark-info->sample* bm sample-rate num-trials))
      (define s2 (performance-info->sample* pi sample-rate num-trials))
      (check-equal? (length s1) (length s2))
      (check-equal? (length s2) num-trials)
      (check-true
        (for/and ([b* (in-list s1)]
                  [p* (in-list s2)])
          (= (length b*) (set-count (list->set b*))
             (length p*) (set-count (list->set p*))
             sample-size)))
      (check-true
        (for/and ([b* (in-list s1)]
                  [p* (in-list s2)])
          (for/and ([b (in-list b*)]
                    [p (in-list p*)])
            (and (configuration<? (string->configuration b) mc)
                 (configuration<? (string->configuration p) mc)))))
      (void))

    (check->sample 'Espionage)
    (check->sample 'futen)
  )

)
