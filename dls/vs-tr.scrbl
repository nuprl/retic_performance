#lang gm-dls-2017
@title[#:tag "sec:vs-tr"]{Related Work}

@; TODO
@; - safe typescript?
@; - strongscript?
@; these are micro systems with reasonable soundness

@; TODO this is ugly text, but hey the information content is all here
@citet[vksb-dls-2014] introduce the syntax of Reticulated Python and three
 semantics for enforcing type annotations: guarded, monotonic@~cite[vcgts-esop-2015], and transient.@note{The implementation of Reticulated has some support for all three semantics. Support for transient is the most mature.}
They do not discuss type soundness.
They report a 10x @|t/p-ratio| for @tt{slowSHA} (specifically, ``the slowSHA test suite ... 10x slowdown under transient compared to normal Python.'')
@; Quite different from ours, is transient better? or is it just different inputs?
They report the @tt{stats} test suite took 1.6 seconds under transient.
@; on par with what we see, our input is definitely bigger

@citet[svcb-snapl-2015] state a theorem that relates the runtime behavior of
 a given well-typed term to the runtime behavior of less precise@note{Term precision is defined in @hyperlink[SNAPL-2015-URL]{Figure 6}@~cite[svcb-snapl-2015].}
 terms (Theorem 5, the @emph{gradual guarantee}).
They furthermore state that this theorem classifies gradual type systems.
They do not argue that Reticulated satisfies an analogous theorem.

@citet[vss-popl-2017] formalize the transient semantics for a lambda calculus.
They conjecture that Reticulated satisfies their main theorem (Theorem 5.5, @emph{open-world soundness}).
They measure the performance of Reticulated on 13 programs from
 @hyperlink["http://pyperformance.readthedocs.io/"]{The Python Performance Benchmark Suite}@note{@TODO{compare their ratios/benchmarks to ours}}
 and report @|t/p-ratio|s.
They do not present data on the performance of any gradually typed configurations.

@citet[takikawa-popl-2016] evaluate the performance of Typed Racket.
They conclude that the cost of preserving type soundness is intolerable,
 and question whether the ideal of gradual typing is realizable in practice.

@; our results are not directly comparable to theirs, apples to oranges
