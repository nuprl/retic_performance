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

(provide
  (all-from-out
    "bib.rkt"
    scribble/acmart
    scribble/doclang
    scriblib/figure
    scribble/example
    scriblib/autobib
    scribble/manual)
  generate-bibliography

  (rename-out
   [acmart:#%module-begin #%module-begin]

   [render-benchmark-name bm]
   ;; Usage: `@bm[benchmark-info]`
   ;; Given a benchmark-info struct, render the name of the benchmark
   ;;  in a standard way.

  )

  ALL-BENCHMARKS
  ;; (listof benchmark-info?)
  ;; Registry of all known benchmarks.
  ;; To change, edit `script/benchmark-info.rkt`.

  NUM-BENCHMARKS
  ;; natural?
  ;; Same as `(length ALL-BENCHMARKS)`

  $
  ;; Usage: `@${some math}`
  ;;  where `some math` is LaTeX-formatted math.
  ;; Wraps its arguments in dollar signs `$ ....$` and sends the result to LaTeX

  ~cite
  ;; Usage: `@~cite[bib-name]`
  ;;  where `bib-name` is an identifier from `bib.rkt`
  ;; Renders a short-style citation to `bib-name`.
  ;; Example:
  ;;   @elem{We love@~cite[matthias]}
  ;; May render to:
  ;;   "We love [409]."
  ;; Where 409 is the number assigned to the bib entry that `matthias` refers to

  citet
  ;; Usage: `@citet[bib-name]`
  ;;  where `bib-name` is an identifier from `bib.rkt`
  ;; Renders a long-style citation to `bib-name`
  ;; Example:
  ;;  @elem{See work by @citet[matthias]}
  ;; May render to:
  ;;  "See work by Felleisen 1901"
  ;; If `matthias` refers to a 1901 article by Felleisen.

  etal
  ;; Usage: `@|etal|`
  ;; Renders "et al." with proper spacing between the words.
  ;; Use `citet` instead.

;;  exact
  ;; Usage: `@exact|{some text}|`
  ;;    or `@exact{some text}`
  ;;  where `some text` is text that should go directly to LaTeX
  ;; Using `|{ ... }|` instead of `{ ... }` ignores any `@` signs
  ;;  or unmatched `}` in the `...`.

  id
  ;; Usage: `@id[foo]`
  ;;  where `foo` is a Racket identifier.
  ;; Renders the display-mode form of the value of `foo`

  note
  ;; Usage: `@note{some text}`
  ;; Renders a footnote containing `some text`.
  ;; The footnote marker will appear where `@note` appears in the source,
  ;;  and the footnote text will appear at the bottom of the current page.
  ;;
  ;; Remember! Footnotes always go after any punctuation.
  ;; (See "Introduction to Notes" here: https://owl.english.purdue.edu/owl/owlprint/717/ )

  parag
  ;; Usage: `@parag{word}`
  ;;  where `word` is a single word or short phrase.
  ;; Renders a label for an upcoming paragraph.

  python
  ;; Usage: `@python{ code }`
  ;;  where `code` is one-or-more-lines of Python code
  ;; Renders a codeblock containing Python code.

  pythonexternal
  ;; Usage: `@pythonexternal{path-string}`
  ;;  where `path-string` refers to a file containing Python code
  ;; Renders the contents of `path-string` in a Python code block

  pythoninline
  ;; Usage: `@pythoninline{code}`
  ;;  where `code` is less than 1 line of Python code
  ;; Renders some Python code in the current line of text.
  ;; Useful for formatting identifiers

  render-overhead-plot*
  ;; (-> (listof benchmark-info?) pict?)
  ;; Render overhead plots for the given benchmarks

  render-exact-runtime-plot*
  ;; (-> (listof benchmark-info?) pict?)
  ;; Render the exact running times for the given benchmarks.
  ;; Running times ordered by number of types.

  sc
  ;; Usage `@sc{some text}`
  ;; Renders `text` in small caps style

  sf
  ;; Usage `@sf{some text}`
  ;; Renders `some text` in serif style

  section-ref
  ;; Usage: `@section-ref{section-name}`
  ;;  where `section-name` appears in a `@section[#:tag section-name]{...}` form
  ;; Renders as "section N", where `N` is the number assigned to the section
  ;;  labeled with `section-name`.
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

(define-cite ~cite citet generate-bibliography
  #:style small-number-style)

(define (sf x)
  (elem #:style "sfstyle" x))

(define (sc x #:sup [sup #f])
  (exact "\\textsc{\\small " x "}"
    (if sup (format "$^~a$" sup) "")))

(define (exact . items)
  (make-element (make-style "relax" '(exact-chars))
                items))

(define etal
  (exact "et~al."))

(define (id x)
  (~a x))

(define ($ . items)
  (apply exact (list "$" items "$")))

(define (parag . x)
  (apply elem #:style "paragraph" x))

(define (python . x)
  (apply exact (append (list "\n\\begin{python}\n") x (list "\n\\end{python}\n"))))

(define (pythoninline . x)
  (apply exact (append (list "\\pythoninline{") x (list "}"))))

(define (pythonexternal a b)
  (apply exact (format "\\pythonexternal{~a}{~a}" a b)))

(define (section-ref section-name)
  (elem (exact "section~")
        (secref section-name)))
