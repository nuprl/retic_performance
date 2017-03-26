#lang gm-dls-2017
@title[#:tag "sec:benchmarks"]{Benchmarks}

 @figure["fig:static-benchmark" "Static Benchmark Characteristics"
   @tabular[
    #:sep @hspace[2]
    #:row-properties '(bottom-border 1)
    #:column-properties '(left right right right)
    @list[
     @list[@bold{Name}       @bold{# Mod} @bold{\# Func (\% typed)} @bold{\# Param}]
@;     @list[@elem{Sample FSM} @elem{ 5}    @elem{999  (10%)}         @elem{999}]
     @list[@elem{Take5}      @elem{ 3}    @elem{999}                @elem{999}]
     @list[@elem{Evolution}  @elem{77}    @elem{999}                @elem{999}]
     @list[@elem{Espionage}  @elem{ 2}    @elem{999}                @elem{999}]
     @list[@elem{Slow SHA}   @elem{ 4}    @elem{999}                @elem{999}]]]
 ]

  @; remove BSL
  @; mention size of the reader, parser etc. - how much computation time does each part take to run
  @; for take5, talk about making the program loop to inc. time > 1 sec


@;@Figure-ref{fig:static-benchmark} talks about the size of our benchmarks.



In this section we give a brief description of the benchmarks used in our performance evaluation. and denote the portion of the benchmark that was annotated with types. If the total number of functions is less than or equal to x for a given benchmark, we annotated all functions. Otherwise, we chose at most x functions to annotate.
We wrote some of the benchmarks and the rest was adapted from other sources. We mention the main changes made to those benchmarks. All of our benchmarks use Timer.py from our utilities library benchmark_tools. This allows us to measure the time it takes for each configuration to run. 

@parag{Sample_FSM}
This benchmark simulates the tension between individuals focused on their own
interest, and the interest of the general population.  In this program,
individuals are represented by finite state automaton. An automata describes
how an individual acts. The transitions between the different states of the
automaton represent how the individual interacts with other individuals. This
simulation assumes a fixed number of actions. The program was fully annotated.

@parag{Take5}
This program is a simulation  of  a Take5 game. The game consists of a dealer
and a number of players. It  is played in rounds, each round consists of turns.
The game is played following a set of rules, and after each turn, the players'
scores are updated. At the end of the game the program outputs the final scores
This program was fully annotated. On average, a Take5 configuration runs in x
seconds. Since that time was too small to measure the differences in
performance across various configurations, The time was scaled by X by letting
the program run x consequtive  simulations of the  game.

@parag{Evolution}
Simulation of an Evolution game. The program takes an argument n, representing
the number of players participating in the game. It then creates a dealer which
runs a complete simulation of the game. The program then outputs the players'
scores. Since the number of functions in this benchmark was too large, we annotated three files: cardplay.py, exchange_for_population.py and exchange_for_species.py.


@parag{Espionage}
This program finds the minimum spanning tree of a graph using Kruskal's algorithm and was fully annotated.

@parag{slowSHA}
Adapted from @citet[vksb-dls-2014]. Originally from
@url{http://github.com/sfstpala/SlowSHA}  Computes SHA-1  and SHA-512 for a
sequence of English words. This benchmark was fully annotated.

@parag{PythonFlow} @note{masphei-2013}
Implements Ford-Fulkerson's Algorithm for finding the maximum flow of a graph. The benchmark was fully annotated.

@parag{N-Queens} @note{@url{https://github.com/cython/cython/blob/master/Demos/benchmarks/nqueens.py}}. A simple fully annotated, brute-force N-Queens solver.

@parag{CallMethods}
A Microbenchmark for evaluating the overhead of function calls. It consists of 32*10^5 calls to trivial functions. The calls do not use varargs or
kwargs, and do not use tuple unpacking. This benchmark was fully annotated. 

@parag{CallMethodSlots}
A Microbenchmark for measuring the overhead of function calls  that that define __slots__ and that have no __dict__ attribute. The calls do not use varargs or kwargs, and do not use tuple unpacking.
When an object has no __dict__ attribute, the JIT can optimize away most of the
attribute lookup. This benchmark measures this optimization. The benchmark was fully annotated.

@parag{Float}
Generates and normalizes a list of points then maximizes them. Adapted from [??]. We added missing type annotations.

@parag{Futen} @note{@url{https://benchmarksgame.com}}
Removed unit test class, nose dependency and jinja2 renderer. 

@parag{Go}
Adapted from @citet[vksb-dls-2014] with the following changes: Refactored benchmark into three files and only Squares.py because the number of functions in the benchmark was too large.

@parag{Chaos} @note{@url{https://github.com/dropbox/pyston/blob/master/minibenchmarks/chaos.py}}
Creates chaosgame-like fractals. We fully annotated this benchmark.


@parag{Fannkuch} @note{@url{http://shootout.alioth.debian.org/}}
"The fannkuch benchmark is defined by programs in Performing Lisp Analysis of the FANNKUCH Benchmark, Kenneth R. Anderson and Duane Rettig. FANNKUCH is an abbreviation for the German word Pfannkuchen, or pancakes, in analogy to flipping pancakes. The conjecture is that the maximum count is approximated by n*log(n) when n goes to infinity."
We fully annotated this benchmark.

@parag{http2}


@parag{Meteor} @note{@url{http://shootout.alioth.debian.org/}}
Implements a solution to the Meteor puzzle. We fully annotated this benchmark.

@parag{N_Body} @note{@url{https://benchmarksgame.com}}
"Model the orbits of Jovian planets, using the same simple symplectic-integrator."
We fully annotated this benchmark.

@parag{PiDigits} @note{@url{http://shootout.alioth.debian.org}}
Computes some of the digits of π to stress big integer arithmetic. We changed NDIGITS to `5000` and fully annotated the benchmark.

@parag{SpectralNorm}  @note{@url{https://benchmarksgame.com}}
Computes the spectral norm of a matrix. We removed main function and fully annotated the benchmark.





