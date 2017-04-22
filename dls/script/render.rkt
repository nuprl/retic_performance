#lang racket/base

;; For making graphs

(provide
  render-overhead-plot*
  ;; (-> (listof benchmark-info?) pict?)

  render-exact-runtime-plot*
  ;; (-> (listof benchmark-info?) pict?)

  render-static-information
  render-ratios-table
  render-samples-plot*
  render-validation-plot*
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
    second
    third
    make-list)
  (only-in math/statistics
    mean)
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

(define (render-samples-plot* bm*)
  (render-benchmark* bm* "samples" samples-plot))

(define (render-validation-plot* bm*)
  (render-benchmark* bm* "validate" validate-samples-plot))

(define (render-benchmark* bm* descr render-one [freeze? #f])
  (define num-pict (length bm*))
  (when (zero? num-pict)
    (raise-user-error 'render-benchmark* "cannot render empty list of zero benchmarks"))
  (define p*
    (parameterize ([*OVERHEAD-PLOT-WIDTH* (exact-floor (/ (- OVERHEADS-WIDTH OVERHEADS-HSPACE) NUM-COLUMNS))]
                   [*OVERHEAD-PLOT-HEIGHT* (exact-floor (/ (+ OVERHEADS-HEIGHT OVERHEADS-VSPACE) num-pict))]
                   [*OVERHEAD-SHOW-RATIO* 'short]
                   [*OVERHEAD-FREEZE-BODY* freeze?]
                   [*LEGEND-VSPACE* 2]
                   [*LEGEND-HSPACE* 4]
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

(define RATIOS-TITLE*
  (map bold '("Benchmark" "untyped/python" "typed/untyped")))

(define (render-ratios-table bm*)
  (define name* (map benchmark->name bm*))
  (tabular
    #:sep (hspace 2)
    #:row-properties '(bottom-border 1)
    #:column-properties '(left right right)
    (cons RATIOS-TITLE*
          (parameterize ([*current-cache-directory* (build-path (current-directory) "with-cache")]
                         [*current-cache-keys* (list (λ () name*))]
                         [*with-cache-fasl?* #f])
            (with-cache (cachefile "ratios-table.rktd")
              (λ ()
                (define pi* (map benchmark->performance-info bm*))
                (append
                  (map render-ratios-row pi*)
                  #;(list (render-ratios-average-row pi*)))))))))

(define (render-ratios-row pi)
  (list (tt (symbol->string (performance-info->name pi)))
        (rnd (untyped/python-ratio pi))
        (rnd (typed/retic-ratio pi))))

;; 2.32, 1.59 .... not too interesting, but also AVERAGE is a useless measure
(define (render-ratios-average-row pi*)
  (define (render-pi*-mean sel)
    (bold (rnd (mean (map sel pi*)))))
  (list (bold "average")
        (render-pi*-mean untyped/python-ratio)
        (render-pi*-mean typed/retic-ratio)))

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
