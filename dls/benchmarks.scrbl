#lang gm-dls-2017
@title[#:tag "sec:benchmarks"]{Benchmarks}

 @figure["fig:static-benchmark" "Static summary of benchmarks"
   @render-static-information[ALL-BENCHMARKS]]
 ]


In this section we give a brief description to each of our benchmarks. For each benchmark, we start with a fully annotated Reticulated Python program to generate our configurations, unless we state otherwise. All configurations use Timer.py from our utilities library to measure the time taken for a given configuration to run. Some programs were adapted from external sources. For these programs, we added type annotations. We state the changes made to the original version in the description.

@parag{Sample_FSM}
Originally written by ayaderaghul@github in Racket and ported to Reticulated Python.
Represents how individuals interact with each other in a population.

Author: .....   Dependencies:

@parag{Take5}
Simulates a Take5 game.
The benchmark runs 500 consecutive  simulations of the  game.

Author: ....   Dependencies: 


@parag{Evolution}
Simulates an Evolution game. 
Since the number of functions in this benchmark was too large, we annotated three files which represent all card plays a player can make during a turn.

Author: .....   Dependencies:


@parag{Espionage}
Finds the minimum spanning tree of a graph using Kruskal's algorithm.

Author: .....   Dependencies:


@parag{slowSHA}
Adapted from @citet[vksb-dls-2014]. Originally from
@url{http://github.com/sfstpala/SlowSHA}  Computes SHA-1  and SHA-512 for a
sequence of English words.

Author: ...   Dependencies:


@parag{PythonFlow} @note{masphei-2013}
Adapted from @url{https://github.com/masphei/PythonFlow}
Implements Ford-Fulkerson's Algorithm for finding the maximum flow of a graph.

Author:masphei-2013   Dependencies:


@parag{N-Queens} @note{@url{https://github.com/cython/cython/blob/master/Demos/benchmarks/nqueens.py}}.
Adapted from @url{https://github.com/cython/cython/blob/master/Demos/benchmarks/nqueens.py}.  A simple brute-force N-Queens solver.

Author: ...   Dependencies:



@parag{CallMethods}
A Microbenchmark for evaluating the overhead of function calls. It consists of 32*10^5 calls to trivial functions. The calls do not use varargs or
kwargs, and do not use tuple unpacking. 

Author: ...   Dependencies:


@parag{CallMethodSlots}
A Microbenchmark for measuring the overhead of function calls  that that define __slots__ and that have no __dict__ attribute. The calls do not use varargs or kwargs, and do not use tuple unpacking.
When an object has no __dict__ attribute, the JIT can optimize away most of the
attribute lookup. This benchmark measures this optimization. 

Author: ...   Dependencies:


@parag{Float}
Generates and normalizes a list of points then maximizes them. Adapted from [??]. 
Author: ...   Dependencies:


@parag{Futen} @note{@url{https://benchmarksgame.com}}
Adapted from @url{https://benchmarksgame.com}. Removed unit test class, nose dependency and jinja2 renderer. 

Author: ...   Dependencies:


@parag{Go}
Adapted from @citet[vksb-dls-2014] with the following changes: Refactored benchmark into three files and only Squares.py because the number of functions in the benchmark was too large.

Author: ...   Dependencies:


@parag{Chaos} @note{@url{https://github.com/dropbox/pyston/blob/master/minibenchmarks/chaos.py}}
Adapted from @url{https://github.com/dropbox/pyston/blob/master/minibenchmarks/chaos.py}. Creates chaosgame-like fractals. We fully annotated this benchmark.

Author: ...   Dependencies:


@parag{Fannkuch} @note{@url{http://shootout.alioth.debian.org/}}
"The fannkuch benchmark is defined by programs in Performing Lisp Analysis of the FANNKUCH Benchmark, Kenneth R. Anderson and Duane Rettig. FANNKUCH is an abbreviation for the German word Pfannkuchen, or pancakes, in analogy to flipping pancakes. The conjecture is that the maximum count is approximated by n*log(n) when n goes to infinity."
We fully annotated this benchmark.

Author: ...   Dependencies:


@parag{http2}

Author: ...   Dependencies:


@parag{Meteor} @note{@url{http://shootout.alioth.debian.org/}}
Adapted from @url{http://shootout.alioth.debian.org/}. Implements a solution to the Meteor puzzle. We fully annotated this benchmark.

Author: ...   Dependencies:


@parag{N_Body} @note{@url{https://benchmarksgame.com}}
Adapted from @url{https://benchmarksgame.com}. "Model the orbits of Jovian planets, using the same simple symplectic-integrator."


Author: ...   Dependencies:


@parag{PiDigits} @note{@url{http://shootout.alioth.debian.org}}
Adapted from @url{http://shootout.alioth.debian.org}. Computes some of the digits of π to stress big integer arithmetic. We changed NDIGITS to `5000`.

Author: ...   Dependencies:


@parag{SpectralNorm}  @note{@url{https://benchmarksgame.com}}
Adapted from @url{https://benchmarksgame.com}. Computes the spectral norm of a matrix. We removed main function.

Author: ...   Dependencies:




