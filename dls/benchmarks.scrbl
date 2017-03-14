#lang scribble/acmart
@require[
  "common.rkt"
]
@section[#:tag "sec:benchmarks"]{Benchmarks}

@; @figure["fig:static-benchmark" "Static Benchmark Characteristics"
@;   @tabular[
@;    #:sep @hspace[2]
@;    #:row-properties '(bottom-border 1)
@;    #:column-properties '(left right right right)
@;    @list[
@;     @list[@bold{Name}       @bold{# Mod} @bold{\# Func (\% typed)} @bold{\# Param}]
@;     @list[@elem{Sample FSM} @elem{ 5}    @elem{999  (10%)}         @elem{999}]
@;     @list[@elem{Take5}      @elem{ 3}    @elem{999}                @elem{999}]
@;     @list[@elem{Evolution}  @elem{77}    @elem{999}                @elem{999}]
@;     @list[@elem{Espionage}  @elem{ 2}    @elem{999}                @elem{999}]
@;     @list[@elem{Slow SHA}   @elem{ 4}    @elem{999}                @elem{999}]]]
@; ]
@; 
@; % remove BSL
@; % mention size of the reader, parser etc. - how much computation time does each part take to run
@; % for take5, talk about making the program loop to inc. time > 1 sec


@;@Figure-ref{fig:static-benchmark} talks about the size of our benchmarks.

@parag{Sample FSM}
This program simulates the tension between individuals focused on their own
interest, and the interest of the general population.  In this program,
individuals are represented by finite state automaton. An automata describes
how an individual acts. The transitions between the different states of the
automaton represent how the individual interacts with other individuals. This
simulation assumes a fixed number of actions. The program was fully annotated
with types to obtain the various configurations.

@parag{Lisp Intepreter}
This project implements an evaluator for a small subset of Racket, called
Beginning Student Language (BSL).  The program receives a BSL program,
evaluates it and prints the result. The program consists of a reader, a parser
and an interpreter, and overall, the program contains n functions which would
produce @${2^n} configurations.  Since this number of configurations is too large
to run, We chose to annotate  the reader  

@parag{Take5}
This program is a simulation  of  a Take5 game. The game consists of a dealer
and a number of players. It  is played in rounds, each round consists of turns.
The game is played following a set of rules, and after each turn, the players'
scores are updated. At the end of the game the program outputs the final scores
This program was entirely typed. On average, a Take5 configuration runs in x
seconds. Since that time was too small to measure the differences in
performance across various configurations, The time was scaled by X by letting
the program run x consequtive  simulations of the  game.


@parag{Evolution}
Simulation of an Evolution game. The program takes an argument n, representing
the number of players participating in the game. It then creates a dealer which
runs a complete simulation of the game. The program then outputs the players'
scores.  Only three files from the program where typed. Those files were of the
classes/types  for all card plays a player can make during a turn.


@parag{Espionage}
This program implements the minimum spanning tree algorithm using Kruskal's algorithm.
The program was entirely typed to produce the various configurations.

@parag{slowSHA}
Adapted from @citet[vksb-dls-2014]. Originally from
@url{http://github.com/sfstpala/SlowSHA}  Computes SHA-1  and SHA-512 for a
sequence of English words.

