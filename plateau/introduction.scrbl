#lang gm-plateau-2017

@require{bib.rkt}

@title[#:tag "sec:introduction"]{How Much does Gradual Soundness Cost?}

Gradual typing systems can help programmers with the task of maintaining
 code written in a dynamically typed language.
If the latter comes with a gradual typing system, developers may incrementally
 add type annotations as they improve a piece of the code base.
The next developer that needs to comprehend this piece of the code base
 can use the type annotations to understand its structure and invariants.

While gradual typing can improve readability and robustness, it has serious
 implications for performance@~cite[tfgnvf-popl-2016 greenman-jfp-2017].
The problem is that gradual typing systems implement soundness with run-time
 type checks, and these checks can impose a large performance cost.

Since the design space of gradual typing comes with a range of soundness
notions, the question arises how much soundness costs in terms of
performance.
A concrete instance of this question is whether Reticulated Python's
 notion of tag soundness@~cite[vss-popl-2017] renders gradual typing more performant than Typed
 Racket's generalized type soundness@~cite[tfffgksst-snapl-2017].

Tag soundness guarantees that if a well-typed expression reduces to a value,
 then the value and expression share the same top-level type constructor
 (see @section-ref{sec:tag-soundness}).
Thus an expression with type @${\tlist{\tint}} can reduce to a list of strings,
 but not to an integer or a function.

In contrast, generalized type soundness guarantees that if an expression
 with type @${\tau} reduces to a value, then the value is well-typed at @${\tau}.
Furthermore, if the evalution ends in a type error, generalized soundness
 guarantees that the error points to one of the finitely-many boundaries
 between statically-typed and dynamically-typed code, thereby helping programmers
 diagnose the source of the error.

Generalized soundness clearly provides stronger guarantees than tag soundness,
 but @citet[tfgnvf-popl-2016] show that its implementation in Typed Racket can
 slow programs by two orders of magnitude.
Prior work on Reticulated does not report the performance of gradually-typed
 programs@~cite[vksb-dls-2014 vss-popl-2017].

This paper reports on the application of the Takikawa performance evaluation
 method@~cite[tfgnvf-popl-2016] to Reticulated.
The central findings are that:
@itemlist[
@item{
 Reticulated experiences a slow down of at most one order of
 magnitude.
}
@item{
 The performance degradation is basically a linear function of the
 number of type annotations.
}
@item{
 Despite the smaller performance overhead, it remains to be seen whether
  developers will tolerate the overhead of gradual typing in Reticulated
  and the weaker notion of soundness.
}
]
@;
To set the stage, this paper first describes the point that Reticulated
 occupies in the design space of gradual typing systems
 (@section-ref{sec:reticulated}).
It then explains our adaptation of the Takikawa method to Reticulated (@section-ref{sec:method}).
@Section-ref{sec:evaluation} presents the details of the evaluation:
 the benchmarks, the measurements, and the conclusions.
