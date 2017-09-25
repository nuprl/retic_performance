#lang gm-pepm-2018
@title[#:tag "sec:conclusion"]{Is Sound Gradual Typing Alive?}

The application of the Takikawa method suggests that any combination of
 statically typed and dynamically typed code in Reticulated runs within one
 order of magnitude of the original Python program.
This impressive performance comes at a three-fold cost.
First, soundness is at the level of type-tags rather than full static types.
Second, run-time type errors point to a set of potentially-guilty
 type boundaries rather than a single location.@note{The version of Reticulated
 in this paper always reports an empty set. @citet[vss-popl-2017] improve the
 error messages and report that the improvement doubled the @|t/u-ratio| in
 most of their benchmark programs.}
Third, fully-typed programs typically suffer more overhead than any other
 configuration.

Our evaluation effort thus leaves us with a number of open research problems:
@itemlist[
@item{
  Will programmers accept tag soundness?
}
@item{
  How does the cost of soundness compare to the cost of expressive types
   and informative error messages?
  This question demands a two-pronged answer:
   (1) Reticulated must improve its types and error messages;
   (2) Typed Racket must implement a form of tag soundness.
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

