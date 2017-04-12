#lang gm-dls-2017
@title[#:tag "sec:benchmarks"]{Benchmarks}

@(define (TODO . arg*) (bold (cons "TODO" arg*))) @; delete this!

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
   Suite;@note{@url{https://github.com/python/performance}}
}
@item{
  and the remaining @integer->word[(length DLS-2017-BENCHMARK-NAMES)] benchmarks
  are open source programs converted to Reticulated by the second author.
}
]

The following summaries of the benchmark programs are sorted by their original
 source.
The summaries also credit the original authors of each program and note
 whether each benchmark contains untyped modules.

@bm-desc["futen"
@hyperlink["http://blog.amedama.jp/"]{@tt{momijiame}}
@url{https://github.com/momijiame/futen}]{
Generates an @hyperlink["https://www.ansible.com/"]{@tt{ansiable}} inventory
 file from an @hyperlink["https://www.openssh.com/"]{OpenSSH} configuration
 file.
}

@bm-desc["http2"
""
""]{
}

@bm-desc["slowSHA"
"Stefano Palazzo"
@url{http://github.com/sfstpala/SlowSHA}]{
Computes SHA-1 and SHA-512 @TODO{double-check} for a sequence of English words.
}

@bm-desc["call_method"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
A Microbenchmark for evaluating the overhead of function calls. It consists of
@${32*10^5} calls to trivial functions. The calls do not use varargs or kwargs,
and do not use tuple unpacking.
}

@bm-desc["call_method_slots"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
A Microbenchmark for measuring the overhead of function calls  that that define
__slots__ and that have no __dict__ attribute. The calls do not use varargs or
kwargs, and do not use tuple unpacking.  When an object has no __dict__
attribute, the JIT can optimize away most of the attribute lookup. This
benchmark measures this optimization.
}

@bm-desc["call_method_simple"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
@TODO{describe me!}
}

@bm-desc["chaos"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
Creates chaosgame-like fractals.
}

@bm-desc["Fannkuch"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
Python adaptation of Anderson and Rettig's microbenchmark.
}

@bm-desc["float"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
Generates and normalizes a list of points then maximizes them.
}

@bm-desc["go"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
Refactored benchmark into three files and only Squares.py because the number of
functions in the benchmark was too large.
}

@bm-desc["meteor"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
Implements a solution to the Meteor puzzle.
}

@bm-desc["nbody"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
Model the orbits of Jovian planets, using the same simple symplectic-integrator.
}

@bm-desc["nqueens"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
A simple brute-force N-Queens solver.
}

@bm-desc["pidigits"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
Computes some of the digits of π to stress big integer arithmetic.
}

@bm-desc["pystone"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
Computes some of the digits of π to stress big integer arithmetic.
}

@bm-desc["spectralnorm"
"The Python Benchmark Suite"
@url{https://github.com/python/performance}]{
Computes the spectral norm of a matrix.
}

@bm-desc["Espionage"
"Zeina Migeed"
""]{
Finds the minimum spanning tree of a graph using Kruskal's algorithm.
}

@bm-desc["Evolution"
"Maha Elkhairy & Kevin McDonough &  Zeina Migeed"
""]{
Simulates an Evolution game.
Since the number of functions in this benchmark was too large, we annotated
three files which represent all card plays a player can make during a turn.
}

@bm-desc["sample_fsm"
"Linh Chi Nguyen"
@url{https://github.com/ayaderaghul/sample-fsm}]{
Originally written in Racket and ported to Reticulated Python.
Represents how individuals interact with each other in a population.
}

@bm-desc["PythonFlow"
"Alfian Ramadhan"
@url{https://github.com/masphei/PythonFlow}]{
Implements Ford-Fulkerson's Algorithm for finding the maximum flow of a graph.
}

@bm-desc["take5"
"Maha Elkhairy & Zeina Migeed"
""]{
Simulates a Take5 game.
The benchmark runs 500 consecutive  simulations of the game.
}
