#lang gm-dls-2017

@title[#:tag "sec:method"]{Evaluation Method}

Takikawa @|etal| introduce a method for evaluating the performance of
a gradual type system.
The method is based on the idea that a performance evaluation cannot assume
how developers will apply gradual typing, nor can it assume that all developers
have identical performance requirements.
Therefore, the method considers all @emph{configurations} that a developer
can obtain by adding types to a program in increments and reports the overhead of these configurations relative to the original, untyped program.

Takikawa @|etal| apply the method to Typed Racket where
each module in a Typed Racket program may be typed or untyped.
Thus a @emph{fully-typed} program with @${M} modules defines a space
 of @${2^M} configurations.@note{Conversely, there may be an infinite number of ways to type an untyped program.} @;For example, @racket[(λ (x) x)].
Takikawa @|etal| measure the overhead of these configurations relative to
 the fully-untyped configuration and plot how the proportion of so-called
 @emph{@deliverable{D}} configurations varies as developers replace the
 parameter @${D} with the worst-case performance overhead they are willing to tolerate.

@section{Adapting Takikawa et al.'s Method}

Reticulated supports fine-grained combinations of typed and untyped code.
One may try to apply the Takikawa method directly to Reticulated. In that case, the evaluation should measure all configurations that a
 developer can obtain by typing a single function parameter, function return,
 or class field. This would result in a large number of configurations. We begin adapting the method to Reticulated by choosing the @emph{granularity} of our evaluation.

@definition["granuarity"]{
  The @emph{granularity} of an evaluation is the syntactic unit at which
   the evaluation will add or remove type annotations.
}

For example, the evaluation in @citet[takikawa-popl-2016] is at the granularity
 of modules.
The evaluation in @citet[vss-popl-2017] is at the granularity
 of whole programs.

Once the granularity is fixed, a performance evaluation must define the programs
 that it will ascribe types to and measure.
Such programs may depend on libraries that a developer does not
 have access to.
An evaluator may also wish to measure the effect of gradual typing on a subset
 of the modules in a large program.
In any event, a performance evaluation must distinguish two groups of modules:

@definition["experimental, control"]{
  The @emph{experimental modules} in a program define its configurations.
  The @emph{control modules} in a program are common across all configurations.
}

The experimental modules and granularity of type annotations define the
 @emph{configurations} of a fully-typed program.
What remains is to measure the performance of these configurations and
 report their overhead relative to the performance a developer would get
 by opting out of gradual typing.
In Typed Racket, this baseline is the performance of Racket running the
 untyped configuration.
In Reticulated, untyped variables still require runtime checks, so the
 baseline is the performance of Python running the untyped configuration.

@definition["performance ratio"]{
  A @emph{performance ratio} is the running time of a program
   divided by the running time of the same program in the absence of gradual typing.
}

After measuring the performance ratio of each configuration, an
 experimentor can classify configurations by their performance. Since
 different software projects will have different performance
 requirements, we choose a metric to summirize the performance
 evaluation.

@definition[@deliverable{D}]{
  For any real-valued @${D}, the proportion of @deliverable{D} configurations
   is the proportion of configurations with @emph{performance ratios} no greater
   than @${D}.
}


@section[#:tag "sec:protocol"]{Protocol}

Sections@|~|@secref{sec:exhaustive} and @secref{sec:linear} report the
 performance of Reticulated at the granularity of function and class
 definitions; more precisely, one component in this experiment is
 either one function (or method) or all fields of one class.  The
 evaluation furthermore adheres to the following protocols for
 @emph{benchmark creation} and @emph{data collection}.

@parag{Benchmark Creation}
Given a Python program, first build a driver module that performs some
 non-trivial computation using the program.
Second, remove any non-determinism or unneccesary I/O actions from the program.
Third, define the experimental modules.
Fourth, infer fully-typed configurations for the experimental modules.

When possible, use existing type annotations and comments to infer
 the fully-typed configuration of the benchmark.
When necessary, use details of the driver module to infer types;
 for example, any polymorphic functions must use monomorphic types
 because Reticulated does not support polymorphism.


@parag{Data Collection}
Enumerate the configuration space and choose a random permutation of the
 enumeration.
Optionally divide the permutation across identical processors or machines.
Run the main module of the configuration a fixed number of times and record
 each running time.
Finally, run the main module of the untyped configuration using the standard
 Python interpreter.


@parag{Details of the Evaluation} All data in this paper was produced by jobs sent
 to the @emph{Karst at Indiana University} high-throughput computing cluster.@note{@url{https://kb.iu.edu/d/bezu}}
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
 an explicit representation of the configuration space of each @emph{module}
 of each benchmark.
After a node selected a configuration to run, it copied the relevant files
 to private storage before running the main module.
Third, we wrapped the main computation of every benchmark in a
 @tt{with} statement@note{@url{https://www.python.org/dev/peps/pep-0343/}}
 to record execution time (via the Python function @|time.process_time|).
