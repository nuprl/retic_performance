#lang gm-dls-2017
@title[#:tag "sec:method"]{Adapting Takikawa et al.'s Method}

For each benchmark, we aimed to choose a set of configurations that represent the overall performance of Reticulated Python, and had size less than x. In our method, we type functions as a whole, yielding 2^n configurations per benchmark, where n is the number of functions in a benchmark. 

@itemlist[
@item{
  Find programs, port to reticulated
}
@item{
  Run against program which generates all possible configurations of the
  program by typing/untyping each function
}
@item{
  Run each configuration for x iterations, recording the time using python's
  system timer
}
@item{
  Machine used was KARST CLUSTER
}

]


@section{Granularity Norm}

@; NOTE need to borrow terms from literature, e.g.
@; - Thatte's type-precision relation
@; - Henglein's "completions" (also erasures?)

Let @${L} be a programming language.
Let @${P} be some program written in the language, composed of @${n_M} modules
 @${M_0 \ldots M_{n_M - 1}}.

A gradual type system for @${L} defines a syntax @${L^\tau} for adding type
 annotations to @${L} programs.
Of course @${P} is an @${L} program; if @${P'} is like @${P} but contains
 some type annotations, we say @${P'} is a @emph{gradually typed configuration}
 of @${P}.
More generally,

@definition["configuration"]{
  Let @${u : L^\tau \rightarrow L} be a function that strips all type annotations
   from an @${L^\tau} program.
  A given @${L^\tau} program @${P} is a @emph{gradually typed configuration}
   of the @${L} progam @${u(P)}.
}

Note that @${u(P) = u(u(P))}.
In other words, every @${L} program is implicitly an @${L^\tau} program
 and implicitly a configuration of itself.

Performance evaluation for a gradually typed language @${L^\tau} is:
@itemlist[
@item{
  select some representative @${L} programs,
}
@item{
  for each program @${P}, compare the performance of @${P} as an @${L} program
   to the performance of its configurations
}
@item{
  summarize the performance
}
]
The fundamental assumption of performance evaluation is that the computed
 summaries are representative of the performance of configurations of an
 arbitrary @${L} program.

There is a serious problem with the description.
For a given program @${P}, the set @${\{P' \mid u(P') = P\}} may be infinite.
See @figure-ref{fig:infinite-configuration-space} for an example.
Key insight from @citet[tfdffthf-ecoop-2015] is to define the notion of a
 @emph{fully-typed configuration}.

@figure["fig:infinite-configuration-space" "Identify function has an infinite configuration space"
  @exact|{
    \fbox{L}
    $\begin{array}{l l l}
       \tau & ::= & \mathsf{Int} \mid \tau \rightarrow \tau
    \\ e & ::= & x \mid \lambda\,x.\,e \mid e~e
    \\ e^\tau & ::= & x \mid \lambda\,x:\tau.\,e^\tau \mid e^\tau~e^\tau
    \end{array}$

    \vspace{1ex}

    $\lambda\,x.\,x$ is an $e$ program with an infinite configuration space
  }|
]

@definition["fully-typed configuration"]{
  Let @${P} be an @${L} program.
  A fully-typed configuration of @${P} is an @${L^\tau} program @${P^\tau}
   such that @${P^\tau} contains a full type annotation everywhere that tha
   syntax of @${L^\tau} allows.
}

Instead of measuring the performance of @${L} programs per se,
 @citet[tfdffthf-ecoop-2015] propose a slightly different protocol:
@itemlist[
@item{
  select some representative @${L} programs,
}
@item{
  for each program @${P}, choose a fully-typed configuration @${P^\tau}
}
@item{
  compare the performance of @${P} to the performance of each configuration
   in the finite set @${\{P' \mid u(P') = P \wedge P' \sqsubseteq P^\tau\}}
}
@item{
  summarize the performance of the @${P'}
}
]

The following definition is central to this approach:

@definition["configuration space"]{
  The configuration space of a fully-typed configuration @${P^\tau} is the set
   @${\{P' \mid P' \sqsubseteq P^\tau\}}.
}

The size of this set depends on the syntax of @${L^\tau}.
Specifically, it depends on the number of locations in @${P} where the programmer
 may add a type annotation.
Informally, we call this the @emph{granularity} of @${L^\tau}.
Formally,

@definition["granularity norm"]{
  The granularity norm of a gradually typed language @${L^\tau} is a function
   @${@gnorm{\cdot}} from ``syntax'' to natural numbers.
  @TODO{restrictions}
}
@; TODO actually has properties of a norm?

@bold{Examples}
@itemlist[
@item{
  Let @${@gnorm{P}_M} count the number of modules in the program @${P}.
  This is the granularity norm for Typed Racket.
  It is also a valid granularity norm for Reticulated Python.
}
@item{
  Let @${@gnorm{P}_f} count the number of function in @${P}.
  This is a valid granularity norm for Reticulated.
}
@item{
  Let @${@gnorm{P}_C} count the number of classes in @${P}.
  This is another valid granularity norm for Reticulated.
}
@item{
  Let @${P} be a program, assume every function in @${P} has a natural-number
   arity (no keyword or optional arguments).
  Let @${@gnorm{P}_\mu} sum the number of classes, number of functions (including methods),
   and arity of each function.
  This is a norm for Reticulated, moreover it is the @emph{finest} such norm,
   in the sense that for any other Reticulated norm
   @${@gnorm{\cdot}_?} the inequality @${@gnorm{P}_? \leq @gnorm{P}_\mu} holds.
}
]

The norm we use is @${@gnorm{P}_z = @gnorm{P}_f + @gnorm{P}_C}.


