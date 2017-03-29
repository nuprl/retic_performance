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

   [num-types
    (-> performance-info? natural?)]
   ;; Count the number of annotatable-positions in the benchmark (for our experiment)
   ;; A benchmark with `F` functions and `C` classes with fields and `M` methods
   ;;  across all the classes has `F + C + M` types.

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

   [filter-time*
    (-> performance-info? (-> real? boolean?) (listof real?))]
   ;; Return the MEAN RUNNING TIMES for configurations whose mean
   ;;  running time satisfies the given predicate.

   [performance-info->sample*
    (-> performance-info? (cons/c natural? (listof path-string?)))]

   [performance-info%sample
    (-> performance-info? path-string? performance-info?)]

  )
  string->configuration
  performance-info-src
  line->configuration-string

  fold/karst
  ;; (-> (or/c path-string? performance-info?)
  ;;     #:f (-> A configuration? natural? (listof real?) A)
  ;;     #:init A A)
  ;; Fold (left) function for Karst data.
  ;; Given function is called with:
  ;; - the accumulated data so far
  ;; - the current line's configuration
  ;; - the number of types in the current configuration
  ;; - the running times for that configuration
)

(require
  "benchmark-info.rkt"
  "config.rkt"
  "util.rkt"
  (only-in racket/path
    path-only)
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
                  (mean (string->time* times-str))))
              (λ (times-str)
                (when (not (unbox tr))
                  (set-box! tr
                    (mean (string->time* times-str))))))))
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

(define/contract (string->num-types t-str)
  (-> string? natural?)
  (string->number t-str))

(define/contract (string->time* times-str)
  (-> string? (non-empty-listof (and/c real? (>=/c 0))))
  (let ([sp (open-input-string (string-replace times-str "," ""))])
    (begin0 (read sp) (close-input-port sp))))

(define (line->values ln line-number)
  (with-handlers ([exn:fail:read? (λ (e) (printf "PARSE ERROR on line ~a~n" line-number) (raise e))])
    (define str* (parse-line ln))
    (define cfg (string->configuration (car str*)))
    (define nt (string->num-types (cadr str*)))
    (define t* (string->time* (caddr str*)))
    (values cfg nt t*)))

(define (untyped-runtime pf)
  (performance-info-untyped-runtime pf))

(define (typed-runtime pf)
  (performance-info-typed-runtime pf))

(define (python-runtime pf)
  (performance-info-python-runtime pf))

(define (num-configurations pf)
  (performance-info-num-configs pf))

(define (num-types pf)
  (log2 (num-configurations pf)))

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

(define (fold/karst pf #:init init #:f f)
  (define src
    (cond
     [(path-string? pf) pf]
     [(performance-info? pf) (performance-info-src pf)]
     [else (raise-argument-error 'fold/karst "(or/c path-string? performance-info?)" 0 pf init f)]))
  (with-input-from-file src 
    (λ ()
      (for/fold ([acc init])
                ([ln (in-lines)]
                 [i (in-naturals)])
        (define-values [cfg nt t*] (line->values ln i))
        (f acc cfg nt t*)))))

(define count-karst-lines
  (let ([lines++ (λ (acc cfg nt t*) (+ acc 1))])
    (λ (ps) (fold/karst ps #:f lines++ #:init 0))))

;; fold/mean : (All (A) Path-String (-> A Real A) #:init (U #f (-> Real A)) -> A)
(define fold/mean
  (let ([line->mean (λ (ln line-number)
                      (with-handlers ([exn:fail:read?
                                       (lambda (e)
                                         (printf "PARSE ERROR on line ~a~n" line-number)
                                         (raise e))])
                        (let ([times-str (caddr (parse-line ln))])
                          (mean (string->time* times-str)))))])
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

(define (filter-time* pf keep?)
  (define (keep-it acc t)
    (if (keep? t) (cons t acc) acc))
  (fold/mean (performance-info-src pf) keep-it #:init (λ (t) (keep-it '() t))))

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

(define (performance-info->sample* pi)
  (define src (performance-info-src pi))
  (define karst (and src (path-only src)))
  (unless karst
    (raise-argument-error 'performance-info->sample* "performance-info? with karst data" pi))
  (define sample* (karst-dir->sample* karst (performance-info-name pi)))
  (when (null? sample*)
    (raise-argument-error 'performance-info->sample* "performance-info? with sample data" pi))
  (define line*
    (with-handlers ([exn:fail:read? (λ (e) (printf "ERROR reading samples files '~a'~n" sample*) (raise e))])
      (map count-karst-lines sample*)))
  (define sample-size (car line*))
  (for ([s (in-list (cdr sample*))]
        [l (in-list (cdr line*))])
    (unless (= l sample-size)
      (raise-user-error 'performance-info->sample* "sample file ~a should have ~a lines, but has ~a instead" s sample-size l)))
  (cons sample-size sample*))

;; Doesn't really belong here, oh well
(define (fix-num-types sample-file)
  (printf "fixing types in '~a'..." sample-file)
  (define bm-name (infer-benchmark-name sample-file))
  (define bm (->benchmark-info bm-name))
  (define mc (benchmark->max-configuration bm))
  (define tmp (path-add-extension sample-file #".tmp"))
  (with-output-to-file tmp #:exists 'replace
    (λ ()
      (with-input-from-file sample-file
        (λ ()
          (for ([ln (in-lines)])
            (define str* (parse-line ln))
            (define cfg (string->configuration (car str*)))
            (define new-num-types (count-types cfg mc))
            (displayln (tab-join (list (car str*) (number->string new-num-types) (caddr str*))))
            (void))))))
  (copy-file tmp sample-file #t)
  (delete-file tmp)
  (void))

(define (count-types cfg max-cfg)
  (for/sum ([c (in-list cfg)]
            [x (in-list max-cfg)])
    (count-zero-bits (natural->bitstring c #:pad (log2 x)))))

(define (infer-benchmark-name sample-file)
  (define dir (or (path-only sample-file) (current-directory)))
  (define-values [base name must-be-dir] (split-path dir))
  (if (path? name)
    (path->string name)
    (raise-user-error 'fix-num-types "could not infer benchmark name from file '~a'" sample-file)))

(define (performance-info%sample pi new-src)
  (performance-info (performance-info-name pi)
                    new-src
                    (count-karst-lines new-src)
                    (performance-info-configs/module* pi)
                    (performance-info-python-runtime pi)
                    (performance-info-untyped-runtime pi)
                    (performance-info-typed-runtime pi)))

;; =============================================================================

(module+ test
  (require rackunit racket/runtime-path rackunit-abbrevs)

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
      (let () ;; filter-time* tests
        (check-equal? (filter-time* pf (λ (t) (= t 100))) (list 100))
        (check-equal? (filter-time* pf (λ (t) (= t 5))) (list 5))
        (check-equal? (filter-time* pf (λ (t) (< t 20))) (list 10 5))
        (void))
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

  (test-case "string->num-types"
    (check-equal?
      (string->num-types "8")
      8)
    (check-exn exn:fail:contract?
      (λ () (string->num-types "0.3")))
    (check-exn exn:fail:contract?
      (λ () (string->num-types "#f"))))

  (test-case "string->time*"
    (check-equal?
      (string->time* "[1, 2, 3]")
      '(1 2 3))
    (check-equal?
      (string->time* "[1.23, 4.554]")
      '(1.23 4.554))
    (check-exn exn:fail:contract?
      (λ () (string->time* "[]")))
    (check-exn exn:fail:contract?
      (λ () (string->time* "[1, -2]"))))

  (test-case "samples"
    (define (check-sample* bm-name)
      (define pi (benchmark->performance-info (->benchmark-info bm-name)))
      (define n+s* (performance-info->sample* pi))
      (define num-configs (car n+s*))
      (define s* (cdr n+s*))
      (check-true (< 0 (length s*)) "positive number of sample files")
      (define count* (map count-karst-lines s*))
      (check-true (apply = num-configs count*))
      (void))

    (check-sample* 'Espionage))

  (test-case "count-types"
    (check-apply* count-types
     ['(0) '(2)
      ==> 1]
     ['(1) '(2)
      ==> 0]
     ['(0 9) '(128 32)
      ==> 10]
     ['(2 16) '(128 32)
      ==> 10]
     ['(5 9) '(128 32)
      ==> 8]
     ['(6 18) '(128 32)
      ==> 8]
     ['(13 18) '(128 32)
      ==> 7]
     ['(14 17 30 2) '(16 64 32 4)
      ==> 7]
     ['(15 55 31 3) '(16 64 32 4)
      ==> 1]
     ['(3 12 21 0) '(16 64 32 4)
      ==> 10]
     ['(0 6 24 1) '(16 64 32 4)
      ==> 12]
     ['(0 6 8 1) '(16 64 32 4)
      ==> 13]
     ['(0 6 8 0) '(16 64 32 4)
      ==> 14]))
)

;; -----------------------------------------------------------------------------

(module+ main
  (require racket/cmdline)
  (define *fix-num-types?* (make-parameter #f))
  (command-line
   #:program "perf-info"
   #:once-each
   [("--fix-num-types") "Reset the type counts in the given files" (*fix-num-types?* #t)]
   #:args benchmark-name*
   (cond
    [(null? benchmark-name*)
     (printf "usage: rp:perf-info <benchmark-name> ...~n")]
    [(*fix-num-types?*)
     (void (map fix-num-types benchmark-name*))]
    [(null? (cdr benchmark-name*))
     (quick-performance-info (car benchmark-name*))]
    [else
     (for ([n (in-list benchmark-name*)])
       (with-handlers ([exn:fail:contract? (λ (e) (printf "WARNING: failure processing '~a'~n" n))])
         (quick-performance-info n)))])))

