#lang racket/base

;; Programming environment for the DLS 2017 submission. Includes utilities for:
;; - formatting
;; - processing datasets
;;
;; Basically, extends `scribble/acmart` with project-specific options.
;; (The file `lang/reader.rkt` sets up the actual reader.)

;; TODO
;; - zeina did you talk to Mike about missing types?
;; - `make python` to compute python info, cache it by the MD5 hash of files
;;   - you can build paper without python3, sloccount installed
;;   - but it will stop you if your cache is out of sync

;; TODO ;; (require racket/contract)
(provide
  (all-from-out
    "bib.rkt"
    scribble/acmart
    scribble/doclang
    scriblib/figure
    scribble/example
    scriblib/autobib
    scribble/manual)

  (rename-out
    [acmart:#%module-begin #%module-begin])

  ALL-BENCHMARKS
  NUM-BENCHMARKS

  $
  citet
  etal
  exact
  id
  note
  parag
  python
  pythonexternal
  pythoninline
  sc
  sf
  ~cite

  (rename-out
   [render-benchmark-name bm])
)

(require
  "bib.rkt"
  "script/config.rkt"
  "script/benchmark-info.rkt"
  "script/render.rkt"
  (only-in racket/class
    class new super-new object% define/public)
  racket/format
  scribble/acmart
  scribble/core
  scribble/example
  scribble/html-properties
  scribble/latex-properties
  scriblib/autobib
  scriblib/figure
  setup/main-collects
  (except-in scribble/doclang
    #%module-begin)
  (only-in scribble/acmart/lang
    [#%module-begin acmart:#%module-begin])
  (except-in scribble/manual
    title author)
  (only-in scriblib/footnote
    note)
  (for-syntax racket/base syntax/parse))

;; =============================================================================

(define ALL-BENCHMARKS
  (all-benchmarks))

(define NUM-BENCHMARKS
  (length ALL-BENCHMARKS))

;; -----------------------------------------------------------------------------

(define (render-benchmark-name bm)
  (tt (symbol->string (benchmark->name bm))))

;; -----------------------------------------------------------------------------

(define small-number-style
  (let ([autobib-style-extras
        (let ([abs (lambda (s)
                     (path->main-collects-relative
                      (collection-file-path s "scriblib")))])
          (list
           (make-css-addition (abs "autobib.css"))
           (make-tex-addition (abs "autobib.tex"))))])
    (new
     (class object%
       (define/public (bibliography-table-style)
         (make-style "AutoBibliography" autobib-style-extras))
       (define/public (entry-style)
         (make-style "Autocolbibentry" autobib-style-extras))
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
                               (make-element (make-style "Autocolbibnumber"
                                                         autobib-style-extras)
                                             (list
                                              (make-element (make-style "label" null)
                                                            (make-label i))
                                              "[" (number->string i) "]")))
               e))
       (super-new)))))

(define-cite ~cite citet
  generate-bibliography
  #:style small-number-style)

(define etal
  "et al.")

(define (sf x)
  (elem #:style "sfstyle" x))

(define (sc x #:sup [sup #f])
  (exact "\\textsc{\\small " x "}"
    (if sup (format "$^~a$" sup) "")))

(define (exact . items)
  (make-element (make-style "relax" '(exact-chars))
                items))

(define (id x)
  (~a x))

(define ($ . items)
  (make-element (make-style "relax" '(exact-chars))
                (list "$" items "$")))

(define (parag . x)
  (apply elem #:style "paragraph" x))

(define (python . x)
  (apply exact (append (list "\n\\begin{python}\n") x (list "\n\\end{python}\n"))))

(define (pythoninline . x)
  (apply exact (append (list "\\pythoninline{") x (list "}"))))

(define (pythonexternal a b)
  (apply exact (format "\\pythonexternal{~a}{~a}" a b)))
