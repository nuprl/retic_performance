#lang gm-plateau-2017

@require{bib.rkt}

@title[#:tag "sec:introduction"]{How Much does Gradual Soundness Cost?}

Gradual typing systems can help programmers with the task of maintaining a
code base in an untyped scripting language. If the latter comes with a
gradual typing system, developers may incrementally add type annotations as
they improve an untyped piece of the code base. The addition of types
reduces the time that the next developer needs to comprehend this piece of
the code base. 

@; @~cite[st-sfp-2006]

While the soundness of the gradual type system guarantees that developers
can easily find and fix an impedance mismatch between typed and untyped
regions of code, it also has serious implications for
performance@~cite[takikawa-popl-2016 greenman-jfp-2017]. The problem is due
to the implementation of soundness with the insertion of run-time checks,
which obviously imposes a cost. In the case of Typed Racket, partially
typed code may slow down by up to two orders of magnitude while fully typed
code is almost always faster than the untyped code.

Since the design space of gradual typing comes with a range of soundness
notions, the question arises how much soundness costs in terms of
performance. For example, Siek et al.'s Reticulated Python
system@~cite[vksb-dls-2014] implements a laxer@~cite[vss-popl-2017] notion
of soundness than Typed Racket. Thus, a concrete instance of the question
is whether Reticulated renders gradual typing more usable than Typed
Racket. 

This paper reports on the application of Takikawa et al.'s method to
Reticulated. The central findings are that 
@itemlist[
@item{Reticulated experiences a slow down of at most one order of
magnitude.} 

@item{The performance degradation is basically a linear function of the
number of type annotations.}

@item{Despite the smaller performance overhead in comparison to Typed
Racket, Reticulated still does not come with a reasonably small @italic{D}
for Takikawa et al.'s notion of @italic{D}-deliverable configurations.}
]
@;
To set the stage, this paper first describes the point that Reticulated
occupies in the design space of gradually typed systems (see
@secref{sec:reticulated}). It then explains our adaptation of Takikawa et
al.'s method to Reticulated's system of gradual typing  (see
@section-ref{sec:method}). @Secref{sec:exhaustive} presents the details of
the evaluation: the benchmarks, the measurements, and the
conclusions. 

@; we may wish to include the linear results idea but if we lack space,
@; it's an obvious piece of writing we can skip. 
