#lang racket/base

;; Racket interface to Python code
;;  for querying static characteristics

(require racket/contract)
(provide
  (contract-out
   [python-sloc
    (-> python-path? exact-nonnegative-integer?)]
   ;; Count source lines of code in a python module

   [python-path?
    (-> any/c boolean?)]
   ;; Return `#t` if the given path string ends in a `.py` suffix, and `#f` otherwise
))

(require
  "system.rkt"
  "util.rkt"
  (only-in racket/path
    path-get-extension)
  (only-in racket/list
    last)
  (only-in racket/string
    string-join
    string-split))

;; =============================================================================

(define (python-path? ps)
  (and (path-string? ps)
       (equal? (path-get-extension ps) #".py")))

(define (python-sloc ps)
  (define ps-str (path-string->string ps))
  (define arg* (list "--details" "--wide" ps-str))
  (define all-output (shell "sloccount" arg*))
  (define cmd-str (string-join (cons "sloccount" arg*)))
  (define col* (string-split (last (string-split all-output "\n"))))
  (define-values [loc lang _src sloccount-ps]
    (if (= 4 (length col*))
      (apply values col*)
      (raise-user-error 'python-sloc
        "failed to parse output of 'sloccount ~a'~n  full output: ~a"
        ps
        all-output)))
  (unless (string=? lang "python")
    (raise-user-error 'python-sloc
      "expected SLOCCOUNT to return 'python' language, got '~a' instead.~n  original command: ~a"
      lang cmd-str))
  (unless (string=? sloccount-ps ps-str)
    (raise-user-error 'python-sloc
      "expected SLOCCOUNT to report path string '~a', got '~a' instead.~nSomething is very wrong!"
      ps-str
      sloccount-ps))
  (define n (string->number loc))
  (unless (exact-nonnegative-integer? n)
    (raise-user-error 'python-sloc
      "expected SLOCCOUNT to report a natural number of lines, got '~a'.~nSomething is very wrong."
      loc))
  n)

;; =============================================================================

(module+ test
  (require rackunit racket/runtime-path)

  (define-runtime-path sloc-example "test/sloc-example.py")
  (define-runtime-path bad-extension-example "test/bad-extension.md")

  (test-case "python-path?"
    (check-pred python-path? sloc-example)
    (check-false (python-path? "foo")))

  (test-case "python-sloc"
    (check-equal?
      (python-sloc sloc-example)
      2))
)
