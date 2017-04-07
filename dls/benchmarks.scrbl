#lang gm-dls-2017
@title[#:tag "sec:benchmarks"]{Benchmarks}

 @figure["fig:static-benchmark" "Static summary of benchmarks"
   @render-static-information[ALL-BENCHMARKS]]
 

In this section we give a brief description to each of our benchmarks. For each benchmark, we start with a fully annotated Reticulated Python program to generate our configurations, unless we state otherwise. All configurations use Timer.py from our utilities library to measure the time taken for a given configuration to run. Some programs were adapted from external sources. For these programs, we added type annotations. We state the changes made to the original version in the description.


@bm-desc["Sample_FSM"
"Linh Chi Nguyen"
"https://github.com/ayaderaghul/sample-fsm"]{
Originally written in Racket and ported to Reticulated Python.
Represents how individuals interact with each other in a population.}

@bm-desc["Take 5"
"Maha Elkhairy & Zeina Migeed"
""]{
Simulates a Take5 game.
The benchmark runs 500 consecutive  simulations of the  game.}


@bm-desc["Evolution"
"Maha Elkhairy & Kevin McDonough &  Zeina Migeed"
""]{
Simulates an Evolution game. 
Since the number of functions in this benchmark was too large, we annotated three files which represent all card plays a player can make during a turn.}

@bm-desc["Espionage"
"Zeina Migeed"
""]{
Finds the minimum spanning tree of a graph using Kruskal's algorithm.}

@bm-desc["SlowSHA"
"Stefano Palazzo"
"http://github.com/sfstpala/SlowSHA"]{
Adapted from @citet[vksb-dls-2014]. Computes SHA-1  and SHA-512 for a
sequence of English words.}

@bm-desc["PythonFlow"
"Alfian Ramadhan"
"https://github.com/masphei/PythonFlow"]{
Implements Ford-Fulkerson's Algorithm for finding the maximum flow of a graph.}

@bm-desc["N-Queens"
"The Python Benchmark Suite"
"https://github.com/python/performance"]{
 A simple brute-force N-Queens solver.}

@bm-desc["CallMethods"
"The Python Benchmark Suite"
"https://github.com/python/performance"]{
A Microbenchmark for evaluating the overhead of function calls. It consists of @${32*10^5} calls to trivial functions. The calls do not use varargs or
kwargs, and do not use tuple unpacking.}


@bm-desc["CallMethodSlots"
"The Python Benchmark Suite"
"https://github.com/python/performance"]{
A Microbenchmark for measuring the overhead of function calls  that that define __slots__ and that have no __dict__ attribute. The calls do not use varargs or kwargs, and do not use tuple unpacking.
When an object has no __dict__ attribute, the JIT can optimize away most of the
attribute lookup. This benchmark measures this optimization.}


@bm-desc["Float"
"The Python Benchmark Suite"
"https://github.com/python/performance"]{
Generates and normalizes a list of points then maximizes them.}



@bm-desc["Futen"
"????"
"???"]{
Removed unit test class, nose dependency and jinja2 renderer.}



@bm-desc["Go"
"The Python Benchmark Suite"
"https://github.com/python/performance"]{
Adapted from @citet[vksb-dls-2014] with the following changes: Refactored benchmark into three files and only Squares.py because the number of functions in the benchmark was too large.}


@bm-desc["Chaos"
"The Python Benchmark Suite"
"https://github.com/python/performance"]{
Creates chaosgame-like fractals. We fully annotated this benchmark.}




@bm-desc["Fannkuch"
"The Python Benchmark Suite"
"https://github.com/python/performance"]{
"The fannkuch benchmark is defined by programs in Performing Lisp Analysis of the FANNKUCH Benchmark, Kenneth R. Anderson and Duane Rettig. FANNKUCH is an abbreviation for the German word Pfannkuchen, or pancakes, in analogy to flipping pancakes. The conjecture is that the maximum count is approximated by n*log(n) when n goes to infinity."
We fully annotated this benchmark.}



@bm-desc["Http2"
""
""]{}


@bm-desc["Meteor"
"The Python Benchmark Suite"
"https://github.com/python/performance"]{
Implements a solution to the Meteor puzzle. We fully annotated this benchmark.}




@bm-desc["N-body"
"The Python Benchmark Suite"
"https://github.com/python/performance"]{
"Model the orbits of Jovian planets, using the same simple symplectic-integrator."}



@bm-desc["Pidigits"
"The Python Benchmark Suite"
"https://github.com/python/performance"]{
Computes some of the digits of π to stress big integer arithmetic.}



@bm-desc["SpectralNorm"
"The Python Benchmark Suite"
"https://github.com/python/performance"]{
Computes the spectral norm of a matrix.}






