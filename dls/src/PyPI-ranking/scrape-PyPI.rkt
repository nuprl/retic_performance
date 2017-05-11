#lang racket/base

(require
  (only-in html-parsing html->xexp)
  (only-in sxml sxpath)
  racket/runtime-path)

;; =============================================================================

(define-runtime-path PyPI.html "PyPI.html")

;; -----------------------------------------------------------------------------

(define (parse-PyPI)
  ((sxpath '(// tr)) (call-with-input-file PyPI.html html->xexp)))

(define (find-ranking tr* package-name)
  (for/first ([tr (in-list tr*)]
              #:when (matching-row? tr package-name))
    (row->rank tr)))

(define (matching-row? tr package-name)
  (define txt* ((sxpath '(td a span *text*)) tr))
  (and (not (null? txt*))
       (string=? (car txt*) package-name)))

(define (row->rank tr)
  (define match* ((sxpath '(td *text*)) tr))
  (car match*))

;; =============================================================================

(module+ main
  (require racket/cmdline)
  (command-line
    #:program "scrape-PyPI"
    #:args package-name*
    (if (null? package-name*)
      (printf "Usage: racket scrape-PyPI.rkt <package-name> ...~n")
      (let ([tr* (parse-PyPI)])
        (for ((pkg (in-list package-name*)))
          (define r (find-ranking tr* pkg))
          (if r
            (printf "- ~a is ranked ~a~n" pkg r)
            (printf "ERROR : failed to find rank for '~a'~n" pkg)))))))
