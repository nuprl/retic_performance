#lang gm-pepm-2018

@title[#:tag "sec:method"]{Evaluation Method}

@citet[tfgnvf-popl-2016] introduce a three-step method for evaluating the performance of
 a gradual typing system:
 (1) identify a suite of fully-typed programs;
 (2) measure the performance of all gradually-typed @emph{configurations} of the programs;
 (3) count the number of configurations with performance overhead no greater than a certain limit.
Takikawa @|etal| apply this method to Typed Racket, a gradual typing system
 with module-level granularity; in other words, a Typed Racket program with @${M} modules has
 @${2^M} gradually-typed configurations.

Reticulated supports gradual typing at a much finer granularity,
 making it impractical to directly apply the Takikawa method.
A naive application would require @${2^a} measurements for one function with @${a} formal parameters,
 and similarly @${2^f} measurements for one class with @${f} fields.
The following subsections therefore generalize the Takikawa method (@section-ref{sec:method:adapt})
 and describe the protocol we use to evaluate Reticulated (@section-ref{sec:protocol}).


@section[#:tag "sec:method:adapt"]{Generalizing the Takikawa Method}

A gradual typing system enriches a dynamically typed language with a notion of static typing;
 that is, some pieces of a program can be statically typed.
The @emph{granularity} of a gradual typing system defines the minimum size of
 such pieces in terms of abstract syntax.
A performance evaluation must define its own granularity to systematically
 explore the ways that a programmer may write type annotations, subject to
 practical constraints.

@definition["granularity"]{
  The @emph{granularity} of an evaluation is the syntactic unit at which
   the evaluation adds or removes type annotations.
}

For example, the evaluation in @citet[tfgnvf-popl-2016] is at the granularity
 of modules.
The evaluation in @citet[vss-popl-2017] is at the granularity
 of whole programs.
@Section-ref{sec:protocol} defines the @emph{function and class-fields} granularity, which we use for this evaluation.

After defining a granularity, a performance evaluation must define a suite of
 programs to measure.
A potential complication is that such programs may depend on external libraries
 or other modules that lie outside the scope of the evaluation.
It is important to distinguish these so-called @emph{control modules} from the
 focus of the experiment.

@definition["experimental, control"]{
  The @emph{experimental modules} in a program define its configurations.
  The @emph{control modules} in a program are common across all configurations.
}

The granularity and experimental modules define the
 @emph{configurations} of a fully-typed program.

@definition["configurations"]{
  Let @${P \tcstep P'}
   if and only if program @${P'} can be obtained from
   @${P} by annotating one syntactic unit in an experimental module.
  Let @${\tcmulti} be the reflexive, transitive closure of the @${\tcstep}
   relation.@note{The @${\tcstep} relation expresses the notion of a
   @emph{type conversion step}@~cite[tfgnvf-popl-2016].
   The @${\tcmulti} relation expresses the notion of @emph{term precision}@~cite[svcb-snapl-2015].}
  @; note^2: `e0 -->* e1` if and only if `e1 <= e0`
  The @emph{configurations} of a fully-typed program @${P^\tau} are all
   programs @${P} such that @${P\!\tcmulti P^\tau}.
  Furthermore, @${P^\tau} is a so-called @emph{fully-typed configuration};
   an @emph{untyped configuration} is a @${P^\lambda} such that @${P^\lambda\!\tcmulti P}
   for all configurations @${P}.
}

An evaluation must measure the performance overhead of these configurations
 relative to some default.
A natural baseline is the performance of the original program, distinct from the
 gradual typing system.

@definition["baseline"]{
 The @emph{baseline performance} of a program is its running time in the absence
  of gradual typing.
}

In Typed Racket, the baseline is the performance of Racket running the
 untyped configuration.
In Reticulated, the baseline is Python running the untyped configuration
This is different from Reticulated running the untyped configuration
 because Reticulated inserts checks in untyped code@~cite[vksb-dls-2014].

@definition["performance ratio"]{
  A @emph{performance ratio} is the running time of a configuration
   divided by the baseline performance of the untyped configuration.
}

An @emph{exhaustive} performance evaluation measures the performance of every
 configuration.
The natural way to interpret this data is to choose a notion of
 "good performance" and count the proportion of "good" configurations.
In this spirit, @citet[tfgnvf-popl-2016] ask programmers to consider the
 performance overhead they could deliver to clients.

@definition[@deliverable{D}]{
  For @$|{D \in \mathbb{R}^{+}}|, a configuration is @emph{@deliverable{D}}
   if its performance ratio is no greater than @${D}.
}

If an exhaustive performance evaluation is infeasible, an alternative is
 to select configurations via simple random sampling and measure the
 proportion of @deliverable{D} configurations in the sample.
Repeating this sampling experiment yields a @emph{simple random approximation}
 of the true proportion of @deliverable{D} configurations.

@definition[@approximation["r" "s" "95"]]{
  Given @${r} samples each containing @${s} configurations chosen uniformly at random,
   a @emph{@approximation["r" "s" "95"]} is a @${95\%} confidence interval for
   the proportion of @deliverable{D} configurations in each sample.
}

The appendix contains mathematical and
 empirical justification for the simple random approximation method.


@section[#:tag "sec:protocol"]{Protocol}

@parag{Granularity}
The evaluation presented in @section-ref{sec:evaluation} is at the granularity
 of @emph{function and class fields}.
One syntactic unit in the experiment is either one function,
 one method, or the collection of all fields for one class.
The class in @figure-ref{fig:cash}, for example, has 3 syntactic units.


@parag{Benchmark Creation}
To convert a Reticulated program into a benchmark, we:
 (1) build a driver module that runs the program and collects timing information;
 (2) remove any non-determinism or I/O actions;@note{@Integer->word[(length '(aespython futen http2 slowSHA))] benchmarks inadvertantly perform I/O actions, see @section-ref{sec:threats}.}
 (3) partition the program into experimental and control modules; and
 (4) add type annotations to the experimental modules.
We modify any Python code that Reticulated's type
 system cannot validate, such as code that requires untagged unions or polymorphism.


@parag{Data Collection}
For benchmarks with at most @$|{2^{21}}| configurations, we conduct an exhaustive
 evaluation.
For larger benchmarks we conduct a simple random approximation using
 @integer->word[NUM-SAMPLE-TRIALS] samples each containing @${@id[SAMPLE-RATE] * (F + C)}
 configurations, where @${F} is the number of functions in the benchmark and
 @${C} is the number of classes.

All data in this paper was produced by jobs we sent
 to the @emph{Karst at Indiana University}@note{@url{https://kb.iu.edu/d/bezu}} high-throughput computing cluster.
Each job:
@itemlist[#:style 'ordered
@item{
  reserved all processors on one node;
}
@item{
  downloaded fresh copies of @|PYTHON|
  and Reticulated (commit @hyperlink["https://github.com/mvitousek/reticulated/commit/e478343ce7c0f2bc50d897b0ad38055e8fd9487d"]{@tt{e478343}}
  on the @hyperlink["https://github.com/mvitousek/reticulated"]{@tt{master}} branch);
}
@item{
  repeatedly:
  selected a random configuration from a random benchmark,
  ran the configuration's main module @id[NUM-ITERATIONS] times,
  and recorded the result of each run.
}
]
Cluster nodes are IBM NeXtScale nx360 M4 servers with two Intel Xeon E5-2650 v2
 8-core processors, 32 GB of RAM, and 250 GB of local disk storage.
