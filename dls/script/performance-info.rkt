#lang racket/base

;; Encapsulates info about a benchmark's performance

;; Command-line usage:
;;     raco rp-perf <benchmark-name> ...
;; Prints summary stats for each `<benchmark-name>`

;; TODO
;; - make sure "alphabetical in Racket" matches configuration order
;; - maybe don't need this, maybe should be part of `benchmark-info`
;; - get max configuration from bm info, isntead of inferring from file?

(require racket/contract)
(provide
  (contract-out
   [performance-info?
    (-> any/c boolean?)]
   ;; Predicate for instances of the `preformance-info` struct

   [rename performance-info-name performance-info->name
    (-> performance-info? symbol?)]

   [benchmark->performance-info
    (-> benchmark-info? performance-info?)]
   ;; Construct a `performance-info` struct from a `benchmark-info` struct

   [python-runtime
    (-> performance-info? real?)]
   ;; Return the runtime of the benchmark's untyped configuration under Python

   [untyped-runtime
    (-> performance-info? real?)]
   ;; Return the runtime of the benchmark's untyped configuration under Reticulated

   [typed-runtime
    (-> performance-info? real?)]
   ;; Return the runtime of the benchmark's fully-typed configuration under Reticulated

   [num-configurations
    (-> performance-info? natural?)]
   ;; Count the number of configurations in a benchmark

   [overhead
    (case->
     (-> performance-info? real? real?)
     (-> performance-info? (-> real? real?)))]
   ;; `(overhead p v)` returns the overhead of the running time `v` relative
   ;;  to the Python configuration of `p`

   [min-overhead
    (-> performance-info? real?)]
   ;; Returns the lowest observed overhead of any configuration in `p`

   [max-overhead
    (-> performance-info? real?)]
   ;; Returns the maximum observed overhead of any configuration in `p`

   [mean-overhead
    (-> performance-info? real?)]
   ;; Returns the average overhead across all configurations in `p`

   [deliverable
    (-> real? (-> performance-info? natural?))]
   ;; `((deliverable D) p)` returns the number of configurations in `p`
   ;; that have overhead at most `D` relative to the Python configuration of `p`

   [typed/python-ratio
    (-> performance-info? real?)]
   ;; Returns the overhead of the fully-typed configuration in `p`
   ;;  relative to the Python configuration

   [typed/retic-ratio
    (-> performance-info? real?)]
   ;; Returns the overhead of the fully-typed configuration in `p`
   ;;  relative to the untyped configuration

   [untyped/python-ratio
    (-> performance-info? real?)]
   ;; Returns the overhead of the untyped configuration in `p`
   ;;  relative to the Python configuration

   [make-D-deliverable?
    (-> real? performance-info? (-> real? boolean?))]
   ;; Return a function that decides whether a given running time is
   ;;  D-deliverable.

   [count-configurations
    (-> performance-info? (-> real? boolean?) natural?)]
   ;; Count the number of configurations
   ;;  (encapsulted by the given `performance-info` struct)
   ;;  that satisfy the given predicate.

  )
  string->configuration
  performance-info-src
  line->configuration-string
)

(require
  "benchmark-info.rkt"
  "util.rkt"
  (only-in racket/math
    natural?)
  (only-in file/gunzip
    gunzip)
  (only-in math/statistics
    mean)
  (only-in racket/string
    string-split
    string-replace))

(define-syntax-rule (TODO) (raise-user-error "not implemented"))

;; =============================================================================

(struct performance-info (
  name ;; Symbol, a benchmark name
  src  ;; Path-String, data from Karst
  num-configs
  configs/module*
  python-runtime
  untyped-runtime
  typed-runtime
) #:transparent
  #:methods gen:custom-write
  [(define (write-proc v port mode)
     (fprintf port "#<performance-info:~a>" (performance-info-name v)))])

(define (make-performance-info name #:src k
                                    #:num-configurations num-configs
                                    #:configurations/module* configs/module*
                                    #:python-runtime python
                                    #:untyped-retic-runtime base-retic
                                    #:typed-retic-runtime typed-retic)
  (performance-info name k num-configs configs/module* python base-retic typed-retic))

(define (gunzip/cd ps)
  (define-values [base name _dir?] (split-path ps))
  (parameterize ([current-directory base])
    (gunzip name))
  (build-path base (file-remove-extension name)))

(define (benchmark->performance-info bm)
  (define k
    (let* ([tab.gz (benchmark->karst-data bm)]
           [tab (and tab.gz (gunzip/cd tab.gz))])
      tab))
  (define name (benchmark->name bm))
  (unless k
    (raise-user-error 'benchmark->performance-info
      "cannot find Karst data for benchmark '~a'" name))
  (define-values [num-configs configs/module* base-retic typed-retic]
    (scan-karst-file k))
  (define python 1) ;; TODO !!!!
  (make-performance-info name
    #:src k
    #:num-configurations num-configs
    #:configurations/module* configs/module*
    #:python-runtime python
    #:untyped-retic-runtime base-retic
    #:typed-retic-runtime typed-retic))

(define (make-configuration-counter)
  (let ([cm (box #f)])
    (values cm
            (λ (cfg/mod*)
              (set-box! cm
                (if (and (unbox cm)
                         (for/and ([v-old (in-list (unbox cm))]
                                   [v-new (in-list cfg/mod*)])
                           (>= v-old v-new)))
                  (unbox cm)
                  cfg/mod*))))))

;; scan-karst-file : Path-String -> (Values Natural (Listof Natural) Natural Natural)
;; Take a "first glance" pass over a data file
;; Return
;; - the number of configurations
;; - the max. number of types per module (in alphabetical order)
(define (scan-karst-file k)
  (define-values [num-configs num-configs++]
    (let ([nc (box 0)])
      (values nc
              (λ ()
                (set-box! num-configs (+ 1 (unbox num-configs)))))))
  (define-values [configs/module* update-configs/module*]
    (make-configuration-counter))
  (define-values [base-retic typed-retic update-base-retic update-typed-retic]
    (let ([ur (box #f)]
          [tr (box #f)])
      (values ur
              tr
              (λ (times-str)
                (set-box! ur
                  (mean (parse-times-string times-str))))
              (λ (times-str)
                (when (not (unbox tr))
                  (set-box! tr
                    (mean (parse-times-string times-str))))))))
  (with-input-from-file k
    (λ ()
      (for ([ln (in-lines)])
        (define-values [cfg-str times-str]
          (let ([ln-info (parse-line ln)])
            (values (car ln-info) (caddr ln-info))))
        (num-configs++)
        (define cfg/mod* (string->configuration cfg-str))
        (define prev-cfg* (unbox configs/module*))
        (update-configs/module* cfg/mod*)
        (when (typed-configuration? cfg/mod*)
          (update-typed-retic times-str))
        (unless (equal? prev-cfg* (unbox configs/module*))
          (update-base-retic times-str))
        (void))))
  (values (unbox num-configs)
          (unbox configs/module*)
          (unbox base-retic)
          (unbox typed-retic)))

(define (karst-file->max-configuration k)
  (define-values [configs/module* update-configs/module*]
    (make-configuration-counter))
  (with-input-from-file k
    (λ ()
      (for ([ln (in-lines)])
        (update-configs/module*
          (string->configuration (line->configuration-string ln)))
        (void))))
  (unbox configs/module*))

(define (typed-configuration? cfg/mod*)
  (andmap zero? cfg/mod*))

(define (line->configuration-string str)
  (let ([str* (parse-line str)])
    (car str*)))

(define/contract (parse-line str)
  (-> string? (list/c string? string? string?))
  (tab-split str))

;; string->configuration : String -> (Listof Natural)
;; Parse a string like `0-0-3` into a list of numbers `'(0 0 3)`
(define/contract (string->configuration cfg-str)
  (-> string? configuration?)
  (map string->number (string-split cfg-str "-")))

(define/contract (parse-times-string times-str)
  (-> string? (non-empty-listof (and/c real? (>=/c 0))))
  (let ([sp (open-input-string (string-replace times-str "," ""))])
    (begin0 (read sp) (close-input-port sp))))

(define (untyped-runtime pf)
  (performance-info-untyped-runtime pf))

(define (typed-runtime pf)
  (performance-info-typed-runtime pf))

(define (python-runtime pf)
  (performance-info-python-runtime pf))

(define (num-configurations pf)
  (performance-info-num-configs pf))

(define overhead
  (case-lambda
   [(pf v)
    ((overhead pf) v)]
   [(pf)
    ;; TODO use python runtime
    (let ([baseline (performance-info-untyped-runtime pf)])
      (λ (v) (/ v baseline)))]))

(define (min-overhead pf)
  (overhead pf (fold/mean (performance-info-src pf) min)))

(define (max-overhead pf)
  (overhead pf (fold/mean (performance-info-src pf) max)))

(define (mean-overhead pf)
  (define 1/N (/ 1 (num-configurations pf)))
  (define (avg acc v)
    (+ acc (* 1/N v)))
  (overhead pf (fold/mean (performance-info-src pf) avg #:init (λ (v) (* 1/N v)))))

;; fold/mean : (All (A) Path-String (-> A Real A) #:init (U #f (-> Real A)) -> A)
(define fold/mean
  (let ([line->mean (λ (ln line-number)
                      (with-handlers ([exn:fail:read?
                                       (lambda (e)
                                         (printf "PARSE ERROR on line ~a~n" line-number)
                                         (raise e))])
                        (let ([times-str (caddr (parse-line ln))])
                          (mean (parse-times-string times-str)))))])
    (λ (filename f #:init [init-f #f])
      (with-input-from-file filename
        (λ ()
          (define init (line->mean (read-line) 1))
          (for/fold ([acc (if init-f (init-f init) init)])
                    ([ln (in-lines)]
                     [i (in-naturals 2)])
            (f acc (line->mean ln i))))))))

(define ((deliverable D) pf)
  (count-configurations pf (make-D-deliverable? D pf)))

(define (make-D-deliverable? D pf)
  (define overhead/pf (overhead pf))
  (lambda (t)
    (<= (overhead/pf t) D)))

(define (count-configurations pf good?)
  (define (add-good? count t)
    (if (good? t) (+ count 1) count))
  (fold/mean (performance-info-src pf)
             add-good?
             #:init (λ (t) (add-good? 0 t))))

(define (typed/python-ratio pf)
  (/ (performance-info-typed-runtime pf)
     (performance-info-python-runtime pf)))

(define (typed/retic-ratio pf)
  (/ (performance-info-typed-runtime pf)
     (performance-info-untyped-runtime pf)))

(define (untyped/python-ratio pf)
  (/ (performance-info-untyped-runtime pf)
     (performance-info-python-runtime pf)))

(define (quick-performance-info bm-name)
  (define bm (->benchmark-info bm-name))
  (define pf (benchmark->performance-info bm))
  (define nc (performance-info-num-configs pf))
  (printf "~a~n" bm-name)
  (printf "- num configs  : ~a~n" nc)
  (printf "- Python  time : ~a~n" "???")
  (printf "- untyped time : ~a~n" (performance-info-untyped-runtime pf))
  (printf "- typed time   : ~a~n" (performance-info-typed-runtime pf))
  (printf "- min overhead : ~a~n" (min-overhead pf))
  (printf "- max overhead : ~a~n" (max-overhead pf))
  (printf "- avg overhead : ~a~n" (mean-overhead pf))
  (let ([d2 ((deliverable 2) pf)])
    (printf "- 2 deliv.     : ~a (~a%)~n" d2 (rnd (pct d2 nc))))
  (let ([d5 ((deliverable 5) pf)])
    (printf "- 5 deliv.     : ~a (~a%)~n" d5 (rnd (pct d5 nc))))
  (void))

;; =============================================================================

(module+ test
  (require rackunit racket/runtime-path)

  (define-runtime-path karst-example "./test/karst-example_tab.gz")

  (test-case "benchmark->performance-info:example-data"
    (define karst-example-gunzip (gunzip/cd karst-example))
    (define-values [num-configs configs/module* base-retic typed-retic]
      (scan-karst-file karst-example-gunzip))
    (check-equal? num-configs 4)
    (check-equal? configs/module* '(1 1))
    (check-equal? base-retic 10)
    (check-equal? typed-retic 20)

    (let ([pf (make-performance-info 'example
                #:src karst-example-gunzip
                #:num-configurations num-configs
                #:configurations/module* configs/module*
                #:python-runtime base-retic ;; TODO
                #:untyped-retic-runtime base-retic
                #:typed-retic-runtime typed-retic)])
      (check-equal? (num-configurations pf) 4)
      (check-equal? (min-overhead pf) 1/2)
      (check-equal? (max-overhead pf) 10)
      (check-equal? (mean-overhead pf) 27/8)
      (check-equal? (typed/retic-ratio pf) 2)
      (check-equal? ((deliverable 2) pf) 3)
      (check-equal? ((deliverable 10) pf) 4)
      (void)))

  ;; general correctness/sanity for a real program
  (let* ([bm (->benchmark-info 'Espionage)]
         [pf (benchmark->performance-info bm)])
    (test-case "performance-info:spot-check"
      (check-true (performance-info? pf))
      (let* ([lo (min-overhead pf)]
             [hi (max-overhead pf)]
             [avg (mean-overhead pf)]
             [nc (num-configurations pf)]
             [d2 ((deliverable 2) pf)]
             [d3 ((deliverable 3) pf)]
             [dhi ((deliverable hi) pf)])
        (check <= lo hi)
        (check <= lo avg)
        (check <= avg hi)
        (check <= d2 nc)
        (check <= d2 d3)
        (check-equal? dhi nc)
        (void)))

    (test-case "quick-stats:spot-check"
      (define quick-stats-str
        (let ([sp (open-output-string)])
          (parameterize ([current-output-port sp])
            (quick-performance-info 'Espionage))
          (begin0 (get-output-string sp) (close-output-port sp))))
      (define m (regexp-match #rx"avg overhead : ([.0-9]+)\n" quick-stats-str))
      (check-true (pair? m))
      (check-equal? (string->number (cadr m)) (mean-overhead pf))
      (void))
  )

  (test-case "typed-configuration?"
    (check-true (typed-configuration? '(0 0 0)))
    (check-true (typed-configuration? '()))
    (check-false (typed-configuration? '(1 0)))
    (check-false (typed-configuration? '(9 8 7 7 9))))

  (test-case "parse-line"
    (check-equal?
      (parse-line "0-0	4	[1, 2, 2, 3]")
      (list "0-0" "4" "[1, 2, 2, 3]"))
    (check-exn exn:fail:contract?
      (λ () (parse-line ""))))

  (test-case "string->configuration"
    (check-equal?
      (string->configuration "0-0")
      '(0 0))
    (check-equal?
      (string->configuration "1-22-333")
      '(1 22 333))
    (check-exn exn:fail:contract?
      (λ () (string->configuration "1-2-four")))
    (check-exn exn:fail:contract?
      (λ () (string->configuration ""))))

  (test-case "parse-times-string"
    (check-equal?
      (parse-times-string "[1, 2, 3]")
      '(1 2 3))
    (check-equal?
      (parse-times-string "[1.23, 4.554]")
      '(1.23 4.554))
    (check-exn exn:fail:contract?
      (λ () (parse-times-string "[]")))
    (check-exn exn:fail:contract?
      (λ () (parse-times-string "[1, -2]"))))

)

;; -----------------------------------------------------------------------------

(module+ main
  (require racket/cmdline)
  (command-line
   #:program "perf-info"
   #:args benchmark-name*
   (cond
    [(null? benchmark-name*)
     (printf "usage: rp:perf-info <benchmark-name> ...~n")]
    [(null? (cdr benchmark-name*))
     (quick-performance-info (car benchmark-name*))]
    [else
     (for ([n (in-list benchmark-name*)])
       (with-handlers ([exn:fail:contract? (λ (e) (printf "WARNING: failure processing '~a'~n" n))])
         (quick-performance-info n)))])))

