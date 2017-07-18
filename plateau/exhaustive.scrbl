#lang gm-plateau-2017
@title[#:tag "sec:exhaustive"]{Exhaustive Evaluation}

@figure["fig:static-benchmark" "Static summary of benchmarks"
  @render-static-information[EXHAUSTIVE-BENCHMARKS]]

This section presents the results of an @defn{exhaustive} performance
 evaluation of @integer->word[NUM-EXHAUSTIVE-BENCHMARKS]
 benchmark programs.
The benchmarks are small Python programs whose @defn{implicit} types are
 expressible in Reticulated.
The results are @defn["performance ratios"] (@figure-ref{fig:ratio}),
 @defn["overhead plots"] (@figure-ref{fig:overhead}), and a series
 of graphs comparing the number of typed components in a configuration
 against the configuration's performance (@figure-ref{fig:exact}).


@section{About the Benchmarks}

@(let ([total @integer->word[NUM-EXHAUSTIVE-BENCHMARKS]]
       [num1 @integer->word[(length DLS-2014-BENCHMARK-NAMES)]]
       [dls-names @authors*[(map (compose1 tt symbol->string) DLS-2014-BENCHMARK-NAMES)]]
       [num2 @integer->word[(length POPL-2017-BENCHMARK-NAMES)]]
       [num3 @integer->word[(length '(Espionage PythonFlow take5))]]
      ) @elem{
  @; Many of the benchmark programs stem from prior work on Reticulated.
  Of the @|total| benchmark programs,
   @|num1| originate from case studies by @citet[vksb-dls-2014],
   @;@note{@|dls-names|.}
   @|num2| are from the evaluation by @citet[vss-popl-2017] on programs from
   the Python Performance Benchmark Suite,
   and the remaining @|num3| originate from open-source programs.
  Every listing of the benchmarks in this section is ordered first by the
   benchmark's origin and second by the benchmark's name.
})
@; REMARK: original authors helpful with (code, test input, comments)

@(let* ([column-descr*
         (list
           @elem{lines of code (@bold{SLOC}), }
           @elem{number of modules (@bold{M}), }
           @elem{number of function and method definitions (@bold{F}), }
           @elem{and number of class definitions (@bold{C}).})]
        [num-col @integer->word[(length column-descr*)]]
       ) @elem{
  @Figure-ref{fig:static-benchmark} tabulates information about the size and
   structure of the @defn{experimental} portions of the benchmarks.
  The @|num-col| columns report the @|column-descr*|
})

The following descriptions credit each benchmark's original author,
 state whether it depends on any @defn{control} modules,
 and briefly summarize its purpose.


@; -----------------------------------------------------------------------------
@; --- WARNING: the order of benchmarks matters!
@; ---  Do not re-order without checking ALL PROSE in this file
@; -----------------------------------------------------------------------------

@bm-desc["futen"
@hyperlink["http://blog.amedama.jp/"]{@tt{momijiame}}
@url{https://github.com/momijiame/futen}
@list[
  @lib-desc["fnmatch"]{Filename matching}
  @lib-desc["os.path"]{Path split, path join, path expand, getenv}
  @lib-desc["re"]{One regular expression match}
  @lib-desc["shlex"]{Split host names from an input string}
  @lib-desc["socket"]{Basic socket operations}
]]{
  Converts an @hyperlink["https://www.openssh.com/"]{OpenSSH} configuration
  file to an inventory file for the
  @hyperlink["https://www.ansible.com/"]{@emph{Ansiable}} framework.
  @; 1900 iterations
}

@bm-desc["http2"
@authors[@hyperlink["https://github.com/httplib2/httplib2"]{Joe Gregorio}]
@url{https://github.com/httplib2/httplib2}
@list[
  @lib-desc["urllib"]{To split an IRI into components}
]]{
  Converts a collection of @hyperlink["https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier"]{Internationalized Resource Identifiers}
  to equivalent @hyperlink["http://www.asciitable.com/"]{ASCII} resource
  identifiers.
  @; 10 iterations
}

@bm-desc["slowSHA"
@authors["Stefano Palazzo"]
@url{http://github.com/sfstpala/SlowSHA}
@list[
  @lib-desc["os"]{path split}
]]{
  Applies the SHA-1 and SHA-512 algorithms to English words.
  @; 1 iteration
}

@bm-desc["call_method"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Microbenchmarks simple method calls;
  the calls do not use argument lists,
  keyword arguments, or tuple unpacking.
  @; Consists of @${32*10^5} calls to trivial functions.
  @; 1 iteration
}

@bm-desc["call_method_slots"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Same as @bm{call_method}, but using receiver objects that declare their methods
   in their @hyperlink["https://docs.python.org/3/reference/datamodel.html#slots"]{@tt{__slots__}}
   attribute.
  @; 1 iteration
}

@bm-desc["call_simple"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Same as @bm{call_method}, using functions rather than methods.
}

@bm-desc["chaos"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[
  @lib-desc["math"]{Square root}
  @lib-desc["random"]{randrange}
]]{
  Creates fractals using the @hyperlink["https://en.wikipedia.org/wiki/Chaos_game"]{@emph{chaos game}} method.
  @; 1 iteration
}

@bm-desc["fannkuch"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Implements Anderson and Rettig's microbenchmark@~cite[ar-lp-1994].
  @; 1 iteration
}

@bm-desc["float"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[
  @lib-desc["math"]{Sin, Cos, Sqrt}
]]{
  Microbenchmarks floating-point operations.
  @; 1 iteration (200,000 points)
}

@bm-desc["go"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[
  @lib-desc["math"]{sqrt log}
  @lib-desc["random"]{randrange random}
  "two untyped modules"
]]{
  Implements the game @hyperlink["https://en.wikipedia.org/wiki/Go_(game)"]{Go}.
  This benchmark is split across three files: an @defn{experimental} module that implements
  the game board, a @defn{control} module that defines constants, and a @defn{control} module
  that implements an AI and drives the benchmark.
  @; 2 iterations
}

@bm-desc["meteor"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Solves the Shootout benchmarks meteor puzzle.
  @note{@url{http://benchmarksgame.alioth.debian.org/u32/meteor-description.html}}
  @; 1 iterations (finds at most 6,000 solutions)
}

@bm-desc["nbody"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Models the orbits of the @hyperlink["https://en.wikipedia.org/wiki/Giant_planet"]{Jovian planets}.
  @; 1 iteration
}

@bm-desc["nqueens"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Solves the @hyperlink["https://developers.google.com/optimization/puzzles/queens"]{@math{N} queens} problem by a brute-force algorithm.
  @; 10 iterations
}

@bm-desc["pidigits"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Microbenchmarks big-integer arithmetic.
  @; 1 iteration (5,000 digits)
}

@bm-desc["pystone"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Implements Weicker's @emph{Dhrystone} benchmark.
  @note{@url{http://www.eembc.org/techlit/datasheets/ECLDhrystoneWhitePaper2.pdf}}
  @; 50,000 iterations
}

@bm-desc["spectralnorm"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Computes the largest singular value of an infinite matrix.
  @; 10 iterations
}

@bm-desc["Espionage"
@authors["Zeina Migeed"]
""
@list[
  @lib-desc["operator"]{itemgetter}
]]{
  Implements Kruskal's spanning-tree algorithm.
  @; 1 iteration
}

@bm-desc["PythonFlow"
@authors["Alfian Ramadhan"]
@url{https://github.com/masphei/PythonFlow}
@list[
  @lib-desc["os"]{path join}
]]{
  Implements the Ford-Fulkerson max flow algorithm. 
  @; no longer needs citation
  @;@~cite[ff-cjm-1956].
  @; 1 iteration
}

@bm-desc["take5"
@authors["Maha Alkhairy" "Zeina Migeed"]
""
@list[
  @lib-desc["random"]{randrange shuffle random seed}
  @lib-desc["copy"]{deepcopy}
]]{
  Implements a card game and a simple player AI.
  @; 500 iterations
}


@section{Performance Ratios}

@figure["fig:ratio" "Performance ratios"
  @render-ratios-table[EXHAUSTIVE-BENCHMARKS]
]

@(define RT (get-ratios-table EXHAUSTIVE-BENCHMARKS))

The table in @figure-ref{fig:ratio} lists three performance ratios.
These ratios correspond to the extreme endpoints of gradual typing:
 the performance of untyped Reticulated relative to Python (the @emph[u/p-ratio]),
 the performance of the fully-typed configuration relative to the untyped configuration in Reticulated (the @emph[t/u-ratio]),
 and the overall delta between fully-typed Reticulated and Python (the @emph[t/p-ratio]).

@(let* ([futen-row (ratios-table-row RT 'futen)]
        [futen-u/p (ratios-row-retic/python futen-row)]
        [futen-t/u (ratios-row-typed/retic futen-row)]) @elem{
  For example, the row for @bm{futen} reports a @|u/p-ratio| of @${@|futen-u/p|}.
  This means that the average time to run the untyped configuration of the
   @bm{futen} benchmark using Reticulated was @${@|futen-u/p|} times slower than the
   average time of running the same code using @|PYTHON|.
  Similarly, the @|t/u-ratio| for @bm{futen} states that the fully-typed configuration
   is @${@|futen-t/u|} times slower than the untyped configuration.
})

On one hand, these ratios demonstrate that migrating a benchmark to
 Reticulated, or from untyped to fully-typed, always adds performance overhead.
The migration never improves performance.
On the other hand, the overhead is always within an order-of-magnitude.
@(let* ([rp* (map ratios-row-retic/python RT)]
        [tr* (map ratios-row-typed/retic RT)]
        [count-< (λ (x* n) (length (filter (λ (str) (< (string->number str) n)) x*)))]
        [rp-<2 (count-< rp* 2)]
        [rp-<3 (count-< rp* 3)]
        [rp-<4.5 (count-< rp* 4.5)]
        [tr-<2 (count-< tr* 2)]
        [tr-<3 (count-< tr* 3)]
        [tr-<3.5 (count-< tr* 3.5)]
        [num-> (for/sum ([rp (in-list rp*)]
                         [tr (in-list tr*)]
                         #:when (> (string->number rp) (string->number tr)))
                 1)])
  (unless (= (length rp*) rp-<4.5)
    (raise-user-error 'performance-ratios
      "expected all retic/python ratios to be < 4.5, but only ~a of ~a are" rp-<4.5 (length rp*)))
  @elem{
    Regarding the @|u/p-ratio|s:
     @integer->word[rp-<2] are below @${2}x,
     @integer->word[(- rp-<3 rp-<2)] are between @${2}x and @${3}x, and
     the remaining @integer->word[(- rp-<4.5 rp-<3)] are below @${4.5}x.
    The @|t/u-ratio|s are typically lower:
      @integer->word[tr-<2] are below @${2}x,
      @integer->word[(- tr-<3 tr-<2)] is between @${2}x and @${3}x,
      and the final @integer->word[(- tr-<3.5 tr-<3)] are below @${3.5}x.
    In particular, @integer->word[num->] benchmarks
     have larger @|u/p-ratio|s than @|t/u-ratio|s.
    This data suggests that migrating an arbitrary
     Python program to Reticulated adds a relatively larger overhead
     than migrating the same program to a fully-typed configuration.
})

@section[#:tag "sec:overhead"]{Overhead Plots}
@; these plots are the main event!
@; - given "any program any configuration", what is probability of OK perf?
@; - how does prob. change as "OK" changes?
@; and minor points for developers:
@; - given U, what proportion of configs. are unusable (sort of, what is worst-case)
@; - slopes => are there pathological type boundaries

@figure*["fig:overhead" "Overhead plots"
  @render-overhead-plot*[EXHAUSTIVE-BENCHMARKS]
]

@Figure-ref{fig:overhead} summarizes the overhead of gradual typing in
 Reticulated @emph{relative to Python} across all
 configurations of the @integer->word[NUM-EXHAUSTIVE-BENCHMARKS] benchmarks.
Each overhead plot reports the percent of @deliverable[] configurations (@|y-axis|)
 for values of @${D} between @${1} and @${@id[MAX-OVERHEAD]} (@|x-axis|).
The @|x-axes| are log-scaled to focus on low overheads;
 vertical tick marks appear at @${1.2}x, @${1.4}x, @${1.6}x, @${1.8}x, @${4}x, @${6}x, and @${8}x overhead.

The heading above the plot for a given benchmark lists the benchmark's name
 and number of configurations.
Note that the number of configurations is equal to @$|{2^{F+C}}|,
 with @${F} and @${C} from @figure-ref{fig:static-benchmark}.
@; TODO being the same

@parag{How to Read the Overhead Plots}
Overhead plots are cumulative distribution functions.
As the value of @${D} increases along the @|x-axis|, the number of
 @deliverable{D} configurations can only increase or stay the same.
The important question is how many configurations are @deliverable{D}
 for low values of @${D}.
The area under the curve is the answer; more is better.
A curve with a large shaded area below it implies that a large number
 of configurations have low performance overhead.
If many benchmarks have many low-overhead configurations, a developer
 that applies gradual typing has a higher chance of arriving at a configuration
 that is @deliverable{D} for a value of @${D} that meets their requirements.

@(let ([d0 "a"]
       [d1 "b"]) @elem{
  After surveying the area under a curve, the second most important aspects of
   an overhead plot are the values of @${D} where the curve starts and ends.
  More precisely, if @${h : \mathbb{R}^+ \rightarrow \mathbb{N}} is a function
   that counts the number of @deliverable{D}
   configurations in a benchmark, the critical points are the smallest
   overheads @${@|d0|, @|d1|} such
   that @${h(@|d0|) > 0} and @${h(@|d1|) = 100}.
  An ideal start-value would lie between zero and one; if @${@|d0| < 1} then
   at least one configuration runs faster than the original Python code.
  The end-value @${@|d1|} is the overhead of the slowest-running configuration
   in the benchmark.
})
@; given the choice of type annotations

Lastly, the slope of a curve corresponds to the likelihood that
 accepting a small increase in performance overhead increases the number
 of deliverable configurations.
A flat curve (zero slope) suggests that the performance of a group of
 configurations is dominated by a common set of type annotations.


@parag{Distilling the Overhead Plots}

Curves in @figure-ref{fig:overhead} typically cover a large area and reach the
 top of the @|y-axis| at a low value of @${D}.
This value is always less than @${@id[MAX-OVERHEAD]}.
In other words, every configuration in the
 experiment is @deliverable[MAX-OVERHEAD].
For many benchmarks, the maximum overhead is significantly lower.
Indeed, seven benchmarks are @deliverable{2}.

None of the configurations in the experiment run faster than the Python baseline.
This is no surprise, because Reticulated adds run-time checks to Python code for
 each type annotation.

@(let ([smooth '(futen http2 slowSHA chaos fannkuch float nbody pidigits pystone PythonFlow take5)])
  @elem{
    @Integer->word[(length smooth)] benchmarks have relatively smooth slopes.
    The plots for the other @integer->word[(- NUM-EXHAUSTIVE-BENCHMARKS (length smooth))]
     benchmarks have wide, flat segments because those
     benchmarks contain at least one function or method that is called frequently.
    For example, if a benchmark creates many instances of a class @tt{C},
     adding a type annotation to the method @tt{C.__init__} adds significant
     overhead.
})

@string-titlecase[@integer->word[(- NUM-EXHAUSTIVE-BENCHMARKS 3)]] benchmarks
 are roughly @deliverable{T}, where @${T} is the @|t/p-ratio| listed in @figure-ref{fig:ratio}.
In these benchmarks, the fully-typed configuration is one of the slowest-running
 configurations.
The notable exception is @bm{spectralnorm}, in which the fully-typed configuration
 runs faster than @${@id[@percent-slower-than-typed{spectralnorm}]\%} of the configurations.
This speedup occurs because of an unsoundness in the implementation of Reticulated;
 in short, the implementation does not dynamically type-check the contents of tuples.@note{@url{https://github.com/mvitousek/reticulated/issues/36}}
@; TODO bad linebreak


@section[#:tag "sec:exact"]{Absolute Running Times}

@figure*["fig:exact" "Running time (in seconds) vs. Number of typed components"
  @render-exact-runtime-plot*[EXHAUSTIVE-BENCHMARKS]
]

Since changing the type annotations in a Reticulated program changes its
 performance, the language should provide a cost model to help developers
 predict the performance of a given configuration.
The plots in @figure-ref{fig:exact} demonstrate that a simple heuristic
 works well for these benchmarks: @emph{the performance of a configuration is
 proportional to the number of typed components in the configuration}.
@;In @section-ref{sec:method} terms, the cost model is @${P(c) \propto @gnorm{c}_\tau}.

@Figure-ref{fig:exact} contains one green point for every run of every
 configuration in the experiment.@note{Recall from @section-ref{sec:protocol},
 the data for each configuration is @id[NUM-ITERATIONS] runs.}
@; This is the entire dataset of the exhaustive evaluation.
Each point compares the number of typed functions, methods, and classes in a
 configuration (@|x-axis|) against its running time in seconds (@|y-axis|).

The plots contain many points with both the same number of typed components
 and similar performance.
To reduce the visual overlap between such points, the points for a given
 configuration are spread across the @|x-axis|.
The @id[NUM-ITERATIONS] points for a configuration with @math{N}
 typed components lie within the interval @${N \pm @id[EXACT-RUNTIME-XSPACE]}
 on the @|x-axis|.
For example, @bm{fannkuch} has two configurations: one untyped
 configuration with zero typed components and one fully-typed configuration
  with one typed component.
To determine whether a point @${(x,y)} in the plot for @bm{fannkuch} represents
 the untyped or fully-typed configuration, round @${x} to the nearest integer.

Overall, there is a clear trend that adding type annotations adds performance
 overhead.
The variations between individual plots fall into four overlapping categories:

@exact-runtime-category["types make things slow"
  '(futen slowSHA chaos float pystone PythonFlow take5)
  (λ (num-in-category) @elem{
    The plots for @|num-in-category| benchmarks show a gradual increase in
     performance as the number of typed components increases.
    Typing any function, class, or method adds a small performance overhead.
})]

@exact-runtime-category[@elem{types make things very slow}
  '(call_method call_method_slots call_simple go http2 meteor nqueens spectralnorm Espionage PythonFlow)
  (λ (num-in-category) @elem{
    @string-titlecase[num-in-category] plots have visible gaps between
     clusters of configurations with the same number of types.
    Configurations below the gap contain type annotations that impose relatively little
     run-time cost.
    Configurations above the gap have some common type annotations that
     add significant overhead.
    Each such gap corresponds to a flat slope in @figure-ref{fig:overhead}.
})]

@exact-runtime-category[@elem{types are free}
  '(fannkuch nbody pidigits)
  (λ (num-in-category) @elem{
    In @|num-in-category| benchmarks, all configurations have similar performance.
    The dynamic checks that enforce type soundness add insignificant overhead.
})]

@; TODO is http2 a type IV ?
@exact-runtime-category[@elem{types make things fast}
  '(call_method call_method_slots spectralnorm)
  (λ (num-in-category) @elem{
    In @|num-in-category| benchmarks, there are some configurations
     that run faster than similar configurations with fewer typed components.
    These speedups happen for one of two reasons: either because of duplicate
     checks on dynamically-typed receivers of method calls,
     or because of omitted checks on values annotated with tuple types.
    The former is due to an overlap between Reticulated's semantics and
     Python's dynamic typing@~cite[vksb-dls-2014].
    The latter is due to a bug in the implementation (see @section-ref{sec:overhead}).
})]


@(let* ([outliers (map bm '(futen float go meteor Espionage))]) @elem{
  @bold{Note}: the data for @authors*[outliers] contain a small number of outliers.
  @Section-ref{sec:threats} addresses these and other threats to validity.
  @; TODO really not much of an address at the moment
})