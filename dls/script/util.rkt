#lang racket/base

;; Utility functions.
;; Maybe these should be somewhere more public.

(require racket/contract)
(provide
  (contract-out
    [tab-split
     (-> string? (listof string?))]
    ;; Split a list of string by its tab characters

    [path-string->string
     (-> path-string? string?)]
    ;; Convert a string or a path to a string

    [rnd
     (-> real? string?)]
    ;; Render a number as a string, round to 2 decimal places.

    [pct
     (-> real? real? real?)]
    ;; `(pct 1 4)` returns 25

    [file-remove-extension
     (-> path-string? path-string?)]
    ;; Removes a Racket-added extension from a filename.
    ;; `(file-remove-extension "foo_tab.gz")` returns "foo.tab"
))

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

(define (string-last-index-of str c)
  (for/fold ([acc #f])
            ([c2 (in-string str)]
             [i (in-naturals)])
    (if (eq? c c2) i acc)))

(define (file-remove-extension fn)
  (define str (path-string->string fn))
  (define no-ext (path->string (path-replace-extension str #"")))
  (define i (string-last-index-of no-ext #\_))
  (string-append (substring no-ext 0 i) "." (substring no-ext (+ i 1))))

;; =============================================================================

(module+ test
  (require rackunit)

  (test-case "path-string->string"
    (check-equal? (path-string->string "hi") "hi")
    (check-equal? (path-string->string (string->path "hi")) "hi"))

  (test-case "tab-split"
    (check-equal? (tab-split "hello") '("hello"))
    (check-equal? (tab-split "dr racket") '("dr racket"))
    (check-equal? (tab-split "dr\tracket") '("dr" "racket")))

  (test-case "rnd"
    (check-equal? (rnd 2) "2")
    (check-equal? (rnd 1/3) "0.33"))

  (test-case "pct"
    (check-equal? (pct 1 2) 50)
    (check-equal? (rnd (pct 1 3)) "33.33"))

  (test-case "string-last-index-of"
    (check-equal? (string-last-index-of "hello" #\h) 0)
    (check-equal? (string-last-index-of "hello" #\o) 4)
    (check-equal? (string-last-index-of "hello" #\l) 3)
    (check-equal? (string-last-index-of "hello" #\Q) #f))

  (test-case "file-remove-extension"
    (check-equal? (file-remove-extension "foo_tab.gz") "foo.tab")
    (check-equal? (file-remove-extension "a_b.c") "a.b"))
)
