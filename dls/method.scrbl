#lang gm-dls-2017 @title[#:tag "sec:method"]{Adapting Takikawa et
al.'s Method}

The Takikawa et al. method considers a space of configurations
obtained by taking a number of typable components at a given
granularity, and generating the set of all possible permutations
obtained by adding or removing the type annotations from these
components. More specifically, a gradually typed system for @${L} defines a syntax
@${L^\tau} for adding type annotations to programs written in
@${L}.  Let @${P} be a program written in @${L} and let
@${P’} be the same program with the possible addition of type
annotations. Then @${P'} is a @emph{gradually typed
configuration} of @${P}.
@definition["configuration"]{ Let
@${u : L^\tau \rightarrow L} be a function that strips all
type annotations from an @${L^\tau} program.  A given
@${L^\tau} program @${P} is a @emph{gradually typed
configuration} of the @${L} progam @${u(P)}.  }
@definition["configuration space"]{ The configuration space
of a fully-typed configuration @${P^\tau} is the set @${\{P'
\mid P' \sqsubseteq P^\tau\}}.  } The size of the configuration space is
bound by the number of locations in @${P} where the
programmer may add a type annotation. Informally, we call
this the @emph{granularity} of @${L^\tau}. For example, if
the smallest component we can type is a module, then for a
given program P the size of the configuration space is @${2^m}
where m is the total number of modules in @${P}.

In Reticulated Python, we are allowed to type all components of
a function signature as well as class fields. Therefore, the
upper bound of the number of elements in a configuration
space for Reticulated is @${2^{c+a+f}} where @${c} is the total
number of class fields, @${a} is the arity for all functions and
@${f} is the total number of functions. The Takikawa et
al. method adapted to Typed Racket measures the largest configuration space
possible, exhaustively. For Reticulated, such space
would be too large due to the finer granularity of the
language. Therefore, we let the typable components generating our configuration space @${C} be function signatures and class fields. Therefore
for some program @${P}, @${C} contains
@${2^{f+c}} elements where @${c} is the number of classes and @${f}
is the number of functions in @${P}.

After determining @${C}, we evaluate the performance
of every element according the metrics described by Takikawa et al,
and interpret the data in a number of ways.
Overhead plots in figure 3 show how many of our benchmarks are D-deliverable.
@definition["D-deliverable"]{ A configuration is D-deliverable if its
performance is no worse than a factor of D slowdown compared to the
untyped configuration.}
Figure 4 describes the running time of a
given configuration vs. the number of typed components in that configuration.
We refer to this as the typed/untyped ratio.
@definition["typed/untyped ratio"]{The typed/untyped ratio of a
performance lattice is the time needed to run the top configuration
divided by the time needed to run the bottom configuration.}



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
