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
@; All three combine to make a programming language useful.
@; All three are in conflict.
Language designers must strike a balance between
 performance, expressiveness, and soundness.

Prior work on Reticulated has focused on its expressiveness and soundness.
@citet[vksb-dls-2014] introduce Reticulated Python and explore three
 semantics for enforcing type annotations: guarded, monotonic@~cite[vcgts-esop-2015], and transient.@note{Reticulated has some support for all three semantics. Support for transient is the most mature.}
Regarding transient, the paper reports a performance ratio of 10x on the @tt{slowSHA}
 program@note{The @emph{performance ratio} is likely the @|t/p-ratio|. Our @tt{slowSHA} benchmark is adapted from their program.}
 and links to a proof of type safety for a core calculus.@note{The link is superceded by a technical report@~cite[vs-tr-2016].}
The paper does not state a type safety guarantee for Reticulated,
 nor does it include data on the performance of partially typed programs.

@citet[svcb-snapl-2015] define a property that relates the runtime behavior of
 two programs along the same path in a configuration lattice (Theorem 5, the @emph{gradual guarantee}).@note{To be precise, the theorem relates programs @${e_0}, @${e_1} such that @${e_0 \righarrow_k e_1} for some @${k}. @hyperlink[SNAPL-2015-URL]{Figure 6} of @citet[svcb-snapl-2015] defines a similar @emph{term precision relation}.}
They claim that this property captures the essential benefit of gradual typing.
They furthermore remark that proving this property for a language with mutable
 references and/or polymorphism is non-trivial.

@citet[vss-popl-2017] formalize Reticulated's transient semantics in a monomorphic
 calculus with references, and prove safety properties including the above-mentioned gradual guarantee.
The proof avoids the challenge with references via an alternative notion of
 type soundness: if @${\vdash\!e\!:\!\mathsf{ref}~\tau} and evaluates to @${v},
 then @${\vdash\!v\!:\!\mathsf{Ref}}.
In other words, the semantics preserves top-level tags.
Transient mitigates the shallow nature of these runtime checks by wrapping
 every dereference site in typed code.
Whenever type-annotated code unboxes a value, a dynamic check ensures that the value is well-tagged.
The authors measure the performance of Reticulated on @integer->word[13] programs from
 @hyperlink["http://pyperformance.readthedocs.io/"]{The Python Performance Benchmark Suite}
 and report @|t/p-ratio|s that are similar to the ones we report here.
The paper does include data on the performance of partially typed programs.

@section{Performance Evaluation}

@citet[tfdffthf-ecoop-2015] present the first comparison between the performance of a
 fully-typed program and the performance of all its partially-typed configurations.
@citet[takikawa-popl-2016] conduct a similar evalution on @integer->word[12] programs.
They conclude that the cost of preserving type soundness @exact{na\"ively} through
 proxies is intolerable, and question whether the ideal of gradual typing
 is realizable in practice.
@citet[greenman-jfp-2017] demonstrate how to compare multiple versions of a
 gradual type system and empirically validate the simple random approximation method.

The results in this paper are not directly comparable to the results
 for Typed Racket@~cite[takikawa-popl-2016].
Typed Racket and Reticulated have different type systems and provide
 different soundness guarantess; for example, Typed Racket supports
 polymorphism, does not support implicit downcasts, and dynamically prevents
 untyped code from writing an ill-typed value to a reference cell@~cite[tfffgksst-snapl-2017].
@; Moreover, Typed Racket attributes any runtime type error to a mis-matched pair:
@;  an untyped value and a static type annotation that the value failed to meet.
But based on the data in this paper, our @emph{opinion} is that the cost of
 preserving type soundness is tolerable and that research on transient semantics
 in general and Reticulated in particular should continue.

