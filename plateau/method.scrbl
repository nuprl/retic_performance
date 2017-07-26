#lang gm-plateau-2017

@title[#:tag "sec:method"]{Evaluation Method}

@citet[takikawa-popl-2016] introduce a three-step method for evaluating the performance of
 a gradual typing system:
 (1) identify a suite of fully-typed programs;
 (2) measure the performance of all gradually-typed @emph{configurations} of the programs;
 (3) count the number of configurations with performance overhead no greater than a certain limit.
Takikawa @|etal| apply this method to Typed Racket, a gradual typing system
 with module-level granularity.
In other words, a fully-typed Typed Racket program with @${M} modules defines
 a space of @${2^M} configurations.

Reticulated supports gradual typing at a much finer granularity,
 making it impractical to directly apply the Takikawa method.
The following subsections therefore generalize the Takikawa method (@section-ref{sec:method:adapt})
 and describe the protocol we use to evaluate Reticulated (@section-ref{sec:protocol}).


@section[#:tag "sec:method:adapt"]{Generalizing the Takikawa Method}

A gradual typing system enriches a dynamically typed language with a notion of static typing.
The type system defines which syntactic units@note{E.g. variables, expressions, modules} of a program may be typed;
 this is the so-called @emph{granularity} of the gradual typing system.
A performance evaluation must consider the ways that a programmer may write
 type annotations, subject to practical constraints.

@definition["granularity"]{
  The @emph{granularity} of an evaluation is the syntactic unit at which
   the evaluation adds or removes type annotations.
}

For example, the evaluation in @citet[takikawa-popl-2016] is at the granularity
 of modules.
The evaluation in @citet[vss-popl-2017] is at the granularity
 of whole programs.
@Section-ref{sec:protocol} defines the @emph{function and class-fields} granularity that we use.

Once the granularity is fixed, the second step is to ascribe types to representative programs.
A potential complication is that such programs may depend on external libraries
 or other modules that lie outside the scope of the evalutation.

@definition["experimental, control"]{
  The @emph{experimental modules} in a program define its configurations.
  The @emph{control modules} in a program are common across all configurations.
}

The experimental modules and granularity of type annotations define the
 configurations of a fully-typed program.

@definition["configurations"]{
  Let @${P \tcstep P'}
   if and only if program @${P'} can be obtained from
   @${P} by annotating one syntactic unit in an experimental module.
  Let @${\tcmulti} be the reflexive, transitive closure of the @${\tcstep} relation.@note{The @${\tcstep} relation expresses the notion of a @emph{type conversion step}@~cite[takikawa-popl-2016]. The @${\tcmulti} relation expresses the notion of @emph{term precision}@~cite[svcb-snapl-2015].}
  @; note^2: `e0 -->* e1` if and only if `e1 <= e0`
  The @emph{configurations} of a fully-typed program @${P^\tau} are all
   programs @${P} such that @${P\!\tcmulti P^\tau}.
}

The next step is to measure the performance of these configurations and
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
   is the proportion of configurations with performance ratios no greater
   than @${D}.
}

@definition[@approximation["r" "s" "95"]]{
  A @${95\%} confidence interval generated from @${r} samples, each made of @${s}
   configurations is a @approximation["r" "s" "95"]
  (informally, a @emph{simple random approximation}.)
 @; ^^^ to disambiguate from other approximations
}

A given sample of @${s} randomly-selected configurations contains some
 number @${n} of @deliverable{D} configurations.
The proportion @${n/s} is the proportion of @deliverable{D} configurations
 in the sample.
Repeating the sampling process @${r} times yields a sequence of proportions;
 the @${95\%} confidence interval of such a sequence is a @approximation["r" "s" "95"].


@section[#:tag "sec:protocol"]{Protocol}

@; TODO add statistics

@Section-ref{sec:exhaustive} reports the
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

When possible, we use existing type annotations or comments to infer
 the fully-typed configuration.
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
 @|PYTHON| interpreter.@note{@url{https://www.python.org/download/releases/3.4.3/}}


@parag{Details of the Evaluation} All data in this paper was produced by jobs we sent
 to the @emph{Karst at Indiana University}@note{@url{https://kb.iu.edu/d/bezu}} high-throughput computing cluster.
Each job:
@itemlist[#:style 'ordered
@item{
  reserved all processors on one node for 24 hours;
}
@item{
  downloaded fresh copies of @|PYTHON|
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


@; ===
@; The method is based on the premise that a performance evaluation cannot assume
@; how developers will apply gradual typing, nor can it assume that all developers
@; have identical performance requirements.
@;
@;Counting the proportion of @deliverable{D} configurations is a useful way to
@; measure the performance overhead of gradual typing because it addresses two
@; forms of uncertainty.
@;First, the parameter @${D} addresses the fact that different software applications
@; have different performance requirements.
@;Second, the proportion quantifies over the entire configuration space of a
@; program---because it is impossible to predict how developers will apply gradual
@;  typing.@note{
@;    The promise of gradual typing is that developers can run @emph{any configuration}.
@;    At present, there is no data to suggest that developers are more likely to
@;    choose some configurations over others.}
@;For an arbitrary configuration, the proportion of @deliverable{D} configurations
@; @emph{is} the probability that this configuration is @deliverable{D}.
@;
@;While computing the exact proportion of @deliverable{D} configurations requires
@; measuring an exponential number of configurations, a random sampling protocol
@; can accurately and quickly approximate it.
@;To illustrate the protocol, suppose a few developers independently apply
@; gradual typing to a program.
@;Each arrives at some configuration and observes some performance overhead.
@;For a given value of @${D} some proportion of the developers have
@; @deliverable{D} configurations.
@;There is a remote chance that this proportion coincides with the true proportion
@; of @deliverable{D} configurations.
@;Intuitively, the chance is less remote if the number of developers is large.
@;But even for a small number of developers, if they repeat this experiment
@; multiple times, then the average proportion of @deliverable{D} configurations
@; should tend towards the true proportion.
@;After all, if the true proportion of @deliverable{D} configurations is
@; @${10\%} then approximately @${1} in @${10} randomly sampled configurations is
@; @deliverable{D}.
