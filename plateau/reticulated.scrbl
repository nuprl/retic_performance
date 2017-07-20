#lang gm-plateau-2017
@title[#:tag "sec:reticulated"]{Reticulated Python}

Reticulated is a gradual typing system for
Python@~cite[vksb-dls-2014].
In Reticulated, programmers can express types using Python's syntax for
 @hyperlink["https://www.python.org/dev/peps/pep-3107/"]{function annotations} and
 @hyperlink["https://www.python.org/dev/peps/pep-0318/"]{decorators}.
Reticulated statically checks the annotations and
 translates them to run-time type checks designed to enforce type soundness.

@; TODO clarify, merge with TR soundness

In a statically typed language, type soundness implies that if a program
 is well-typed, running the program results in one of three possible
 outcomes:
 the program (1) evaluates to a value of the expected type,
 (2) diverges, or (3) throws an exception from a well-defined set.
For partially-typed programs, in which typed and untyped code interact,
 there is a fourth outcome: the program can (4) throw an exception
 due to a boundary between typed and untyped code@~cite[tfffgksst-snapl-2017].
Reticulated aims to enforce the first three conditions by static type-checking,
 and the fourth by dynamic type-checking.

@Figure-ref{fig:cash} presents a well-typed class definition.
If we add the method call @pythoninline{c1.add_cash(20)} to the program,
 then Reticulated raises a static type error because the integer @pythoninline{20}
 is not an instance of the @pythoninline{Cash} class.
Contrast this to an ill-typed call that occurs in a dynamically-typed context:

@nested[
@python|{
    def dyn_add_cash(amount):
      c1.add_cash(amount)

    dyn_add_cash(20)
}|]@;
The variable @pythoninline{amount} is not annotated, so Reticulated
 cannot statically prove that all calls to @pythoninline{dyn_add_cash} violate
 the assumptions of the @pythoninline{add_cash} method.
To preserve type soundness, Reticulated rewrites the method to defensively
 check its arguments; in particular, Reticulated adds one structural type check
 for each argument of @pythoninline{add_cash}.
At run-time, the check for the second argument throws an exception
 before the call @pythoninline{dyn_add_cash(c1, 20)} causes
 the program to fail.

Reticulated inserts similar checks around
  function calls, to enforce the declared return type, and
  around reads from variables or data structures, to detect strong updates@~cite[vksb-dls-2014].
These pervasive checks implement a notion of soundness that protects
 typed code without inhibiting untyped code@~cite[vss-popl-2017].

@figure["fig:cash" "Reticulated syntax"
@python|{
import math

@fields({"dollars": Int, "cents":Int})
class Cash:
  def __init__(self:Cash, d:Int, c:Int)->Void:
    self.dollars = d
    self.cents = c

  def add_cash(self:Cash, other:Cash)->Void:
    self.dollars += other.dollars
    self.cents += other.cents

c1 = Cash(1000, 0)
}|]


@; -----------------------------------------------------------------------------
@section{TBA: Properties, Guarantees, or Lack Thereof}

@section[#:tag "sec:vs-tr:types"]{Types}

@; math types side-by-side with programming types
Document the types Reticulated has, document the grammar?

Mention the types Retic does not have.


@section[#:tag "sec:vs-tr:errors"]{Error Messages}

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
 raises the check error.
The stack may contain only well-typed code (see the appendix for an example).


@section[#:tag "sec:vs-tr:soundness"]{Alternative Soundness}

Sound type systems are useful because they provide guarantees.
A sound @emph{static} type system guarantees that evaluating a well-typed program can result in one of three possible outcomes:
 evaluation terminates with a value of the same type; evaluation diverges; or evaluation raises an error from a well-defined set.
A sound @emph{gradual} type system cannot provide the same guarantee because it admits untyped code.
Thus, a gradual type system must redefine soundness.
@; TODO never repeat anything ever in this short paper

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

