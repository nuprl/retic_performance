#lang racket/base

;; Encapsulates info about a benchmark's performance

;; Command-line usage:
;;     raco rp-perf <benchmark-name> ...
;; Prints summary stats for each `<benchmark-name>`

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
   ;;  relative to the untyped configuration (aka typed/untyped-ratio)

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

   [unzip-karst-data
    (-> path-string? (or/c #f path-string?))]

   [count-better-with-types
    (-> (listof benchmark-info?) natural?)]
   ;; Count the number of typed configurations that run faster than
   ;;  some configuration with less types, across all the given benchmarks.

   [find-speedy-types
    (-> (listof benchmark-info?) (hash/c symbol? (listof (cons/c string? string?)) #:immutable #t #:flat? #t))]
   ;; Enumerate all pairs of configurations C0 C1 such that:
   ;; - C0 has fewer typed components than C1
   ;; - C0 is SLOWER than C1
   ;; Return a hash of all enumerations for all given benchmarks.

  )
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
  (only-in math/statistics
    mean)
  (only-in racket/list
    append*
    remove-duplicates
    list-set)
  (only-in racket/path
    path-only)
  (only-in racket/math
    natural?)
  (only-in file/gunzip
    gunzip)
  (only-in math/statistics
    mean)
  (only-in racket/string
    string-replace))

;; =============================================================================

(define HOME (retic-performance-home-dir))

(struct performance-info (
  name ;; Symbol, a benchmark name
  src  ;; Path-String, data from Karst
  num-configs
  python-runtime
  untyped-runtime
  typed-runtime
) #:transparent
  #:methods gen:custom-write
  [(define (write-proc v port mode)
     (fprintf port "#<performance-info:~a>" (performance-info-name v)))])

(define (make-performance-info name #:src k
                                    #:num-configurations num-configs
                                    #:python-runtime python
                                    #:untyped-retic-runtime base-retic
                                    #:typed-retic-runtime typed-retic)
  (performance-info name k num-configs python base-retic typed-retic))

(define (gunzip/cd ps)
  (define-values [base name _dir?] (split-path ps))
  (parameterize ([current-directory base])
    (gunzip name))
  (build-path base (file-remove-extension name)))

(define (unzip-karst-data kd)
  (let* ([tab.gz kd]
         [tab (and tab.gz (gunzip/cd tab.gz))])
    tab))

(define (->performance-info pi)
  (cond
   [(performance-info? pi)
    pi]
   [(benchmark-info? pi)
    (benchmark->performance-info pi)]
   [else
    (benchmark->performance-info (->benchmark-info pi))]))

(define (benchmark->performance-info bm)
  (define name (benchmark->name bm))
  (define kd (benchmark->karst-data bm))
  (define k (and kd (unzip-karst-data kd)))
  (define-values [num-configs configs/module* base-retic typed-retic]
    (if kd
      (scan-karst-file k)
      (values (benchmark->num-configurations bm)
              (benchmark->max-configuration bm)
              #f
              #f))) ;; So glad we are untyped
  (unless (and (= num-configs (benchmark->num-configurations bm))
               (equal? configs/module* (benchmark->max-configuration bm)))
    (raise-user-error 'benchmark->performance-info "fatal error processing ~a" name))
  (define python
    (mean (benchmark->python-data bm)))
  (make-performance-info name
    #:src k
    #:num-configurations num-configs
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
          (map add1 (unbox configs/module*))
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
  (map add1 (unbox configs/module*)))

(define (typed-configuration? cfg/mod*)
  (andmap zero? cfg/mod*))

(define (line->configuration-string str)
  (let ([str* (parse-line str)])
    (car str*)))

(define/contract (parse-line str)
  (-> string? (list/c string? string? string?))
  (tab-split str))

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
    (let ([baseline (performance-info-python-runtime pf)])
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

(define (all-configurations pi)
  (define (add-config H cfg _nt t*)
    (hash-set H cfg t*))
  (fold/karst pi #:init (make-immutable-hash) #:f add-config))

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
  (printf "- Python time : ~a~n" (performance-info-python-runtime pf))
  (printf "- untyped time : ~a~n" (performance-info-untyped-runtime pf))
  (printf "- typed time   : ~a~n" (performance-info-typed-runtime pf))
  (printf "- untyped/python : ~a~n" (untyped/python-ratio pf))
  (printf "- typed/untyped : ~a~n" (typed/retic-ratio pf))
  (printf "- typed/python : ~a~n" (typed/python-ratio pf))
  (printf "- min overhead : ~a~n" (min-overhead pf))
  (printf "- max overhead : ~a~n" (max-overhead pf))
  (printf "- avg overhead : ~a~n" (mean-overhead pf))
  (let ([d2 ((deliverable 2) pf)])
    (printf "- 2 deliv.     : ~a (~a%)~n" d2 (rnd (pct d2 nc))))
  (let ([d5 ((deliverable 5) pf)])
    (printf "- 5 deliv.     : ~a (~a%)~n" d5 (rnd (pct d5 nc))))
  (void))

(define (performance-info->sample* pi)
  (define sample* (karst-dir->sample* (retic-performance-karst-dir HOME) (performance-info-name pi)))
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
  (printf "fixing types in '~a'...~n" sample-file)
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
    (if (= 1 x) ;; TODO right place to test this? Checking for files with ZERO type annotations. Really the file should be in the "both" directory
      0
      (count-zero-bits (natural->bitstring c #:pad (log2 x))))))

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
                    (performance-info-python-runtime pi)
                    (performance-info-untyped-runtime pi)
                    (performance-info-typed-runtime pi)))

(define (count-better-with-types bm*)
  (for/sum ([n+c* (in-list (better-with-types bm*))])
    (length (cdr n+c*))))

(define (better-with-types bm*)
  (for/list ([(n cc*) (in-hash (find-speedy-types bm*))])
    (cons n (remove-duplicates (map cdr cc*)))))

(define (find-speedy-types bm*)
  (for/hash ([bm (in-list bm*)])
    (define name (benchmark->name bm))
    (define mc (benchmark->max-configuration bm))
    (define pi (benchmark->performance-info bm))
    (when (< (expt 2 17) (performance-info-num-configs pi))
      (raise-user-error 'find-speedy-types "benchmark '~a' is too large" name))
    (define AC (all-configurations pi))
    (define speedy-pairs
      (for*/list ([(c0 t0*) (in-hash AC)]
                  [c1 (in-list (successors c0 mc))]
                  #:when (significantly-faster? (hash-ref AC c1) t0*))
        (cons (configuration->string c0) (configuration->string c1))))
    (values name speedy-pairs)))

(define (significantly-faster? t1* t0*)
  (define u0 (mean t0*))
  (define u1 (mean t1*))
  (and (< u1 u0)
       (let ([c0 (confidence-interval t0*)]
             [c1 (confidence-interval t1*)])
         (and (< (+ u1 c1) u0)
              (< u1 (- u0 c0))))))

(define (successors cfg max-config)
  (append*
    (for/list ([mod-id (in-list cfg)]
               [mod-num-bits (in-list max-config)]
               [i (in-naturals)])
      (define bits (natural->bitstring mod-id #:pad (log2 mod-num-bits)))
      (for/list ([c (in-string bits)]
                 [j (in-naturals)]
                 #:when (eq? c #\1))
        (list-set cfg i
          (bitstring->natural (string-set bits j #\0)))))))

(define (string-set str index new-char)
  (define str2 (string-copy str))
  (string-set! str2 index new-char)
  str2)

;; =============================================================================

(module+ test
  (require rackunit racket/runtime-path rackunit-abbrevs)

  (define-runtime-path karst-example "./test/karst-example_tab.gz")

  (test-case "benchmark->performance-info:example-data"
    (define karst-example-gunzip (gunzip/cd karst-example))
    (define-values [num-configs configs/module* base-retic typed-retic]
      (scan-karst-file karst-example-gunzip))
    (check-equal? num-configs 4)
    (check-equal? configs/module* '(2 2))
    (check-equal? base-retic 10)
    (check-equal? typed-retic 20)

    (let ([pf (make-performance-info 'example
                #:src karst-example-gunzip
                #:num-configurations num-configs
                #:python-runtime base-retic
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

  (test-case "benchmark->performance-info:no-data"
    (check-pred performance-info?
      (benchmark->performance-info (->benchmark-info 'stats))))

  ;; general correctness/sanity for a real program
  (let* ([bm (->benchmark-info 'Espionage)]
         [pf (benchmark->performance-info bm)])
    (test-case "performance-info:spot-check"
      (check-true (performance-info? pf))
      (check <= (performance-info-python-runtime pf) (performance-info-untyped-runtime pf))
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
     ['(0) '(1)
      ==> 0]
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

  (test-case "successors"
    (check-apply* successors
     ['(1) '(32)
      ==> '((0))]
     ['(2) '(32)
      ==> '((0))]
     ['(16) '(32)
      ==> '((0))]
     ['(3) '(32)
      ==> '((1) (2))]))

  (test-case "string-set"
    (check-apply* string-set
     ["hello" 0 #\H
      ==> "Hello"]
     ["hello" 4 #\H
      ==> "hellH"]))

  (let ()
    (define futen (->benchmark-info 'futen))
    (define spectralnorm (->benchmark-info 'spectralnorm))
    (define call_method (->benchmark-info 'call_method))
    (define fannkuch (->benchmark-info 'fannkuch))

    (test-case "better-with-types"
      (check-apply* count-better-with-types
       [(list fannkuch) ==> 0]
       [(list spectralnorm) ==> 13]
       [(list call_method) ==> 66]
       [(list futen spectralnorm fannkuch) ==> 24511]))

    (test-case "find-speedy-types"
      (check-apply* find-speedy-types
       [(list fannkuch)
        ==> (make-immutable-hash '((fannkuch . ())))]
       [(list fannkuch spectralnorm)
        ==> (make-immutable-hash
              '((fannkuch . ())
                (spectralnorm . (("10" . "2") ("23" . "21") ("26" . "10")
                                 ("26" . "18") ("28" . "12") ("28" . "20")
                                 ("30" . "14") ("30" . "22") ("24" . "8")
                                 ("24" . "16") ("16" . "0") ("18" . "2")
                                 ("20" . "4") ("12" . "4") ("8" . "0")
                                 ("14" . "6") ("22" . "6")))))])))
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

