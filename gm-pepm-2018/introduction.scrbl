#lang gm-pepm-2018

@require{bib.rkt}

@title[#:tag "sec:introduction"]{How Much does Soundness Cost?}

Gradual typing systems can help programmers with the task of maintaining
 code written in a dynamically typed language.
If the language comes with a gradual typing system, developers may incrementally
 add type annotations as they improve a piece of the code base.
The next developer that needs to comprehend this part of the application
 can use the type annotations to understand its structure and invariants.

While gradual typing can improve readability and robustness, it has serious
 implications for performance.
The problem is that gradual typing systems enforce type soundness with
 run-time assertions that check whether values supplied by dynamically typed
 code match the type system's assumptions.
These checks can impose a large performance cost.

Since the design space of gradual typing comes with a range of soundness notions,
 the question arises how much soundness costs in terms of performance.
One such notion is Typed Racket's generalized type soundness@~cite[tfffgksst-snapl-2017].
At a high level, generalized soundness states that if a well-typed term
 reduces to a value, the value has the expected type.
Otherwise, evaluation halts with a type error that directs the programmer to
 the source of the unexpected value.
The performance cost of this guarantee is evidently high.
An evaluation by @citet[tfgnvf-popl-2016] found that Typed Racket's
 implementation of generalized soundness can slow a working program by over two
 orders of magnitude.

A second notion of gradual type soundness is Reticulated's tag soundness@~cite[vss-popl-2017].
Tag soundness guarantees that if a well-typed expression reduces to a value,
 then the value has the correct top-level type constructor (see @section-ref{sec:reticulated}).
Thus an expression with type @${\tlist{\tint}} may reduce to a list of strings,
 but not to an integer or a function.

One might expect that gradual typing in Reticulated comes at a lower
 performance cost, but this claim has not been systematically evaluated.
For example, both @citet[vss-popl-2017] and @citet[mt-oopsla-2017] report
 the performance of Reticulated on fully-typed and fully-untyped programs,
 but do not report the performance of programs that actually use gradual typing.
Part of the challenge is that Reticulated supports the addition of type
 annotations at a fine granularity, making exhastive evaluation infeasible
 for many programs.
We address this limitation with an evaluation
 method based on random sampling (see @section-ref{sec:method:adapt} and the appendix).

This paper contributes a systematic evaluation of the cost of gradual typing
 in Reticulated.
The central findings are:
@itemlist[
@item{
 Reticulated experiences a slow down of at most one order of magnitude
  at a function-level granularity;
}
@item{
 the performance degradation is approximately a linear function of the
 number of type annotations; and
}
@item{
 random sampling can approximate the performance overhead of gradual typing
  in Reticulated with a linear number of samples from an exponentially-large space.
}
]

@Section-ref{sec:reticulated} introduces Reticulated,
@Section-ref{sec:method} adapts the Takikawa method, and
@Section-ref{sec:evaluation} presents the evaluation.

@;This paper first describes the point that Reticulated
@; occupies in the design space of gradual typing systems
@; (@section-ref{sec:reticulated}).
@;It then explains how to adapt the Takikawa method to Reticulated (@section-ref{sec:method}).
@;@Section-ref{sec:evaluation} presents the details of the evaluation:
@; the benchmarks, the data, and the conclusions.
