#lang racket/base

;; Plotting

;; TODO ?
;; - average-case
;; - worst-case
;; - paths
;; - lattice
;; - overhead delta (what's the delta between?)

(require racket/contract)
(provide
  (contract-out
    [overhead-plot
     (-> performance-info? pict?)]
    ;; Render an overhead plot for the given benchmark

    [samples-plot
     (-> performance-info? pict?)]

    [exact-runtime-plot
     (-> performance-info? pict?)]
    ;; TODO once implemented, check whether y-axis permits graphing all on ONE axis

    [validate-samples-plot
     (-> performance-info? pict?)]
))

(require
  "benchmark-info.rkt"
  "performance-info.rkt"
  "sample.rkt"
  "util.rkt"
  pict
  plot/no-gui
  plot/utils
  (only-in math/statistics
    mean)
  (only-in racket/format
    ~r)
  (only-in racket/list
    range)
  (only-in racket/math
    exact-ceiling
    exact-floor))

;; =============================================================================
;; Parameters, constants

(define TICK-SIZE 4)
(define TITLE-FACE "Liberation Serif")
(define SAMPLE-COLOR "darkorange")
;(define SAMPLE-COLOR "chocolate")

(define-syntax-rule (defparam id val type)
  (begin (define id (make-parameter val))
         (provide id)))

(defparam *LEGEND-VSPACE* 10 Pict-Units)
(defparam *LEGEND-HSPACE* 20 Pict-Units)
(defparam *OVERHEAD-PLOT-WIDTH* 600 Pict-Units)
(defparam *OVERHEAD-PLOT-HEIGHT* 300 Pict-Units)
(defparam *OVERHEAD-FONT-FACE* "bold" Font-Face)
(defparam *OVERHEAD-FONT-SCALE* 0.03 Nonnegative-Real)
(defparam *OVERHEAD-LABEL?* #f boolean?)
(defparam *OVERHEAD-LINE-COLOR* 3 plot-color/c)
(defparam *OVERHEAD-LINE-STYLE* 'solid plot-pen-style/c)
(defparam *OVERHEAD-LINE-WIDTH* 1 Nonnegative-Real)
(defparam *OVERHEAD-MAX* 10 Natural)
(defparam *OVERHEAD-SHOW-RATIO* #t (U Symbol Boolean))
(defparam *OVERHEAD-SAMPLES* 20 Natural)
(defparam *FONT-SIZE* 10 Natural)
(defparam *CACHE-SIZE* (expt 2 16) Natural) ;; max num. configs to store in memory
(defparam *POINT-SIZE* 3 Positive-Index)
(defparam *POINT-ALPHA* 0.4 Nonnegative-Real)
(defparam *CONFIGURATION-X-JITTER* 0.4 Real)
(defparam *OVERHEAD-FREEZE-BODY* #f boolean?)
(defparam *CONFIDENCE-LEVEL* 95 Percent)
(defparam *INTERVAL-ALPHA* 1 Nonnegative-Real)


;; -----------------------------------------------------------------------------

(define (exact-runtime-plot pi)
  (define nt (num-types pi))
  (define max-runtime (box 0))
  (define num-points (box 0))
  (define elem*
    (list
      (make-vrule* nt)
      (fold/karst pi
        #:init '()
        #:f (λ (acc cfg num-types t*)
              (cons (configuration-points
                      (for/list ([t (in-list t*)]
                                 [x (in-list (linear-seq (- num-types (*CONFIGURATION-X-JITTER*)) (+ num-types (*CONFIGURATION-X-JITTER*)) (length t*)))])
                        (set-box! max-runtime (max (unbox max-runtime) t))
                        (set-box! num-points (+ (unbox num-points) 1))
                        (list x t)))
                    acc)))))
  (define y-max (exact-ceiling (unbox max-runtime)))
  (define body (maybe-freeze
    (parameterize ([plot-x-ticks (make-exact-runtime-xticks nt)]
                   [plot-y-ticks (make-exact-runtime-yticks y-max)]
                   [plot-x-far-ticks no-ticks]
                   [plot-y-far-ticks no-ticks]
                   [plot-tick-size TICK-SIZE]
                   [plot-font-face (*OVERHEAD-FONT-FACE*)]
                   [plot-font-size (*FONT-SIZE*)])
      (plot-pict elem*
        #:x-min (- 0 0.5)
        #:x-max (+ nt 0.5)
        #:y-min 0
        #:y-max y-max
        #:x-label (and (*OVERHEAD-LABEL?*) "Num Type Ann.")
        #:y-label (and (*OVERHEAD-LABEL?*) "Time (ms)")
        #:width (*OVERHEAD-PLOT-WIDTH*)
        #:height (*OVERHEAD-PLOT-HEIGHT*)))))
  (exact-add-legend (performance-info->name pi) (unbox num-points) body))

(define (overhead-plot pi)
  (define body (maybe-freeze
    (parameterize ([plot-x-ticks (make-overhead-x-ticks)]
                   [plot-x-transform log-transform]
                   [plot-y-ticks (make-overhead-y-ticks)]
                   [plot-x-far-ticks no-ticks]
                   [plot-y-far-ticks no-ticks]
                   [plot-tick-size TICK-SIZE]
                   [plot-font-face (*OVERHEAD-FONT-FACE*)]
                   [plot-font-size (*FONT-SIZE*)])
      (plot-pict
        (list
          (make-count-configurations-function pi)
          (tick-grid))
        #:x-min 1
        #:x-max (*OVERHEAD-MAX*)
        #:y-min 0
        #:y-max 100
        #:x-label (and (*OVERHEAD-LABEL?*) "Overhead (vs. retic-untyped)")
        #:y-label (and (*OVERHEAD-LABEL?*) "% Configs.")
        #:width (*OVERHEAD-PLOT-WIDTH*)
        #:height (*OVERHEAD-PLOT-HEIGHT*)))))
  (overhead-add-legend pi body))

(define (samples-plot pi)
  (define-values [sample-size sample*] (performance-info->sample-info pi))
  (define mean-overhead
    (let ([dc*
           (for/list ([s (in-list sample*)])
             (make-simple-deliverable-counter (performance-info%sample pi s)))])
      (λ (r)
        (mean (for/list ([dc (in-list dc*)]) (dc r))))))
  (define body (maybe-freeze
    (parameterize ([plot-x-ticks (make-overhead-x-ticks)]
                   [plot-x-transform log-transform]
                   [plot-y-ticks (make-overhead-y-ticks)]
                   [plot-x-far-ticks no-ticks]
                   [plot-y-far-ticks no-ticks]
                   [plot-tick-size TICK-SIZE]
                   [plot-font-face (*OVERHEAD-FONT-FACE*)]
                   [plot-font-size (*FONT-SIZE*)]
                   [*OVERHEAD-LINE-COLOR* SAMPLE-COLOR])
      (plot-pict
        (list
          (parameterize ([*INTERVAL-ALPHA* 0.4])
            (make-count-configurations-function mean-overhead))
          (make-sample-function-interval
            (for/list ([s (in-list sample*)])
              (performance-info%sample pi s)))
          (tick-grid))
        #:x-min 1
        #:x-max (*OVERHEAD-MAX*)
        #:y-min 0
        #:y-max 100
        #:x-label (and (*OVERHEAD-LABEL?*) "Overhead (vs. retic-untyped)")
        #:y-label (and (*OVERHEAD-LABEL?*) "% Configs.")
        #:width (*OVERHEAD-PLOT-WIDTH*)
        #:height (*OVERHEAD-PLOT-HEIGHT*)))))
  (samples-add-legend pi sample-size (length sample*) body))

(define (validate-samples-plot pi)
  (define-values [sample-size sample*] (performance-info->sample-info pi))
  (define body (maybe-freeze
    (parameterize ([plot-x-ticks (make-overhead-x-ticks)]
                   [plot-x-transform log-transform]
                   [plot-y-ticks (make-overhead-y-ticks)]
                   [plot-x-far-ticks no-ticks]
                   [plot-y-far-ticks no-ticks]
                   [plot-tick-size TICK-SIZE]
                   [plot-font-face (*OVERHEAD-FONT-FACE*)]
                   [plot-font-size (*FONT-SIZE*)]
                   [*OVERHEAD-LINE-WIDTH* 0.5])
      (plot-pict
        (list
          (make-count-configurations-function pi)
          (parameterize ([*OVERHEAD-LINE-COLOR* SAMPLE-COLOR])
            (make-sample-function-interval
              (for/list ([s (in-list sample*)])
                (performance-info%sample pi s))))
          (tick-grid)
          (make-count-configurations-function pi #:interval? #f))
        #:x-min 1
        #:x-max (*OVERHEAD-MAX*)
        #:y-min 0
        #:y-max 100
        #:x-label (and (*OVERHEAD-LABEL?*) "Overhead (vs. retic-untyped)")
        #:y-label (and (*OVERHEAD-LABEL?*) "% Configs.")
        #:width (*OVERHEAD-PLOT-WIDTH*)
        #:height (*OVERHEAD-PLOT-HEIGHT*)))))
  (samples-add-legend (performance-info->name pi) sample-size (length sample*) body))

;; -----------------------------------------------------------------------------

(define (performance-info->sample-info pi)
  (let ([a+b (performance-info->sample* pi)])
    (values (car a+b) (cdr a+b))))

(define (maybe-freeze p)
  (if (*OVERHEAD-FREEZE-BODY*)
    (freeze p)
    p))

(define (configuration-points p**)
  (define i 2)
  (points p**
    #:color (->pen-color i)
    #:alpha (*POINT-ALPHA*)
    #:sym 'fullcircle
    #:size (*POINT-SIZE*)))

(define (make-vrule* count)
  (for/list ([i (in-range (+ 1 count))])
    (vrule (- i 0.5) #:width 0.2 #:color 0)))

(define (make-count-configurations-function pi #:interval? [ivl #t])
  (define f (if (performance-info? pi) (make-deliverable-counter pi) pi))
  (if ivl
    (function-interval
      (λ (r) 0)
      f
      0 (*OVERHEAD-MAX*)
      #:alpha (*INTERVAL-ALPHA*)
      #:color (*OVERHEAD-LINE-COLOR*)
      #:line1-color (*OVERHEAD-LINE-COLOR*)
      #:line2-color (*OVERHEAD-LINE-COLOR*)
      #:line1-width (*OVERHEAD-LINE-WIDTH*)
      #:line2-width (*OVERHEAD-LINE-WIDTH*)
      #:samples (*OVERHEAD-SAMPLES*)
      #:style (*OVERHEAD-LINE-STYLE*))
    (function
      f
      0 (*OVERHEAD-MAX*)
      #:color (*OVERHEAD-LINE-COLOR*)
      #:width (*OVERHEAD-LINE-WIDTH*)
      #:samples (*OVERHEAD-SAMPLES*)
      #:style (*OVERHEAD-LINE-STYLE*))))

;; make-simple-deliverable-counter : (-> performance-info? (-> real? natural?))
;; Specification for `make-deliverable-counter`
(define (make-simple-deliverable-counter pi)
  (define nc (num-configurations pi))
  (λ (D)
    (pct (count-configurations pi (make-D-deliverable? D pi)) nc)))

;; make-deliverable-counter : (-> performance-info? (-> real? natural?))
;; Same behavior as `make-deliverable-counter`, but `(make-deliverable-counter p)`
;;  has two side-effects for efficiency:
;; - if called with `i` such that `(= 100 ((make-deliverable-counter p) i))`
;;   then future calls to the function return 100 immediately
;; - if called with `i` such that `(= N ((make-deliverable-counter p) i))`
;;   and `(<= (* (- 100 N) (num-configurations pi)) (*CACHE-SIZE*))`,
;;   then saves `N` and future calls only check whether the remaining configurations
;;   are now deliverable
;; Both side-effects assume monotonic calling contexts.
;; If `plot` made calls in a non-monotonic order, these would be WRONG!
(define (make-deliverable-counter pi)
  (define nc (num-configurations pi))
  (define all-good? (box #f))
  (define cache (box #f)) ;; (U #f (Pairof Natural (Listof Real)))
  (λ (D)
    (if (unbox all-good?)
      100
      (let* ([good? (make-D-deliverable? D pi)]
             [num-good (if (unbox cache)
                         (+ (car (unbox cache))
                            (for/sum ([t (in-list (cdr (unbox cache)))] #:when (good? t)) 1))
                         (count-configurations pi good?))]
             [n (pct num-good nc)])
        (when (= n 100)
          (set-box! all-good? #t))
        (unless (or (unbox cache) (unbox all-good?))
          (define num-configs-left (- nc num-good))
          (when (<= num-configs-left (*CACHE-SIZE*))
            (set-box! cache (cons num-good (filter-time* pi (λ (t) (not (good? t))))))))
        n))))

(define (make-sample-function-interval pi*)
  (define (make-get-percents)
    (let ([ctr* (map make-deliverable-counter pi*)])
      (λ (r)
        (for/list ([ctr (in-list ctr*)])
          (ctr r)))))
  (function-interval
    (λ (r) (lower-confidence ((make-get-percents) r)))
    (λ (r) (upper-confidence ((make-get-percents) r)))
    0 (*OVERHEAD-MAX*)
    #:alpha (*INTERVAL-ALPHA*)
    #:color (*OVERHEAD-LINE-COLOR*)
    #:line1-color (*OVERHEAD-LINE-COLOR*)
    #:line1-width (*OVERHEAD-LINE-WIDTH*)
    #:line2-color (*OVERHEAD-LINE-COLOR*)
    #:line2-width (*OVERHEAD-LINE-WIDTH*)
    #:samples (*OVERHEAD-SAMPLES*)
    #:style 'solid
    #:label #f))

(define (lower-confidence n*)
  (- (mean n*) (error-bound n*)))

(define (upper-confidence n*)
  (+ (mean n*) (error-bound n*)))

(define (error-bound n*)
  (define cv
    (case (*CONFIDENCE-LEVEL*)
     [(95) 1.96]
     [(98) 2.326]
     [else (error 'error-bounds "Unknown confidence level '~a'" (*CONFIDENCE-LEVEL*))]))
  (confidence-interval n* #:cv cv))

(define (make-overhead-x-ticks)
  (define MAJOR-TICKS (list 1 2 (*OVERHEAD-MAX*)))
  (define MINOR-TICKS
    (append (for/list ([i (in-range 12 20 2)]) (/ i 10))
            (for/list ([i (in-range 4 20 2)]) i)))
  (define m-ticks
    (ticks (real*->ticks-layout MAJOR-TICKS)
           (ticks-format/units "x")))
  (ticks-add m-ticks MINOR-TICKS #f))

(define (make-overhead-y-ticks)
  (define NUM-TICKS 3)
  (define UNITS "%")
  (ticks (λ (ax-min ax-max)
           (for/list ([y (in-list (linear-seq ax-min ax-max NUM-TICKS #:end? #t))])
             (pre-tick (exact-floor y) #t)))
         (ticks-format/units UNITS)))

(define (make-exact-runtime-xticks num-types)
  (define x*
    (if (<= num-types 6)
      (range (+ 1 num-types))
      (map exact-floor (linear-seq 0 num-types 5 #:start? #t #:end? #t))))
  (ticks (real*->ticks-layout x*)
         (λ (ax-min ax-max pre-ticks)
           (for/list ([pt (in-list pre-ticks)])
             (number->string (pre-tick-value pt))))))

(define (make-exact-runtime-yticks max-runtime)
  (define x* (list 0 (exact->inexact (/ max-runtime 2)) max-runtime))
  (ticks (real*->ticks-layout x*)
         (λ (ax-min ax-max pre-ticks)
           (for/list ([pt (in-list pre-ticks)])
             (define v (pre-tick-value pt))
             (cond
              [(= v max-runtime)
               (format "~as" v)]
              [else
               (~r v #:precision 1)])))))

(define ((real*->ticks-layout x*) ax-min ax-max)
  (for/list ([x (in-list x*)])
    (pre-tick x #t)))

(define ((ticks-format/units units) ax-min ax-max pre-ticks)
  (for/list ([pt (in-list pre-ticks)])
    (define v (pre-tick-value pt))
    (if (= v ax-max)
      (format "~a~a" (number->string v) units)
      (number->string v))))

(define (overhead-add-legend pi pict)
  (define name (render-benchmark-name (performance-info->name pi)))
  (define tp-ratio
    (if (*OVERHEAD-SHOW-RATIO*)
      (render-typed/python-ratio (typed/python-ratio pi))
      (blank 0 0)))
  (define nc (render-count (num-configurations pi) "configurations"))
  (add-legend (hb-append (*LEGEND-HSPACE*) name tp-ratio)
              pict
              nc))

(define (exact-add-legend bm-name num-points pict)
  (define name (render-benchmark-name bm-name))
  (define np (render-count num-points "points"))
  (add-legend name pict np))

(define (samples-add-legend pi sample-size num-samples pict)
  (define-values [name tp-ratio]
    (cond
     [(performance-info? pi)
      (values (performance-info->name pi)
              (if (*OVERHEAD-SHOW-RATIO*)
                (render-typed/python-ratio (typed/python-ratio pi))
                (blank 0 0)))]
     [else
      (values pi (blank 0 0))]))
  (define s-info (title-text (format "~a samples of ~a configurations" num-samples sample-size)))
  (add-legend (hb-append (*LEGEND-HSPACE*) (render-benchmark-name name) tp-ratio)
              pict s-info))

(define (add-legend top-left body top-right)
  (rt-superimpose
    (vl-append (*LEGEND-VSPACE*) top-left body)
    top-right))

(define (title-text str [angle 0])
  (text str (cons 'bold TITLE-FACE) (*FONT-SIZE*) angle))

(define (render-benchmark-name sym)
  (title-text (symbol->string sym)))

(define (render-typed/python-ratio r)
  (define text
    (case (*OVERHEAD-SHOW-RATIO*)
     ['short (format "(~ax)" (rnd r))]
     [else (format "typed/python ratio: ~ax" (rnd r))]))
  (parameterize ([*FONT-SIZE* (sub1 (*FONT-SIZE*))])
    (title-text text)))

(define (render-count n descr)
  (title-text (format "~a ~a" (add-commas n) descr)))

(define (sample-info->overhead-plot si)
  (raise-user-error 'sample-info->overhead "not implemented"))

(define (performance-vs-num-types-plot pi)
  (raise-user-error 'performance-vs-num-types "not implemented"))

;; =============================================================================

(module+ main
  (require racket/cmdline)
  (define OVERHEAD 'overhead)
  (define EXACT 'exact)
  (define SAMPLE 'sample)
  (define VALIDATE 'validate)
  (define *plot-type* (make-parameter OVERHEAD))
  (command-line
   #:program "rp-plot"
   #:once-any
   [("-o" "--overhead") "Make overhead plot" (*plot-type* OVERHEAD)]
   [("-e" "--exact") "Plot exact running times" (*plot-type* EXACT)]
   [("-s" "--sample") "Plot samples" (*plot-type* SAMPLE)]
   [("-v" "--validate") "Validate samples" (*plot-type* VALIDATE)]
   #:args benchmark-name*
   (cond
    [(null? benchmark-name*)
     (printf "usage: raco rp-plot <benchmark-name> ...~n")]
    [else
     (define pi*
       (if (null? (cdr benchmark-name*))
         (list (benchmark->performance-info (->benchmark-info (car benchmark-name*))))
         (for/list ([n (in-list benchmark-name*)])
           (with-handlers ([exn:fail? (λ (e) (printf "Error processing '~a', run 'raco rp-plot ~a' to debug.~n" n n))])
             (benchmark->performance-info (->benchmark-info n))))))
     (define render-one
       (case (*plot-type*)
        [(overhead) overhead-plot]
        [(exact) exact-runtime-plot]
        [(sample) samples-plot]
        [(validate) validate-samples-plot]
        [else (raise-user-error 'rp-plot "unknown plot type '~a'" (*plot-type*))]))
     (define p*
       (parameterize ([*FONT-SIZE* 14])
         (map render-one pi*)))
     (save-pict "rp-plot.png" (apply vl-append 50 p*))])))

;; =============================================================================

(module+ test
  (require rackunit rackunit-abbrevs)

  ;; TODO what to test?
  ;; - actually works, makes plots for various inputs
  ;; - same plots for "same" inputs
  ;; - count-configs fucntion? but it's a plot/function
  ;; - make ticks? also weird output format
  ;; - add legend? ditto idk what besides comparing argb pixels

  (test-case "deliverable-counter"
    (define (check-deliverable-counter/cache bm-name)
      (define pi (benchmark->performance-info (->benchmark-info bm-name)))
      (define f0 (make-simple-deliverable-counter pi))
      (define f1 (make-deliverable-counter pi))
      (define seq (linear-seq 1 (*OVERHEAD-MAX*) (*OVERHEAD-SAMPLES*)))
      (define-values [v*0 t0]
        (force/cpu-time (λ () (map f0 seq))))
      (define-values [v*1 t1]
        (force/cpu-time (λ () (map f1 seq))))
      (check-equal? v*0 v*1)
      (check < t1 t0)
      (void))

    ;; Maybe want to put a time limit on this. For me it's like 20 seconds, I don't mind --ben
    (check-deliverable-counter/cache 'PythonFlow)
    (check-deliverable-counter/cache 'call_simple)
  )

)
