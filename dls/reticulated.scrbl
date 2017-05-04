#lang gm-dls-2017
@title[#:tag "sec:reticulated"]{Gradual Typing}


Gradual typing enables programmers to incrementally add sound types to
their programs.

In order to understand the soundness guarantees gradual typing
provides, we must
define soundness for partially typed programs.
In general, soundness
means that if a program is well-typed, one of the following outcomes
will occur@~cite[tfffgksst-snapl-2017]:

1- The program terminates with the expected type.

2- The execution diverges.

3- The program throws an exception from a well-defined set.

For partially typed programs however, we need an extra statement
addressing the interaction between the typed and untyped parts of the
code:

4- The program throws an exception at one of the boundaries between the
typed and untyped code.


Reticulated Python a is sound gradual typing system developed by
Vitousek et al. at Indiana University.

Reticulated enforces the soundness definition stated above by
inserting runtime checks into various parts of the program to prevent
it from terminating with a type error at the well-typed regions.

Consider the following example from Reticulated of a @code{Point}
class:

@python|{ import math

@fields({'x': Float, 'y':Float})
class Point:
  def __init__(self:Point,
               x:Float,
	       y:Float)
               ->Void:
    self.x = x self.y = y
  def distance(self:Point,
               other:Point)
               ->Float:
     dx = self.x - other.x
     dy = self.y - other.y
     return math.sqrt(dx**2 + dy**2)

  def wrong(p): p.x = str(p.x)
  
p1 = Point(1, 2) p2 = Point(3, 4)
wrong(p1)
dist = p1.distance(p2) }|


Here, @code{wrong} violates the class's types by incorrectly mutating
the @code{x} field of @code{Point} with a string value.

To prevent a runtime type error from occurring when calling the
@code{distance} function, Reticulated inserts checks at the places
where fields x and y are invoked besides the checks which ensure that
@code{p1} and @code{p2} are @code{Point} classes with members x and y
and checking that the function returns a @code{float}



since @code{self.x} is not a @code{float}, that check should fail
terminating the program before the operation occurs and before the
program can terminate with a type error.

A full list of sites where checks are inserted can be found at
@~cite[vksb-dls-2014] but they are generally inserted at entries to
function bodies as we showed above, inside for loops and use-sites of
variables with non-base types.

In that sense, Reticulated Python adheres to the soundness definition
above because the well-typed parts of the program do not terminate
with a type-error due to the presence of the runtime checks.





