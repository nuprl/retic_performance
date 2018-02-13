#lang racket/base

;; Parameters, configuration functions

(require racket/contract)
(provide
  CONFIG-DIR

  (contract-out
    [retic-performance-home-dir
     (-> path-string?)]
    ;; Return a path to the root of your `retic_performance` repo.
    ;; MUST BE CALLED from inside the repo.

    [retic-performance-benchmarks-dir
     (-> path-string? path-string?)]
    ;; Build a path to your benchmarks directory
    ;;  given a path to your repo directory

    [retic-performance-karst-dir
     (-> path-string? path-string?)]
    ;; Build a path to your Karst data directory
    ;;  given a path to your repo directory

    [benchmark-dir->typed-dir
     (-> path-string? path-string?)]
    ;; Build a path to a benchmark's typed code directory
    ;;  given a path to the benchmark's root directory

    [karst-dir->sample*
     (-> path-string? symbol? (or/c #f (listof path-string?)))]

    [benchmark-dir->name
     (-> is-benchmark-directory? symbol?)]

    [benchmark-dir->benchmarks-dir
     (-> path-string? path-string?)]
    ;; Build a path to a benchmark's exploded configurations directory,
    ;;  given a path to the benchmark's root directory

    [is-benchmark-directory?
     (-> any/c boolean?)]
    ;; Return `#true` if the given value is a benchmark's root directory
))

(require
  "system.rkt"
  file/glob
  racket/runtime-path)

;; =============================================================================

(define BENCHMARKS "benchmarks")
(define CONFIG-DIR "Benchmark")
(define DATA "data")
(define KARST "karst")
(define TYPED "typed")
(define SAMPLE "sample")

(define-runtime-path PWD ".")
(define-runtime-path RP_HOME "../")

(define (retic-performance-home-dir)
  (if (find-executable-path "git")
    (parameterize ([current-directory PWD])
      (shell "git" '("rev-parse" "--show-toplevel")))
    RP_HOME))

(define (retic-performance-benchmarks-dir home-dir)
  (build-path home-dir BENCHMARKS))

(define (retic-performance-data-dir home-dir)
  (build-path home-dir DATA))

(define (retic-performance-karst-dir home-dir)
  (build-path (retic-performance-data-dir home-dir) KARST))

(define (benchmark-dir->typed-dir bm-dir)
  (build-path bm-dir TYPED))

(define (benchmark-dir->benchmarks-dir bm-dir)
  (build-path bm-dir CONFIG-DIR))

(define (karst-dir->sample* k-dir bm-name)
  (define prefix (build-path k-dir SAMPLE (symbol->string bm-name)))
  (and (directory-exists? prefix)
       (glob (build-path prefix "sample*.tab"))))

(define (is-benchmark-directory? p)
  (and (path-string? p)
       (directory-exists? p)
       (directory-exists? (build-path p TYPED))))

(define (benchmark-dir->name bm-dir)
  (define-values [base name must-be-dir] (split-path bm-dir))
  (string->symbol (path->string name)))

;; =============================================================================

(module+ test
  (require rackunit)

  (define CI? (getenv "CI"))

  (unless CI?
    (define home (retic-performance-home-dir))
    (test-case "home-dir"
      (check-pred directory-exists? home))
    (test-case "is-benchmark-directory?"
      (define futen (build-path (retic-performance-benchmarks-dir home) "futen"))
      (check-true (is-benchmark-directory? futen))
      (check-false (is-benchmark-directory? home)))
    (test-case "benchmark-dir->name"
      (check-equal? (benchmark-dir->name "foo/bar/baz/") 'baz)))
)
