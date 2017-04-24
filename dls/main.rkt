#lang racket/base

;; Programming environment for the DLS 2017 submission. Includes utilities for:
;; - formatting
;; - processing datasets
;;
;; Basically, extends `scribble/acmart` with project-specific options.
;; (The file `lang/reader.rkt` sets up the actual reader.)

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
  bm-desc

  TODO
  ;; Usage: @TODO{message}
  ;;  where `message` is an element.
  ;; Renders a bold-style "TODO" message.

  lib-desc
  ;; (->* [string?] [#:rest pre-content?] pre-content?)
  ;; @lib-desc[lib-name]{descr}
  ;; Render a description of a Python library used by one of the benchmarks

  DLS-2014-BENCHMARK-NAMES
  POPL-2017-BENCHMARK-NAMES
  DLS-2017-BENCHMARK-NAMES
  ;; (listof symbol?)

  MAX-OVERHEAD

  benchmark->name

  u/p-ratio
  t/u-ratio
  t/p-ratio

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

  NUM-ITERATIONS
  ;; TODO check this number against the datasets

  $
  ;; Usage: `@${some math}`
  ;;  where `some math` is LaTeX-formatted math.
  ;; Wraps its arguments in dollar signs `$ ....$` and sends the result to LaTeX

  authors
  ;; Usage: `@authors[author-name ...]
  ;;  where `author-name` is a string
  ;; Renders a sequence of author names

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

  deliverable
  ;; Usage: `@deliverable[N]`
  ;;  where `N` is a string or positive real number
  ;; Renders as "N-deliverable"

  etal
  ;; Usage: `@|etal|`
  ;; Renders "et al." with proper spacing between the words.
  ;; Use `citet` instead.

  exact
  ;; Usage: `@exact|{some text}|`
  ;;    or `@exact{some text}`
  ;;  where `some text` is text that should go directly to LaTeX
  ;; Using `|{ ... }|` instead of `{ ... }` ignores any `@` signs
  ;;  or unmatched `}` in the `...`.

  id
  ;; Usage: `@id[foo]`
  ;;  where `foo` is a Racket identifier.
  ;; Renders the display-mode form of the value of `foo`

  integer->word
  ;; (->* [integer?] [#:title? any/c] string?)
  ;; Coverts a small number into a string.
  ;; Capitalizes the string when `#:title?` is non-#f

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

  render-static-information
  ;; (-> (listof benchmark-info?) table?)
  ;; Build a table of static information about each benchmark

  render-ratios-table
  ;; (-> (listof benchmark-info?) table?)
  ;; Build a table of Python/Retic/Typed ratios

  render-samples-plot*
  ;; (-> (listof benchmark-info?) pict?)
  ;; Plots the random-sample data for the given benchmarks
  ;;  as multiple lines on a single graph.
  ;; See also `render-validate-samples-plot*`

  render-validate-samples-plot*
  ;; (-> (listof benchmark-info?) pict?)
  ;; Plots the overhead of each benchmark alongside a confidence interval
  ;;  generated from the benchmark's random samples.
  ;; See also `render-samples-plot*`

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
  "script/util.rkt"
  (only-in "script/plot.rkt"
    *OVERHEAD-MAX*)
  (only-in racket/class
    class new super-new object% define/public)
  (only-in racket/list
    add-between
    partition)
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

(define NUM-ITERATIONS
  40)

(define MAX-OVERHEAD
  ;; TODO maybe MAX-OVERHEAD should be parameter?
  (*OVERHEAD-MAX*))

;; -----------------------------------------------------------------------------

(define (->benchmark x)
  (define key
    (cond
     [(string? x) (string->symbol x)]
     [(symbol? x) x]
     [else (raise-argument-error '->benchmark "(or/c string? symbol?)" x)]))
  (or
    (for/first ([bm (in-list ALL-BENCHMARKS)]
                #:when (eq? key (benchmark->name bm)))
      bm)
    (raise-argument-error '->benchmark "the name of a benchmark" x)))

(define (render-benchmark-name str)
  (define bm (->benchmark str))
  (tt (symbol->string (benchmark->name bm))))

(define (warning msg . arg*)
  (display "[WARNING] ")
  (apply printf msg arg*)
  (newline))

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

(define (authors . a*)
  (cond
   [(null? a*)
    (raise-argument-error 'authors "at least one argument" a*)]
   [(null? (cdr a*))
    (car a*)]
   [(null? (cddr a*))
    (string-append (car a*) " and " (cadr a*))]
   [else
    (apply string-append
      (add-between a* ", " #:before-last ", and "))]))

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

(define (bm-desc title author url lib . descr)
   (elem
     (parag title)  (smaller "from " author)
     (linebreak)
     ;ignore `url`
     (format-deps lib)
     (linebreak)
     descr))

(define (format-deps dep*)
  (if (null? dep*)
    "No dependencies."
    (let-values ([(lib* other*) (partition lib? dep*)])
      (list "Depends on "
            (cond
             [(null? lib*)
              other*]
             [(null? other*)
              (format-lib lib*)]
             [else
              (list (format-lib lib*) ", and " other*)])
            "."))))

(define (format-lib lib*)
  (define n*
    (for/list ([l (in-list lib*)])
      (hyperlink (lib-url l) (tt (lib-name l)))))
  (define l-str (if (null? (cdr lib*)) "library" "libraries"))
  (list "the " (add-between n* ", " #:before-last ", and ") " " l-str))

(struct lib [name url] #:transparent)

;; Names and URLs for standard Python libraries
(define LIB-INDEX*
  (list (lib "copy" "https://docs.python.org/3/library/copy.html")
        (lib "fnmatch" "https://docs.python.org/3/library/fnmatch.html")
        (lib "itertools" "https://docs.python.org/3/library/itertools.html")
        (lib "math" "https://docs.python.org/3/library/math.html")
        (lib "operator" "https://docs.python.org/3/library/operator.html")
        (lib "os" "https://docs.python.org/3/library/os.html")
        (lib "random" "https://docs.python.org/3/library/random.html")
        (lib "re" "https://docs.python.org/3/library/re.html")
        (lib "shlex" "https://docs.python.org/3/library/shlex.html")
        (lib "socket" "https://docs.python.org/3/library/socket.html")
        (lib "urllib" "https://docs.python.org/3/library/urllib.html")))

(define (lib-desc name . why)
  (or (for/first ([l (in-list LIB-INDEX*)]
                  #:when (string=? name (lib-name l)))
        l)
      (begin
        (warning "no URL for library ~a, please add to `lib-index*` in `main.rkt`")
        (lib name ""))))

(define u/p-ratio
  "untyped/python ratio")

(define t/u-ratio
  "typed/untyped ratio")

(define t/p-ratio
  "typed/python ratio")

(define (deliverable [D "D"])
  (define d-str
    (cond
     [(string? D)
      D]
     [(and (real? D) (positive? D))
      (number->string D)]
     [else
      (raise-argument-error 'deliverable "(or/c positive-real? string?)" D)]))
  (elem (emph d-str) "-deliverable"))

(define (TODO . msg)
  (apply bold "TODO: " msg))
