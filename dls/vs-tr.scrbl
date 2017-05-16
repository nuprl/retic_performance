#lang gm-dls-2017

@; TODO no future tense!

@title[#:tag "sec:vs-tr"]{Why is Reticulated so Fast ...}

The worst slowdown we observe in Reticulated is one order of magnitude.
By contrast, many partially typed Typed Racket programs are two order of
 magnitude slower than their untyped counterparts@~cite[takikawa-popl-2016 greenman-jfp-2017].
While implementation technology and the peculiarities of the benchmarks
 affect performance, this huge gap suggests fundamental differences.

We have identified three factors that contribute to the relative
 performance of Reticulated.
First, Reticulated's type system lacks support for unions, recursive types,
 and variable-arity functions.
Second, Reticulated's error messages rarely provide actionable feedback.
Third, Reticulated enforces a lax notion of type soundness compared to
 Typed Racket.
All three factors affect both programmers and performance.


@section{Missing Types}
@(define pystone-union-fields
        @; grep for 'PtrComp = ' to find assignments
        @; It's initially `None`, and assigned away-from and back-to `None`
        @;  in `Proc1`
        '(PSRecord.PtrComp))
@(define stats-union-functions
        @; Most of these functions all have a dead-giveaway pair of lines:
        @; ```
        @;  if type(cols) not in [list,tuple]:
        @;      cols = [cols]
        @; ```
        '(abut simpleabut colex linexand recode))
@(define dyn* '(go pystone stats take5))
@; TODO add better in-file evidence

@Integer->word[(length dyn*)] of our benchmarks use type @tt{Dyn} because
 Reticulated cannot express the desired type.
The @bm{pystone} and @bm{stats} benchmarks use @tt{Dyn} to implement
 untagged union types.
The @bm{go} benchmark uses @tt{Dyn} to avoid creating a recursive class type.
Lastly, one function in the @bm{take5} benchmark uses @tt{Dyn} because it accepts
 optional arguments.
@;@note{The implementation of Reticulated currently ignores
@; the types on functions that use optional arguments, argument lists, and/or keyword arguments.
@; Bug report: @url{https://github.com/mvitousek/reticulated/issues/32}.}
These cases represent idiomatic Python code; indeed, @|PEP-484|
 specifies syntax for generics, untagged union types, recursive types, optional
 arguments, and keyword arguments.

Enforcing a union types or (equi-)recursive types requires a disjunction of
 type checks at runtime.
Enforcing the signature of a variable-arity procedure requires a sequence
 of type checks.
In contrast, the types that Reticulated currently supports are all enforced by
 unit-cost tag checks.


@section{Localized Errors}
@; Context-Free Errors
@; Least-Knowledge Errors
@(define vss-popl-2017-benchmarks
   '(callsimple nqueens pidigits meteor fannkuch nbody callmethod
     callmethodslots pystone float chaos go spectralnorm))
@(define vss-2x-benchmarks
   '(nqueens meteor fannkuch callmethod callmethodslots pystone float chaos go))

Errors matter@~cite[f-keynote-2002].
When systems work, everyone is happy, but when systems break, developers really
 want to see high quality error messages.

Reticulated currently produces simple error messages that supply (1) a value
 that failed some check and (2) a stack trace.
Improving these messages is important, but will add runtime overhead.
@;The messages rarely communicate the static type that led to the failing check,
@; or the boundary where a bad untyped entered typed code@~cite[tfffgksst-snapl-2017].
For example, @citet[vss-popl-2017] built an extension to Reticulated that
 augments check failures with a list of all the casts that may have led
 to the fault.
Their evaluation reports the @|t/p-ratio|s of
 @integer->word[(length vss-popl-2017-benchmarks)]
 programs from @|TPPBS|; in @integer->word[(length vss-2x-benchmarks)]
 programs, blame tracking at least doubled the @|t/p-ratio|.


@section{Alternative Soundness}

Sound type systems are useful because they provide guarantees.
If a static type system proves that a term has type @${\tau}, then @${\tau}
 specifies the term's behavior.
The type system can use this specification to find bugs throughout a program,
 the compiler can rely on this specification to generate efficient code,
 and the programmer can trust this specification as an API.

Gradual type systems cannot provide exactly the same guarantees,
 but Typed Racket's soundness is very similar to conventional soundness.
In Typed Racket, typed code is sound in the conventional sense, for example, the
 compiler may use the types to eliminate runtime tag-checks@~cite[sthff-padl-2012].
Untyped code is quarantined.
An untyped value @${v} can only cross the boundary into typed code by being
 ascribed a type @${\tau}.
Typed Racket enforces the behavioral specification implied by @${\tau}
 by compiling the type to a contract; if @${v} does not meet the contract,
 the programmer receives an error message containing @${v}, @${\tau}, and
 the relevant boundary@~cite[tfffgksst-snapl-2017].

@figure["fig:magic" "A well-typed Reticulated program"
@python|{
    def add_one(xs)->List(Int):
      return xs + [1]

    print(add_one(["A", "B"]))
}|]

Reticulated takes a different approach, and guarantees only tag-level soundness.
It is perfectly acceptable for a Reticulated term with type @tt{List(String)}
 to evaluate to a value @${v} with a different type, so long as @${v} is some
 kind of list (see @figure-ref{fig:magic}).
When typed code reads from @${v} expecting a value with type @${\tau'},
 tag-level soundness implies that Reticulated will check the unpacked value
 against the tag of @${\tau'}.
Note that @${\tau'} need not be @tt{String}, but it must match the unpacked
 value.

Reticulated's shallow, by-need runtime checks impose less performance overhead
 than Typed Racket's behavioral contracts.
The open question is whether developers find these checks sufficiently useful.
On one hand, Reticulated types cannot enforce datatype invariants, e.g., to
 to guarantee that all instances of the @tt{Cash} class in
 @section-ref{sec:reticulated} have integer-valued fields.
On the other hand, developers may value the increased flexibility and pay-as-you-annotate
 cost model.

