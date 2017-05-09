#lang gm-dls-2017
@title[#:tag "sec:method"]{Adapting Takikawa et al.'s Method}

For each benchmark, we aimed to choose a set of configurations that represent the overall performance of Reticulated Python, and had size less than x. In our method, we type functions as a whole, yielding 2^n configurations per benchmark, where n is the number of functions in a benchmark. 

@itemlist[
@item{
  Find programs, port to reticulated
}
@item{
  Run against program which generates all possible configurations of the
  program by typing/untyping each function
}
@item{
  Run each configuration for x iterations, recording the time using python's
  system timer
}
@item{
  Machine used was KARST CLUSTER
}

]


@section{Landscape}

@; NOTE need to borrow terms from literature, e.g.
@; - Thatte's type-precision relation
@; - Henglein's "completions" (also erasures?)

@; TODO
@; - syntax for P(c) ~ ||c||t

Let @${L} be a programming language.
Let @${P} be some program written in the language, composed of @${n_M} modules
 @${M_0 \ldots M_{n_M - 1}}.

A gradual type system for @${L} defines a syntax @${L^\tau} for adding type
 annotations to @${L} programs.
Of course @${P} is an @${L} program; if @${P'} is like @${P} but contains
 some type annotations, we say @${P'} is a @emph{gradually typed configuration}
 of @${P}.
More generally,

@definition["configuration"]{
  Let @${u : L^\tau \rightarrow L} be a function that strips all type annotations
   from an @${L^\tau} program.
  A given @${L^\tau} program @${P} is a @emph{gradually typed configuration}
   of the @${L} progam @${u(P)}.
}

Note that @${u(P) = u(u(P))}.
In other words, every @${L} program is implicitly an @${L^\tau} program
 and implicitly a configuration of itself.

Performance evaluation for a gradually typed language @${L^\tau} is:
@itemlist[
@item{
  select some representative @${L} programs,
}
@item{
  for each program @${P}, compare the performance of @${P} as an @${L} program
   to the performance of its configurations
}
@item{
  summarize the performance
}
]
The fundamental assumption of performance evaluation is that the computed
 summaries are representative of the performance of configurations of an
 arbitrary @${L} program.

There is a serious problem with the description.
For a given program @${P}, the set @${\{P' \mid u(P') = P\}} may be infinite.
See @figure-ref{fig:infinite-configuration-space} for an example.
Key insight from @citet[tfdffthf-ecoop-2015] is to define the notion of a
 @emph{fully-typed configuration}.

@figure["fig:infinite-configuration-space" "Identify function has an infinite configuration space"
  @exact|{
    \fbox{L}
    $\begin{array}{l l l}
       \tau & ::= & \mathsf{Int} \mid \tau \rightarrow \tau
    \\ e & ::= & x \mid \lambda\,x.\,e \mid e~e
    \\ e^\tau & ::= & x \mid \lambda\,x:\tau.\,e^\tau \mid e^\tau~e^\tau
    \end{array}$

    \vspace{1ex}

    $\lambda\,x.\,x$ is an $e$ program with an infinite configuration space
  }|
]

@definition["fully-typed configuration"]{
  Let @${P} be an @${L} program.
  A fully-typed configuration of @${P} is an @${L^\tau} program @${P^\tau}
   such that @${P^\tau} contains a full type annotation everywhere that tha
   syntax of @${L^\tau} allows.
}

@definition["implicit types"]{
  An program @${P} is implicitly typed if @${P} has at least one
   fully-typed configuration.
  The type annotations in a given fully-typed configuration for @${P}
   are a manifestation of the @emph{implicit types} in @${P}.
}

Of course, a given @${L} program may not have any fully-typed configurations.
@; ... such programs are ??? (we don't need this definition so why bother)

Instead of measuring the performance of @${L} programs per se,
 @citet[tfdffthf-ecoop-2015] propose a slightly different protocol:
@itemlist[
@item{
  select some representative @${L} programs,
}
@item{
  for each program @${P}, choose a fully-typed configuration @${P^\tau}
}
@item{
  compare the performance of @${P} to the performance of each configuration
   in the finite set @${\{P' \mid u(P') = P \wedge P' \sqsubseteq P^\tau\}}
}
@item{
  summarize the performance of the @${P'}
}
]

The following definition is central to this approach:

@definition["configuration space"]{
  The configuration space of a fully-typed configuration @${P^\tau} is the set
   @${\{P' \mid P' \sqsubseteq P^\tau\}}.
}

The size of this set depends on the syntax of @${L^\tau}.
Specifically, it depends on the number of locations in @${P} where the programmer
 may add a type annotation.
Informally, we call this the @emph{granularity} of @${L^\tau}.
Formally,

@definition["granularity norm"]{
  The granularity norm of a gradually typed language @${L^\tau} is a function
   @${@gnorm{\cdot}} from ``syntax'' to natural numbers.
  @TODO{restrictions}
}
@; TODO actually has properties of a norm?

@bold{Examples}
@itemlist[
@item{
  Let @${@gnorm{P}_M} count the number of modules in the program @${P}.
  This is the granularity norm for Typed Racket.
  It is also a valid granularity norm for Reticulated Python.
}
@item{
  Let @${@gnorm{P}_f} count the number of function in @${P}.
  This is a valid granularity norm for Reticulated.
}
@item{
  Let @${@gnorm{P}_C} count the number of classes in @${P}.
  This is another valid granularity norm for Reticulated.
}
@item{
  Let @${P} be a program, assume every function in @${P} has a natural-number
   arity (no keyword or optional arguments).
  Let @${@gnorm{P}_\mu} sum the number of classes, number of functions (including methods),
   and arity of each function.
  This is a norm for Reticulated, moreover it is the @emph{finest} such norm,
   in the sense that for any other Reticulated norm
   @${@gnorm{\cdot}_?} the inequality @${@gnorm{P}_? \leq @gnorm{P}_\mu} holds.
}
]

Other things being equal a larger norm is better, but the size of a configuration
 space is exponential in the norm.
Two ways to reduce the size:
@itemlist[#:style 'ordered
@item{
  Use a coarser, non-trivial norm.
}
@item{
  Refactor programs.
  Remove unused functions or class fields,
   inline simple functions,
   do not measure libraries.
  @; TODO did we do anything else?
}
]

Makes sense not to measure external libraries.
A programmer using gradual typing probably cannot change library code.
Other code, may make less sense to not measure it.
So, important to distinguish between experimental and control modules.

Informally, a @emph{whole program} @${P} is self-contained code, e.g.
 if a line of code in ${P} depends on some other code, that code is included
 somewhere in @${P}.
For performance evaluation we distinguish between @emph{experimental} and
 @emph{control} portions of a whole program @${P}.
The experimental code in @${P} is some code @${P' \subseteq P} for which a
 fully-typed configuration exists.
A @defn{proper} performance evaluation will measure the configuration space
 of @${P'}.
The control code in @${P} is everything not in the experimental portion,
 intuitively a subset @${P_c} such that @${P_c = P \setminus P'}.

Unless we say otherwise, all control code is untyped.

@definition[(elem u/p-ratio " " t/u-ratio " " t/p-ratio)]{
  TBA
}

@definition["performance ratio"]{
  TBA, need to generalize "typed/untyped" and "typed/python" and "untyped/python".
}

@definition[@deliverable{D}]{
  TBA
}

@definition["exhaustive evaluation"]{
  Measure everything in configuration space.
}

@definition["approximate evaluation"]{
  Measure some things in configuration space, in a principled way.
  @Section-ref{sec:linear} introduces one form of approximation (@approximation["s" "t" "P"])
   and demonstrates that linear-sized samples of a configuration space
   provide a good approximation.
  @; maybe explanation should use parameters. huh
}


@section[#:tag "sec:protocol"]{Protocol}

The performance evaluations in this paper adhere to the following protocols
 for @emph{benchmark creation} and @emph{data collection}.

@; In this application of the Takikawa method, experimental _components_
@;  are always modules so we will not say "component"
@; Written as general "recipe to follow", except for details of Karst

@parag{Benchmark Creation}
Given a Python program, first build a driver module that performs some
 non-trivial computation using the program.
Second, remove any non-determinism or unneccesary I/O actions@note{e.g. print
 statements and requests for user input} from the program.
Third, define the experimental modules.
Fourth, infer fully-typed configurations for the experimental modules.

When possible, use existing type annotations and comments to infer
 the fully-typed configuration of the benchmark.
When necessary, use details of the driver module to infer types;
 for example, any polymorphic functions on lists must use monomorphic types
 because Reticulated does not support Python's syntax for generics.@note{@url{https://www.python.org/dev/peps/pep-0484/#generics}}


@parag{Data Collection}
Enumerate the configuration space and choose a random permutation of the
 enumeration.
Optionally divide the permutation across multiple processors or machines.
Run the main module of the configuration a fixed number of times and record
 each running time.
Finally, run the main module of the untyped configuration using the standard
 Python interpreter.


@parag{Details of the Evaluations}

Sections@|~|@secref{sec:exhaustive} and @secref{sec:linear} present data
 from the @emph{Karst at Indiana University} high-throughput computing cluster.@note{@url{https://kb.iu.edu/d/bezu}}
Each job that we scheduled on the cluster:
@itemlist[#:style 'ordered
@item{
  reserved all processors on an arbitrary cluster node for a 24-hour span;
}
@item{
  downloaded fresh copies of @|PYTHON|@note{@url{https://www.python.org/download/releases/3.4.3/}}
  and Reticulated (commit @hyperlink["https://github.com/mvitousek/reticulated/commit/e478343ce7c0f2bc50d897b0ad38055e8fd9487d"]{@tt{e478343}}
  on the @hyperlink["https://github.com/mvitousek/reticulated"]{@tt{master}} branch);
}
@item{
  for the rest of the 24-hour span:
  selected a random configuration to measure,
  ran the configuration's main module @id[NUM-ITERATIONS] times,
  and recorded the result of each run.
}
]
The data is the result of running such jobs in parallel.
Cluster nodes are IBM NeXtScale nx360 M4 servers with two Intel Xeon E5-2650 v2
 8-core processors, 32 GB of RAM, and 250 GB of local disk storage.@note{@url{https://kb.iu.edu/d/bezu#overview}}

Three details of the Karst protocol warrant further attention.
First, nodes selected a random configuration by reading from a
 text file that contained a permutation of the configuration space.
This text file was stored on a dedicated machine.
Second, the same dedicated machine that stored the text file also stored
 an explicit representation of the configuration space of each @emph{module}
 of each benchmark.
After a node selected a configuration to run, it copied the relevant files
 to private storage before running the main module.
Third, we wrapped the main computation of every benchmark in a
 @tt{with} statement@note{@url{https://www.python.org/dev/peps/pep-0343/}}
 to record execution time (via the Python function
 @hyperlink["https://docs.python.org/3/library/time.html#time.process_time"]{@tt{time.process_time()}}).

The online supplement to this paper contains scripts that implement the above
 protocol, both for the Karst cluster and for a typical workstation.
