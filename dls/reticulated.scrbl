#lang gm-dls-2017
@title[#:tag "sec:reticulated"]{Gradual Typing}

Reticulated Python a is sound gradual typing system developed by
Vitousek et al. at Indiana University. It is a source-to-source
translator for Python 3. Given a Python program, Reticulated outputs a
Python program with checks and casts that should guarantee the
soundness of the program. In order to discuss how those checks enforce
soundness, we define soundness for partially typed programs.

In general, soundness means that if a program is well-typed, one of
three outcomes will occur@~cite[tfffgksst-snapl-2017]:The program
terminates with the expected type, fail to terminate, or throw an
exception from a well-defined set. For partially typed programs;
however, there is a fourth outcome addressing the interaction between
the typed and untyped parts of the code. The program can throw an
exception at one of the boundaries between the typed and untyped
code. Therefore, Reticulated enforces the soundness definition stated
above by inserting runtime checks into various parts of the program to
prevent it from terminating with a type error at the well-typed
regions.

Consider the following example from Reticulated of a @code{Currency}
class:

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

  def calc_tax(self:Currency) -> Currency:
    amt = .15 *
          (self.dollars +
	   self.cents/100)
    return amt

}|


Here, @code{calc_tax} violates the signature by incorrectly returning
a @code{float} instead of a @code{Currency}. To prevent a runtime type error from occurring when calling @code{calc_tax}, Reticulated inserts the following checks into the program:

1- A check inside the function body, to verify that the class fields invoked within the function are of the correct type, in case they were mutated at some point in the program.

2- A check inside the function body that verifies that the function arguments are of the correct type.

3- A check at the call site that verifies that correctness of the output type of the function.

since @code{amt} is not of type @code{Currency}, check #2 should fail
terminating the program before it can fail with a runtime type error.

These checks are only related to @code{calc_tax}. Further checks are inserted when instantiating classes. A full list of sites where checks are inserted can be found at@~cite[vksb-dls-2014].
While Reticulated aims to achieve the soundness definition
above (because the well-typed parts of the program do not terminate
with a type error due to the presence of the runtime checks), section 5.x shows
that there are still soundness gaps in the language. 
