#lang racket/base

;; For making graphs

(provide
  render-overhead-plot*
  ;; (-> (listof benchmark-info?) pict?)

  render-exact-runtime-plot*
  ;; (-> (listof benchmark-info?) pict?)

  render-static-information
)

(require
  "benchmark-info.rkt"
  "performance-info.rkt"
  "plot.rkt"
  "python.rkt"
  "util.rkt"
  pict
  with-cache
  (only-in racket/format
    ~a)
  (only-in scribble/manual
    tt
    tabular
    hspace
    bold)
  (only-in racket/list
    make-list)
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
                   [*current-cache-keys* (list (λ () (list OVERHEADS-WIDTH OVERHEADS-HEIGHT OVERHEADS-VSPACE OVERHEADS-HSPACE)))]
                   [*with-cache-fasl?* #f])
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

(define STATIC-INFO-TITLE*
  (map bold '("Benchmark" "SLOC" "M" "F" "C" "m")))

(define (render-static-information bm*)
  (tabular
    #:sep (hspace 2)
    #:row-properties '(bottom-border 1)
    #:column-properties (cons 'left (make-list (sub1 (length STATIC-INFO-TITLE*)) 'right))
    (cons STATIC-INFO-TITLE*
          (map render-static-row bm*))))

(define (render-static-row bm)
  (define py (benchmark-info->python-info bm))
  (cons
    (tt (symbol->string (benchmark->name bm)))
    (map number->string (list
      (benchmark->sloc bm)
      (python-info->num-modules py)
      (python-info->num-functions py)
      (python-info->num-classes py)
      (python-info->num-methods py)))))

;; =============================================================================

(module+ test
  (require rackunit (only-in scribble/core table?))

  (test-case "render-table"
    (check-pred table? (render-static-information (list (->benchmark-info 'futen))))
  )
)

;(module+ main
;  
;
;)
