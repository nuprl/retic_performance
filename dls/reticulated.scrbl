#lang gm-dls-2017
@title[#:tag "sec:reticulated"]{Gradual Typing}

Reticulated Python a is sound gradual typing system developed by
Vitousek et al. at Indiana University for Python 3. In Reticulated,
programmers can express types in their programs using Python
annotations stated in PEP 484
@note{@url{https://www.python.org/dev/peps/pep-0484/}}.  Given a
Python program, Reticulated outputs a Python program with checks and
casts that should guarantee the soundness of the program. In order to
discuss how those checks enforce soundness, we define soundness for
partially typed programs.

In general, soundness means that if a program is well-typed, one of
three outcomes will occur@~cite[tfffgksst-snapl-2017]:The program
terminates with the expected type, fail to terminate, or throw an
exception from a well-defined set. For partially typed programs;
however, there is a fourth outcome addressing the interaction between
the typed and untyped parts of the code. The program can throw an
exception at one of the boundaries between the typed and untyped
code. Reticulated enforces the first three statements by statically
checking the fully typed parts of the programs, and the fourth
statement by inserting runtime checks into various parts of the
program to prevent it from terminating with a type error at the
well-typed regions.

Consider the following fully typed class definition in Reticulated:

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


By adding the following call to our code:

@code{c1.add_cash(20)}

Reticulated expectedly terminates with a static type error because
@code{add_cash} is called with an argument of type @code{int},
while it expects a @code{Cash}. However if we consider adding
@code{main} to our program and making a call to that function instead,

@python|{

def main(cash1:Dyn, cash2:Dyn):
  cash1.add_cash(cash2)

main(c1,20)
}|

we notice that the program is no longer fully typed. Furthermore, the
call @code{main(c1, 20)} causes a violation the signature of @code{add_cash} by
incorrectly passing it an @code{int} instead of a @code{Cash}. To
prevent a runtime type error from occurring when calling @code{main},
Reticulated inserts the following checks into the program:
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
A check at the call site (@code{main})that verifies that correctness of the
output type of @code{main}.
}]

since @code{20} is a @code{Cash}, check #2 should fail
terminating the program before it can fail with a runtime type error.

These checks are only related to @code{add_cash}. Further checks are
inserted when instantiating classes. A full list of sites where checks
are inserted can be found at@~cite[vksb-dls-2014].
