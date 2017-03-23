#lang racket/base

;; API for making system calls

(require racket/contract)
(provide
  (contract-out
   [shell
    (-> string? (listof string?) string?)]
   ;; `(shell cmd arg*)` finds the executable that `cmd` denotes,
   ;;  then invokes the executable with arguments `arg*`.
   ;; Raises an exception if the executable exists uncleanly,
   ;;  otherwise returns a string containing all output produced by the exe.
))

(require
  "util.rkt"
  (only-in racket/port
    with-output-to-string)
  (only-in racket/string
    string-trim)
  (only-in racket/system
    system*))

;; =============================================================================

;; TODO warn if falling back?

(define (shell pre-exe cmd*)
  (define exe (find-exe pre-exe))
  (define success? (box #f))
  (define str
    (with-output-to-string
      (lambda ()
        (set-box! success? (apply system* exe cmd*)))))
  (if (unbox success?)
    (string-trim str)
    (raise-user-error 'shell "failed to apply '~a' to arguments '~a'" exe cmd*)))

;; find-exe : string? -> path-string?
(define (find-exe pre-exe)
  (define fep (find-executable-path pre-exe))
  (if (path? fep)
    fep
    (raise-user-error 'shell "cannot find executable '~a', please install and try again" pre-exe)))

;; =============================================================================

(module+ test
  (require rackunit)

  (test-case "shell"
    (check-regexp-match #rx"^Welcome to Racket"
      (shell "racket" '("--version"))))

  (test-case "find-exe"
    (check-equal?
      (find-exe "racket")
      (find-executable-path "racket"))
    (check-exn exn:fail:user?
      (lambda () (find-exe "this-is-not-racket-this-is-sparta"))))

)
