#lang racket/base

;; Static information about the benchmark programs.

;; TODO
;; - num typed functions (in experiment)
;; - num function parameters
;; - num classes
;; - num methods

(require racket/contract)
(provide
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

    [benchmark->sloc
     (-> benchmark-info? natural?)]
    ;; Estimate the source-lines-of-code (SLOC) in the benchmark's modules

    [benchmark->karst-data
     (-> benchmark-info? (or/c #f path-string?))]
    ;; Return a path to the benchmark's data from the Karst cluster, if any

    [all-benchmarks
     (-> (listof benchmark-info?))]
    ;; Return a list of all known benchmarks

    [->benchmark-info
     (-> (or/c symbol? string? path-string?) benchmark-info?)]
    ;; Return the benchmark that the given data refers to
  )

  make-benchmark-info
  ;; Low-level constructor. Provided for testing.
)

(require
  "config.rkt"
  "python.rkt"
  "util.rkt"
  (only-in racket/math
    natural?)
  (only-in racket/path
    file-name-from-path)
  (only-in racket/string
    string-contains?)
  (only-in racket/format
    ~a))

;; =============================================================================

(define HOME (retic-performance-home-dir))

(define DLS-2014-BENCHMARK-NAMES '(
  PythonFlow ;; TODO where did this come from?
  futen ;; TODO from where?
  http2 ;; TODO from where?
  slowSHA
))
(define POPL-2017-BENCHMARK-NAMES '(
  call_method
  call_method_slots
  call_simple
;  chaos
;  fannkuch
  float
  go
  meteor
  nbody
;  nqueens
;  pidigits
;  pystone
  spectralnorm
))
(define DLS-2017-BENCHMARK-NAMES '(
  Espionage
;  Evolution
;  sample_fsm_python
  take5
))

(struct benchmark-info (
  module* ;; (Listof String)
  name    ;; Symbol
  src     ;; Path-String
) #:transparent )

(define (make-benchmark-info name #:module* module* #:src src)
  (benchmark-info module* name src))

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

(define (benchmark->sloc bm)
  (define ty (benchmark->typed-dir bm))
  (for/sum ([m (in-list (benchmark-info-module* bm))])
    (python-sloc (build-path ty m))))

;; benchmark->karst-data : (-> benchmark-info? (U #f path-string?))
(define (benchmark->karst-data bm)
  (define name (symbol->string (benchmark-info-name bm)))
  (define karst-path
    (path-add-extension (build-path (retic-performance-karst-dir HOME) name) "_tab.gz"))
  (and (file-exists? karst-path)
       karst-path))

(define (all-benchmarks)
  (for/list ([bm-name (in-list (append DLS-2014-BENCHMARK-NAMES
                                       POPL-2017-BENCHMARK-NAMES
                                       DLS-2017-BENCHMARK-NAMES))])
    (->benchmark-info bm-name)))

(define (->benchmark-info bm-name)
  (cond
   [(simple-name? bm-name)
    (->benchmark-info (build-path (retic-performance-benchmarks-dir HOME) (~a bm-name)))]
   [(is-benchmark-directory? bm-name)
    (path->benchmark-info bm-name)]
   [else
    (raise-argument-error '->benchmark-info "path to benchmark folder" bm-name)]))

(define (path->benchmark-info src)
  (define simple-name (path->simple-name src))
  (define mod*
    (for/list ([p (in-list (directory-list (benchmark-dir->typed-dir src)))])
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

;; =============================================================================

(module+ test
  (require rackunit)

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
      (check-pred benchmark->karst-data bm)
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

)
