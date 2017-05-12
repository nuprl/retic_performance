#lang gm-dls-2017
@title[#:tag "sec:vs-tr"]{Whence this Paper}

@; TODO
@; - safe typescript?
@; - strongscript?
@; these are micro systems with reasonable soundness

Performance is one important aspect of a gradual type system.
Two other, equally important aspects are (1) the system's ability to express common programming
 @; --- especially idioms of the host language but lets not get ahead of ourselves ---
 idioms and (2) the guarantees its types provide.
@; Prior work starts these off??

@citet[vksb-dls-2014] introduce Reticulated Python and three
 semantics for enforcing type annotations: guarded, monotonic@~cite[vcgts-esop-2015], and transient.@note{Reticulated has some support for all three semantics. Support for transient is the most mature.}
Regarding transient, the paper reports a @|t/u-ratio| of 10x on the @tt{slowSHA}
 program and links to a proof of type safety for a core calculus.@note{The link is superceded by a technical report@~cite[vs-tr-2016].}
The paper does not include data on the performance of partially typed programs,
 nor does it state a type safety guarantee for Reticulated.
@; nor define type soundness for transient
@; ^^^^ YO BEN, your paper is about performance not soundness so the RW should be focused like that

@citet[svcb-snapl-2015] state a theorem that relates the runtime behavior of
 a given well-typed term to the runtime behavior of less precise@note{Term precision is defined in @hyperlink[SNAPL-2015-URL]{Figure 6}@~cite[svcb-snapl-2015].}
 terms (Theorem 5, the @emph{gradual guarantee}).
They furthermore state that this theorem classifies gradual type systems.
They do not argue that Reticulated satisfies an analogous theorem.

@citet[vss-popl-2017] formalize the transient semantics for a lambda calculus.
They conjecture that Reticulated satisfies their main theorem (Theorem 5.5, @emph{open-world soundness});
 this may be true, but the examples in the next section question the usefulness of the theorem.
They measure the performance of Reticulated on 13 programs from
 @hyperlink["http://pyperformance.readthedocs.io/"]{The Python Performance Benchmark Suite}@note{@TODO{compare their ratios/benchmarks to ours}}
 and report @|t/p-ratio|s.
They do not present data on the performance of any gradually typed configurations.

@citet[takikawa-popl-2016] evaluate the performance of Typed Racket.
They conclude that the cost of preserving type soundness is intolerable,
 and question whether the ideal of gradual typing is realizable in practice.

@; our results are not directly comparable to theirs, apples to oranges
