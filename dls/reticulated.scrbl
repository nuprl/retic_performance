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
class Currency:
  def __init__(self:Currency,
	       dollars:Int,
	       cents:Int)
	       ->Void:
    self.dollars = dollars 
    self.cents = cents
    
  def add_currency(self:Currency,
                   other:Currency)
		   -> Currency:
    d = self.dollars +
        other.dollars
    c = self.cents +
        other.cents
    return Currency(d + int (c / 100),
                    c % 100)
    
c1 = Currency(1000, 0)   
}|


By adding the following call to our code:

@code{c1.add_currency(20)}

Reticulated expectedly terminates with a static type error because
@code{add_currency} is called with an argument of type @code{int},
while it expects a @code{Currency}. However if we consider adding
@code{main} to our program and making a call to that function instead,

@python|{

def main(curr1:Dyn, curr2:Dyn):
  return curr1.add_currency(curr2)

main(c1,20)
}|

we notice that the program is no longer fully typed. Furthermore, the
call @code{main(c1, 20)} causes a violation the signature of @code{add_currency} by
incorrectly passing it an @code{int} instead of a @code{Currency}. To
prevent a runtime type error from occurring when calling @code{main},
Reticulated inserts the following checks into the program:

1- A check in @code{add_currency}, for each class field
invoked within the function body to verify its type, in case they were
mutated at some point in the program.

2- A check in @code{add_currency} that verifies that the function
arguments are of the correct type.

3- A check in @code{add_currency} to verify that the return value is a
@code{currency}.

4- A check at the call site (@code{main})that verifies that correctness of the
output type of @code{main}.


since @code{20} is a @code{Currency}, check #2 should fail
terminating the program before it can fail with a runtime type error.

These checks are only related to @code{add_currency}. Further checks are
inserted when instantiating classes. A full list of sites where checks
are inserted can be found at@~cite[vksb-dls-2014]. While Reticulated
aims to achieve the soundness definition above (because the well-typed
parts of the program do not terminate with a type error due to the
presence of the runtime checks), section 5.x shows that there are
still soundness gaps in the language.