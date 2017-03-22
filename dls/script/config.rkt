#lang racket/base

;; Parameters, configuration functions

(provide
  retic-performance-home-dir
  retic-performance-benchmarks-dir
  retic-performance-karst-dir
  benchmark-dir->typed-dir

  is-benchmark-folder?)

(require
  "system.rkt")

;; =============================================================================

(define BENCHMARKS "benchmarks")
(define DATA "data")
(define KARST "karst")
(define TYPED "typed")

(define (retic-performance-home-dir)
  (shell "git" '("rev-parse" "--show-toplevel")))

(define (retic-performance-benchmarks-dir home-dir)
  (build-path home-dir BENCHMARKS))

(define (retic-performance-data-dir home-dir)
  (build-path home-dir DATA))

(define (retic-performance-karst-dir home-dir)
  (build-path (retic-performance-data-dir home-dir) KARST))

(define (benchmark-dir->typed-dir bm-dir)
  (build-path bm-dir TYPED))

(define (is-benchmark-folder? p)
  (and (path-string? p)
       (directory-exists? p)
       (directory-exists? (build-path p TYPED))))

;; =============================================================================

(module+ test
  (require rackunit)

  (define home (retic-performance-home-dir))

  (test-case "home-dir"
    (check-pred directory-exists? home))

  (test-case "is-benchmark-folder?"
    (define futen (build-path (retic-performance-benchmarks-dir home) "futen"))
    (check-true (is-benchmark-folder? futen))
    (check-false (is-benchmark-folder? home))))

