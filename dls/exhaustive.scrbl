#lang gm-dls-2017
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
 of graphs comparing the @emph{number} of type annotations in a configuration
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
Note that each @|x-axis| is log-scaled; vertical tick marks appear at 1.2x,
 1.4x, 1.6x, 1.8x, 4x, 6x, and 8x.
Lastly, the benchmarks' name, @|t/p-ratio|, and number of configurations appear
 above each plot.

@; To note:
@; - lowest x-value with non-zero y-value = u/p-ratio
@; - lowest x-value with y=100 = max overhead

Observations:
@itemlist[
@item{
  Every configuration in the experiment is @deliverable[10].
  In other words, no combination of typed and untyped components in this
   experiment led to a performance overhead that exceeded 10x.
}
@item{
  Six benchmarks are @deliverable[2].
@;  @emph{Interpretation:} nearly one-third of the benchmark suite
@;   demonstrates little-to-no overhead.
}
@item{
  Eleven benchmarks have smooth slopes.
  A smooth slope implies that gradual typing imposes a gradual performance
   overhead, in the sense that adding a type annotation to any given component
   adds roughly the same performance overhead.
  @; TODO make this formal? Could be a cool slogan.
  @; - how to check? delta with/without each compnoent?
  @; - slogan to call it ... "continuous" ?
  @; - validate on Racket?
  @; - really matches gaps in the graph?
}
@item{
  There is no apparent correlation between a benchmark's size and its worst-case
   performance overhead.
  @TODO{need to confirm with the largest benchmarks}
}
@item{
  Ten benchmarks are approximately @deliverable{T},
   where @emph{T} is the @|t/p-ratio|.
  Contrariwise, the @bm{spectralnorm} benchmark has some partially-typed
   configurations with significantly higher overhead than the fully-typed
   configuration.
}
]


@section{Results III: Absolute Running Time}
@; what do these tell us? (less than overhead plots and even ratios, but still interesting I think)
@; for the developer:
@; - overall trend, more types = more slow
@;   - (usually, but NOT ALWAYS)
@;   - generally, num.types as a predictive model
@; for reader:
@; - helps explain slope, vertical gap = flat slope
@; - see outliers in measurements (very small number)
@; - size of experiment & design space

@figure*["fig:exact" "Running time (in seconds) vs. Number of typed components"
  @render-exact-runtime-plot*[EXHAUSTIVE-BENCHMARKS]
]

The graphs in @figure-ref{fig:exact} are the final component of the exhaustive
 evaluation of Reticulated.
These graphs serve two purposes: they explain the @emph{slopes} of the
 overhead plots (in @figure-ref{fig:overhead}) and illustrate an overall trend
 in the dataset.

Each graph in @figure-ref{fig:exact} contains one point for every trial of
 every configuration in the dataset.
These individual runs are summarized by their running time (on the @|y-axis|)
 and the (integer) number of types in the underlying configuration
 (on the @|x-axis|).

Most plots contain a massive number of points.
This is because the data for each benchmark consists of exponentially many
 configurations, and the data for each configuration consists of
 @id[NUM-ITERATIONS] trials.
To make these plots readable, the points associated with a given configuration
 are translucent and equally-spaced along the @|x-axis|.
In particular, the points for a configuration with @math{N} type annotations
 lie within the @|x-axis| interval [@math{N-@id[EXACT-RUNTIME-XSPACE]}
 @math{N+@id[EXACT-RUNTIME-XSPACE]}].
@; TLDR ROUND TO THE NEAREST INTEGER, VISUALLY!!!!!!!!!!!!

In general, these plots clearly show that configurations with more type
 annotations tend to run slower than configurations that use the dynamic type.
@; A type annotation in Reticulated implies dynamic checks, plain and simple.
@; The transpiler does not use types to generate more efficient code;
@;  HOWEVER each check also doesn't cost that much, most curves are gradual
The notable exception to this rule is @bm{spectralnorm}; the overhead in
 @bm{spectralnorm} configurations with fewer type annotations comes from
 assertions that a dynamically typed object implements certain methods.
See @secref{sec:pathologies} for details.

@; TODO is the gap from ANNOTATIONS or from BOUNDARIES ????
@; - I think annotation, just because reticulated
The second, more subtle, lesson underscored by @figure-ref{fig:exact} is the
 reason for the flat slopes in the overhead plots of @figure-ref{fig:overhead}.
Each flat slope in @figure-ref{fig:overhead} corresponds to a vertical space
 between clusters of points in @figure-ref{fig:exact}.
In terms of gradually-typed configurations, these ``gaps'' indicate an
 ``expensive'' type annotation---a type annotation that imposes a large
 runtime cost on the benchmark when it is enforced by Reticulated.
@; TODO so awkward
Many configurations will contain the same expensive annotation (or annotations);
 such configurations are vertically clustered in @figure-ref{fig:exact}.
@; TODO ha ha ha goto sleep and try again

Lastly, @figure-ref{fig:exact} shows outliers in the dataset.
The data for five benchmarks includes abnormally large running times.
These benchmarks are:
 @bm{futen}, @bm{float}, @bm{go}, @bm{meteor}, and @bm{Espionage}.
@Secref{sec:threats} addresses these and other threats to validity.
