#lang racket/base

;; For making graphs

(provide
  render-overhead-plot*
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
  (define bm-name* (map benchmark->name bm*))
  (with-cache (cachefile "overhead-plot.rktd")
    #:keys (list (λ () (list* OVERHEADS-WIDTH OVERHEADS-HEIGHT OVERHEADS-VSPACE OVERHEADS-HSPACE bm-name*)))
    #:use-cache? #f
    (λ ()
      (define pi*
        (for/list ([bm (in-list bm*)])
          ;; TODO don't hide errors
          (with-handlers ([exn:fail? (λ (e) (printf "No performance-info for ~a, skipping" (benchmark->name bm)))])
            (benchmark->performance-info bm))))
      (define num-pict (length pi*))
      (define p**
        (parameterize ([*OVERHEAD-PLOT-WIDTH* (exact-floor (/ (- OVERHEADS-WIDTH OVERHEADS-HSPACE) NUM-COLUMNS))]
                       [*OVERHEAD-PLOT-HEIGHT* (exact-floor (/ (+ OVERHEADS-HEIGHT OVERHEADS-VSPACE) num-pict))]
                       [*OVERHEAD-SHOW-RATIO* #f]
                       [*LEGEND-VSPACE* 2]
                       [*FONT-SIZE* 8])
          (columnize (map overhead-plot pi*) NUM-COLUMNS)))
      (define col*
        (map (λ (p*) (apply vl-append OVERHEADS-VSPACE p*)) p**))
      (apply ht-append OVERHEADS-HSPACE col*))))

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
