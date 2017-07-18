#lang gm-plateau-2017

@title[#:tag "sec:vs-tr"]{Why is Reticulated so Fast ...}

The worst observed slowdown of Reticulated over Python is within one order of magnitude.
By contrast, many partially typed Typed Racket programs are two orders of
 magnitude slower than Racket@~cite[takikawa-popl-2016 greenman-jfp-2017].
While implementation technology and the peculiarities of the programs
 affect performance, this order-of-magnitude gap suggests fundamental differences.

We have identified three factors that reduce the overhead of Reticulated
 relative to Python.
First, Reticulated's type system lacks support for common Python idioms.
Second, Reticulated's error messages rarely provide actionable feedback.
@; transcendent incredible
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
@(define dyn* '(go pystone stats take5 lisp))
@; TODO add better in-file evidence

Reticulated currently lacks union types, recursive types, and types for variable-arity functions.
Consequently, Reticulated cannot fully-type some programs in our experiment.
One common issue is Python code that uses @tt{None} as a default value.
The benchmark versions of such code use well-typed defaults instead.
Other benchmark versions resort to dynamic typing.
Both @bm{pystone} and @bm{stats} suffer from the lack of union types,
 and @bm{go} contains a recursive class type.
Lastly, we tried typing a Lisp interpreter, but the program made too-heavy use of union and recursive types.

Rewrites are time-consuming and prone to introduce bugs; mandatory dynamic typing
 contradicts the goals of gradual typing.
Thus, it would benefit developers if Reticulated followed @|PEP-484| and added
 support for unions, recursive types, and functions with optional, variable, and keyword arguments.

Enforcing these types at run-time, however, will impose a higher cost than
 the single-test types that Reticulated programmers must currently use.
A union type or (equi-)recursive type requires a disjunction of type tests, and
 a variable-arity procedure requires a sequence of type checks.
If, for example, every type annotation @${\tau} in our benchmarks were a
 union type with @${\tau} and @tt{Void}, then overall performance would be nearly
 twice as worse as it currently is.


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
A dynamic type error is the result of a mismatch between a type annotation and an untyped value.
Typically, a dynamic type error occurs long after the value enters typed code.

When Reticulated discovers a static type error, it reports the current line number and the conflicting types.
To its credit, this information often pinpoints the source of the fault.

When Reticulated discovers a dynamic type error, it prints a value,
 the name of the check that failed, and a stack trace.
This information does little to help diagnose the problem.
For one, the relevant type annotation is not reported.
A programmer must scan the stack trace for line numbers and consider the type
 annotations that are in scope.
Second, the value in the error message may not be the value that caused the error.
For instance, the reported value may be an element of an ill-typed data structure
 or a return value of an ill-typed function.
Third, the relevant boundary is rarely on the stack trace when the program
 raises the check error. The stack may contain only well-typed code (see the appendix for an example).

Refining the dynamic error messages will add performance overhead.
For example, @citet[vss-popl-2017] built an extension to Reticulated that reports a set of potentially-guilty casts when a dynamic type error occurs.
They report that tracking these casts can double a program's @|t/p-ratio|.

@section[#:tag "sec:vs-tr:soundness"]{Alternative Soundness}

Sound type systems are useful because they provide guarantees.
A sound @emph{static} type system guarantees that evaluating a well-typed program can result in one of three possible outcomes:
 evaluation terminates with a value of the same type; evaluation diverges; or evaluation raises an error from a well-defined set.
A sound @emph{gradual} type system cannot provide the same guarantee because it admits untyped code.
Thus, a gradual type system must redefine soundness.

One approach is to @emph{generalize} traditional type soundness with a fourth clause to cover interactions between typed and untyped code.
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
  @${e} signals an error due to a partial primitive operation; or
}
@item{
  @${e} raises an exception that points to the guilty boundary@~cite[dthf-esop-2012] between typed and untyped code.
}
]

A second approach is to @emph{modify} soundness.
Reticulated@~cite[vss-popl-2017] takes this approach, and weakens the first and fourth clauses:
@exact|{
\begin{itemize}
\item[$1'$.]
  $e$ reduces to a value ${v}$ with type tag ${\lfloor\tau\rfloor}$;
\item[$4'$.]
  $e$ signals an exception that points to a set of potentially guilty boundaries between typed and untyped code.
\end{itemize}
The type tag of ${\tau}$ is its outermost constructor.
For example, the type tag of ${\mathsf{List(Int)}}$ is ${\mathsf{List}}$.}|
The set of boundaries is always empty in the version of Reticulated that was public when we began our evaluation@~cite[vksb-dls-2014];
 @section-ref{sec:vs-tr:errors} addresses the performance implications of @${4'}.

As @figure-ref{fig:magic} demonstrates, the modified clause @${1'} implies that a Reticulated term with
 type @tt{List(String)} may evaluate to a list containing any kind of data.
On one hand, this fact is harmless because type-tag soundness implies that any
 read from a variable with type @tt{List(String)} in typed code is tag-checked.
On the other hand, Reticulated does not monitor values that leave a typed region.
Thus, two interesting scenarios can arise:
@exact|{\begin{description}
\item[The \href{"https://en.wikipedia.org/wiki/Mary_Mallon"}{\emph{typhoid mary}} scenario]
  Typed code can create an ill-typed value,
  pass it to untyped code, and trigger an error by violating an implicit
  assumption in the untyped code.
  The source of such ``disguised'' type errors may be impossible to pinpoint.
\item[The \href{"https://en.wikipedia.org/wiki/Sybil_(Schreiber_book)"}{\emph{sybil}} scenario]
  Two typed contexts can safely reference the same value at incompatible types.
\end{description}%
It remains to be seen whether these potential scenarios cause serious issues in practice.
Developers may embrace the flexibility of alternative soundness and use
 Reticulated in combination with unit tests.
}|

The performance implications of @${1'} are substantial.
A gradual type system that enforces traditional soundness must exhaustively traverse
 data structures before they leave typed code, and must monitor functional values
 to ensure their future applications are well-typed.
Enforcing @${1'} requires a tag check, nothing more.

@figure["fig:magic"
        @list{A well-typed Reticulated program}]{
@python|{
    def make_strings()->List(String):
      xs = []
      for i in range(3):
        if   i == 0: xs.append(i)
        elif i == 1: xs.append([True])
        else       : xs.append(make_strings)
      return xs

    make_strings()
}|}
