#lang gm-plateau-2017
@title[#:tag "sec:reticulated"]{Reticulated Python}

Reticulated is a gradual typing system for Python that gives programmers the
 ability to annotate functions and class fields with types@~cite[vksb-dls-2014].
The type annotations describe program invariants.
Reticulated enforces the invariants by statically checking the type annotations
 and dynamically checking the values that flow into annotated positions.

@; syntax & semantics?

By way of example, @figure-ref{fig:cash} presents a type-annotated class representing US currency.
The annotations imply two high-level invariants:
 (1) instances of the @pythoninline{Cash} class have integer-valued fields, and
 (2) the @pythoninline{add_cash} method is only invoked with instances of the @pythoninline{Cash} class.
Reticulated enforces these invariants within the @pythoninline{add_cash} method
 by translating the type annotations into dynamic checks that protect the two
 arguments of @pythoninline{add_cash} and the four dereferences of the fields
 @pythoninline{dollars} and @pythoninline{cents}.
These defensive checks protect statically typed code from dynamically-typed Python code.

@figure["fig:cash" "Reticulated syntax"
@python|{
@fields({"dollars": Int, "cents":Int})
class Cash:
  def __init__(self:Cash, d:Int, c:Int)->Void:
    self.dollars = d
    self.cents = c

  def add_cash(self:Cash, other:Cash)->Void:
    self.dollars += other.dollars
    self.cents += other.cents
}|]


@section{Tag-Level Soundness}

Reticulated uses dynamic type checks to implement a form of type soundness.@note{@citet[vss-popl-2017] use the term @emph{open-world soundness} and conjecture that Reticulated is open-world sound.}
Informally, if @pythoninline{e} is a well-typed expression, then
 evaluating @pythoninline{e} can result in four possible outcomes:
@itemlist[#:style 'ordered
@item{
  the program execution terminates with a value @pythoninline{v} that has the same @emph{type tag} as the expression @pythoninline{e};
}
@item{
  the execution diverges;
}
@item{
  the execution ends in an exception due to a partial computational primitive (e.g., division-by-zero);
}
@item{
  the execution ends in a type error due to a failed assertion inserted by Reticulated.
}
]@;
Furthermore, if @pythoninline{e} appears in the context of a larger Python program,
 then the program can observe exactly these four outcomes.

A @emph{type tag} is essentially a type constructor without parameters.
For completeness, @figure-ref{fig:retic-types} documents Reticulated's types @${\tau},
 tags @${\kappa}, and the mapping @$|{\tagof{\cdot}}| from types to tags.

Reticulated's form of soundness, henceforth @emph{tag soundness}, differs from conventional type soundness in two significant ways.
First, tag soundness does not rule out type errors in well-typed programs.
Second, tag soundness implies that a term with type @pythoninline{List(Int)}
 can produce any kind of @pythoninline{List}.
In @figure-ref{fig:magic}, for example, the term @pythoninline{make_strings()}
 has the static type @pythoninline{List(String)} but evaluates to a list containing
 an integer, a boolean, and a function.
Put another way, Reticulated supports only tag-level compositional reasoning.

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


@subsection[#:tag "sec:defense"]{In Defense of Tag Soundness}

Reticulated's main design goal is to provide seamless interaction with Python code.@note{Specifically, CPython 3@~cite[vksb-dls-2014 vss-popl-2017].}
If a programmer debugging a large Python codebase wants to be sure that one
 function always returns values of a given type, he or she can use Reticulated
 to enforce that @emph{one type} without affecting the rest of the program.
To quote the vision paper of @citet[svcb-snapl-2015]:

@nested[#:style 'inset @emph{
  That is, programmers should be able to add or remove type annotations without
  any unexpected impacts on their program, such as whether it still typechecks
  and whether its runtime behavior remains the same.
}]
@;
Consequently, Reticulated cannot implement a standard form of type soundness.
There are two fundamental reasons why Reticulated must aim for a different guarantee.

First, any interaction between type-annotated code and dynamically-typed
 Python code can potentially cause a dynamic type error.
On one hand, the Reticulated type annotation might not match the behaviors implemented
 by the Python code.
On the other hand, the Python code might contain a bug.
These impedance mismatches cannot be caught without a static analysis of the
 Python code.
Tag-level soundness admits this reality with its fourth clause, which states
 that execution may end in a type error.

Second, Python code may inspect the representation of values.
Reticulated must therefore ensure that a type-annotated value is
 indistinguishable from a Python version of the same value.
In particular, a Reticulated list must be indistinguishable from a Python list;
 the only way to meet this criterion is to use the same list in both cases.@note{
 Other gradually-typed languages use proxies to approximate indistinguishability@~cite[thf-popl-2008 rsfbv-popl-2015 rnv-ecoop-2015 wmwz-ecoop-2017].
 This approach typically fails when values are serialized or sent across an FFI boundary.}
This indistinguishability constraint explains why it is difficult for
 Reticulated to predict the type of a run-time value.

Reticulated @emph{chooses} to implement tag-level soundness instead of some
 other compromise because of an implicit design goal:
 @emph{all dynamic type checks run in near-constant time}.@note{This goal is implicit in the implementation of Reticulated, and assumed by @citet[vss-popl-2017].}
Intuitively, tag-level checks should impose little performance overhead no
 matter how a programmer adds types to a Python program.
Prior work on Reticulated does not evaluate this claim@~cite[vksb-dls-2014 vss-popl-2017].

@figure["fig:retic-types" "Reticulated types and type tags" @exact|{
  $\begin{array}{l l l}
    \tau & = & \ldots \\
    \kappa & = & \ldots \\[0.6mm]
  \end{array}$

  \fbox{$\tagof{\tau} = \kappa$}
  $\begin{array}{l l l}
    \tagof{Int} & = & Int \\
    \tagof{List(\tau)} & = & \rightarrow \\
    \tagof{\tau \rightarrow \tau} & = & \rightarrow
  \end{array}$
}|]

@; -----------------------------------------------------------------------------
@;
@;@section[#:tag "sec:vs-tr:types"]{Types}
@;
@;@; math types side-by-side with programming types
@;Document the types Reticulated has, document the grammar?
@;
@;Mention the types Retic does not have.
@;
@;
@;@section[#:tag "sec:vs-tr:errors"]{Error Messages}
@;
@;Two kinds of faults can occur in Reticulated: static type errors and dynamic type errors.
@;A static type error is a mismatch between two types.
@;A dynamic type error is the result of a mismatch between a type annotation and an untyped value.
@;Typically, a dynamic type error occurs long after the value enters typed code.
@;
@;When Reticulated discovers a static type error, it reports the current line number and the conflicting types.
@;To its credit, this information often pinpoints the source of the fault.
@;
@;When Reticulated discovers a dynamic type error, it prints a value,
@; the name of the check that failed, and a stack trace.
@;This information does little to help diagnose the problem.
@;For one, the relevant type annotation is not reported.
@;A programmer must scan the stack trace for line numbers and consider the type
@; annotations that are in scope.
@;Second, the value in the error message may not be the value that caused the error.
@;For instance, the reported value may be an element of an ill-typed data structure
@; or a return value of an ill-typed function.
@;Third, the relevant boundary is rarely on the stack trace when the program
@; raises the check error.
@;The stack may contain only well-typed code (see the appendix for an example).
@;
@;
@;@section[#:tag "sec:vs-tr:soundness"]{Alternative Soundness}
@;
@;Sound type systems are useful because they provide guarantees.
@;A sound @emph{static} type system guarantees that evaluating a well-typed program can result in one of three possible outcomes:
@; evaluation terminates with a value of the same type; evaluation diverges; or evaluation raises an error from a well-defined set.
@;A sound @emph{gradual} type system cannot provide the same guarantee because it admits untyped code.
@;Thus, a gradual type system must redefine soundness.
@;@; TODO never repeat anything ever in this short paper
@;
@;One approach is to @emph{generalize} traditional type soundness with a fourth clause to cover interactions between typed and untyped code.
@;Typed Racket takes this approach@~cite[tfffgksst-snapl-2017].
@;In particular, if a program @${e} is well typed at type @${\tau}, then either:
@;@itemlist[#:style 'ordered
@;@item{
@; @${e} reduces to a value @${v} with type @${\tau};
@;}
@;@item{
@;  @${e} diverges;
@;}
@;@item{
@;  @${e} signals an error due to a partial primitive operation; or
@;}
@;@item{
@;  @${e} raises an exception that points to the guilty boundary@~cite[dthf-esop-2012] between typed and untyped code.
@;}
@;]
@;
@;A second approach is to @emph{modify} soundness.
@;Reticulated@~cite[vss-popl-2017] takes this approach, and weakens the first and fourth clauses:
@;@exact|{
@;\begin{itemize}
@;\item[$1'$.]
@;  $e$ reduces to a value ${v}$ with type tag ${\tagof{\tau}}$;
@;\item[$4'$.]
@;  $e$ signals an exception that points to a set of potentially guilty boundaries between typed and untyped code.
@;\end{itemize}
@;The type tag of ${\tau}$ is its outermost constructor.
@;For example, the type tag of ${\mathsf{List(Int)}}$ is ${\mathsf{List}}$.}|
@;The set of boundaries is always empty in the version of Reticulated that was public when we began our evaluation@~cite[vksb-dls-2014];
@; @section-ref{sec:vs-tr:errors} addresses the performance implications of @${4'}.
@;
@;As @figure-ref{fig:magic} demonstrates, the modified clause @${1'} implies that a Reticulated term with
@; type @tt{List(String)} may evaluate to a list containing any kind of data.
@;On one hand, this fact is harmless because type-tag soundness implies that any
@; read from a variable with type @tt{List(String)} in typed code is tag-checked.
@;On the other hand, Reticulated does not monitor values that leave a typed region.
@;Thus, two interesting scenarios can arise:
@;@exact|{\begin{description}
@;\item[The \href{"https://en.wikipedia.org/wiki/Mary_Mallon"}{\emph{typhoid mary}} scenario]
@;  Typed code can create an ill-typed value,
@;  pass it to untyped code, and trigger an error by violating an implicit
@;  assumption in the untyped code.
@;  The source of such ``disguised'' type errors may be impossible to pinpoint.
@;\item[The \href{"https://en.wikipedia.org/wiki/Sybil_(Schreiber_book)"}{\emph{sybil}} scenario]
@;  Two typed contexts can safely reference the same value at incompatible types.
@;\end{description}%
@;It remains to be seen whether these potential scenarios cause serious issues in practice.
@;Developers may embrace the flexibility of alternative soundness and use
@; Reticulated in combination with unit tests.
@;}|
@;
