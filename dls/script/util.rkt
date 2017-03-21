#lang racket/base

(provide
  tab-split
  path-string->string)

(require
  (only-in racket/string
    string-split))

;; =============================================================================

(define TAB "\t")

(define (path-string->string ps)
  (if (string? ps) ps (path->string ps)))

(define (tab-split str)
  (string-split str TAB))
