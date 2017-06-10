#lang scribble/manual

;; TODO organize id / param / proc
@require[
  (for-label
    gm-dls-2017
    with-cache
    (only-in racket/contract any/c listof or/c)
    (only-in scribble/base pre-content? element? paragraph? table?)
    (only-in racket/pict pict?)
    (only-in racket/format ~a)
    (only-in scriblib/figure figure figure*))]
@title{Reference}

@defmodulelang[gm-dls-2017]{
  The @racketmodname[gm-dls-2017] language provides the reader from
   @racketmodname[scribble/base] and all exports from the @racketmodname[gm-dls-2017] module.
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
@; --- defparams

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

@defproc[(benchmark->name [bm benchmark-info?]) string?]{
  Get the name from a benchmark.
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

@deftogether[(
  @defproc[(integer->word [n integer?]) string?]
  @defproc[(Integer->word [n integer?]) string?]
)]{
  Format the given integer as a word in English.
  The function @racket[integer->word] returns lowercase words; the function
   @racket[Integer->word] returns uppercase words.
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


@section{Static Benchmark Information}

@defmodule[gm-dls-2017/script/benchmark-info]{
}


@section{Reticulated Performance Data}

@defmodule[gm-dls-2017/script/performance-info]{
}

@;script/benchmark-info.rkt
@;script/performance-info.rkt
@;script/python.rkt
@;script/sample.rkt
@;script/util.rkt
@;script/config.rkt
@;script/plot.rkt
@;script/render.rkt
@;script/system.rkt
