#lang racket/base

(provide
  tab-split
  path-string->string
  rnd
  pct)

(require
  (only-in racket/format
    ~r)
  (only-in racket/string
    string-split))

;; =============================================================================

(define TAB "\t")

(define (path-string->string ps)
  (if (string? ps) ps (path->string ps)))

(define (tab-split str)
  (string-split str TAB))

(define (rnd n)
  (~r n #:precision 2))

(define (pct part total)
  (* 100 (/ part total)))
