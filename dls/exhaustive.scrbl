#lang gm-dls-2017
@title[#:tag "sec:exhaustive"]{Exhaustive Evaluation}

@; TODO
@; dont forget, people will jump to these sections without reading the definitions
@; - first pargraph on "distilling" needs work

@figure["fig:static-benchmark" "Static summary of benchmarks"
  @render-static-information[EXHAUSTIVE-BENCHMARKS]]

This section presents the results of an @defn{exhaustive} performance
 evaluation of @integer->word[NUM-EXHAUSTIVE-BENCHMARKS]
 benchmark programs.
The benchmarks are small Python programs whose @defn{implicit} types are
 expressible in Reticulated.
The results are @defn["performance ratios"] (@figure-ref{fig:ratio}),
 @defn["overhead plots"] (@figure-ref{fig:overhead}), and a series
 of graphs comparing the @emph{number} of typed components in a configuration
 against the configuration's performance (@figure-ref{fig:exact}).


@section{About the Benchmarks}

@(let ([total @integer->word[NUM-EXHAUSTIVE-BENCHMARKS]]
       [num1 @integer->word[(length DLS-2014-BENCHMARK-NAMES)]]
       [dls-names @authors*[(map (compose1 tt symbol->string) DLS-2014-BENCHMARK-NAMES)]]
       [num2 @integer->word[(length POPL-2017-BENCHMARK-NAMES)]]
       [num3 @integer->word[(length DLS-2017-BENCHMARK-NAMES)]]
      ) @elem{
  @; Many of the benchmark programs stem from prior work on Reticulated.
  Of the @|total| benchmark programs,
   @|num1| originate from case studies by @citet[vksb-dls-2014],@note{@|dls-names|.}
   @|num2| are from the evaluation by @citet[vss-popl-2017] on programs from
   @hyperlink["http://pyperformance.readthedocs.io/"]{The Python Performance Benchmark Suite},
   and the remaining @|num3| originate from open-source programs.
  (Every list of the benchmarks in this section is ordered first by the
   benchmarks' origin and second by the benchmark's names.)
})
@; REMARK: original authors helpful with (code, test input, comments)

@(let* ([column-descr*
         (list
           @elem{lines of code (@bold{SLOC}),@note{Computed using David A. Wheeler's @hyperlink["https://www.dwheeler.com/sloccount/"]{@tt{sloccount}} utility.} }
           @elem{number of modules (@bold{M}), }
           @elem{number of function and method definitions (@bold{F}), }
           @elem{and number of class definitions (@bold{C}).})]
        [num-col @integer->word[(length column-descr*)]]
       ) @elem{
  @Figure-ref{fig:static-benchmark} tabulates information about the size and
   structure of the @defn{experimental} portions of the benchmarks.
  The @|num-col| columns report the @|column-descr*|
})

The following descriptions credit the benchmarks' original authors,
 state whether the benchmarks depend on any @defn{control} modules,
 and briefly summarize the purpose of the @defn{experimental} modules.


@; -----------------------------------------------------------------------------
@; --- WARNING: the order of benchmarks matters!
@; ---  Do not re-order without checking ALL PROSE in this file
@; -----------------------------------------------------------------------------

@bm-desc["futen"
@hyperlink["http://blog.amedama.jp/"]{@tt{momijiame}}
@url{https://github.com/momijiame/futen}
@list[
  @lib-desc["fnmatch"]{Filename matching}
  @lib-desc["os"]{Path split, path join, path expand, getenv}
  @lib-desc["re"]{One regular expression match}
  @lib-desc["shlex"]{Split host names from an input string}
  @lib-desc["socket"]{Basic socket operations}
]]{
  Generates an @hyperlink["https://www.ansible.com/"]{@tt{ansiable}} inventory
  file from an @hyperlink["https://www.openssh.com/"]{OpenSSH} configuration
  file.
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
  Computes SHA-1 and SHA-512 digests for a sequence of English words.
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
  Solves the Shootout benchmarks meteor puzzle.@note{@url{http://benchmarksgame.alioth.debian.org/u32/meteor-description.html#meteor}}
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
  Implements Weicker's @emph{Dhrystone} benchmark.@note{@url{http://www.eembc.org/techlit/datasheets/ECLDhrystoneWhitePaper2.pdf}}
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
  Implements Kruskal's spanning-tree algorithm@~cite[k-ams-1956].
  @; 1 iteration
}

@bm-desc["Evolution"
@authors["Maha Elkhairy" "Kevin McDonough" "Zeina Migeed"]
""
@list[
  @(let ([num-python-files-in-both-dir 90] @;; ./find "../benchmarks/Evolution/both" -name "*.py" | wc -l
         [num-test-files 21]) @;; ./find "../benchmarks/Evolution/both/evo_test" -name "*.py" | wc -l
    @elem{@id[(- num-python-files-in-both-dir num-test-files)] untyped modules})
]]{
  Implements a card game.
  The experimental modules represent the possible actions
   that a player can take on each turn.
  The control modules encode the players, cards, and game logic.
  @; 20 iterations
}

@bm-desc["sample_fsm"
@authors["Linh Chi Nguyen"]
@url{https://github.com/ayaderaghul/sample-fsm}
@list[
  @lib-desc["itertools"]{cycles}
  @lib-desc["os"]{path split}
  @lib-desc["random"]{random randrange}
]]{
  Simulates the interactions of economic agents via finite-state automata@~cite[n-mthesis-2014].
  This benchmark is adapted from a similar Racket program called @tt{fsmoo}@~cite[greenman-jfp-2017].
  @; 100 iterations
}

@bm-desc["PythonFlow"
@authors["Alfian Ramadhan"]
@url{https://github.com/masphei/PythonFlow}
@list[
  @lib-desc["os"]{path join}
]]{
  Implements the Ford-Fulkerson max flow algorithm@~cite[ff-cjm-1956].
  @; 1 iteration
}

@bm-desc["take5"
@authors["Maha Elkhairy" "Zeina Migeed"]
""
@list[
  @lib-desc["random"]{randrange shuffle random seed}
  @lib-desc["copy"]{deepcopy}
]]{
  Implements a card game and a simple player AI.
  @; 500 iterations
}


@section{Performance Ratios}
@; MOTIVATION (to appear in Section 3)
@; - highlevel picture of performance, coarse answer to "what is perf"
@; - overhead of choosing retic at all, vs. Python
@; - overhead of fully typing, frames expectation

@figure["fig:ratio" "Performance ratios"
  @render-ratios-table[EXHAUSTIVE-BENCHMARKS]
]

The table in @figure-ref{fig:ratio} lists data for two performance ratios.
The @emph[u/p-ratio] reports the overhead of Reticulated relative to Python.
The @emph[t/u-ratio] reports the overhead of the fully-typed
 configuration relative to the untyped configuration.

For example, the row for @bm{futen} reports a @|u/p-ratio| of 1.61.
This means that the average time to run the untyped configuration of the
 @bm{futen} benchmark using Reticulated was 1.61 times slower than the
 average time of running the same source code using @|PYTHON|.
Similarly, the @|t/u-ratio| for @bm{futen} states that the fully-typed configuration
 is 1.04 times slower than the untyped configuration.

These ratios demonstrate that migrating a benchmark to Reticulated, or
 from untyped to fully-typed, adds performance overhead.
In all cases, this overhead is somewhere between zero overhead (as opposed
 to a non-zero @emph{speedup}) and an order-of-magnitude slowdown.

Regarding the @|u/p-ratio|s: ten are below 2x,
 five are between 2x and 3x, and
 the remaining four are below 4.5x.
The @|t/p-ratio|s are typically lower:
  sixteen are below 2x,
  one is between 2x and 3x,
  and the final two are below 3.5x.
In particular, fourteen of the benchmarks
 have smaller @|t/u-ratio|s than @|u/p-ratio|s.
This data suggests that migrating an arbitrary
 Python program to Reticulated will add a relatively larger overhead
 than migrating the same program to a fully-typed configuration.

@; For developers:
@; - the PERFORMANCE pain of choosing retic
@; - should be LESS than the PERFORMANCE pain of adding type annotations
@; - I mean, the overall pain will be their PRODUCT
@; - but just running under retic should tell you what to expect


@section{Overhead Plots}
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
 for @emph{D} between 1 and @id[MAX-OVERHEAD] (@|x-axis|).
The @|x-axes| are log-scaled to emphasize the practical importance of low
 overheads;
 vertical tick marks appear at 1.2x, 1.4x, 1.6x, 1.8x, 4x, 6x, and 8x.

The heading above the plot for a given benchmark lists the benchmark's name,
 @|t/p-ratio| (in parentheses), and number of configurations.
Note that the @|t/p-ratio| is equal to the product of the @|u/p-ratio| and
 @|t/u-ratio| reported in @figure-ref{fig:ratio}.
The number of configurations is equal to @$|{2^{F+C}}|,
 where @${F} and @${C} denote the corresponding values from
 @figure-ref{fig:static-benchmark}.
@; TODO clarify "corresponding values"? Could say, "denote the number of functions (F) and number of classes (C) reported in ....

@parag{How to Read the Overhead Plots}
@; HMMMM "are" is NOT correct, but it sticks.
Overhead plots are cumulative distribution functions.
As the value of @${D} increases along the @|x-axis|, the number of
 @deliverable{D} configurations can only increase.
In other words, blue is better!
The larger the shaded area under the curve on each plot, the more configurations
 are @deliverable{D} for low values of @${D}.
And if a benchmark has many @deliverable{D} configurations, a developer
 that applies gradual typing has a higher chance of arriving at a configuration
 that is @deliverable{D}.

After surveying the area under a curve, the second most important aspects of
 an overhead plot are the values of @${D} where the curve starts and ends.
More precisely, if @${f} is a function that counts the number of @deliverable{D}
 configurations in a fixed benchmark, the critical points are the smallest
 values @${d_{min}, d_{max}} such
 that @${f(d_{min}) > 0} and @${f(d_{max}) = 100}.
An ideal start-value would lie between zero and one; if @${d_{min} < 1} then
 at least one configuration runs faster than the original Python code.
The end-value @${d_{max}} is the overhead of the slowest-running configuration
 in the benchmark.
@; given the choice of type annotations

Lastly, the slope of a curve corresponds to the likelihood that
 accepting a small increase in performance overhead makes a given configuration
 deliverable.
A flat curve (zero slope) indicates that the performance of a group of
 configurations is dominated by a common set of type annotations.


@parag{Distilling the Overhead Plots}

Curves in @figure-ref{fig:overhead} typically cover a large area and reach the
 top of the @|y-axis| at a low value of @${D}.
This value is always less than 10; every configuration in the experiment is
 @deliverable{10}.
Six benchmarks are even @deliverable{2}.
Including these six, @integer->word[@sub1[NUM-EXHAUSTIVE-BENCHMARKS]] benchmarks are
 roughly @deliverable{T}, where @${T} is the @|t/p-ratio| listed above each plot.
The only exception is @bm{spectralnorm}, which has some configurations where
 adding a type annotation can improve performance.
In fact this improvement is due to a bug Reticulated's implementation, see
 @section-ref{sec:pathologies}.

None of the configurations in the experiment run faster than the Python baseline.
This is no surprise, since Reticulated only adds runtime checks to Python code.

Eleven benchmarks have smooth slopes.
The other seven have flat segments because there are type boundaries in these
 benchmarks that introduce significant overhead.


@section[#:tag "sec:exact"]{Absolute Running Times}

@figure*["fig:exact" "Running time (in seconds) vs. Number of typed components"
  @render-exact-runtime-plot*[EXHAUSTIVE-BENCHMARKS]
]

Since removing type annotations in a Reticulated program can change its
 performance, a natural question is whether one can @emph{predict} the
 performance for a given configuration.
The plots in @figure-ref{fig:exact} demonstrate that a simple heuristic
 works well for these benchmarks: @emph{the performance of a configuration is
 proportional to the number of typed components in the configuration}.
In @section-ref{sec:method} terms, @${P(c) \sim @gnorm{c}_\tau}.
@; TOO CUTE

@Figure-ref{fig:exact} contains one green point for every run of every
 configuration in the experiment.@note{Recall from @section-ref{sec:protocol},
 the data for each configuration is @id[NUM-ITERATIONS] runs.}
@; This is the entire dataset of the exhaustive evaluation.
Each point compares the number of @emph{typed components} in a configuration
 (@|x-axis|) against its running time in seconds (@|y-axis|).
A typed component is either a typed function or a typed class definition.

Most plots contain a very large number of points; to make the plots readable,
 the points associated with a given configuration are spread across the @|x-axis|.
In particular, the @id[NUM-ITERATIONS] points for a configuration with @math{N}
 type annotations lie within the interval @${N \pm @id[EXACT-RUNTIME-XSPACE]}
 on the @|x-axis|.
For example, the @bm{fannkuch} benchmark has two configurations: one untyped
 configuration with zero types and one fully-typed configuration with one type.
To determine whether a point @${(x,y)} in the plot for @bm{fannkuch} represents
 the untyped or fully-typed configuration, round the point's
 @${x}-component to the nearest integer.

Overall, there is a clear trend that adding type annotations adds performance
 overhead.
The variations between individual plots fall into four overlapping categories:

@exact-runtime-category["types make things slow"
  '(futen http2 slowSHA chaos float pystone PythonFlow take5)
  (λ (num-in-category) @elem{
    The plots for @|num-in-category| benchmarks show a gradual increase in
     performance as the number of type annotations increases.
    Adding @emph{any} single type annotation adds a small performance overhead.
})]

@exact-runtime-category[@elem{types make things really slow}
  '(call_method call_method_slots call_simple go meteor nqueens spectralnorm Espionage)
  (λ (num-in-category) @elem{
    @string-titlecase[num-in-category] plots have vertical "gaps" between
     clusters of configurations.
    Configurations below the gap contain type annotations that impose little
     runtime cost.
    Configurations above the gap have some common type annotations that
     add significant overhead.
    Each gaps corresponds to a flat slope in @figure-ref{fig:overhead}.
})]

@exact-runtime-category[@elem{types are free}
  '(fannkuch nbody pidigits)
  (λ (num-in-category) @elem{
    In @|num-in-category| plots, all configurations have approximately equal performance.
    The dynamic checks that enforce type soundness add insignificant overhead.
})]

@; TODO is http2 a type IV ?
@exact-runtime-category[@elem{types make things fast}
  '(call_method call_method_slots spectralnorm)
  (λ (num-in-category) @elem{
    In @|num-in-category| of the benchmarks, adding some types to some
     configurations actually improves performance.
    These speedups are due to issues in the implementation of Reticulated.
    @bm{spectralnorm} types remove a check that the inner component of a tuple
     is an integer.
    Types in @bm{call_method} and @bm{call_method_slots} remove checks that
     a value used as an object binds certain fields.
})]


@(let* ([outliers (map bm '(futen float go meteor Espionage))]) @elem{
  @emph{Note:} the data for @authors*[outliers] contain a small number of outliers.
  @Section-ref{sec:threats} addresses these and other threats to validity.
})
