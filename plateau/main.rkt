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
    scriblib/autobib)
  (except-out (all-from-out scribble/manual) url)

  (rename-out
   [acmart:#%module-begin #%module-begin]

   [render-benchmark-name bm]
   ;; Usage: `@bm{name}`
   ;; Given something that uniquely identifies a benchmark, render the
   ;;  benchmark's canonical name.
   ;; This is essentially `tt`, but it catches typos.

   [render-benchmark-names* bm*]
   ;; Usage: `@bm*{name1 name2 ...}
   ;; Render multiple benchmark names.

   [format-url url]
   ;; Usage: @url{URL}
   ;;  format a URL, removes the `http://` prefix if given

  )

  generate-bibliography
  bm-desc

  exact-runtime-category
  ;; Usage: @category[name bm* make-descr]
  ;;  where `name` is a string, broadly describes the category
  ;;    and `bm*` is a list of benchmark names (e.g. symbols)
  ;;    and `make-descr` is a thunk (-> string? element?)
  ;;        that accepts a string representing the length of `bm*`
  ;;        and produces text that defines and carefully describes the category.
  ;; Renders a "category describing a group of exact runtime plots"

  percent-slower-than-typed
  ;; Usage: @percent-slower-than-typed{benchmark-name}
  ;; Extremely specialized function, count the number of configurations
  ;;  that run slower than the typed configuration.

  x-axis y-axis
  x-axes y-axes
  ;; Usage: @|x-axis|
  ;; Renders "x-axis", with or without italics on the `x` (depends what looks better)

  *PLOT-HEIGHT*
  ;; Parameter to fix height of individual overhead plots

  *CACHE-SUFFIX*
  ;; (Parameterof String)
  ;; Optional tag to distinguish different cachefiles that would have the same name.

  *SINGLE-COLUMN?*
  ;; (Parameterof Boolean)
  ;; When true, put all plots in 1 column

  SNAPL-2015-URL
  ;; URL to the SNAPL paper by Siek et.al

  gnorm
  ;; Usage: @${@gnorm{x}}
  ;;  where `x` is measurable syntax

  definition
  ;; Usage: @definition[term]{defn ...}
  ;;  where `term` is a term to define and `defn ...` defines the term.
  ;; Renders a definition

  defn
  ;; Usage: @defn[term]
  ;;  where `term` is previously defined in a `definition`
  ;; Renders a reference to a technical term.

  lib-desc
  ;; (->* [string?] [#:rest pre-content?] pre-content?)
  ;; @lib-desc[lib-name]{descr}
  ;; Render a description of a Python library used by one of the benchmarks

  DLS-2014-BENCHMARK-NAMES
  POPL-2017-BENCHMARK-NAMES
  DLS-2017-BENCHMARK-NAMES
  ;; (listof symbol?)

  MAX-OVERHEAD
  EXACT-RUNTIME-XSPACE

  benchmark->name

  u/p-ratio
  t/u-ratio
  t/p-ratio

  EXHAUSTIVE-BENCHMARKS
  VALIDATE-BENCHMARKS
  SAMPLE-BENCHMARKS
  ;; (listof benchmark-info?)
  ;; Registry of all known benchmarks.
  ;; To change, edit `script/benchmark-info.rkt`.

  NUM-EXHAUSTIVE-BENCHMARKS
  ;; natural?
  ;; Same as `(length EXHAUSTIVE-BENCHMARKS)`

  NUM-VALIDATE-SAMPLES
  ;; natural?
  ;; Number of benchmarks in both the `EXHAUSTIVE-BENCHMARKS` and `SAMPLES-BENCHMARKS` lists

  NUM-NEW-SAMPLES
  ;; natural?
  ;; Number of benchmarks that are exclusive to the `SAMPLE-BENCHMARKS` list

  NUM-ITERATIONS
  ;; Number of times we ran each configuration for each benchmark.

  SAMPLE-RATE
  ;; Constant, defines sample size.
  ;; The sample size for a benchmark with N type-able components is
  ;;  `SAMPLE-RATE * N`

  NUM-SAMPLE-TRIALS
  ;; Constant, defines number of sample trials.
  ;; i.e. how many times we took random samples for each benchmark

  NUM-BETTER-WITH-TYPES
  ;; Number of configurations that run faster than some configuration with
  ;;  fewer typed components. (This is rare, and usually indicates a bug.)

  BENCHMARKS-WITH-FIRST-CLASS-FUNCTIONS
  ;; Number of benchmarks that use first-class function types
  ;; (ignores object types)

  PYTHON
  ;; "Python 3.4.3",
  ;;  the proper name of the version of python that we used to collect data

  $
  ;; Usage: `@${some math}`
  ;;  where `some math` is LaTeX-formatted math.
  ;; Wraps its arguments in dollar signs `$ ....$` and sends the result to LaTeX

  authors
  authors*
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

  cspace
  ;; Usage: `@cspace{C}`
  ;;  where `C` is a string.
  ;; Renders a meta-variable that represents a configuration space.

  deliverable
  ;; Usage: `@deliverable[N]`
  ;;  where `N` is a string or positive real number
  ;; Renders as "N-deliverable"

  approximation
  ;; Usage: `@approximation[r s pct]`
  ;;  where `r`, `s` are variables
  ;;  and `pct` is a percentage.
  ;; Renders as "pct% r,s-approximation"

  sra
  ;; Usage: @|sra|

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
  Integer->word
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

  Section-ref
  section-ref
  ;; Usage: `@section-ref{section-name}`
  ;;  where `section-name` appears in a `@section[#:tag section-name]{...}` form
  ;; Renders as "section N", where `N` is the number assigned to the section
  ;;  labeled with `section-name`.

  ;; --------------------------------------------------------------------------
  ;; hyperlinks

  mypy
  PEP-483
  PEP-484
  TPPBS
  time.process_time

  ;; -----------------------------------------------------------------------------
  ;; performance ratio utils

  get-ratios-table
  ratios-table-row
  ratios-row-retic/python
  ratios-row-typed/retic
  ratios-row-typed/python
)

(require
  "bib.rkt"
  "script/config.rkt"
  "script/benchmark-info.rkt"
  (prefix-in pi: "script/performance-info.rkt")
  "script/render.rkt"
  "script/util.rkt"
  (only-in "script/plot.rkt"
    *CONFIGURATION-X-JITTER*
    *OVERHEAD-MAX*)
  (only-in racket/class
    class new super-new object% define/public)
  (only-in racket/list
    add-between
    partition)
  racket/format
  racket/string
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

(define-values [EXHAUSTIVE-BENCHMARKS VALIDATE-BENCHMARKS SAMPLE-BENCHMARKS]
  (let ([bm* (all-benchmarks)])
    (define e* (filter benchmark->karst-data bm*))
    (define n* (map benchmark->name e*))
    (define s* (filter (λ (bm) (and (not (memq (benchmark->name bm) '(Evolution take5))) (benchmark->sample-data bm) #t)) bm*))
    (define-values [v* r*] (partition (λ (bm) (memq (benchmark->name bm) n*)) s*))
    (values e* v* r*)))

(define-values [NUM-EXHAUSTIVE-BENCHMARKS NUM-VALIDATE-SAMPLES NUM-NEW-SAMPLES]
  (values (length EXHAUSTIVE-BENCHMARKS)
          (length VALIDATE-BENCHMARKS)
          (length SAMPLE-BENCHMARKS)))

(define NUM-ITERATIONS
  40)

(define NUM-BETTER-WITH-TYPES
  ;; See unit test for this constant below
  ;; Maybe better to have count per benchmark?
  139975)

(define PYTHON
  "Python 3.4.3")

(define SAMPLE-RATE
  10)

(define NUM-SAMPLE-TRIALS
  10)

(define MAX-OVERHEAD
  (*OVERHEAD-MAX*))

(define EXACT-RUNTIME-XSPACE
  (*CONFIGURATION-X-JITTER*))

(define SNAPL-2015-URL
  "http://drops.dagstuhl.de/opus/volltexte/2015/5031/")

(define BENCHMARKS-WITH-FIRST-CLASS-FUNCTIONS
  '(spectralnorm))

;; -----------------------------------------------------------------------------

(define (->benchmark x)
  (define key
    (cond
     [(string? x) (string->symbol x)]
     [(symbol? x) x]
     [else (raise-argument-error '->benchmark "(or/c string? symbol?)" x)]))
  (or
    (for/first ([bm (in-list EXHAUSTIVE-BENCHMARKS)]
                #:when (eq? key (benchmark->name bm)))
      bm)
    (for/first ([bm (in-list VALIDATE-BENCHMARKS)]
                #:when (eq? key (benchmark->name bm)))
      bm)
    (for/first ([bm (in-list SAMPLE-BENCHMARKS)]
                #:when (eq? key (benchmark->name bm)))
      bm)
    (raise-argument-error '->benchmark "the name of a benchmark" x)))

(define (render-benchmark-name str)
  (define bm (->benchmark str))
  (tt (symbol->string (benchmark->name bm))))

(define (render-benchmark-names . str*)
  (render-benchmark-names* str*))

(define (render-benchmark-names* str*)
  (authors* (map render-benchmark-name str*)))

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
  (authors* a*))

(define (authors* a*)
  (cond
   [(null? a*)
    (raise-argument-error 'authors "at least one argument" a*)]
   [(null? (cdr a*))
    (car a*)]
   [(null? (cddr a*))
    (list (car a*) " and " (cadr a*))]
   [else
    (add-between a* ", " #:before-last ", and ")]))

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

(define (pythonexternal a)
  (exact (format "\\pythonexternal{~a}" a)))

(define (gnorm var)
  (format "\\|~a\\|" var))

(define (definition term . defn*)
  (make-paragraph plain
    (list
      (exact "\\vspace{1ex}\n")
      (bold "Definition")
      (cons (element #f (list " (" (emph term) ") ")) defn*)
      (exact "\\vspace{1ex}\n"))))

(define (defn term)
  term)

(define (bm-desc title author url lib . descr)
  ;(void (->benchmark title)) ;; assert that 'title' is the name of a benchmark
  (elem
    (parag title)  (smaller "from " author)
    (linebreak)
    ;ignore `url`
    (format-deps lib)
    (linebreak)
    descr))

(define exact-runtime-category
   (let* ([cat-num (box 0)]
          [get-number (λ ()
                        (set-box! cat-num (+ (unbox cat-num) 1))
                        (case (unbox cat-num) [(1) "I"] [(2) "II"] [(3) "III"] [(4) "IV"] [else (error 'get-number)]))])
     (λ (name pre-bm* make-descr)
       (define bm-name* (map render-benchmark-name pre-bm*))
       (define perf-type (format "Type ~a " (get-number)))
       (elem (bold perf-type)
             ~ ~
             (emph "(" name ")") ": "
             (make-descr (integer->word (length pre-bm*)))
             "\n"
             "\n"
             (list "The " (authors* bm-name*) " benchmarks are of " perf-type ".")))))

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
  (list "the " (authors* n*) " " l-str))

(struct lib [name url] #:transparent)

;; Names and URLs for standard Python libraries
(define LIB-INDEX*
  (list (lib "copy" "https://docs.python.org/3/library/copy.html")
        (lib "fnmatch" "https://docs.python.org/3/library/fnmatch.html")
        (lib "itertools" "https://docs.python.org/3/library/itertools.html")
        (lib "math" "https://docs.python.org/3/library/math.html")
        (lib "operator" "https://docs.python.org/3/library/operator.html")
        (lib "os" "https://docs.python.org/3/library/os.html")
        (lib "os.path" "https://docs.python.org/3/library/os.html#module-os.path")
        (lib "random" "https://docs.python.org/3/library/random.html")
        (lib "re" "https://docs.python.org/3/library/re.html")
        (lib "shlex" "https://docs.python.org/3/library/shlex.html")
        (lib "socket" "https://docs.python.org/3/library/socket.html")
        (lib "struct" "https://docs.python.org/3/library/struct.html")
        (lib "urllib" "https://docs.python.org/3/library/urllib.html")))

(define (lib-desc name . why)
  (or (for/first ([l (in-list LIB-INDEX*)]
                  #:when (string=? name (lib-name l)))
        l)
      (begin
        (warning "no URL for library ~a, please add to `lib-index*` in `main.rkt`" name)
        (lib name "https://www.google.com"))))

(define u/p-ratio
  "retic/python ratio")

(define t/u-ratio
  "typed/retic ratio")

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
  (elem ($ d-str) "-deliverable"))

(define (approximation r s [pct #f])
  (define pct-elem
    (if pct
      (elem ($ (~a pct)) "%-")
      (elem)))
  (define r-elem
    (if (real? r) (~a r) r))
  (define s-elem
    (if (real? s) (~a s) s))
  (elem pct-elem ($ r-elem ", " s-elem) "-approximation"))

(define sra
  "simple random approximation")

(define (cspace [letter "C"])
  (bold letter))

(define (Section-ref s)
  (elem "Section" ~ (secref s)))

(define (section-ref s)
  (elem "section" ~ (secref s)))

(define (axes q)
  (elem (emph q) "-axes"))

(define x-axes
  (axes "x"))

(define y-axes
  (axes "y"))

(define (axis q)
  (elem (emph q) "-axis"))

(define x-axis
  (axis "x"))

(define y-axis
  (axis "y"))

(define (format-url str)
  (hyperlink str
    (url
      (remove-prefix "www."
        (remove-prefix "http[^:]*://" str)))))

(define (remove-prefix rx str)
  (define m (regexp-match (string-append "^" rx "(.*)$") str))
  (if m (cadr m) str))

(define (percent-slower-than-typed pre-bm)
  (define pi (pi:benchmark->performance-info (->benchmark pre-bm)))
  (define total (pi:num-configurations pi))
  (define num-good ((pi:deliverable (pi:typed/python-ratio pi)) pi))
  (round (pct (- total num-good) total)))

(define (Integer->word i)
  (integer->word i #:title? #t))

;; =============================================================================
;; Hyperlinks (i.e. non-academic references

(define PEP-483
  (hyperlink "https://www.python.org/dev/peps/pep-0483/" (emph "PEP 483: The Theory of Type Hints")))

(define PEP-484
  (hyperlink "https://www.python.org/dev/peps/pep-0484/" (emph "PEP 484: Type Hints")))

(define mypy
  (hyperlink "http://mypy-lang.org/" (emph "Mypy")))

(define TPPBS
  (hyperlink "http://pyperformance.readthedocs.io/" "The Python Performance Benchmark Suite"))

(define time.process_time
  (hyperlink "https://docs.python.org/3/library/time.html#time.process_time" (tt "time.process_time()")))

;; =============================================================================

(module+ test
  ;; Test claims & expectations from the paper
  ;; aka extra layer of authentication

  (require
    rackunit
    racket/set)

  ;; ------------------------------------------------------------------

  ;; TODO make this an error
  (define (test-error msg . arg*)
    (display "WARNING: ")
    (apply printf msg arg*)
    (newline))

  ;; ------------------------------------------------------------------

  (test-case "all-benchmarks"
    (check set=?
      (map benchmark->name EXHAUSTIVE-BENCHMARKS)
      '(futen http2 slowSHA call_method call_method_slots call_simple chaos fannkuch float go meteor nbody nqueens pidigits pystone spectralnorm Espionage PythonFlow take5))
    (check set=?
      (map benchmark->name (append VALIDATE-BENCHMARKS SAMPLE-BENCHMARKS))
      '(futen slowSHA chaos pystone Espionage PythonFlow sample_fsm aespython stats)))

  (test-case "partitioning benchmarks"
    (check-equal? NUM-EXHAUSTIVE-BENCHMARKS 19)
    (check-equal? NUM-VALIDATE-SAMPLES 6)
    (check-equal? NUM-NEW-SAMPLES 3))

  (test-case "->benchmark"
    (check-equal? (car SAMPLE-BENCHMARKS) (->benchmark (benchmark->name (car SAMPLE-BENCHMARKS))))
    (check-exn #rx"the name of a benchmark"
      (λ () (->benchmark 'zeina)))
    (check-exn #rx"string?"
      (λ () (->benchmark 8))))

  (test-case "authors"
    (check-exn exn:fail:contract?
      (λ () (authors)))
    (check-equal? (authors "john doe") "john doe")
    (check-equal? (authors "a" "b") (list "a" " and " "b"))
    (check-equal? (authors "a" "b" "c") (list "a" ", " "b" ", and " "c")))

  (test-case "percent-slower-than-typed"
    (check-equal? (percent-slower-than-typed "spectralnorm") 38))

  (test-case "remove-prefix"
    (check-equal?
      (remove-prefix "hello" "hello world")
      " world")
    (check-equal?
      (remove-prefix "b" (remove-prefix "a" "abc"))
      "c")
    (check-equal?
      (remove-prefix "a" (remove-prefix "b" "cba"))
      "cba"))

)

#;
(module+ test ;; These tests are slow
  (require
    racket/set
    (only-in gm-plateau-2017/script/benchmark-info
      benchmark-info->python-info)
    (only-in gm-plateau-2017/script/python
      python-info->all-types
      python-info->num-types)
    (only-in gm-plateau-2017/script/performance-info
      benchmark->performance-info
      untyped/python-ratio
      typed/retic-ratio
      typed/python-ratio
      unzip-karst-data
      fold/karst))

  (test-case "num-first-class-functions"
    (check-equal?
      (for/list ([bm (in-list (all-benchmarks))]
                 #:when (for/or ([t-str (in-set (python-info->all-types (benchmark-info->python-info bm)))])
                          (and t-str (regexp-match? #rx"^Function" t-str))))
        (benchmark->name bm))
      BENCHMARKS-WITH-FIRST-CLASS-FUNCTIONS))

   ;; ------------------------------------------------------------------

  (define (count-lines fn)
    (with-input-from-file fn
      (λ () (for/sum ((ln (in-lines))) 1))))

  (define (check-karst-iterations karst-file)
    (fold/karst karst-file
      #:init #true
      #:f (λ (acc cfg num-types t*)
            (unless (>= (length t*) NUM-ITERATIONS)
              (test-error "configuration ~a has ~a iterations, expected at least ~a iterations (in file ~a)" cfg (length t*) NUM-ITERATIONS karst-file))
            acc)))

  (define (check-fully-annotated bm)
    (let ([t* (python-info->all-types (benchmark-info->python-info bm))])
      (when (set-member? t* #f)
        (test-error "benchmark ~a is missing some type annotation(s)" (benchmark->name bm)))
      (when (for/or ([t (in-set t*)]) (and t (regexp-match? #rx"Dyn" t)))
        (test-error "benchmark ~a uses the Dyn type" (benchmark->name bm)))))

  ;; ------------------------------------------------------------------

  (test-case "num-iterations:exhaustive"
    (for/and ([bm (in-list EXHAUSTIVE-BENCHMARKS)])
      (check-true (check-karst-iterations (unzip-karst-data (benchmark->karst-data bm))))))

  (test-case "num-iterations:sample"
    (for*/and ([bm (in-list (append VALIDATE-BENCHMARKS SAMPLE-BENCHMARKS))]
               [d (in-list (benchmark->sample-data bm))])
      (check-true (check-karst-iterations d))))

  (test-case "num-iterations:python"
    (for/and ([bm (in-list (append EXHAUSTIVE-BENCHMARKS VALIDATE-BENCHMARKS SAMPLE-BENCHMARKS))])
      (define t* (benchmark->python-data bm))
      (check-true (and t* (>= (length t*) NUM-ITERATIONS)))))

  (test-case "sample-rate"
    (define (check-sample-rate bm)
      (define expected-num-samples (* SAMPLE-RATE (python-info->num-types (benchmark-info->python-info bm))))
      (check-true
        (for/and ([d (in-list (benchmark->sample-data bm))])
          (define nl (count-lines d))
          (unless (= nl expected-num-samples)
            (test-error "file ~a has ~a lines, expected ~a lines" d nl expected-num-samples))
          #true)))

    (for-each check-sample-rate (append VALIDATE-BENCHMARKS SAMPLE-BENCHMARKS)))

  (test-case "sample-trials"
    (define (check-sample-trials bm)
      (define st (length (benchmark->sample-data bm)))
      (unless (= NUM-SAMPLE-TRIALS st)
        (test-error "benchmark ~a has ~a samples, expected ~a samples" (benchmark->name bm) st NUM-SAMPLE-TRIALS))
      (void))

    (for-each check-sample-trials (append VALIDATE-BENCHMARKS SAMPLE-BENCHMARKS)))


  (test-case "num-better-with-types"
    (check-equal?
      (pi:count-better-with-types EXHAUSTIVE-BENCHMARKS)
      NUM-BETTER-WITH-TYPES))

  (test-case "fully-annotated"
    (for-each check-fully-annotated (all-benchmarks)))

  (test-case "performance-ratios-product"
    (define EPS 0.0001)
    (for ((bm (in-list (all-benchmarks))))
      (define pi (benchmark->performance-info bm))
      (check-=
        (* (typed/retic-ratio pi)
           (untyped/python-ratio pi))
        (typed/python-ratio pi)
        EPS)))
)
