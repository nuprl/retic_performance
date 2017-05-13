#lang gm-dls-2017
@title[#:tag "sec:experience"]{Future Directions}

Three mysteries uncovered during the evaluation require further attention:
@itemlist[
@item{
  four benchmarks do not have fully-typed configurations;
}
@item{
  both @bm{call_method} and @bm{call_method_slots} have configurations
   that run faster (than untyped) with some type annotations, but slower
   (than untyped) when fully-annotated;
}
@item{
  the @bm{spectralnorm} benchmark has some partially-typed configurations
   that run slower than the fully-typed configuration.
}
]

Incidentally, these three abnormalities suggest three avenues for future work
 on Reticulated.
First, the type system must add support for polymorphism, untagged unions,
 recursive types, and variable-arity functions.
Second, the runtime system must generate @emph{actionable}@~cite[s-thesis-2015] error messages.
Third, Reticlated's notion of type soundness must be clarified and
 investigated further.


@section{Types for Python}
@; TODO steal a samth title?

Four benchmarks use the dynamic type because Reticulated cannot express
 part of their logical structure.
Of course, no type system can accomodate all of the ad-hoc techniques that
 programmers use to assert their programs' correctness.
But the uses of type dynamic in these benchmarks arise from common programming idioms.
In fact, @|PEP-484| specifies a syntax for generics, untagged union types,
 recursive types, optional arguments, and keyword arguments.
Hence there is some awareness within the Python community that a practical
 static type system must accomodate these idioms.


@subsection{Polymorphism}

The @bm{stats} benchmark contains polymorphic functions on lists, e.g.,
 a function that extracts one column from a matrix.
Reticulated has no syntax for polymorphism.


@subsection{Untagged Unions}

@(let ([pystone-union-fields
        @; grep for 'PtrComp = ' to find assignments
        @; It's initially `None`, and assigned away-from and back-to `None`
        @;  in `Proc1`
        '(PSRecord.PtrComp)]
       [stats-union-functions
        @; Most of these functions all have a dead-giveaway pair of lines:
        @; ```
        @;  if type(cols) not in [list,tuple]:
        @;      cols = [cols]
        @; ```
        '(abut simpleabut colex linexand recode)]
      ) @elem{
  The @bm{pystone} and @bm{stats} benchmarks use the dynamic type to implement
   untagged union types.
  Specifically, @integer->word[(length pystone-union-fields)]
   class field in @bm{pystone} may bind either a reference to
   an object or @pythoninline{None}.
  @Integer->word[(length stats-union-functions)]
   functions in @bm{stats} accept either numbers or lists of numbers.
  Furthermore, one of these @bm{stats} functions implements a rank polymorphic
   algorithm@~cite[ssm-esop-2014].
  @; basically need case->,
  @;  but rank polymorphic types might be inspiring to someone

  The second author contributed to an implementation of union types for
   Reticulated during a research assistantship.
  The code is on a development branch of Reticulated.@note{The branch is currently named @hyperlink["https://github.com/mvitousek/reticulated/tree/2.0unions"]{@tt{2.0unions}}.}
})


@subsection{Recursive Types}

The @bm{go} benchmark contains a class representing one square on a game board.
This class declares a field that holds a list of neighboring squares.
Reticulated's syntax allows this recursive field, but its static type checker
 rejects it with a 260-kilobyte error message.
The type checker similarly rejects the following definition of an @${N}-ary tree.

@python|{
@fields({'children': List(Tree)})
class Tree:
  children = []
  def add_child(self:Tree, that:Tree):
    self.children.append(that)
}|


@subsection{Variable-Arity Functions}

Python functions may accept optional arguments, a variable number of positional arguments,
 and/or a variable number of keyword arguments.@note{@url{https://docs.python.org/dev/tutorial/controlflow.html#more-on-defining-functions}}
@; also keyword-only arguments https://www.python.org/dev/peps/pep-3102/
Reticulated supports the Python syntax, but ignores any type annotations on
 such functions.
An open issue on the Reticulated GitHub repository documents this unsoundness.@note{@url{https://github.com/mvitousek/reticulated/issues/32}}


@section{Actionable Error Messages}

Felleisen used the slogan ``errors matter'' for his POPL 2002 keynote@~cite[f-keynote-2002].
He meant that when systems work, everyone is happy, but when systems break,
 developers really want to see high quality error messages.
This desire has motivated a long line research on generating actionable messages
 for static type errors.
 @; TODO cite @~cite[].

A gradually typed language must produce actionable messages for a new class of
 errors---type errors that occur at runtime after an untyped value flows into
 a typed context.
Fortunately, the recipe to generate a useful error message is straightforward.
Such messages must direct programmers to the relevant boundary and supply
 both the untyped value and mis-matched type annotation as witnesses@~cite[tfffgksst-snapl-2017].

Reticulated fails to meet this requirement.
To illustrate, suppose an untyped context passes a string to a typed context
 expecting an integer.
Reticulated simply raises a runtime exception with the relevant value, e.g. @tt{Exception: hello}.
Such messages fortunately come with a stack trace; however:
@itemlist[
@item{
  the top 3 stack frames are part of the Reticulated interpreter, and
}
@item{
  the only trace of the source program's type annotation is the function name
   @tt{check_type_int} on the third-highest stack frame.@note{Not to be confused with the function @tt{check_type_bool} on the second-highest stack frame!}
}
]

@;@figure["fig:add1" "Errors Matter"
@;@python|{
@;  def add1(n:Int):
@;    return n + 1
@;
@;  def dyn_add1(x:Dyn):
@;    return add1(x)
@;
@;  dyn_add1("NaN")
@;  # Exception: NaN
@;}|]

Let us return to the benchmark programs, specifically @bm{call_method} and @bm{call_method_slots}.
These benchmarks are similar; they repeatedly call methods on a given object.
When the benchmarks are fully untyped, Reticulated's semantics dictate
 that every method call is preceded by a runtime check that the receiver binds
 the relevant method.
This check is not required when the receiver is typed, hence the performance
 improvement.

The performance improvement in @bm{call_method} is relevant to this subsection
 on error messages because Python, as a dynamically typed language, performs
 the same check on the receiver object.
What's more, Python gives significantly better error messages.
Consider a simple, errant method call:
@;
@codeblock|{
    "hello".unbound_method()
}| @;
@;
Python reports the relevant object, the relevant line number, and the expected ``type'':
@;
@codeblock|{
    Traceback (most recent call last):
      File "unbound_method.py", line 1, in <module>
        "hello".unbound_method()
    AttributeError: "str" object has no attribute
      "unbound_method"
}| @;
@;
To its credit Reticulated prints this same message, but additionally prints
 a 13-line stack trace and the bottom line:

@codeblock|{
    retic.transient.CheckError: hello
}|

Simply removing Reticulated's runtime check would improve both performance
 and usability.


@section{Clear Guarantees}

A static type system is useful insofar as it provides guarantees.
For example, let @tt{/} be a C-style function that divides machine integers
 such that, e.g., @tt{4/2} evaluates to 2 and @tt{"A"/"Z"} returns an arbitrary
 integer by interpreting the memory addresses of the strings @tt{"A"} and @tt{"Z"}
 as machine integers.
The latter call is an example of a type error.
A traditional static type system rules out such errors by assigning
 @tt{/} the type @${\mathsf{Int} \times \mathsf{Int} \rightarrow \mathsf{Int}}
 and enforcing the invariant that @tt{/} may only be applied to arguments with
 type @${\mathsf{Int}}.
The possibility of a @emph{value error} due to dividing by zero still remains,
 but type errors are impossible, guaranteed.

In general, in a traditional static type system, the type @${\tau \rightarrow \tau'}
 expresses a global invariant.
If @${f} is a function with this type, then the typechecker
 will guarantee that @${f} is never invoked on ill-typed input.
Similarly, if the type @tt{List(Int)} represents a @emph{mutable} list of
 integers, the type checker will ensure that every value written to the list
 has type @tt{Int}.

Reticulated does not provide such guarantees.
For example, suppose @tt{tail} is a typed function that expects a list of strings
 and returns a similar list of strings without the first element.
An untyped caller can invoke @tt{tail} with a list of integers.
Given such input, @tt{tail} will return a list of integers.
Nothing goes wrong.
An untyped caller can furthermore mutate the output of @tt{tail} and write
 any sort of value to the list.
Again, nothing goes wrong.
@Figure-ref{fig:tail} contains an similar program that prints the integer 10
 when run.
Nothing goes wrong.

@figure["fig:tail" "A well-typed Reticulated program"
  @python|{
    def tail(xs:List(String))->List(String):
      return xs[1:]

    def magic(xs):
      return tail(xs)

    ys = magic([4,5,6,7])
    ys[0] = tail
    print(ys[1] * ys[2])
    # 10
}| ]

The only ``magic'' in this example is the fact that some ill-typed programs
 do not commit type errors.
Applying a parametric function like @tt{tail} to any list is safe, no matter
 the type assigned to @tt{tail}.
If @tt{tail} furthermore checked that its argument supported the slice operation,
 then one could apply @tt{tail} to any input without fear of type errors.

Driven by this insight, Reticulated interprets types as @emph{local assumptions}
 rather than @emph{global invariants}.
The typechecker uses type annotations to rewrite partial user-defined functions
 into total functions that check their assumptions just before such assumptions
 become crucial for preventing a type error.
Naturally, this shallow and delayed type check is the secret to Reticulated's
 efficient gradual typing.


@subsection{An Ounce of Sewage}

Recall the @tt{Cash} class from @section-ref{sec:reticulated}.
The class fields @tt{dollar} and @tt{cents} are type annotated, perhaps to
 guard against rounding errors due to floating-point arithmetic.
In a traditional statically typed language, the annotation would be a global
 invariant.
In Reticulated, the field types are enforced only in type-annotated contexts.
A malicious (or naive!) programmer can easily mix in floating point numbers:

@python|{
def cash_me_out(c):
  c.dollars = 4.20
  return c

c1 = cash_me_out(Cash())
print(c1.dollars)
# 4.20
}|

Good programmers will of course annotate all their functions and avoid such mistakes.
@;Good programmers will also respect API boundaries,
@; write thoughtful unit tests,
@; and carefully document their designs.
As for human programmers, they will have to learn to do better.

