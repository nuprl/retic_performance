#lang racket/base

;; For making graphs

(provide
  render-overhead-plot*
  ;; (-> (listof benchmark-info?) pict?)

  render-exact-runtime-plot*
  ;; (-> (listof benchmark-info?) pict?)
)

(require
  "benchmark-info.rkt"
  "performance-info.rkt"
  "plot.rkt"
  "util.rkt"
  pict
  with-cache
  (only-in racket/math
    exact-floor))

;; =============================================================================

(define OVERHEADS-WIDTH 600)
(define OVERHEADS-HEIGHT 1000)
(define OVERHEADS-HSPACE 30)
(define OVERHEADS-VSPACE 10)
(define NUM-COLUMNS 3)

;; -----------------------------------------------------------------------------

(define (render-overhead-plot* bm*)
  (render-benchmark* bm* "overhead" overhead-plot))

(define (render-exact-runtime-plot* bm*)
  (render-benchmark* bm* "exact-runtime" exact-runtime-plot #t))

(define (render-benchmark* bm* descr render-one [freeze? #f])
  (define num-pict (length bm*))
  (define p*
    (parameterize ([*OVERHEAD-PLOT-WIDTH* (exact-floor (/ (- OVERHEADS-WIDTH OVERHEADS-HSPACE) NUM-COLUMNS))]
                   [*OVERHEAD-PLOT-HEIGHT* (exact-floor (/ (+ OVERHEADS-HEIGHT OVERHEADS-VSPACE) num-pict))]
                   [*OVERHEAD-SHOW-RATIO* #f]
                   [*OVERHEAD-FREEZE-BODY* freeze?]
                   [*LEGEND-VSPACE* 2]
                   [*FONT-SIZE* 8]
                   [*current-cache-directory* (build-path (current-directory) "with-cache")]
                   [*current-cache-keys* (list (λ () (list OVERHEADS-WIDTH OVERHEADS-HEIGHT OVERHEADS-VSPACE OVERHEADS-HSPACE)))])
      (filter values
        (for/list ([bm (in-list bm*)])
          (with-cache (cachefile (format "~a-~a.rktd" descr (benchmark->name bm)))
            (λ ()
              (collect-garbage 'major)
              (render-one (benchmark->performance-info bm))))))))
  (define col*
    (map (λ (p*) (apply vl-append OVERHEADS-VSPACE p*))
         (columnize p* NUM-COLUMNS)))
  (apply ht-append OVERHEADS-HSPACE col*))

;; =============================================================================

(module+ test
  (require rackunit)

  (test-case ""
  )
)

;(module+ main
;  
;
;)
