#lang gm-plateau-2017

@title[#:tag "sec:method"]{Evaluation Method}

@citet[tfgnvf-popl-2016] introduce a three-step method for evaluating the performance of
 a gradual typing system:
 (1) identify a suite of fully-typed programs;
 (2) measure the performance of all gradually-typed @emph{configurations} of the programs;
 (3) count the number of configurations with performance overhead no greater than a certain limit.
Takikawa @|etal| apply this method to Typed Racket, a gradual typing system
 with module-level granularity.
In other words, a Typed Racket program with @${M} modules has
 @${2^M} gradually-typed configurations.

Reticulated supports gradual typing at a much finer granularity,
 making it impractical to directly apply the Takikawa method.
The following subsections therefore generalize the Takikawa method (@section-ref{sec:method:adapt})
 and describe the protocol we use to evaluate Reticulated (@section-ref{sec:protocol}).


@section[#:tag "sec:method:adapt"]{Generalizing the Takikawa Method}

A gradual typing system enriches a dynamically typed language with a notion of static typing;
 that is, some pieces of a program can be statically typed.
The @emph{granularity} of a gradual typing system defines the minimum size of
 such pieces in terms of abstract syntax.
A performance evaluation must consider the ways that a programmer may write
 type annotations, subject to the type system's granularity and practical constraints.

@definition["granularity"]{
  The @emph{granularity} of an evaluation is the syntactic unit at which
   the evaluation adds or removes type annotations.
}

For example, the evaluation in @citet[tfgnvf-popl-2016] is at the granularity
 of modules.
The evaluation in @citet[vss-popl-2017] is at the granularity
 of whole programs.
@Section-ref{sec:protocol} defines the @emph{function and class-fields} granularity that we use.

After defining a granularity, a performance evaluation must define a suite of
 programs to measure.
A potential complication is that such programs may depend on external libraries
 or other modules that lie outside the scope of the evaluation.

@definition["experimental, control"]{
  The @emph{experimental modules} in a program define its configurations.
  The @emph{control modules} in a program are common across all configurations.
}

The granularity and experiemental modules define the so-called
 configurations of a fully-typed program.

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

A performance evaluation must measure the running time of these configurations
 relative to the @emph{baseline} performance of the untyped configuration in
 the absence of gradual typing.
In Typed Racket, the baseline is the performance of Racket running the
 untyped configuration.
Reticulated adds type checks to un-annotated programs@~cite[vksb-dls-2014],
 so its baseline is Python running the untyped configurations.

@definition["performance ratio"]{
  A @emph{performance ratio} is the running time of a configuration
   divided by the baseline performance of the untyped configuration.
}

An @emph{exhaustive} performance evaluation measures the performance of every
 configuration.
The natural way to interpret this data is to choose binary a notion of
 "good performance" and count the proportion of "good" configurations.
In this spirit, @citet[tfgnvf-popl-2016] ask programmers to consider the
 performance overhead they could deliver to clients.

@definition[@deliverable{D}]{
  For @$|{D \in \mathbb{R}^{+}}|, a configuration is @emph{@deliverable{D}}
   if its performance ratio is no greater than @${D}.
}

If an exhaustive performance evaluation is infeasible, one alternative is
 to select configurations via simple random sampling and measure the
 proportion of @deliverable{D} configurations in the sample.
Repeating this sampling experiment yields a @emph{simple random approximation}
 of the true proportion of @deliverable{D} configurations.

@definition[@approximation["r" "s" "95"]]{
  Given @${r} samples each containing @${s} configurations chosen uniformly at random,
   a @emph{@approximation["r" "s" "95"]} is a @${95\%} confidence interval for
   the proportion of @deliverable{D} configurations in each sample.
}

Our technical report contains theoretical and empirical justification
 for the simple random approximation method@~cite[gm-tr-2017].


@section[#:tag "sec:protocol"]{Protocol}

@parag{Granularity}
The evaluation presented in @section-ref{sec:evaluation} is at the granularity
 of @emph{function and class fields}.
In general, one syntactic unit in the experiment is either one function,
 one method, or the collection of all fields for one class.
The class in @figure-ref{fig:cash}, for example, has 3 syntactic units.


@parag{Benchmark Creation}
To convert a Reticulated program into a benchmark, we:
 (1) build a driver module that runs the program and collects timing information;
 (2) remove any non-determinism or I/O actions;
 (3) partition the program into experimental and control modules; and
 (4) add type annotations to the experimental modules.
We modify any Python code that Reticulated's type
 system cannot validate, such as code that requires untagged unions or polymorphism.


@parag{Data Collection}
For benchmarks with at most @$|{2^{21}}| configurations, we conduct an exhaustive
 evaluation.
For a larger benchmark, with @${F} functions and @${C} classes,
 we conduct a simple random approximation using
 @integer->word[NUM-SAMPLE-TRIALS] samples each containing @${@id[SAMPLE-RATE] * (F + C)}
 configurations.

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
  selected a random configuration to measure,
  ran the configuration's main module @id[NUM-ITERATIONS] times,
  and recorded the result of each run.
}
]
Cluster nodes are IBM NeXtScale nx360 M4 servers with two Intel Xeon E5-2650 v2
 8-core processors, 32 GB of RAM, and 250 GB of local disk storage.
