#lang gm-pepm-2018
@title[#:tag "sec:conclusion"]{Is Sound Gradual Typing Alive?}

Our application of the Takikawa method suggests that any combination of
 statically typed and dynamically typed code in Reticulated runs within one
 order of magnitude of the original Python program.
This impressive performance comes at a three-fold cost.
First, soundness is at the level of type-tags rather than full static types.
Second, run-time type errors do not describe the source of the ill-typed value.
Third, fully-typed programs typically suffer more overhead than any other
 combination of typed and untyped code.

Our evaluation thus raises a number of open research problems.
First among these is whether programmers will accept tag soundness as
 a compromise between classic type soundness and performance.

A second question is how the cost of soundness compares to the cost of
 expressive types and precise error messages.
Experience by @citet[vss-popl-2017] suggests that the cost of useful error
 messages is high.
They extend Reticulated to track a set of @emph{possibly-guilty} boundaries
 and find that maintaining the set doubled the @|t/u-ratio| in the majority
 of their benchmark programs.

A third question is whether Reticulated can reduce its overhead relative
 to Python.
Ideally, untyped Reticulated programs should have the same performance as Python.

Finally, we ask whether Reticulated can leverage type information to remove
 run-time checks from Python programs.
The current implementation performs far worse than Typed Racket on fully-typed
 programs because the latter only adds run-time checks at boundaries between
 statically-typed and dynamically-typed code.

@;@acks{
@;  This paper is supported by @hyperlink["https://www.nsf.gov/awardsearch/showAward?AWD_ID=1518844"]{NSF grant CCF-1518844}.
@;  Part of this work was completed while the second author was an REU under Jeremy Siek at Indiana University.
@;  We thank
@;   Matthias Felleisen,  @; advisor
@;   Michael Vitousek,    @; making retic, working with Zeina, fixing bugs
@;   Sam Tobin-Hochstadt, @; access to Karst
@;   Spenser Bauman,      @; advice about Karst
@;   Tony Garnock-Jones,  @; insisting that overhead plots are CDFs
@;   and Ming-Ho Yee.     @; reading a draft
@;}
