#lang gm-plateau-2017

@require{bib.rkt}

@title[#:tag "sec:introduction"]{How Much does Gradual Soundness Cost?}

Gradual typing systems can help programmers with the task of maintaining
 code written in a dynamically typed language.
If the latter comes with a gradual typing system, developers may incrementally
 add type annotations as they improve a piece of the code base.
The next developer that needs to comprehend this piece of the code base
 can use the type annotations to understand its structure and invariants.

While gradual typing can improve readability and
 robustness, it has serious implications for performance@~cite[tfgnvf-popl-2016 greenman-jfp-2017].
The problem is that gradual typing systems implement soundness with run-time
 type checks, which obviously impose a performance cost.

Since the design space of gradual typing comes with a range of soundness
notions, the question arises how much soundness costs in terms of
performance.
A concrete instance of this question is whether Reticulated Python's
 notion of tag soundness@~cite[vss-popl-2017] renders gradual typing more performant than Typed
 Racket's generalized type soundness@~cite[tfffgksst-snapl-2017].

In the case of Typed Racket, @citet[tfgnvf-popl-2016] have shown that
 gradual typing can slow programs by up to two orders of magnitude.
There is no analogous data for Reticulated.
@citet[vss-popl-2017] report slowdowns within one order of magnitude for
 fully-typed programs, but do not report the performance of programs that mix
 statically typed and dynamically typed code.

This paper reports on the application of the Takikawa method@~cite[tfgnvf-popl-2016]
 to Reticulated.
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
 developers will tolerate the overhead of gradual typing in Reticulated.
}
]
@;
To set the stage, this paper first describes the point that Reticulated
 occupies in the design space of gradual typing systems
 (@section-ref{sec:reticulated}).
It then explains our adaptation of the Takikawa method to Reticulated (@section-ref{sec:method}).
@Section-ref{sec:evaluation} presents the details of the evaluation:
 the benchmarks, the measurements, and the conclusions.
