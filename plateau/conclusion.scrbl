#lang gm-plateau-2017
@title[#:tag "sec:conclusion"]{Is Sound Gradual Typing Alive?}

The application of the Takikawa method to Reticulated demonstrates that at
 least one gradually typed language has a performant implementation.
In particular, the overhead plots for Reticulated look an order of magnitude
 better than those for Typed Racket.
Appearances are misleading, however.
Typed Racket implements a generalized form of type soundness whereas
 Reticulated implements tag soundness.
Furthermore, Reticulated has a less expressive type system and lacks
 the property that every run-time type error is attributed
 to a boundary between statically-typed and dynamically-typed
 code.@note{@citet[vss-popl-2017] attribute run-time type errors to sets of
 coercions. Implementing this weaker guarantee doubled the @|t/u-ratio| in
 most of their benchmark programs.}

Our evaluation effort thus confirms a widely held conjecture and leaves us
 with a number of open research problems:
@itemlist[
@item{
  Will programmers accept tag soundness?
  Substantial user studies are needed.
}
@item{
  How does the cost of soundness compare to the cost of expressive types
   and informative error messages?
  This question demands a two-pronged answer:
   (1) Reticulated must implement additional types and improve its error messages;
   (2) Typed Racket must implement tag soundness.
}
@item{
  Can Reticulated reduce its overhead relative to Python?
  Ideally, Reticulated programs with no type annotations should have the
   same performance as Python.
}
@item{
  Can Reticulated use type information to remove dynamic checks from Python programs?
  At present, Typed Racket is more performant than Reticulated on fully-typed
   programs because it adds run-time checks only when linked to dynamically-typed code.
  @;Reticulated cannot make the same assumption, but a JIT compiler
  @; may be able to generate code with performance to match Typed Racket.
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

