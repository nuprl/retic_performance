#lang gm-plateau-2017
@title[#:tag "sec:reticulated"]{Reticulated Python}

Reticulated is a gradual typing system for Python@note{Specifically, CPython 3.}
 that gives programmers the ability to annotate functions and class fields with types@~cite[vksb-dls-2014 vss-popl-2017].
By way of example, @figure-ref{fig:cash} presents a type-annotated class representing US currency.
The annotations imply two high-level invariants:
 (1) instances of the @pythoninline{Cash} class have integer-valued fields, and
 (2) the @pythoninline{add_cash} method is only invoked with instances of the @pythoninline{Cash} class.
Reticulated enforces these invariants within the @pythoninline{add_cash} method
 by translating the type annotations into dynamic checks that protect the two
 arguments of @pythoninline{add_cash} and the four dereferences of the fields
 @pythoninline{dollars} and @pythoninline{cents}.
These defensive checks protect the statically typed method from arbitrary callers.

@figure["fig:cash" "A well-typed class" @python|{
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
@;Furthermore, if @pythoninline{e} appears in the context of a larger Python program,
@; then the program can observe exactly these four outcomes.

A @emph{type tag} is essentially a type constructor without parameters.
For completeness, @figure-ref{fig:retic-types} presents selected types @${\tau}
 and tags @${\kappa}, as well as the mapping @$|{\tagof{\cdot}}| from types to tags.@note{The
  type @${\tdyn} is the dynamic type.
  Every Python term is well-typed at @${\tdyn}.}

Note that Reticulated's form of soundness, henceforth @emph{tag soundness},
 differs from conventional type soundness in two significant ways.
First, tag soundness does not rule out type errors in well-typed programs.
Second, tag soundness implies that a term with type @pythoninline{List(Int)}
 can produce any kind of @pythoninline{List}.
In @figure-ref{fig:magic}, for example, the term @pythoninline{make_strings()}
 has the static type @pythoninline{List(String)} but evaluates
 to a list containing an integer, an empty list, and a function.
Put another way, Reticulated supports only tag-level compositional reasoning.

@figure["fig:magic" "A well-typed function"
@python|{
    def make_strings()->List(String):
      xs = []
      for i in range(3):
        if   i == 0: xs.append(i)
        elif i == 1: xs.append([])
        else       : xs.append(make_strings)
      return xs

    make_strings() # returns [0, [], <function>]
}|]


@subsection[#:tag "sec:defense"]{In Defense of Tag Soundness}

Reticulated's main design goal is to provide seamless interaction with Python code.
To quote the vision paper of @citet[svcb-snapl-2015]:

@nested[#:style 'inset @emph{
  That is, programmers should be able to add or remove type annotations without
  any unexpected impacts on their program, such as whether it still typechecks
  and whether its runtime behavior remains the same.
}]
@;
Consequently, Reticulated cannot implement a standard form of type soundness.
There are two fundamental reasons why Reticulated must aim for a different guarantee.

First, any interaction between typed code and dynamically-typed
 Python code can potentially cause a dynamic type error.
There are two reasons for this.
On one hand, the Reticulated type annotation might not match the behaviors implemented
 by the Python code.
On the other hand, the Python code might contain a bug.
These impedance mismatches cannot be caught without a static analysis of the
 Python code.
Tag-level soundness admits this reality with its fourth clause, which states
 that execution may end in a type error.

Second, Python code may inspect the representation of values.
Reticulated must therefore ensure that a value from statically-typed code is
 indistinguishable from a Python value.
The only way to meet this criterion is to use the same value in both
 cases.@note{Other gradually-typed languages use proxies to approximate
  indistinguishability@~cite[thf-popl-2008 rsfbv-popl-2015 rnv-ecoop-2015 wmwz-ecoop-2017].
  This approach typically fails when values are serialized or sent across an FFI boundary.}
In particular, a Reticulated list must be indistinguishable from a Python list.
This indistinguishability constraint explains why it is difficult for
 Reticulated to predict the run-time type of a value.

Reticulated @emph{chooses} to implement tag-level soundness instead of some
 other compromise because of an implicit design goal;
 @emph{all dynamic type checks run in near-constant time}.@note{This goal is implicit in the implementation of Reticulated, and assumed by @citet[vss-popl-2017].}
Instead of checking the type of values within a data structure, Reticulated
 stops at the structure's outermost tag.
Hence list types require an @${\Theta(1)} tag check and structural object types
 with @${f} fields require a @${\Theta(f)} check that the given value binds
 the proper fields.
Intuitively, such checks should impose little overhead no matter how a programmer
 adds type annotations.

@figure["fig:retic-types"
        @elem{Selected types (@${\tau}) and type tags (@${\kappa})}
        #:style left-figure-style @exact|{
  $\begin{array}{l l l}
    \tau & = & \tint \mid
               \tlist{\tau} \mid
               \tfunction{\tau}{\tau} \mid
               \tdyn \\
    \kappa & = & \kint \mid
                 \klist \mid
                 \kfunction \mid
                 \kdyn \\[2mm]
  \end{array}$

  {\fbox{$\tagof{\tau} = \kappa$} \hfil} \\
  ${\setlength{\arraycolsep}{4mm}\begin{array}{l l}
    \tagof{\tint} = \kint          & \tagof{\tfunction{\tau}{\tau'}} = \kfunction \\
    \tagof{\tlist{\tau}} = \klist  &  \tagof{\tdyn} = \kdyn \\
  \end{array}}$
}|]


@section{In Contrast, Generalized Type Soudness}

Typed Racket@~cite[thf-popl-2008 tfffgksst-snapl-2017] implements a
 soundness guarantee that generalizes conventional type soundness.
It is useful to compare Typed Racket's soundness to tag soundness.

If the Typed Racket expression @pythoninline{e} has the static type @${\tau},
 then evaluating @pythoninline{e} can result in four possible outcomes:
@itemlist[#:style 'ordered
@item{
  the program execution terminates with a value @pythoninline{v} that
  has type @${\tau'} such that @${\tau'} is a subtype of @${\tau};
}
@item{
  the execution diverges;
}
@item{
  the execution ends in an exception due to a partial computational primitive (e.g., division-by-zero);
}
@item{
  the execution ends in a type error that points to one of the fixed number of
   boundaries between statically typed and dynamically typed code.
}
]

In contrast to Reticulated, Typed Racket types are sound in the conventional
 sense; a term with type @$|{\tlist{\tint}}| cannot yield a list of strings.
Furthermore, Typed Racket guarantees that every run-time type error directs
 programmers to the mis-matched value and type annotation at its root.

These guarantees are clearly an improvement over tag soundness,
 but have two non-obvious costs.
First, the host language must implement proxies that protect
 typed code@~cite[chaperones-impersonators].
Second, gradually-typed programs suffer the allocation, interposition, and
 validation costs implied by the proxies.
As mentioned in the introduction, these run-time costs can slow gradually typed
 programs by two orders of magnitude@~cite[tfgnvf-popl-2016] or more@~cite[greenman-jfp-2017].
