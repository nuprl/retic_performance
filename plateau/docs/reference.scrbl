#lang scribble/manual

@require[
  (for-label
    gm-plateau-2017
    with-cache
    openssl/md5
    (only-in gm-plateau-2017/script/benchmark-info benchmark-info?)
    (only-in gm-plateau-2017/script/performance-info performance-info?)
    (only-in racket/string string-split string-join)
    (only-in racket/math natural?)
    (only-in racket/set set/c)
    (only-in racket/base time-apply path-string? string? symbol? real?)
    (only-in racket/contract and/c >=/c between/c cons/c any/c listof or/c)
    (only-in scribble/decode pre-content?)
    (only-in scribble/core element? paragraph? table?)
    (only-in pict pict?)
    (only-in racket/format ~a)
    (only-in scriblib/figure figure figure*))]
@title{Reference}

@defmodulelang[gm-plateau-2017]{
  The @racketmodname[gm-plateau-2017] language provides the reader from
   @racketmodname[scribble/base] and all exports from the @racketmodname[gm-plateau-2017] module.
}

Other modules in the collection process the Reticulated benchmarks and the datasets.
The modules are documented in the sections below.

@; -----------------------------------------------------------------------------
@; --- defids

@deftogether[(
  @defidform[x-axis]
  @defidform[y-axis]
  @defidform[x-axes]
  @defidform[y-axes]
)]{
  Render the phrase @emph{x-axis}, etc.
}

@deftogether[(
  @defidform[SNAPL-2015-URL]
  @defidform[mypy]
  @defidform[PEP-483]
  @defidform[PEP-484]
  @defidform[TPPBS]
  @defidform[time.process_time]
)]{
  URLs and hyperlinks.
}

@deftogether[(
  @defidform[DLS-2014-BENCHMARK-NAMES]
  @defidform[POPL-2017-BENCHMARK-NAMES]
  @defidform[DLS-2017-BENCHMARK-NAMES]
)]{
  Lists of benchmark names, organized by source.
}

@deftogether[(
  @defidform[EXHAUSTIVE-BENCHMARKS]
  @defidform[VALIDATE-BENCHMARKS]
  @defidform[SAMPLE-BENCHMARKS]
)]{
  Lists of benchmarks, organized by dataset type.
}

@deftogether[(
  @defidform[MAX-OVERHEAD]
  @defidform[NUM-EXHAUSTIVE-BENCHMARKS]
  @defidform[NUM-VALIDATE-SAMPLES]
  @defidform[NUM-NEW-SAMPLES]
  @defidform[NUM-ITERATIONS]
  @defidform[SAMPLE-RATE]
  @defidform[NUM-SAMPLE-TRIALS]
  @defidform[NUM-BETTER-WITH-TYPES]
  @defidform[BENCHMARKS-WITH-FIRST-CLASS-FUNCTIONS]
  @defidform[PYTHON]
)]{
  Various constants for the paper / experiment / analysis.
}

@defidform[EXACT-RUNTIME-XSPACE]{
  Maximum distance between a point on an exact runtime plot
   and the (integer) number of types in the configuration that the point
   represents.
}

@deftogether[(
  @defidform[u/p-ratio]
  @defidform[t/u-ratio]
  @defidform[t/p-ratio])
]{
  Format the name of a performance ratio.
}

@defidform[sra]{
  Format the phrase @emph{simple random approximation}. No typos!
}

@defidform[etal]{
  Format @emph{et al.} with proper spacing.
}

@; -----------------------------------------------------------------------------
@; --- defprocs

@defproc[(bm [str string?]) element?]{
  Render the name of a benchmark program.
}

@defproc[(bm* [str string?] ...) element?]{
  Render a sequence of benchmark names.
}

@defproc[(url [str string?]) element?]{
  Similar to the @racket[url] procedure from @racketmodname[scribble/base],
   but does some extra formatting.
}

@defproc[(generate-bibliography) part?]{
  Generate the bibliography.
  Call this at the end of the document.
  See also @racketmodname[scriblib/autobib].
}

@defproc[(~cite [b bib?] ...) element?]{
  Format a citation.
  See also @racketmodname[scriblib/autobib].
}

@defproc[(citet [b bib?]) element?]{
  Format a noun-style citation.
  See also @racketmodname[scriblib/autobib].
}

@defproc[(bm-desc [title string?] [author pre-content?] [url element?] [lib (listof pre-content?)] [description pre-content?] ...) element?]{
  Formats data describing a benchmark program.
}

@defproc[(exact-runtime-category [cat-name string?] [names (listof string?)] [make-description (-> string? pre-content?)]) element?]{
  Format a description for a class of plots.
  The class is named @racket[cat-name] and consists of the plots for the
   benchmarks @racket[names].
  The function @racket[make-description] accepts a string describing the number
   of @racket[names] and returns an element that further describes the category.
}

@defproc[(percent-slower-than-typed [name string?]) integer?]{
  Count the percentage of configurations of benchmark @racket[name] that run
   slower than the fully-typed configuration.
}

@defproc[(definition [term string?] [description string?] ...) paragraph?]{
  Format a definition for @racket[term] with content @racket[description ...].
}

@defproc[(defn [term string?]) element?]{
  Format a reference to a defined term.
}

@defproc[(lib-desc [name string?] [description string?] ...) pre-content?]{
  Format the name of a Python library and a description of how the library
   was used.
}

@defproc[($ [str string?] ...) element?]{
  Pass the given content to LaTeX math mode.
}

@deftogether[(
  @defproc[(authors [str string?] ...) element?]
  @defproc[(authors* [strs (listof string?)]) element?]
)]{
  Format a list of author names.
}

@defproc[(deliverable [D (or/c pre-content? real?)]) element?]{
  Format @emph{D-deliverable}.
}

@defproc[(approximation [r (or/c pre-content? real?)] [s (or/c pre-content? real?)] [pct (or/c pre-content? real?)]) element?]{
  Format @emph{@racket[pct]%-@racket[r],@racket[s]-approximation}.
}

@defproc[(exact [str string?] ...) element?]{
  Pass the given content directly to LaTeX.
}

@defproc[(id [x any/c]) pre-content?]{
  Same as @racket[~a].
}

@defproc[(Integer->word [n integer?]) string?]{
  Format the given integer as a capitalized word in English.
}

@defproc[(parag [title string?]) element?]{
  Format @racket[title] as the name of a paragraph.
}

@defproc[(python [code string?] ...) element?]{
  Format a block of Python code.
}

@defproc[(pythonexternal [filename string?]) element?]{
  Format the contents of the file @racket[filename] as a block of Python code.
}

@defproc[(pythoninline [code string?] ...) element?]{
  Format one line of Python code.
}

@deftogether[(
  @defproc[(sc [str string?] ...) element?]
  @defproc[(sf [str string?] ...) element?]
)]{
  Format small caps (@racket[sc]) and sans-serif (@racket[sf]) text.
}

@deftogether[(
  @defproc[(Section-ref [tag string?]) element?]
  @defproc[(section-ref [tag string?]) element?]
)]{
  Format a reference to a section.
}


@section{Static Benchmark Information}

A benchmark program consists of:
@itemlist[
@item{
  a set of fully-typed Python modules;
}
@item{
  other Python modules and data files.
}
]

The "other modules" may be typed or untyped;
 the point is that all configurations use identical copies of these modules.

@defmodule[gm-plateau-2017/script/benchmark-info]{
  API to the benchmark programs
}

@defproc[(benchmark-info? [v any/c]) boolean?]{
  Predicate for benchmark information.
}

@defproc[(benchmark->name [bm benchmark-info?]) string?]{
  Get the name from a benchmark.
}

@defproc[(benchmark->module* [bm benchmark-info?]) (listof string?)]{
  Get the names of the Python modules in the benchmark.
}

@defproc[(benchmark->src [bm benchmark-info?]) path-string?]{
  Return a path to the directory that contains the benchmark.
}

@defproc[(benchmark->num-modules [bm benchmark-info?]) natural?]{
  Count the number of modules in the benchmark.
}

@defproc[(benchmark->num-configurations [bm benchmark-info?]) natural?]{
  Count the number of configurations in the benchmark.
}

@defproc[(benchmark->max-configuration [bm benchmark-info?]) configuration?]{
  Return a configuration that is larger than any configuration in the benchmark, i.e. "max plus one".
}

@defproc[(benchmark->sloc [bm benchmark-info?]) natural?]{
  Count the source-lines-of-code in the benchmark.
  Uses David A. Wheeler's @tt{sloccount}.
}

@deftogether[(
  @defproc[(benchmark->karst-data [bm benchmark-info?]) (or/c #f path-string?)]
  @defproc[(benchmark->sample-data [bm benchmark-info?]) (or/c #f path-string?)]
)]
  Return a path to the benchmark's Karst data, if such data exists.
  The function @racket[benchmark->karst-data] finds the exhaustive data;
   the function @racket[benchmark->sample-data] finds data for randomly-sampled configurations.
}

@deftogether[(
  @defproc[(benchmark->python-data [bm benchmark-info?]) (listof real?)]
  @defproc[(benchmark->karst-retic-untyped [bm benchmark-info?]) (listof real?)]
  @defproc[(benchmark->karst-retic-typed [bm benchmark-info?]) (listof real?)]
)]{
  Return a list of Python, fully-untyped, or fully-typed runtimes.
  If such data does not exist, return an arbitary list.

  The idea with the "arbitrary" list is to return data that suffices to build
   an "obviously wrong" plot.
  Now that the paper is finished, we could error if the data does not exist.
}

@defproc[(all-benchmarks) (listof benchmark-info?)]{
  Return a list of all known benchmarks.
}

@defproc[(configuration? [v any/c]) boolean?]{
  A @deftech{configuration} is one way of mixing typed and untyped code in a benchmark.
  This predicate returns @racket[#true] when given an identifier for a configuration.
}

@deftogether[(
  @defproc[(configuration->natural [bm benchmark-info?] [cfg configuration?]) natural?]
  @defproc[(natural->configuration [bm benchmark-info?] [n natural?]) configuration?]
  @defproc[(configuration<? [cfg0 configuration?] [cfg1 configuration?]) boolean?]
)]{
  These functions define a bijection between @tech{configurations} and natural numbers,
   and consequently a total order.
}

@deftogether[(
  @defproc[(string->configuration [str string?]) configuration?]
  @defproc[(configuration->string [cfg configuration?]) string?]
)]{
  Map between @tech{configurations} and strings.
}

@defproc[(benchmark-info->python-info? [bm benchmark-info?]) python-info?]{
  Return low-level data about the Python modules in a benchmark.
}


@section{Python Data}

The Python script @filepath{gm-plateau-2017/script/explode_module.py} extracts information
 about the structure of a Python module (e.g., number of classes).

@defmodule[gm-plateau-2017/script/python]{
  API to Python syntax trees
}

@deftogether[(
  @defstruct*[python-info ([name symbol?] [module? (listof module-info?)])]
  @defstruct*[module-info ([name symbol?] [function? (listof function-info?)])]
  @defstruct*[class-info ([name symbol?] [field* (listof field-info?)] [method* (listof function-info?)])]
  @defstruct*[function-info ([name symbol?] [dom* (listof field-info?)] [cod (or/c string? #f)])]
  @defstruct*[field-info ([name symbol?] [type string?])]
)]{
  Structs for Python syntax.
  Note that nested classes and nested functions are not supported.
}

@defproc[(python-path? [v any/c]) boolean?]{
  Return @racket[#true] for path strings that end with the suffix @filepath{.py}.
}

@defproc[(python-sloc [ps python-path?]) natural?]{
  Count the source-lines-of-code in a Python module.
}

@defproc[(python-info->max-configuration [py python-info?]) configuration?]{
  Return the max-plus-one configuration for a Python program.
}

@defproc[(benchmark-dir->python-info [d is-benchmark-directory?]) python-info?]{
  Parse the Python files in a directory.
}

@deftogether[(
  @defproc[(python-info->module* [py python-info?]) (listof string?)]
  @defproc[(python-info->num-modules [py python-info?]) natural?]
  @defproc[(python-info->function* [py python-info?]) (listof string?)]
  @defproc[(python-info->num-functions [py python-info?]) natural?]
  @defproc[(python-info->class* [py python-info?]) (listof string?)]
  @defproc[(python-info->num-classes [py python-info?]) natural?]
  @defproc[(python-info->method* [py python-info?]) (listof string?)]
  @defproc[(python-info->num-methods [py python-info?]) natural?]
  @defproc[(python-info->domain* [py python-info?]) (listof (listof field-info?))]
  @defproc[(python-info->num-parameters [py python-info?]) natural?]
  @defproc[(python-info->return* [py python-info?]) (listof string?)]
  @defproc[(python-info->num-returns [py python-info?]) natural?]
  @defproc[(python-info->field* [py python-info?]) (listof field-info?)]
  @defproc[(python-info->num-fields [py python-info?]) natural?]
  @defproc[(python-info->all-types [py python-info?]) (set/c (or/c #f string?))]
  @defproc[(python-info->num-types [py python-info?]) natural?]
)]{
  For querying a Python AST.
}


@section{Reticulated Performance Data}

@defmodule[gm-plateau-2017/script/performance-info]{
  API to performance data
}

@defproc[(performance-info? [v any/c]) boolean?]{
  Predicate for performance information.
}

@defproc[(performance-info->name [pi performance-info?]) symbol?]{
  Return the name of the underlying benchmark.
}

@defproc[(benchmark->performance-info [bm benchmark-info?]) performance-info?]{
  Collect performance information for the given benchmark.
}

@deftogether[(
  @defproc[(python-runtime [pi performance-info?]) real?]
  @defproc[(untyped-runtime [pi performance-info?]) real?]
  @defproc[(typed-runtime [pi performance-info?]) real?]
)]{
  Get extreme running times.
}

@defproc[(num-configurations [pi performance-info?]) natural?]{
  Count the number of configurations in the underlying benchmark.
}

@defproc[(num-types [pi performance-info?]) natural?]{
  Count the maximum number of type annotations in the underlying benchmark.
}

@defproc[(overhead [pi performance-info?] [r real?]) real?]{
  Compute the overhead of the given number @racket[r] relative to the Python
   running time.
}

@deftogether[(
  @defproc[(min-overhead [pi performance-info?]) real?]
  @defproc[(max-overhead [pi performance-info?]) real?]
  @defproc[(mean-overhead [pi performance-info?]) real?]
)]{
  Find the minumum / maximum / mean performance overheads, across all configurations.
}

@defproc[(deliverable [D real?]) (-> performance-info? natural?)]{
  Return a function that counts the number of @emph{D-deliverable} configurations.
}

@deftogether[(
  @defproc[(typed/python-ratio [pi performance-info?]) real?]
  @defproc[(typed/retic-ratio [pi performance-info?]) real?]
  @defproc[(untyped/python-ratio [pi performance-info?]) real?]
)]{
  Compute performance ratios.
}

@defproc[(make-D-deliverable [D real?] [pi performance-info?]) (-> real? boolean?)]{
  Return a predicate on running times; the predicate returns @racket[#true] for
   running times that are at most @racket[D] times slower than the Python
   running time.
}

@defproc[(count-configurations [pi performance-info?] [good? (-> real? boolean?)]) natural?]{
  Count the number of configurations that satisfy the predicate @racket[good?].
}

@defproc[(filter-time* [pi performance-info?] [good? (-> real? boolean?)]) (listof real?)]{
  Return the mean running times for configurations whose mean running time satisfies the given predicate.
}

@defproc[(performance-info->sample* [pi performance-info?]) (cons/c natural? (listof path-string?))]{
  Return a pair with (1) sample size and (2) paths to sample data.
}

@defproc[(performance-info%sample [pi performance-info?] [ps path-string?]) performance-info?]{
  Return performance information about the given file of sampled data.
}

@defproc[(unzip-karst-data [ps path-string?]) (or/c #f path-string?)]{
  Unzip the Karst data at the given @tt{gzip}'d file.
}

@defproc[(performance-info-src [pi performance-info?]) path-string?]{
  Return a path to (exhaustive) Karst data.
}

@defproc[(line->configuration-string [ln string?]) string?]{
  Parse a line of Karst data to a string representing a configuration.
}

@defproc[(fold/karst [input (or/c path-string? performance-info?)] [#:f f (-> A configuration? natural? (listof real?) A)] [#:init init A]) A]{
  Fold (left) over Karst data.
}


@section{Generating Plots}

@defmodule[gm-plateau-2017/script/plot]{
  for building plots
}

@deftogether[(
  @defproc[(overhead-plot [pi performance-info?]) pict?]
  @defproc[(exact-runtime-plot [pi performance-info?]) pict?]
  @defproc[(validate-samples-plot [pi performance-info?]) pict?]
  @defproc[(samples-plot [pi performance-info?]) pict?]
)]{
  Plot performance data.
}

@deftogether[(
  @defparam[*LEGEND-VSPACE* n natural? #:value 10]
  @defparam[*LEGEND-HSPACE* n natural? #:value 20]
  @defparam[*OVERHEAD-PLOT-WIDTH* n natural? #:value 600]
  @defparam[*OVERHEAD-PLOT-HEIGHT* n natural? #:value 300]
  @defparam[*OVERHEAD-FONT-FACE* f string? #:value "bold"]
  @defparam[*OVERHEAD-FONT-SCALE* n (>=/c 0) #:value 0.03]
  @defparam[*OVERHEAD-LABEL?* lbl? boolean? #:value #f]
  @defparam[*OVERHEAD-LINE-COLOR* c plot-color/c #:value 3]
  @defparam[*OVERHEAD-LINE-STYLE* s plot-pen-style/c #:value 'solid]
  @defparam[*OVERHEAD-LINE-WIDTH* lw (>=/c 0) #:value 1]
  @defparam[*OVERHEAD-MAX* om natural? #:value 10]
  @defparam[*OVERHEAD-SHOW-RATIO* sr (or/c boolean? symbol?) #:value #t]
  @defparam[*OVERHEAD-SAMPLES* os natural? #:value 20]
  @defparam[*FONT-SIZE* fs natural? #:value 10]
  @defparam[*CACHE-SIZE* cs natural? #:value (expt 2 16)]
  @defparam[*POINT-SIZE* ps natural? #:value 3]
  @defparam[*POINT-ALPHA* a (>=/c 0) #:value 0.4]
  @defparam[*CONFIGURATION-X-JITTER* j real? #:value 0.4]
  @defparam[*OVERHEAD-FREEZE-BODY* f? boolean? #:value #f]
  @defparam[*CONFIDENCE-LEVEL* c (between/c 0 100) #:value 95]
  @defparam[*INTERVAL-ALPHA* r (>=/c 0) #:value 1]
  @defparam[*RATIO-DOT-SYM* s point-sym/c #:value 'plus]
  @defparam[*RATIO-DOT-SIZE* n natural? #:value 8]
  @defparam[*RATIO-DOT-COLOR* c string? #:value "firebrick"]
  @defparam[*TYPED/PYTHON-RATIO-XTICK?* t? boolean? #:value #f]
)]{
  Parameters to control ANY aspect of your plots.
  Ha Ha Ha.
}


@section{Rendering Figures}

@defmodule[gm-plateau-2017/script/render]{}

@deftogether[(
  @defproc[(render-overhead-plot* [bm* (listof benchmark-info?)]) pict?]
  @defproc[(render-exact-runtime-plot* [bm* (listof benchmark-info?)]) pict?]
  @defproc[(render-static-information [bm* (listof benchmark-info?)]) table?]
  @defproc[(render-ratios-table [bm* (listof benchmark-info?)]) table?]
  @defproc[(render-samples-plot* [bm* (listof benchmark-info?)]) pict?]
  @defproc[(render-validate-samples-plot* [bm* (listof benchmark-info?)]) pict?]
)]{
  Render figures for the given benchmarks.
  These procedures yield plots and tables similar to those in the paper.
}

@defparam[*PLOT-HEIGHT* h exact-integer?]{
  Determines the height of plots.
}

@defparam[*CACHE-SUFFIX* s string?]{
  Determines the suffix of cache files.
  See @racketmodname[with-cache].
}

@defparam[*SINGLE-COLUMN?* single? boolean?]{
  When @racket[#true], render plots in single-column format.
  (You will want to manually change the enclosing @racket[figure*] to a
   @racket[figure]. If you don't know what I mean, then just don't change
   this parameter.)
}

@deftogether[(
  @defproc[(get-ratios-table [bm* (listof benchmark-info?)]) list?]
  @defproc[(ratios-table-row [rt list?]) list?]
  @defproc[(ratios-row-retic/python [rr list?]) string?]
  @defproc[(ratios-row-typed/retic [rr list?]) string?]
  @defproc[(ratios-row-typed/python [rr list?]) string?]
)]{
  Helpers for reading performance ratios.
  The idea is, build the table once and read it many times for data.
}


@section{System Calls}

@defmodule[gm-plateau-2017/script/system]{
  A system call interface
}

@defproc[(shell [program path-string?] [args (or/c path-string? (listof path-string?))]) string?]{
  Invoke the given program with the given command-line arguemnts, return the program's standard output.
}

@defproc[(md5sum [ps path-string?]) string?]{
  Compute an MD5 hash for the given file.
  See also @racketmodname[openssl/md5].
}

@section{Utility Functions}

@defmodule[gm-plateau-2017/script/util]{
  Miscellaneous utilities
}

@defproc[(tab-split [str string?]) (listof string?)]{
  Split a string by tab characters.
  See also @racket[string-split].
}

@defproc[(tab-join [str* (listof string?)]) string?]{
  Join a list of strings using tab characters.
  See also @racket[string-join].
}

@defproc[(path-string->string [ps path-string?]) string?]{
  Convert a path or string to a string.

  This function is surprisingly useful in untyped code, and extremely useful in typed code.
}

@defproc[(ensure-directory [d path-string?]) void?]{
  Create the directory @racket[d], unless it already exists.
}

@defproc[(rnd [r real?]) string?]{
  Round a number to 2 decimal places.
}

@defproc[(pct [numerator real?] [denominator real?]) real?]{
  Return @racket[(* 100 (/ numerator denominator))].
}

@defproc[(log2 [n natural?]) natural?]{
  Return the log base 2 of a power of 2.
}

@defproc[(file-remove-extension [ps path-string?]) path-string?]{
  Remove the extension from a filename.
}

@defproc[(add-commas [r real?]) string?]{
  Format a real number to a string with commas in the normal places (between every 3 digits).
}

@defproc[(save-pict [ps path-string?] [p pict?]) boolean?]{
  Save the given pict to the given path string.
}

@defproc[(columnize [vals list?] [n natural?]) (listof list?)]{
  Arrange the given values into @racket[n] lists of almost-equal length.
}


@defproc[(force/cpu-time [thunk (-> any/c)]) (values any/c natural?)]{
  Execute the given thunk.
  Return the result and the elapsed CPU time.
  See also @racket[time-apply].
}

@deftogether[(
  @defproc[(natural->bitstring [n natural?] [#:pad k natural?]) string?]
  @defproc[(bitstring->natural [s string?]) natural?]
)]{
  A bijection between natural numbers and @racket[k]-bit strings of @racket{1} and @racket{0}.
}

@defproc[(count-zero-bits [s string?]) natural?]{
  Count the number of @litchar{0} characters in a string.
}

@defproc[(integer->word [n integer?] [#:title? title? any/c #f]) string?]{
  Convert a small integer to an English word.
  When @racket[title?] is non-@racket[#f], return a capitalized word.
}


