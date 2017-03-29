#lang gm-dls-2017

@require{bib.rkt}

@title[#:tag "sec:introduction"]{Introduction}

Siek and Taha's 2006 paper@~cite[st-sfp-2006] introduces the notion of
gradual typing, a sound variant of Common Lisp's optional typing. Using
gradual typing, ``programmers should be able to add or remove type
annotations without any unexpected impacts on their program.'' One
unexpected impact would be the application of a function on integers to a
string; similarly, when typed code hands an array of floats to untyped
code, the programmer expects that the untyped code does not assign a
boolean to one of the array's slots.  By contrast, a programmer might
expect the addition of types to speed up the program execution because the
compiler can exploit the type information.

Gradual typing implements the sound combination of typed and untyped code
with the insertion of run-time checks. At a high level, a gradual typing
system uses the type annotations to determine whether and where a, say,
typed function may flow into the function position of an application and
adds a type there to ensure the argument value matches the expected
type. If not, the run-time check raises an exception. Clearly, the
insertion of such run-time checks imposes a cost, and the question arises
how significant this cost is.

In 2016, @citet[takikawa-popl-2016] present the first proper method for
evaluating the performance of gradual typing systems. Their method is to
measure @emph{all} partial conversions from typed to untyped code. That is,
if there are @math{n} code components, Takikawa et al. propose to measure
@math{2^n} configurations. Doing so mimics the process through which
programmers may gradually equip all possible sites for type declarations
with annotations. In order to evaluate these measurements, they propose a
simple metric, @emph{the deliverable count up to @math{X}}, meaning the
number of configurations whose performance slow-down is below
@math{X}. Follow-up work by @citet[greenman-jfp-2017] confirms that a
@emph{linear} amount of random sampling approximates the comprehensive but
exponential measurements well in the case of Typed Racket.

Simultaneously to Siek and Taha's original work, Tobin-Hochstadt and
Felleisen's vision paper@~cite[thf-dls-2006] launches the development of
Typed Racket, based on almost the same idea as gradual typing. Instead of
allowing programmers to annotate arbitrary functions and classes, their
proposal insists on annotating entire Racket modules with types. In 2016,
with Typed Racket under development for 10 years, Takikawa et al.'s
performance evaluation of Typed Racket indicates that the module-based form
of gradual typing has disastrous performance characteristics. Only a small
fraction of mixed-typed configurations is @math{3x}-deliverable; note that
@math{3x} is a rather generous measure considering that few developers
would accept such a slow down.

This paper contributes three insights. First, it explains an adaptation of
Takikawa et al.'s method (see @section-ref{sec:method}) for Reticulated
Python's gradual typing system@~cite[vksb-dls-2014], which is relatively
faithful to Siek and Taha's original proposal. Second, it reports on the
results of applying the adapted method to Reticulated (see
@section-ref{sec:measurements}).  While the performance of Reticulated seems to
be significantly better than Typed Racket's, we conjecture that this
due to (1) a significant gap in Reticulated's soundness, (2)
Reticulated's lack of expressiveness, and (3) low-quality error messages
(see @section-ref{sec:vs-tr}).  Third, the paper confirms Greenman et
al.'s insight that linear sampling is a sufficiently good approximation of
the exponential set of measurements for the adapted method (see
@section-ref{sec:linear}). The next couple of sections present the background
for this paper.
