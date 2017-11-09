#lang gm-pepm-2018
@title[#:tag "sec:reticulated"]{Reticulated Python}

Reticulated is a gradual typing system for Python@note{Specifically, CPython 3.}
 that gives programmers the ability to annotate functions and class fields with types@~cite[vksb-dls-2014 vss-popl-2017].
By way of example, @figure-ref{fig:cash} presents a type-annotated class representing US currency.
The annotations imply two high-level invariants:
 (1) instances of the @pythoninline{Cash} class have integer-valued fields, and
 (2) the @pythoninline{add_cash} method is only invoked with instances of the @pythoninline{Cash} class.

Within the @pythoninline{add_cash} method, Reticulated enforces these invariants
 by translating the type annotations into dynamic checks that protect the two
 arguments of @pythoninline{add_cash} and the four dereferences of the fields
 @pythoninline{dollars} and @pythoninline{cents}@~cite[vksb-dls-2014].
These checks defend the statically typed method from arbitrary callers.
If a Python context invokes @pythoninline{add_cash} with an integer, the
 inserted checks will halt the program with a so-called @emph{dynamic type error}.

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


@section[#:tag "sec:tag-soundness"]{Tag Soundness}

Reticulated uses dynamic type checks to implement a form of type
 soundness.@note{@citet[vss-popl-2017] use the phrase @emph{open-world soundness}.
 They conjecture that Reticulated is open-world sound.}
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
  the execution ends in a dynamic type error.
}
]@;
@;Furthermore, if @pythoninline{e} appears in the context of a larger Python program,
@; then the program can observe exactly these four outcomes.

A @emph{type tag} is essentially a type constructor without parameters.
For completeness, @figure-ref{fig:retic-types} presents selected types @${\tau}
 and tags @${\kappa}, as well as the mapping @$|{\tagof{\cdot}}| from types to tags.@note{The
  type @${\tdyn} is the dynamic type.
  Every expression is well-typed at @${\tdyn}.}


Tag soundness is clearly weaker than standard type soundness; a well-typed
 program can reduce to a value that does not match its static type annotation.
@Figure-ref{fig:magic} demonstrates with an expression that has the static
 type @pythoninline{List(Int)} but evaluates to a list containing a string, an
 empty list, and a function.
This particular program succeeds because the @pythoninline{append} method
 is dynamically typed, but the general issue is that Reticulated supports
 only tag-level compositional reasoning.
A programmer cannot trust the types beyond their top-level constructor.

@figure["fig:retic-types"
        @elem{Selected types (@${\tau}) and type tags (@${\kappa})}
        #:style left-figure-style @exact|{
  $\begin{array}{l l l}
    \tau & \Coloneqq & \tint \mid
               \tlist{\tau} \mid
               \tfunction{\tau}{\tau} \mid
               \tdyn \\
    \kappa & \Coloneqq & \kint \mid
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

@figure["fig:magic" "A strange but well-typed function"
@python|{
    def make_ints()->List(Int):
      xs = []
      xs.append("NaN")
      xs.append([])
      xs.append(make_ints)
      return xs

    make_ints() # returns ["NaN", [], <function>]
}|]


Nevertheless, tag soundness is a useful guarantee in the context of Reticulated.
Reticulated's main design goal is to provide seamless interaction with
 the Python 3 runtime and libraries.
To quote the vision paper of @citet[svcb-snapl-2015]:
 @nested[#:style 'inset @emph{
    [P]rogrammers should
    be able to add or remove type annotations without any unexpected impacts on
    their program, such as whether it still typechecks and whether its runtime
    behavior remains the same.}]@;
Consequently, Reticulated cannot implement a standard form of type soundness.
There are two fundamental reasons why Reticulated must aim for a different guarantee.

First, any interaction between Reticulated code and Python code can potentially
 cause a dynamic type error.
There are two reasons for this.
On one hand, the Reticulated type annotation might not match the behaviors implemented
 by the Python code.
On the other hand, the Python code might contain a bug.
These impedance mismatches cannot be caught without a static analysis of the
 Python code, and so the fourth clause of tag soundness states that evaluation
 may end in a dynamic typing error.

Second, Python code may inspect the representation of values.
Reticulated must therefore ensure that a value from statically-typed code is
 indistinguishable from a Python value.
The only way to meet this criterion is to use the same value in both
 cases.@note{Other gradually-typed languages use proxies to approximate
  indistinguishability@~cite[thf-popl-2008 wmwz-ecoop-2017].
  This approach typically fails when values are serialized or sent across a foreign function interface (FFI).}
In particular, a Reticulated list must be indistinguishable from a Python list.
This indistinguishability constraint explains why it is difficult for
 Reticulated to predict the run-time type of a value.

Reticulated chooses to implement tag soundness instead of some
 other compromise because of a secondary design goal:
 @emph{all dynamic type checks run in near-constant time}.@note{This goal is implicit in the implementation of Reticulated@~cite[vss-popl-2017].}
Instead of checking the type of values within a data structure, Reticulated
 stops at the structure's outermost tag.
Hence list types require an @${\Theta(1)} tag check and structural object types
 with @${f} fields require a @${\Theta(f)} check that the given value binds
 the proper fields.
Intuitively, such checks should impose little overhead no matter how a programmer
 adds type annotations.

