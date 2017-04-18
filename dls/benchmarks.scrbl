#lang gm-dls-2017
@title[#:tag "sec:benchmarks"]{Benchmarks}

@figure["fig:static-benchmark" "Static summary of benchmarks"
  @render-static-information[ALL-BENCHMARKS]]

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

The following summaries of the benchmark programs are sorted by their original
source.
The summaries also credit the original authors of each program and note
whether each benchmark contains untyped modules.

@bm-desc["futen"
@hyperlink["http://blog.amedama.jp/"]{@tt{momijiame}}
@url{https://github.com/momijiame/futen}
@list[
  @lib-desc["os"]{Path split, path join, path expand, getenv}
  @lib-desc["fnmatch"]{Filename matching}
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
@hyperlink["https://github.com/httplib2/httplib2"]{Joe Gregorio}
@url{https://github.com/httplib2/httplib2}
@lib-desc["urllib"]{To split an IRI into components}
]{
  Converts a collection of Internationalized Resource Identifiers
  (@hyperlink["https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier"]{IRIs})
  to equivalent @hyperlink["http://www.asciitable.com/"]{ASCII} resource
  identifiers.
  @; 10 iterations
}

@bm-desc["slowSHA"
"Stefano Palazzo"
@url{http://github.com/sfstpala/SlowSHA}
@lib-desc["os"]{path split}
]{
  Computes SHA-1 and SHA-512 digests for a sequence of English words.
  @; 1 iteration
}

@bm-desc["call_method"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[]]{
  Stress test for method calls; the calls do not use argument lists,
  keyword arguments, or tuple unpacking.
  @; Consists of @${32*10^5} calls to trivial functions.
  @; 1 iteration
}

@bm-desc["call_method_slots"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[]]{
  Stresses calls to methods that have been declared through an object's @tt{__slots__} attribute.
  @; 1 iteration
}

@bm-desc["call_method_simple"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[]]{
  Stress test for function calls.
  This benchmark is similar to @tt{call_method}, but using functions rather than methods.
}

@bm-desc["chaos"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[
@lib-desc["math"]{Square root}
@lib-desc["random"]{randrange}
]]{
  Creates fractals using the @hyperlink["https://en.wikipedia.org/wiki/Chaos_game"]{@emph{chaos game}} method.
  @; 1 iteration
}

@bm-desc["fannkuch"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[]]{
  Implements Anderson and Rettig's microbenchmark@~cite[ar-lp-1994].
  @; 1 iteration
}

@bm-desc["float"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@lib-desc["math"]{Sin, Cos, Sqrt}]{
  Stress test for floating-point operations.
  @; 1 iteration (200,000 points)
}

@bm-desc["go"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[
  @lib-desc["math"]{sqrt log}
  @lib-desc["random"]{randrange random}
]]{
  Implements a simple AI for playing @hyperlink["https://en.wikipedia.org/wiki/Go_(game)"]{go}.
  This benchmark is split across three files: a typed module that implements
  the game board, an untyped module that defines constants, and an untyped module
  that implements the AI and drives the benchmark.
  @; 2 iterations
}

@bm-desc["meteor"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[]]{
  A solver for the Shootout benchmarks meteor puzzle.@note{@url{http://benchmarksgame.alioth.debian.org/u32/meteor-description.html#meteor}}
  @; 1 iterations (finds at most 6,000 solutions)
}

@bm-desc["nbody"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[]]{
  Models the orbits of the @hyperlink["https://en.wikipedia.org/wiki/Giant_planet"]{Jovian planets}.
  @; 1 iteration
}

@bm-desc["nqueens"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[]]{
  A brute-force solver for the @hyperlink["https://developers.google.com/optimization/puzzles/queens"]{N queens} problem.
  @; 10 iterations
}

@bm-desc["pidigits"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[]]{
  Stress test for big-integer arithmetic.
  @; 1 iteration (5,000 digits)
}

@bm-desc["pystone"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[]]{
  Python adaptation of Weicker's @emph{Dhrystone} benchmark.@note{@url{http://www.eembc.org/techlit/datasheets/ECLDhrystoneWhitePaper2.pdf}}
  @; 50,000 iterations
}

@bm-desc["spectralnorm"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}
@list[]]{
  Computes the largest singular value of an infinite matrix.
  @; 10 iterations
}

@bm-desc["Espionage"
"Zeina Migeed"
""
@lib-desc["operator"]{itemgetter}]{
  Implements and tests Kruskal's algorithm.
  @; 1 iteration
}

@bm-desc["Evolution"
"Maha Elkhairy, Kevin McDonough, and Zeina Migeed"
""
@list[]]{
  Implements a card game.
  This benchmark tests the performance impact of gradual typing on the files
  that represent possible card plays that a player can make.
  The program includes 40 other files; these remain untyped throughout the
  experiment.
  @; 20 iterations
}

@bm-desc["sample_fsm"
"Linh Chi Nguyen"
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
"Alfian Ramadhan"
@url{https://github.com/masphei/PythonFlow}
@lib-desc["os"]{path join}]{
  Implements the Ford-Fulkerson max flow algorithm.
  @; 1 iteration
}

@bm-desc["take5"
"Maha Elkhairy & Zeina Migeed"
""
@list[]]{
  Implements a card game and a simple player AI.
  @; 500 iterations
}

