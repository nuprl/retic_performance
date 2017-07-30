#lang gm-plateau-2017
@title[#:tag "sec:conclusion"]{Is Sound Gradual Typing Alive?}

The application of the Takikawa method to Reticulated demonstrates that at
 least one gradually typed language has a performant implementation.
In particular, the overhead plots for Reticulated look an order of magnitude
 better than those for Typed Racket.
Appearances are misleading, however.
Typed Racket implements a generalized form of type soundness whereas
 Reticulated implements tag soundness.
Furthermore, Reticulated lacks untagged union types, recursive types,
 and Typed Racket's guarantee that every run-time type error is attributed
 to a static boundary between statically-typed and dynamically-typed
 code.@note{@citet[vss-popl-2017] attribute run-time type errors to sets of
 coercions. Implementing this weaker guarantee doubled the @|t/u-ratio| in
 most of their benchmark programs.}

Our evaluation effort thus confirms a widely held conjecture and leaves us
 with a number of open research problems:
@itemlist[
@item{
  Will programmers accept the shallow guarantees of tag soundness?
  Substantial user studies are needed.
}
@item{
  Exactly how much does soundness affect performance?
  To answer this question, Typed Racket must implement tag soundness
   and/or Reticulated must implement generalized soundness.
}
@item{
  Can Reticulated use type information to @emph{remove} dynamic checks
   from programs, or does its implementation prohibit standard type-based optimizations?
}
]



@acks{
  This paper is supported by @hyperlink["https://www.nsf.gov/awardsearch/showAward?AWD_ID=1518844"]{NSF grant CCF-1518844}.
  Part of this work was completed while the second author was an REU under Jeremy Siek at Indiana University.
  We thank
   Matthias Felleisen,  @; advisor
   Michael Vitousek,    @; making retic, working with Zeina, fixing bugs
   Sam Tobin-Hochstadt, @; access to Karst
   Spenser Bauman,      @; advice about Karst
   Tony Garnock-Jones,  @; insisting that overhead plots are CDFs
   and Ming-Ho Yee.     @; reading a draft
}

