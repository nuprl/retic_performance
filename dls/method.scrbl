#lang gm-dls-2017 @title[#:tag "sec:method"]{Adapting Takikawa et
al.'s Method} @section{Takikawa et al. method}

Takikawa et al. describe a method for measuring the
performance of a gradually typed system.  A gradually typed system for
a language @${L} defines a syntax @${L^\tau} for adding type
annotations to programs written in @${L}. The method first considers a
space of configurations obtained by taking a number of typable
components at a given granularity, and generating the set of all
possible permutations obtained by adding or removing the type
annotations from these components.

@definition["configuration"]{Let @${P} be a program written in @${L}
and let @${P’} be the same program with the possible addition of type
annotations. Then @${P'} is a @emph{configuration} of @${P}.}

@definition["configuration space"]{A configuration space of a
fully-typed configuration @${P^\tau} is the set @${\{P' \mid P'
\sqsubseteq P^\tau\}}.  } The size of a given configuration space is
bound by the number of locations in @${P} where the programmer may add
a type annotation. Informally, we call this the @emph{granularity} of
@${L^\tau}. For example, if the smallest component we can type is a
module, then for a given program P the size of the configuration space
is @${2^m} where m is the total number of modules in @${P}.

In the method proposed by Takikawa et al., we generate a configuration
lattice, which is a way to visualize a configuration space C. We then
measure all the elements of C. This allows us to generate a
performance lattice which labels all c @${\in} C with its performance.
The performance of the system overall which is represented by a number
of representative programs overall (and hence a set of confuguration
spaces), is evaluated in a number of ways.

Overhead plots show how many benchmarks are @${D}-deliverable.
@definition["D-deliverable"]{ A configuration is D-deliverable if its
performance is no worse than a factor of D slowdown compared to the
untyped configuration.} We also consider the performance of each
configuration relative to its typed/untyped ratio.
@definition["typed/untyped ratio"]{The typed/untyped ratio of a
performance lattice is the time needed to run the top configuration
divided by the time needed to run the bottom configuration.}  This
gives us an idea about how many components need to be typed in order
to achieve a @${D}-deliverable configuration for some constant @${D}.

This method could not be adapted to Reticulated in the exact way it
was adapted to Typed Racket.  Specifically, in case of Typed Racket,
where the smallest typable component for a given program @${P} is a module
@${m}, the number of elements in the largest configuration space possible
for @${P} is @${2^m}. In Reticulated Python, we are allowed to type all
components of a function signature as well as class fields. Therefore,
the upper bound of the number of elements in a configuration space for
Reticulated is @${2^{c+a+f}} where @${c} is the total number of class
fields, @${a} is the arity for all functions and @${f} is the total
number of functions. The Takikawa et al. method adapted to Typed
Racket measures the largest configuration space possible,
exhaustively. For Reticulated, such space would be too large due to
the finer granularity of the language. Therefore, we let the typable
components generating our configuration space @${C} be function
signatures and class fields. Therefore for some program @${P}, @${C}
contains @${2^{f+c}} elements where @${c} is the number of classes and
@${f} is the number of functions in @${P}.

Unlike the performance evaluation for Typed Racket, we are unable to
draw the performance and configuration lattices due to the size of our
configuration spaces, but we note that our performance lattice looks
different from a Typed Racket performance lattice. In Reticulated
Python, there is an extra configuration to consider. Namely the
regular Python configuration. That also implies that we have two
variations of the typed/untyped ratio. One that compares the fully
typed Reticulated configuration to the untyped Reticulated
configuration, and another that compares it to the untyped Python
configuration. In the following section, we describe the evaluation
process in detail.


@section[#:tag "sec:protocol"]{Protocol}

Our performance evaluation adheres to the following protocols
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
 for example, any polymorphic functions must use monomorphic types
 because Reticulated does not support Python's syntax for generics.@note{@url{https://www.python.org/dev/peps/pep-0484/#generics}}


@parag{Data Collection}
Enumerate the configuration space and choose a random permutation of the
 enumeration.
Optionally divide the permutation across identical processors or machines.
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
  reserved all processors on one node for 24 hours;
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

