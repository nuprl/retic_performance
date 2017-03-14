#lang racket/base

(provide
  (all-from-out
    "bib.rkt"
    scriblib/footnote
    ;scriblib/figure
    scribble/eval
    scriblib/autobib
    scribble/manual)
  (all-defined-out))

(require
  "bib.rkt"
  racket/class
  scriblib/footnote
  scriblib/figure
  scribble/core
  scribble/eval
  scriblib/autobib
  scribble/latex-properties
  setup/main-collects
  scribble/html-properties
  (except-in scribble/manual
    author
    secref)
  (for-syntax
    racket/base
    syntax/parse))

;; =============================================================================

(define NUM-BENCHMARKS "???")

(define autobib-style-extras
  (let ([abs (lambda (s)
               (path->main-collects-relative
                (collection-file-path s "scriblib")))])
    (list
     (make-css-addition (abs "autobib.css"))
     (make-tex-addition (abs "autobib.tex")))))

(define bib-single-style (make-style "AutoBibliography" autobib-style-extras))

(define bibentry-style (make-style "Autobibentry" autobib-style-extras))
(define colbibnumber-style (make-style "Autocolbibnumber" autobib-style-extras))
(define colbibentry-style (make-style "Autocolbibentry" autobib-style-extras))

(define small-number-style
  (new
   (class object%
     (define/public (bibliography-table-style) bib-single-style)
     (define/public (entry-style) colbibentry-style)
     (define/public (disambiguate-date?) #f)
     (define/public (collapse-for-date?) #f)
     (define/public (get-cite-open) "[")
     (define/public (get-cite-close) "]")
     (define/public (get-group-sep) ", ")
     (define/public (get-item-sep) ", ")
     (define/public (render-citation date-cite i)
       (make-element
        (make-style "Thyperref" (list (command-extras (list (make-label i)))))
        (list (number->string i))))
     (define/public (render-author+dates author dates) dates)
     (define (make-label i)
       (string-append "autobiblab:" (number->string i)))
     (define/public (bibliography-line i e)
       (list (make-paragraph plain
                             (make-element colbibnumber-style
                                           (list
                                            (make-element (make-style "label" null)
                                                          (make-label i))
                                            "[" (number->string i) "]")))
             e))
     (super-new))))

(define author+date-style/link
  (new
   (class object%
     (define/public (bibliography-table-style) bib-single-style)
     (define/public (entry-style) bibentry-style)
     (define/public (disambiguate-date?) #t)
     (define/public (collapse-for-date?) #t)
     (define/public (get-cite-open) "(")
     (define/public (get-cite-close) ")")
     (define/public (get-group-sep) "; ")
     (define/public (get-item-sep) ", ")
     (define/public (render-citation date-cite i)
       (make-element
        (make-style "Thyperref" (list (command-extras (list (make-label i)))))
        date-cite))
     (define/public (render-author+dates author dates)
        (list* author " " dates))
     (define (make-label i)
       (string-append "autobiblab:" (number->string i)))
     (define/public (bibliography-line i e)
       (list (make-compound-paragraph
              plain
              (list (make-paragraph plain (list (make-element (make-style "label" null)
                                                              (make-label i))))
                     e))))
     (super-new))))

(define-cite ~cite citet generate-bibliography #:style small-number-style)

(define etal "et al.")

(define (sf x) (elem #:style "sfstyle" x))

(define (sc x #:sup [sup #f])
  (exact "\\textsc{\\small " x "}"
    (if sup (format "$^~a$" sup) "")))

(define (exact . items)
  (make-element (make-style "relax" '(exact-chars))
                items))

(define ($ . items)
  (make-element (make-style "relax" '(exact-chars))
                (list "$" items "$")))

(define (parag . x)
  (apply elem #:style "paragraph" x))

