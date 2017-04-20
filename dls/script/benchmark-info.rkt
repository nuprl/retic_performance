#lang racket/base

;; Static information about the benchmark programs.

(require racket/contract)
(provide
  DLS-2014-BENCHMARK-NAMES
  POPL-2017-BENCHMARK-NAMES
  DLS-2017-BENCHMARK-NAMES
  (contract-out
    [benchmark-info?
     (-> any/c boolean?)]
    ;; Predicate for the `benchmark-info` struct

    [rename benchmark-info-name benchmark->name
     (-> benchmark-info? symbol?)]
    ;; Return the name of a benchmark

    [rename benchmark-info-module* benchmark->module*
     (-> benchmark-info? (listof string?))]
    ;; Return the names of all modules in the benchmark

    [rename benchmark-info-src benchmark->src
     (-> benchmark-info? path-string?)]
    ;; Return a path to this benchmark's directory

    [benchmark->num-modules
     (-> benchmark-info? natural?)]
    ;; Return the number of modules in the given benchmark

    [benchmark->num-configurations
     (-> benchmark-info? natural?)]
    ;; Return the number of configurations in the benchmark

    [benchmark->max-configuration
     (-> benchmark-info? configuration?)]
    ;; Return the largest-plus-one configuration in the benchmark

    [benchmark->sloc
     (-> benchmark-info? natural?)]
    ;; Estimate the source-lines-of-code (SLOC) in the benchmark's modules

    [benchmark->karst-data
     (-> benchmark-info? (or/c #f path-string?))]
    ;; Return a path to the benchmark's data from the Karst cluster, if any

    [benchmark->python-data
     (-> benchmark-info? (or/c (listof real?) #f))]
    ;; Return the benchmark's Python runtimes, if any

    [all-benchmarks
     (-> (listof benchmark-info?))]
    ;; Return a list of all known benchmarks

    [->benchmark-info
     (-> (or/c symbol? string? path-string?) benchmark-info?)]
    ;; Return the benchmark that the given data refers to

    [configuration->natural
     (-> benchmark-info? configuration? natural?)]
    ;; Map a configuration to a natural number,
    ;;  isomorphism with natural->configuration

    [configuration<?
     (-> configuration? configuration? boolean?)]
    ;; True if first argument is lexicographically less than the second,
    ;;  assumes arguments of equal length

    [configuration->string
     (-> configuration? string?)]
    ;; Render a configuration as a string, e.g., 0-0-7

    [natural->configuration
     (-> benchmark-info? exact-nonnegative-integer? configuration?)]
    ;; If second argument is `N`, return the `N`-th configuration
    ;;  according to some deterministic, undocumented order

    [benchmark-info->python-info
     (-> benchmark-info? python-info?)]
))

(require
  "config.rkt"
  "python.rkt"
  "util.rkt"
  file/glob
  (only-in racket/math
    natural?)
  (only-in racket/path
    file-name-from-path)
  (only-in racket/string
    string-join
    string-contains?)
  (only-in racket/format
    ~a))

;; =============================================================================

(define HOME (retic-performance-home-dir))

(define DLS-2014-BENCHMARK-NAMES '(
  futen
  http2
  slowSHA
))
(define POPL-2017-BENCHMARK-NAMES '(
  call_method
  call_method_slots
  call_simple
  chaos
  fannkuch
  float
  go
  meteor
  nbody
  nqueens
  pidigits
  pystone
  spectralnorm
))
(define DLS-2017-BENCHMARK-NAMES '(
  Espionage
;  Evolution
;  sample_fsm
  PythonFlow
  take5
))

(struct benchmark-info (
  module* ;; (Listof String)
  name    ;; Symbol
  src     ;; Path-String
  cfg*    ;; Configuration (the max. configuration)
) #:transparent
  #:methods gen:custom-write
  [(define (write-proc bm port mode)
     (fprintf port "#<benchmark-info:~a>" (benchmark-info-name bm)))])

;; -----------------------------------------------------------------------------

(define (make-benchmark-info name #:module* module* #:src src)
  (define cfg* (->max-configuration src module*))
  (benchmark-info module* name src cfg*))

(define (benchmark->num-modules bm)
  (length (benchmark-info-module* bm)))

(define (benchmark->num-functions bm)
  (raise-user-error 'benchmark->num-functions "not implemented"))

(define (benchmark->num-classes bm)
  (raise-user-error 'benchmark->num-classes "not implemented"))

(define (benchmark->num-methods bm)
  (raise-user-error 'useless))

(define (benchmark->num-parameters bm)
  (raise-user-error 'num-params "not implemented"))

(define (benchmark->typed-dir bm)
  (benchmark-dir->typed-dir (benchmark-info-src bm)))

(define (benchmark->max-configuration bm)
  (benchmark-info-cfg* bm))

(define (benchmark->num-configurations bm)
  (for/product ([n (in-list (benchmark->max-configuration bm))])
    n))

(define (configuration<? c0 c1)
  (for/and ([v0 (in-list c0)]
            [v1 (in-list c1)])
    (< v0 v1)))

(define (->max-configuration src mod*)
  (or (benchmark-dir->max-configuration src mod*)
      (python-info->max-configuration (benchmark-dir->python-info src))))

(define (benchmark-dir->max-configuration ps mod*)
  (and (directory-exists? ps)
       (let ([cfg-rev*
              (for/fold ([acc '()])
                        ([m (in-list mod*)])
                (define m-dir (build-path ps CONFIG-DIR (path-replace-extension m #"")))
                (and acc
                     (directory-exists? m-dir)
                     (cons (length (glob (build-path m-dir "*.py"))) acc)))])
         (and cfg-rev* (reverse cfg-rev*)))))

(define (benchmark->sloc bm)
  (define ty (benchmark->typed-dir bm))
  (for/sum ([m (in-list (benchmark-info-module* bm))])
    (python-sloc (build-path ty m))))

(define (benchmark-info->python-info bm)
  (benchmark-dir->python-info (benchmark-info-src bm)))

;; benchmark->karst-data : (-> benchmark-info? (U #f path-string?))
(define (benchmark->karst-data bm)
  (define name (symbol->string (benchmark-info-name bm)))
  (define karst-path
    (path-add-extension (build-path (retic-performance-karst-dir HOME) name) "_tab.gz"))
  (and (file-exists? karst-path)
       karst-path))

(define (benchmark->python-data bm)
  (define name (symbol->string (benchmark-info-name bm)))
  (define python-path
    (path-add-extension (build-path (retic-performance-karst-dir HOME) name) "_untyped.tab"))
  (if (not (file-exists? python-path))
    (begin (printf "WARNING: no Python data for benchmark '~a' at location '~a'~n" name python-path)
           '(1))
    (with-input-from-file python-path
      (λ ()
        (let loop ()
          (define v (read-line))
          (if (eof-object? v)
            '()
            (let ([n (string->number v)])
              (if n
                (cons n (loop))
                (raise-user-error 'python-data "corrupted data file '~a', please fix" python-path)))))))))

(define (benchmark->exploded bm)
  (define d (benchmark-dir->benchmarks-dir (benchmark-info-src bm)))
  (and (directory-exists? d)
       (for/and ([m (in-list (benchmark-info-module* bm))])
         (directory-exists? (build-path d (path-replace-extension m #""))))
       d))

(define (all-benchmarks)
  (for/list ([bm-name (in-list (append DLS-2014-BENCHMARK-NAMES
                                       POPL-2017-BENCHMARK-NAMES
                                       DLS-2017-BENCHMARK-NAMES))])
    (->benchmark-info bm-name)))

(define (->benchmark-info bm-name)
  (cond
   [(simple-name? bm-name)
    (define bm-dir (build-path (retic-performance-benchmarks-dir HOME) (~a bm-name)))
    (unless (directory-exists? bm-dir)
      (raise-argument-error '->benchmark-info "benchmark name" bm-name))
    (->benchmark-info bm-dir)]
   [(is-benchmark-directory? bm-name)
    (path->benchmark-info bm-name)]
   [else
    (raise-argument-error '->benchmark-info "path to benchmark folder" bm-name)]))

(define (path->benchmark-info src)
  (define simple-name (path->simple-name src))
  (define mod*
    (for/list ([p (in-list (glob (build-path (benchmark-dir->typed-dir src) "*")))])
      (path->string (file-name-from-path p))))
  (make-benchmark-info simple-name
    #:module* mod*
    #:src src))

(define (path->simple-name src)
  (string->symbol (path-string->string (file-name-from-path src))))

(define (simple-name? bm-name)
  (or (symbol? bm-name)
      (and (string? bm-name)
           (not (string-contains? bm-name "/")))))

(define (configuration->string cfg)
  (string-join (map number->string cfg) "-"))

(define (configuration->natural bm cfg)
  (define mc0 (benchmark->max-configuration bm))
  (define-values [mc-rev cfg-rev]
    (let loop ([mc mc0]
               [cfg cfg]
               [mc-rev '()]
               [cfg-rev '()])
      (cond
       [(and (null? mc) (null? cfg))
        (values mc-rev cfg-rev)]
       [(or (null? mc) (null? cfg))
        (raise-argument-error 'configuration->natural (format "~a-digit configuration" (length mc0)) 1 bm cfg)]
       [else
        (loop (cdr mc) (cdr cfg) (cons (car mc) mc-rev) (cons (car cfg) cfg-rev))])))
  (define-values [n offset]
    (for/fold ([acc 0]
               [offset 1])
              ([base (in-list mc-rev)]
               [digit (in-list cfg-rev)]
               [pos (in-naturals)])
      (when (< digit 0)
        (raise-argument-error 'configuration->natural (format "exact-nonnegative-integer? (position ~a)" pos) 1 bm cfg))
      (unless (< digit base)
        (raise-argument-error 'configuration->natural (format "configuration element too large at position ~a" pos) 1 bm cfg))
      (values (+ acc (* digit offset))
              (* base offset))))
  n)

;; natural->configuration : benchmark-info? natural? -> configuration?
;;
;; The max configuration for a benchmark defines a sort-of base,
;;  instead of base N numbers its base A-B-C-.... (idk what to call that)
;; Suppose the max configuration is `N1-N2-N3`,
;; - the max number representable in this base is `(N1*N2*N3)-1`
;; - all numbers in this base can be represented as "bitstrings" of 3 bits,
;;   where the first bit is less than `N1`,
;;   and the second bit it less than `N2`,
;;   and the third bit is less than `N3`
;; - a way to derive a bitstring is to pick `k1` `k2` `k3` in order, such that
;;   - `(k1 * N2 * N3) < N1*N2*N3` and `((k1 + 1) * N2 * N3) >= N1*N2*N3`
;;   - `(k2 * N3) < ((N1*N2*N3)-(k1 * N2 * N3))` and `((k1 + 1) * N3) >= ((N1*N2*N3)-(k1 * N2 * N3))`
;;   - ditto for `k3 * 1`
;;
;; So much hot air. Time to call a mathematician?
;;
;; Maybe, simpler to expand the configuration to the (classic) bitstring it
;;  stands for and go from there. Max config -> bitstring -> natural to bits
;;  -> chunk bits into numbers
(define (natural->configuration bm n)
  (when (< n 0)
    (raise-argument-error 'natural->configuration "exact-nonnegative-integer?" n))
  (define max-config (benchmark->max-configuration bm))
  (define offset*
    (for/fold ([acc '(1)])
              ([base-k (in-list (reverse (cdr max-config)))])
      (cons (* base-k (car acc)) acc)))
  (define max-natural
    (* (car max-config) (car offset*)))
  (unless (< n max-natural)
    (raise-argument-error 'natural->configuration (format "integer less than ~a" max-natural) 1 bm n))
  (define num-left (box n))
  (for/list ([offset-k (in-list offset*)])
    (for/first ([i (in-naturals)]
                #:when (> (* (+ i 1) offset-k) (unbox num-left)))
      (begin (set-box! num-left (- (unbox num-left) (* i offset-k)))
             i))))

;; =============================================================================

(module+ main
  (require racket/cmdline "python.rkt")
  (command-line
    #:program "rp-info"
    #:args benchmark-name*
    (for ([n (in-list benchmark-name*)])
      (define bm (->benchmark-info n))
      (define py (benchmark-info->python-info bm))
      (printf "~a : ~a configs~n" n (benchmark->num-configurations bm))
      (printf "  max cfg : ~a~n" (benchmark->max-configuration bm))
      (printf "  #modules : ~a~n" (python-info->num-modules py))
      (printf "  #functions : ~a~n" (python-info->num-functions py))
      (printf "  #classes : ~a~n" (python-info->num-classes py))
      (printf "  #methods : ~a~n" (python-info->num-methods py)))))

;; =============================================================================

(module+ test
  (require rackunit rackunit-abbrevs)

  (test-case "->benchmark-info"
    (let* ([n (car DLS-2014-BENCHMARK-NAMES)]
           [bm (->benchmark-info n)]
           [k (benchmark->karst-data bm)]
           [small-loc 50])
      (check-equal? (benchmark-info-name bm) n)
      (check-true (and (member "main.py" (benchmark-info-module* bm)) #t))
      (check-equal?
        (benchmark->num-modules bm)
        (length (benchmark-info-module* bm)))
      (check-pred file-exists? (benchmark->karst-data bm))
      (let ([pd (benchmark->python-data bm)])
        (check-pred list? pd)
        (check < 1 (length pd))
        (check-true (andmap real? pd)))
      (check > (benchmark->sloc bm) small-loc
        (format "expected benchmark '~a' to contain at least ~a LOC" n small-loc))
      ))

  (test-case "->benchmark-info:fail"
    (check-exn exn:fail:contract?
      (λ () (->benchmark-info 42)))
    (check-exn exn:fail:contract?
      (λ () (->benchmark-info '|hello world|))))

  (test-case "path->simple-name"
    (check-equal?
      (path->simple-name "hello/world")
      'world)
    (check-equal?
      (path->simple-name (string->path "hello/world"))
      'world))

  (test-case "simple-name?"
    (check-true (simple-name? "hello"))
    (check-true (simple-name? 'hello))
    (check-false (simple-name? "hello/world")))

  (test-case "max-configuration"
    (define (check-max-configuration bm-name expected)
      (define bm (->benchmark-info bm-name))
      (define src (benchmark-info-src bm))
      (define mod* (benchmark-info-module* bm))
      (define c1 (->max-configuration src mod*))
      (define c2 (benchmark-dir->max-configuration src mod*))
      (define c3 (python-info->max-configuration (benchmark-dir->python-info src)))
      (check-equal? c1 c2
        (format "~a : ->max = ~a, benchmark-dir->max = ~a" src c1 c2))
      (check-equal? c2 c3)
      (check-equal? c3 expected))

    (check-max-configuration 'fannkuch '(2))
    (check-max-configuration 'Espionage '(128 32))
    (check-max-configuration 'slowSHA '(16 64 32 4)))

  (test-case "configuration<?"
    (check-apply* configuration<?
     ['(0) '(1)
      ==> #t]
     ['(0) '(0)
      ==> #f]
     ['(2 2 4) '(3 3 9)
      ==> #t]
     ['(5 2 4) '(3 3 9)
      ==> #f]))

  (test-case "configuration->string"
    (check-apply* configuration->string
     ['()
      ==> ""]
     ['(3)
      ==> "3"]
     ['(1 2 3)
      ==> "1-2-3"]))

  (test-case "natural<->configuration"
    (define (check-natural<->configuration bm-name in/out* err-nat* err-cfg*)
      (define bm (->benchmark-info bm-name))
      (for ([io (in-list in/out*)])
        (define n (car io))
        (define cfg (cadr io))
        (define msg1 (format "(natural->configuration ~a ~a)" bm-name n))
        (define msg2 (format "(configuration->natural ~a ~a)" bm-name cfg))
        (check-equal? (natural->configuration bm n) cfg msg1)
        (check-equal? (configuration->natural bm cfg) n msg2)
        (void))
      (for ([e (in-list err-nat*)])
        (define msg (format "(natural->configuration ~a ~a)" bm-name e))
        (check-exn exn:fail:contract?
          (lambda () (natural->configuration bm e))
          msg))
      (for ([e (in-list err-cfg*)])
        (define msg (format "(configuration->natural ~a ~a)" bm-name e))
        (check-exn exn:fail:contract?
          (lambda () (configuration->natural bm e))
          msg)))

    (check-natural<->configuration 'nqueens
      '((0 (0))
        (1 (1))
        (2 (2))
        (3 (3)))
      '(4 -1)
      '((4) (-1)))

    (check-natural<->configuration 'futen
      '((0 (0 0 0))
        (6 (0 0 6))
        (1025 (0 1 1))
        (2048 (1 0 0))
        (2050 (1 0 2)))
      (list (* 16 2 1024))
      '((0 0 1025) (0 0 1024) ()))

    (check-natural<->configuration 'slowSHA
      `((0 (0 0 0 0))
        (4 (0 0 1 0))
        (128 (0 1 0 0))
        (8192 (1 0 0 0))
        (16385 (2 0 0 1))
        (32768 (4 0 0 0))
        (,(sub1 (* 16 64 32 4)) (15 63 31 3)))
      (list (* 16 64 32 4))
      '((1 1 1 5) (16 64 32 4) (16 11 12 3)))
  )

  (test-case "benchmark->num-configurations"
    (check-apply* benchmark->num-configurations
     [(->benchmark-info 'futen)
      ==> (* 16 2 1024)]
     [(->benchmark-info 'fannkuch)
      ==> 2]))

  (test-case "benchmark-info->python-info"
    (define (check-python-info bm)
      (define py (benchmark-info->python-info bm))
      (check-pred python-info? py)
      (check-equal? (benchmark-info-module* bm) (python-info->module* py)
        (format "~a module names" (benchmark-info-name bm)))
      (check-equal? (benchmark->max-configuration bm) (python-info->max-configuration py)
        (format "~a max configuration" (benchmark-info-name bm)))
      (void))

    (for-each check-python-info (all-benchmarks)))

)
