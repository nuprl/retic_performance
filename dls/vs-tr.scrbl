#lang gm-dls-2017
@title[#:tag "sec:vs-tr"]{Comparing with Typed Racket}

@section{A Lack of Soundness}

@section{A Lack of Expressiveness}

@section{A Lack of Error-Messages}

In 2001, Felleisen used the slogan ``errors matter'' for his POPL
keynote. He meant that when systems work, everyone is happy, but when
systems break, developers really want to see high quality error messages. 


@section{A Lack of Type Boundaries}

In Typed Racket, if @racket[f] is a typed function and
 @racket[g] is a typed function that calls @racket[f], then
 values that flow from @racket[g] into @racket[f] are not dynamically checked.
Such values are safe because they do not cross a type boundary.

Type boundaries are complicated, and very important to Typed Racket.

Reticulated is much simpler.
If @racket[f] is a typed function, then it will check its inputs
 no matter what.
Even if they come from a typed context.

(Maybe this discussion belongs in "Lack of Error Messages")


@;=============================================================================
@; https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make
@; - default arguments are "shared"
@; - subclasses dont get COPY of fields ... wow


@; https://blog.codinghorror.com/loose-typing-sinks-ships/
@;
@; The only errors that matter are runtime errors: until you have eliminated
@; those, you don't have a functional app. And those errors tend to be a hell of a
@; lot more subtle than "Oops, I called the .Bark method on a Cat!"
@;
@; Basically the value of compile time checking isn't that great, compared to the
@; overwhelming value of real world testing. That's what all these hardcore Java
@; figures are saying: they used to feel that way, too.. until experience taught
@; them otherwise. Just because your program compiles means basically nothing.
@;
@; Once you factor in the cost (both mental overhead and simple keyboard typing)
@; of all that "checking" in terms of programmer productivity (forced inheritance
@; model to get a .Bark method, cast cast cast) .. it's pretty clear that dynamic
@; typing is superior.


@; https://docs.google.com/document/d/1aXs1tpwzPjW9MdsG5dI7clNFyYayFBkcXwRDo-qvbIk/preview
@; question: how was author able to build large apps in Python without
@;           static typechecking?
@; - tests
@; - test cases define correctness, nothing else
@; - types just catch some things earlier,
@; - what matters, is they get CAUGHT
@; - dynamic typing catches these
@; - and since Python easier to write code, easier to write tests and be happy

@; TODO read PEPs
@; http://legacy.python.org/dev/peps/pep-0484/
@; http://legacy.python.org/dev/peps/pep-0483/
@; http://legacy.python.org/dev/peps/
