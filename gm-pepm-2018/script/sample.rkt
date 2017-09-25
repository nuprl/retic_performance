#lang racket/base

;; Create and collect sampled data

(require racket/contract)
(provide
  (contract-out
    [sample-info?
     (-> any/c boolean?)]
))

(require
  "benchmark-info.rkt"
  "performance-info.rkt"
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

(struct sample-info (
  ;; what should be here? how to connect to benchmark-info?
) #:transparent )

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

(define big-random
  (let ([LIMIT 4294967087])
    (lambda (k)
      (if (<= k LIMIT)
        (random k)
        (let* ([p0 (/ LIMIT k)] ;; probability of choosing a bin with LIMIT items
               [bin+prob*
                ;; split big number into chunks we can draw from,
                ;;  save "probability of picking from this bin" with each ... sort of
                (let loop ([num-left k] [i 1])
                  (if (<= num-left LIMIT)
                    (list (cons num-left 1))
                    (cons (cons LIMIT (* i p0)) (loop (- num-left LIMIT) (add1 i)))))]
               ;;[_v (printf "bins ~a~n" (for/list ([x (in-list bin+prob*)]) (cons (car x) (exact->inexact (cdr x)))))]
               [r (random)])
          (for/first ([bp (in-list bin+prob*)]
                      #:when (<= r (cdr bp)))
            (car bp)))))))

(define (num-configurations->sample-size nc rate)
  (let ([nm (log2 nc)])
    (* rate nm)))

(define (benchmark-info->sampler bm)
  (define nc (benchmark->num-configurations bm))
  (λ ()
    (configuration->string (natural->configuration bm (big-random nc)))))

(define (max-configuration->sampler cfg)
  (λ ()
    (configuration->string
      (for/list ([mx (in-list cfg)])
        (random mx)))))

;; 2017-04-21:
;; The old algorithm for picking samples was:
;; -- count num. configurations
;; -- pick random natural numbers
;; -- convert chosen naturals to configurations
;; This algorithm is too slow on large benchmarks. New algorithm:
;; -- get max configuration
;; -- for all digits in configuration, pick random digit in range
;; More direct, should scale the same way saving configurations on disk scales.
(define (generate-samples bm-name)
  (define bm (->benchmark-info bm-name))
  (define random-configuration ;; (-> String)
    (max-configuration->sampler (benchmark->max-configuration bm)))
  (define o (get-output-directory bm-name))
  (define sample-size
    (num-configurations->sample-size (benchmark->num-configurations bm) (*sample-rate*)))
  (debug "Storing output in ~a/" o)
  (for ([i (in-range (*num-trials*))])
    (with-output-to-file (build-path o (format "samples.txt~a" i))
      #:exists 'replace
      (lambda ()
        (for ([s (in-range sample-size)])
          (displayln (random-configuration)))))))

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
      (define s1 (benchmark-info->sampler bm))
      (define s2 (max-configuration->sampler (benchmark->max-configuration bm)))
      (check-true
        (for/and ([i (in-range 200)])
          (and (configuration<? (string->configuration (s1)) mc)
               (configuration<? (string->configuration (s2)) mc))))
      (void))

    (check->sample 'Espionage)
    (check->sample 'futen)
  )

  (test-case "big-random"
    (check-pred big-random 4)
    (check-pred big-random 4294967087)
    (check-pred big-random 4294967088)
    (check-pred big-random 8000000000)
    (check-pred big-random 13000000000))

)

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

