#lang gm-dls-2017

@title[#:tag "sec:vs-tr"]{Why is Reticulated so Fast ...}

The worst slowdown we observe in Reticulated is within one order of magnitude.
By contrast, many partially typed Typed Racket programs are two orders of
 magnitude slower than their untyped counterparts@~cite[takikawa-popl-2016 greenman-jfp-2017]. While implementation technology and the peculiarities of the programs
 affect performance, this order-of-magnitude gap suggests fundamental differences between Typed Racket and Reticulated.

We have identified three factors that contribute to the seemingly-impressive performance of Reticulated. First, Reticulated's type system lacks support for common Python idioms. Second, Reticulated's error messages rarely provide actionable feedback. 
Third, Reticulated guarantees an alternative notion of type soundness.

@section[#:tag "sec:vs-tr:types"]{Missing Types}
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

Reticulated currently lacks union types, recursive types, and types for variable-arity functions.
These types are essential for expressing common Python idioms; in fact @|PEP-484| specifies syntax for generics, untagged union types,
 recursive types, optional arguments, and keyword arguments.
We rewrote several programs that used optional arguments and union types. 
Four of the benchmarks continue to use dynamic typing because Reticulated cannot express the desired type:
the @bm{pystone} and @bm{stats} programs require union types;
the @bm{go} program contains a recursive class type;
and one function in @bm{take5} accepts optional arguments.@note{@url{https://github.com/mvitousek/reticulated/issues/32}}
Such rewrites are both time-consuming and prone to introduce bugs.

Enforcing these types at run-time, however, will impose a higher cost than
 the single-test types that Reticulated programmers must currently use.
A union type or (equi-)recursive type requires a disjunction of type tests, and
 a variable-arity procedure requires a sequence of type checks.
If, for example, every type annotation @${T} in our benchmarks was instead a
 union type with @${T} and @tt{Void}, then overall performance would be nearly
 2x worse.


@section[#:tag "sec:vs-tr:errors"]{Uninformative Errors}
@(define vss-popl-2017-benchmarks
   '(callsimple nqueens pidigits meteor fannkuch nbody callmethod
     callmethodslots pystone float chaos go spectralnorm))
@(define vss-2x-benchmarks
   '(nqueens meteor fannkuch callmethod callmethodslots pystone float chaos go))

Errors matter@~cite[f-keynote-2002].
When systems work, everyone is happy, but when systems break, developers want error messages that pinpoint the source of the fault.

Two kinds of faults can occur in Reticulated: static type errors and dynamic type errors.
A static type error is a mismatch between two types.
A dynamic type error is the result of a mismatch between a type annotation and an untyped value;
 typically, a dynamic type error occurs long after the mis-matched value entered typed code.

When Reticulated discovers a static type error, it reports the current line number and the conflicting types.
To its credit, this information often pinpoints the source of the fault.

When Reticulated discovers a dynamic type error, it prints a value that failed some check (e.g., @pythoninline|{ retic.transient.CheckError: 20 }|) and a stack trace.
This information does little to help the programmer to discover what went wrong.

Refining the dynamic error messages will add performance overhead.
For example, @citet[vss-popl-2017] built an extension to Reticulated that reports a set of potentially-guilty casts when a dynamic type error occurs.
Their evaluation reports that tracking these casts may double a program's @|t/p-ratio|.

@section[#:tag "sec:vs-tr:soundness"]{Alternative Soundness}

Sound type systems are useful because they provide guarantees.
A sound @emph{static} type system guarantees that evaluating a well-typed program can result in one of three possible outcomes:
 evaluation terminates with a value of the same type; evaluation diverges; or evaluation raises an error from a well-defined set.
A sound @emph{gradual} type system cannot provide the same guarantee because it admits untyped code.
Thus, a gradual type system must redefine soundness.

One approach is to generalize traditional type soundness with a fourth clause to cover interactions between typed and untyped code.
Typed Racket takes this approach@~cite[tfffgksst-snapl-2017].
In particular, if a program @${e} is well typed at type @${\tau}, then either:
@itemlist[#:style 'ordered
@item{
 @${e} reduces to a value @${v} with type @${\tau};
}
@item{
  @${e} diverges;
}
@item{
  @${e} raises an error from a well-defined set; or
}
@item{
  @${e} raises an exceptional error that points to one boundary between typed and untyped code.
}
]

A second approach is to modify the traditional notion of soundness.
Reticulated takes this approach@~cite[vss-popl-2017], and changes the first
 clause:@note{As for the other clauses, the version of Reticulated that we
  evaluated will either diverge, raise an error due to an inserted check (see
  @section-ref{sec:vs-tr:errors}), or raise a Python error. Reticulated with
  blame@~cite[vss-popl-2017] will either diverge, raise an error that blames one
  or more type boundaries, or raise a Python error.}
@exact|{
\begin{itemize}
\item[1.']
  $e$ reduces to a value ${v}$ with type tag ${\lfloor\tau\rfloor}$.
\end{itemize}
The type tag of ${\tau}$ is its outermost constructor. For example,
 the type tag of ${\mathsf{List(Int)}}$ is ${\mathsf{List}}$.
}|

As @figure-ref{fig:magic} demonstrates, this alternative soundness implies that a Reticulated term with
 type @tt{List(String)} may evaluate to a list containing any kind of data.
On one hand, this fact is harmless since type-tag soundness implies that any
 read from a variable with type @tt{List(String)} is tag-checked.
On the other hand, Reticulated does not monitor values that leave a typed region.
Thus, two interesting scenarios can arise:
@itemlist[#:style 'ordered
@item{
  (the @emph{typhoid mary} scenario) Typed code can create an ill-typed value,
  pass it to untyped code, and trigger an error by violating an implicit
  assumption in the untyped code.
  The source of such ``disguised'' type errors may be impossible to pinpoint.
}
@item{
  (the @emph{sybil} scenario) Two typed contexts can safely reference the same value at incompatible types.
}
]@;
It remains to be seen whether these potential scenarios cause serious issues in practice.
Developers may embrace the flexibility of the alternative soundness and use
 Reticulated in combination with unit tests.
The only conclusion our data supports is that Reticulated's type-tag checks
 impose less performance overhead than Typed Racket's behavioral contracts.

@figure["fig:magic"
        @list{A well-typed Reticulated program}]{
@python|{
    def make_strings()->List(String):
      xs = []
      for i in range(3):
        if   i == 0: xs.append(i)
        elif i == 1: xs.append(True)
        else       : xs.append(make_strings)
      return xs

    make_strings()
}|}

