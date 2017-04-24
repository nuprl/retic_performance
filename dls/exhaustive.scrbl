#lang gm-dls-2017
@title[#:tag "sec:exhaustive"]{Exhaustive Evaluation}

@figure["fig:static-benchmark" "Static summary of benchmarks"
  @render-static-information[ALL-BENCHMARKS]]

This section presents the results of an @emph{exhaustive} performance
 evaluation of @integer->word[NUM-BENCHMARKS] benchmark programs.
The benchmarks are small Python programs whose @emph{implicit} types are
 expressible in Reticulated.
Broadly speaking, the benchmark programs come from three sources:
@itemlist[
@item{
  @integer->word[(length DLS-2014-BENCHMARK-NAMES)] benchmarks are adaptations
   of case studies conducted by @citet[vksb-dls-2014];
}
@item{
  @integer->word[(length POPL-2017-BENCHMARK-NAMES)] benchmarks are from
   the recent evaluation of Transient Reticulated@~cite[vss-popl-2017] on
   microbenchmarks from the Python Performance Benchmark
   Suite;@note{@url{https://github.com/python/performance}} and
}
@item{
  the remaining @integer->word[(length DLS-2017-BENCHMARK-NAMES)] benchmarks
  are open source programs converted to Reticulated by the second author.
}
]

@Figure-ref{fig:static-benchmark} tabulates information about the size and
 structure of the @emph{gradually typed} portions of the benchmarks.@note{In contrast, some benchmarks depend on third-party libraries or other untyped code.}
The five columns report the lines of code (@bold{SLOC}),@note{Computed using David A. Wheeler's @hyperlink["https://www.dwheeler.com/sloccount/"]{@tt{sloccount}} utility.}
 number of modules (@bold{M}),
 number of top-level function definitions (@bold{F}),
 number of class definitions (@bold{C}),
 and number of methods (@bold{m}).

The following descriptions briefly summarize the purpose of each benchmark.
In addition, the descriptions credit the original authors of each program and
 state whether the benchmark relies on any libraries or untyped modules.

@; -----------------------------------------------------------------------------
@; --- WARNING: the order of benchmarks matters!
@; ---  Do not re-order without changing the prose!
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
  Converts a collection of Internationalized Resource Identifiers
  (@hyperlink["https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier"]{IRIs})
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
  Microbenchmarks the overhead of standard method calls;
  the calls do not use argument lists,
  keyword arguments, or tuple unpacking.
  @; Consists of @${32*10^5} calls to trivial functions.
  @; 1 iteration
}

@bm-desc["call_method_slots"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Microbenchmarks the overhead of calls to methods that have been declared
  through an object's @tt{__slots__} attribute.
  @; 1 iteration
}

@bm-desc["call_method_simple"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Microbenchmarks standard function calls.
  This benchmark is similar to @tt{call_method}, but using functions rather
  than methods.
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
  Implements a simple AI for playing @hyperlink["https://en.wikipedia.org/wiki/Go_(game)"]{Go}.
  This benchmark is split across three files: a typed module that implements
  the game board, an untyped module that defines constants, and an untyped module
  that implements the AI and drives the benchmark.
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
  Solves the @hyperlink["https://developers.google.com/optimization/puzzles/queens"]{N queens} problem by a brute-force algorithm.
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
  Implements Kruskal's spanning-tree algorithm.
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
  The gradually typed modules in this benchmark represent the possible actions
  that a player can take on each turn.
  The untyped modules encode the players, cards, and game logic.
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
  This benchmark is adapted from a similar Racket program.
  @; 100 iterations
}

@bm-desc["PythonFlow"
@authors["Alfian Ramadhan"]
@url{https://github.com/masphei/PythonFlow}
@list[
  @lib-desc["os"]{path join}
]]{
  Implements the Ford-Fulkerson max flow algorithm.
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


@section{Protocol}

@; - pick types
@; - type everyting
@; - granularity
@; - karst, specs
@; - iterations
@; - what/where timings

@section{Results I: Performance Ratios}

@figure["fig:ratio" "Performance ratios"
  @render-ratios-table[ALL-BENCHMARKS]
]

The table in @figure-ref{fig:ratio} presents two sets of performance ratios.
The @emph[u/p-ratio] reports the overhead of Reticulated relative to Python and
The @emph[t/u-ratio] reports the overhead of the fully-typed Reticulated
 configuration relative to the untyped configuration.
For example, the row for @bm{futen} reports a @|u/p-ratio| of 1.61.
This means that the average time to run the untyped configuration of the
 @bm{futen} benchmark using Reticulated was 1.61 times slower than the
 average time of running the same source code using Python 3.4.
The @|t/u-ratio| for @bm{futen} implies that the fully-typed configuration
 is 1.04 times slower than the untyped configuration, both run using Reticulated.

Observations:
@itemlist[
@item{
  Every ratio in the table is either 1x or greater.
  @emph{Interpretation:} migrating from Python to Reticulated---or from the untyped
   configuration to the fully-typed configuration---never leads to a performance
   improvement in the benchmark programs.
}
@item{
  Ten @|u/p-ratio|s are below 2x,
  five @|u/p-ratio|s are between 2x and 3x,
  and the remaining four @|u/p-ratio|s are below 4.5x.
}
@item{
  Sixteen @|t/u-ratio|s are below 2x,
  one @|t/u-ratio| is below 3x,
  and the other two @|t/u-ratio|s are below 3.5x.
}
@item{
  For fourteen benchmarks, the @|t/u-ratio| is less than the @|u/p-ratio|.
  @emph{Interpretation:} migrating from the untyped configuration to the
   fully-typed configuration typically adds less overhead than migrating
   the untyped program from Python to Reticulated.
}
]


@section{Results II: Overhead Plots}

@figure*["fig:overhead" "Overhead plots"
  @render-overhead-plot*[ALL-BENCHMARKS]
]

@Figure-ref{fig:overhead} summarizes the overhead of gradual typing in
 Reticulated @emph{relative to Python} across all
 configurations of the @integer->word[NUM-BENCHMARKS] benchmarks.
Each overhead plot reports the percent of @deliverable[] configurations (@emph{y}-axis)
 for @emph{D} between 1 and @id[MAX-OVERHEAD] (@emph{x}-axis).
Note that the @emph{x}-axes are log-scaled; vertical tick marks appear at 1.2x,
 1.4x, 1.6x, 1.8x, 4x, 6x, and 8x.
Lastly, the benchmarks' name, @|t/p-ratio|, and number of configurations appear above
 each plot.

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
  In six benchmarks, every configuration is @deliverable[2].
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
  In ten benchmarks, nearly 100% of configurations are @deliverable{T}
   where @emph{T} is the @|t/p-ratio|.
  Contrariwise, the @bm{spectralnorm} benchmark has some partially-typed
   configurations with significantly higher overhead than the fully-typed
   configuration.
}
]


@section{Results III: Absolute Running Time}

@figure*["fig:exact" "Exact running times (sec)"
  @render-exact-runtime-plot*[ALL-BENCHMARKS]
]


