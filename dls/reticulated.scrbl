#lang gm-dls-2017
@title[#:tag "sec:reticulated"]{Gradual Typing}


Gradual typing does not only enable programmers to incrementally add types to their programs, but also provides soundness guarantees that describe the runtime behavior of a given program.

In order to understand the soundness guarantees Gradual Typing provides, and why they are important for the programmer, we must define soundness for partially typed programs. In general, soundness means that if a program is well-typed, it will never terminate with a type error.

For partially typed programs however, the definition is slightly different. A partially typed program is sound if it terminates with a type error at one of the boundaries between typed and untyped code, but otherwise does not terminate with a type error.

Reticulated enforces that definition by inserting runtime checks into various parts of the program to prevent it from terminating with a type error at the well-typed regions.

Consider the following example from Reticulated of a @code{Point} class:

@python|{
import math

@fields({'x': Float, 'y':Float})
class Point:
  def __init__(self:Point,
  x:Float, y:Float)->Void:
    self.x = x
    self.y = y
    
  def distance(self:Point,
  other:Point)->Float:
    dx = self.x - other.x
    dy = self.y - other.y
    return math.sqrt(dx**2 + dy**2)

def wrong(p):
  p.x = str(p.x)
  
p1 = Point(1, 2)
p2 = Point(3, 4)

wrong(p1)

dist = p1.distance(p2)
}|


Here, @code{wrong} violates the class's types by incorrectly mutating the @code{x} field of @code{Point} with a string value.

To prevent a runtime type error from occurring when calling the @code{distance} function, Reticulated inserts checks at the points where fields x and y are invoked as follows besides the checks which ensure that @code{p1} and @code{p2} are @code{Point} classes with members x and y. Therefore, the distance function is as follows:

@python{
  def distance(self, other):
        check0(self)
        check0(other)
        dx = (check_type_float(self.x) -
	      check_type_float(other.x))
        dy = (check_type_float(self.y) -
	      check_type_float(other.y))
        return check_type_float
	       (check_type_function
	       (check1(math).sqrt)
	       (((dx ** 2) + (dy ** 2))))}


In this case,

@code{check_type_float(self.x)} should fail terminating the program before the operation occurs and before the program can terminate with a type error.

A full list of sites where checks are inserted can be found at @~cite[vksb-dls-2014] but they are generally inserted at entries to function bodies as we showed above, inside for loops and use-sites of variables with non-base types.

In that sense, Reticulated Python adheres to the soundness definition above because the well-typed parts of the program do not terminate with a type-error due to the presence of the runtime checks.





