#lang gm-dls-2017
@title[#:tag "sec:reticulated"]{Gradual Typing}

Reticulated Python is a gradual typing system by Vitousek et al. for
Python 3. In Reticulated, programmers can express types according to
PEP 484 @note{@url{https://www.python.org/dev/peps/pep-0484/}}.
Reticulated outputs a Python program with checks and
casts that aim to guarantee type soundness.
 In general, soundness means that if a program is well-typed, one of
three outcomes occurs@~cite[tfffgksst-snapl-2017]: the program
terminates with the expected type, fails to terminate, or throws an
exception from a well-defined set. For partially typed programs,
however, there is a fourth outcome addressing the interaction between
the typed and untyped parts of the code. The program can throw an
exception due to one of the boundaries between the typed and untyped
code. Reticulated enforces the first three statements by statically
checking the fully typed parts of the programs, and the fourth
statement by inserting runtime checks into various parts of the
program.

Consider the following class definition in Reticulated:

@python|{
import math

@fields({'dollars': Int, 'cents':Int})
class Cash:
  def __init__(self:Cash, d:Int, c:Int):
    self.dollars = d
    self.cents = c

  def add_cash(self:Cash, other:Cash):
    self.dollars += other.dollars
    self.cents += other.cents

c1 = Cash(1000, 0)
}|


If we add the following expression to our fully typed code:
@code{c1.add_cash(20)}, Reticulated terminates with a static type
error because @code{add_cash} is called with an argument of type
@code{int}, while it expects an instance of @code{Cash}.Now
contrast this situation with one where we add a @code{main} function:

@python|{

def main(cash1, cash2):
  cash1.add_cash(cash2)

main(c1,20)
}|

This program is no longer fully typed. Furthermore, the call
@code{main(c1, 20)} does not match the signature of @code{add_cash}
because @code{add_cash} expects @code{other} to be an instance of
@code{Cash}. Normally in Python3, the program would terminate the program
with an attribute error when we try to extract the field
@code{dollars} from the argument of type @code{int}.
Reticulated aims to catch such problems earlier. In particular,
Reticulated inserts the following dynamic checks:
@itemlist[#:style 'ordered
@item{
A check in @code{add_cash}, for each class field
invoked within the function body to verify its type, in case they were
mutated at some point in the program.
}
@item{
A check in @code{add_cash} that verifies that the function
arguments are of the correct type.
}
@item{
A check in @code{add_cash} to verify that the return value is a
@code{Cash}.
}
@item{
A check at the call site @code{main(c1,20)} that verifies that correctness of the
output type of @code{main}.
}]

since @code{20} is not an instance of @code{Cash}, check #2 should
fail and should point the user to the call site
@code{cash1.add_cash(cash2)}.

These checks are only related to @code{add_cash}. Further checks are
inserted for other cases. A full list of sites where checks are
inserted can be found at@~cite[vksb-dls-2014].
