#lang racket/base

;; API for making system calls

(require racket/contract)
(provide
  (contract-out
   [shell
    (-> string? (or/c string? (listof string?)) string?)]
   ;; `(shell cmd arg*)` finds the executable that `cmd` denotes,
   ;;  then invokes the executable with arguments `arg*`.
   ;; Raises an exception if the executable exists uncleanly,
   ;;  otherwise returns a string containing all output produced by the exe.

   [md5sum
    (-> path-string? string?)]
   ;; Compute MD5 hash of the contents of the given file

))

(require
  "util.rkt"
  (only-in openssl/md5
    md5)
  (only-in racket/port
    with-output-to-string)
  (only-in racket/string
    string-trim)
  (only-in racket/system
    system*))

;; =============================================================================

;; TODO warn if falling back?

(define (shell pre-exe pre-cmd)
  (define exe (find-exe pre-exe))
  (define success? (box #f))
  (define cmd* (if (string? pre-cmd) (list pre-cmd) pre-cmd))
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

(define (md5sum ps)
  (call-with-input-file ps md5))

;; =============================================================================

(module+ test
  (require rackunit racket/runtime-path (only-in racket/string string-split))
  (define-runtime-path sloc-example "test/sloc-example.py")

  (test-case "shell"
    (check-regexp-match #rx"^Welcome to Racket"
      (shell "racket" '("--version"))))

  (test-case "find-exe"
    (check-equal?
      (find-exe "racket")
      (find-executable-path "racket"))
    (check-exn exn:fail:user?
      (lambda () (find-exe "this-is-not-racket-this-is-sparta"))))

  (test-case "md5sum"
    (define (check-md5 ps)
      (define openssl-md5 (md5sum sloc-example))
      (define system-md5 (car (string-split (shell "md5sum" (path->string sloc-example)))))
      (check-equal? openssl-md5 system-md5))

    (check-md5 sloc-example)
  )
)
