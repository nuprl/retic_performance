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

(define (performance-info->sample* pi rate trials)
  (define nc (num-configurations pi))
  (define sample-size
    (let ([nm (log2 nc)])
      (* rate nm)))
  (define index-to-sample*
    (for/list ([_i (in-range trials)])
      (let loop ([acc (set)])
        (if (= sample-size (set-count acc))
          acc
          (loop (set-add acc (random nc)))))))
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

(define (generate-samples bm-name)
  (define bm (->benchmark-info bm-name))
  (define o (get-output-directory bm-name))
  (define pi (benchmark->performance-info bm))
  (debug "Storing output in ~a/" o)
  (define sample* (performance-info->sample* pi (*sample-rate*) (*num-trials*)))
  (for ([s (in-list sample*)]
        [i (in-naturals)])
    (with-output-to-file (build-path o (format "~a-samples.txt~a" bm-name i))
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
   #:args (benchmark-name)
   (generate-samples benchmark-name)))
