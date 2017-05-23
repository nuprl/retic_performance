#lang gm-dls-2017

@title[#:tag "sec:method"]{Evaluation Method}

@citet[takikawa-popl-2016] introduce a method for evaluating the performance of
a gradual type system.
The method is based on the premise that a performance evaluation cannot assume
how developers will apply gradual typing, nor can it assume that all developers
have identical performance requirements.
Therefore, the method considers all possible configurations that a developer
may obtain by incrementally adding types and reports the overhead of all configurations relative to the original, untyped program.

Takikawa @|etal| apply this method to Typed Racket, a gradual typing system
 that permits typed and untyped modules.
Thus a fully-typed program with @${M} modules defines a space
 of @${2^M} configurations.
@;@note{Conversely, there may be an infinite number of ways to type an untyped program.} @;For example, @racket[(λ (x) x)].
Takikawa @|etal| measure the overhead of these configurations relative to
 the fully-untyped configuration and plot how the proportion of so-called
 @emph{@deliverable{D}} configurations varies as developers instantiate the
 parameter @${D} with the highest performance overhead they can tolerate.


@section{Adapting Takikawa et al.'s Method}

Reticulated supports fine-grained combinations of typed and untyped code.
It would be impractical to directly apply the Takikawa method; measuring all
configurations would take more time than the universe has left.
It would also be impractical to ignore the fine granularity of Reticulated and
 apply the module-level protocol that @citet[takikawa-popl-2016] used for Typed Racket.
The practical choice lies somewhere in between, and it depends on the size of the
 programs at hand and computing resources available.

@definition["granuarity"]{
  The @emph{granularity} of an evaluation is the syntactic unit at which
   the evaluation adds or removes type annotations.
}

For example, the evaluation in @citet[takikawa-popl-2016] is at the granularity
 of modules.
The evaluation in @citet[vss-popl-2017] is at the granularity
 of whole programs.
@Section-ref{sec:protocol} defines the @emph{function and class-fields} granularity used in this paper.

Once the granularity is fixed, the second step in applying the method is to
 ascribe types to representative programs.
A potential complication is that such programs may depend on external libraries
 or other modules that lie outside the scope of the evalutation.

@definition["experimental, control"]{
  The @emph{experimental modules} in a program define its configurations.
  The @emph{control modules} in a program are common across all configurations.
}

The experimental modules and granularity of type annotations define the
 configurations of a fully-typed program.

@definition["configurations"]{
  Let @${P \rightarrow_1 P'}
   if and only if program @${P'} can be obtained from
   @${P} by annotating one syntactic unit in an experimental module.
  Let @${\sqsubseteq} be the reflexive, transitive closure of the @${\rightarrow_1} relation.@note{The @${\rightarrow_1} relation expresses the notion of a @emph{type conversion step}@~cite[takikawa-popl-2016]. The @${\sqsubseteq} relation expresses the notion of @emph{term precision}@~cite[svcb-snapl-2015].}
  The @emph{configurations} of a fully-typed program @${P^\tau} are all
   programs @${P} such that @${P \sqsubseteq P^\tau}.
}

What remains is to measure the performance of these configurations and
 report their overhead relative to the performance a developer would get
 by opting out of gradual typing.
In Typed Racket, this baseline is the performance of Racket running the
 untyped configuration.
In Reticulated, untyped variables still require run-time checks, so the
 baseline is the performance of Python running the untyped configuration.

@definition["performance ratio"]{
  A @emph{performance ratio} is the running time of a program
   divided by the running time of the same program in the absence of gradual typing.
}

After measuring the performance ratio of each configuration, the final step
 is to classify configurations by their performance.
Since different applications have different performance requirements, the
 only rational way to report performance is with a parameterized metric.

@definition[@deliverable{D}]{
  For real-valued @${D}, the proportion of @deliverable{D} configurations
   is the proportion of configurations with @emph{performance ratios} no greater
   than @${D}.
}


@section[#:tag "sec:protocol"]{Protocol}

Sections@|~|@secref{sec:exhaustive} and @secref{sec:linear} report the
 performance of Reticulated at a function and class-fields granularity;
 more precisely, one syntactic unit in the experiment is either one function, one method, or
 the collection of all fields for one class.
The evaluation furthermore adheres to the following protocols for
 benchmark creation and data collection.

@parag{Benchmark Creation}
Given a Python program, we first build a driver module that performs some
 non-trivial computation using the program.
Second, we remove any non-determinism or I/O actions from the program.
Third, we define the experimental modules.
Fourth, we ascribe types to the experimental modules.

When possible, we use existing type annotations and comments to infer
 the fully-typed configuration of the benchmark.
When necessary, we use details of the driver module to infer types;
 for example, any polymorphic functions must use monomorphic types
 because Reticulated does not support polymorphism.


@parag{Data Collection}
We enumerate the configuration space and choose a random permutation of the
 enumeration.
Optionally, we divide the permutation across identical processors or machines.
We run the main module of the configuration a fixed number of times and record
 each running time.
Finally, we run the main module of the untyped configuration using the
 @|PYTHON| interpreter.


@parag{Details of the Evaluation} All data in this paper was produced by jobs we sent
 to the @emph{Karst at Indiana University}@note{@url{https://kb.iu.edu/d/bezu}} high-throughput computing cluster.
Each job:
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
Cluster nodes are IBM NeXtScale nx360 M4 servers with two Intel Xeon E5-2650 v2
 8-core processors, 32 GB of RAM, and 250 GB of local disk storage.

Three details of the Karst protocol warrant further attention.
First, nodes selected a random configuration by reading from a
 text file that contained a permutation of the configuration space.
This text file was stored on a dedicated machine.
Second, the same dedicated machine that stored the text file also stored
 all configurations for each @emph{module} of each benchmark.
After a node selected a configuration to run, it copied the relevant files
 to private storage before running the main module.
Third, we wrapped the main computation of every benchmark in a
 @hyperlink["https://www.python.org/dev/peps/pep-0318/"]{@tt{with} statement}
 that recorded execution time using the Python function @|time.process_time|.
