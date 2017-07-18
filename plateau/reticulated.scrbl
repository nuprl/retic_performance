#lang gm-plateau-2017
@title[#:tag "sec:reticulated"]{Reticulated Python}

Reticulated is a gradual typing system for
Python@~cite[vksb-dls-2014].
In Reticulated, programmers can express types using Python's syntax for
 @hyperlink["https://www.python.org/dev/peps/pep-3107/"]{function annotations} and
 @hyperlink["https://www.python.org/dev/peps/pep-0318/"]{decorators}.
Reticulated statically checks the annotations and
 translates them to run-time type checks designed to enforce type soundness.

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
