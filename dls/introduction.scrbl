#lang gm-dls-2017

@require{bib.rkt}

@title[#:tag "sec:introduction"]{Measuring Reticulated}

Siek and Taha's 2006 paper@~cite[st-sfp-2006] introduces the notion of
gradual typing, a sound variant of Common Lisp's optional typing. Using
gradual typing, ``programmers should be able to add or remove type
annotations without any unexpected impacts on their program''@~cite[svcb-snapl-2015].
@; TODO 'is' ???
One unexpected impact is the application of a function on integers to a
string; similarly, when typed code passes an array of floats to untyped
code, the programmer expects that the untyped code does not assign a
boolean to one of the array's slots. By contrast, a programmer may
expect the addition of types to speed up the program execution because the
compiler can exploit the type information.

Gradual typing implements the sound combination of typed and untyped code
with the insertion of run-time checks. At a high level, a gradual typing
system uses the type annotations to determine whether and where a
typed value may flow into the function position of an application and
adds a check there to ensure the argument value matches the expected
type. If not, the run-time check raises an exception. Clearly, the
insertion of such run-time checks imposes a cost, and the question arises
how significant this cost is.

@citet[takikawa-popl-2016] present the first comprehensive method for
evaluating the performance of gradual typing systems.
If a program consists of @${n} components, Takikawa et al. propose to measure
@math{2^n} configurations. Doing so mimics the process through which
programmers may gradually equip all possible sites for type declarations
with annotations. In order to evaluate these measurements, they propose a
simple metric, the proportion of @emph{D-deliverable} configurations, meaning the
number of configurations whose running time is at most
@math{D}x slower than the untyped configuration.
Follow-up work by @citet[greenman-jfp-2017] confirms that a
@emph{linear} amount of random sampling approximates the
exponential measurements well in the case of Typed Racket.

Simultaneously to Siek and Taha's original work, Tobin-Hochstadt and
Felleisen launched the development of
Typed Racket, based on almost the same idea as gradual typing@~cite[thf-dls-2006].
In 2016, with Typed Racket under development for 10 years, Takikawa et al.'s
performance evaluation of Typed Racket indicates that this form
of gradual typing has disastrous performance characteristics.

This paper contributes three insights. First, it explains an adaptation of
Takikawa et al.'s method (see @section-ref{sec:method}) for Reticulated@~cite[vksb-dls-2014],
a gradual typing system that is relatively
faithful to Siek and Taha's original proposal. Second, it reports on the
results of applying the adapted method to Reticulated (see
@section-ref{sec:exhaustive}). While the performance of Reticulated seems to
be significantly better than Typed Racket's, we conjecture that this
due to (1) a significant gap in Reticulated's soundness, (2)
Reticulated's lack of expressiveness, and (3) low-quality error messages
(see @section-ref{sec:vs-tr}).
@;Third, the paper confirms a suspicion that the overhead in an arbitrary
@; Reticulated program is proportional to the number of type annotations in the program (see @section-ref{sec:exhaustive}).
Third, the paper confirms Greenman et
al.'s insight that linear sampling is a sufficiently good approximation of
the exponential set of measurements for the adapted method (see
@section-ref{sec:linear}). The next section presents the background material.
