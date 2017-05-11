#lang gm-dls-2017
@title[#:tag "sec:experience"]{Soundness, Expressiveness, Errors}

@; TODO try just jumping into the examples

The focus of this paper is the performance overhead of gradual typing in
 Reticulated Python.
Performance, however, is just one aspect of a gradual type system.
The system's ability to express common programming idioms
 @; --- especially idioms of the host language but lets not get ahead of ourselves ---
 and the guarantees its types provides are equally important.
Furthermore performance, expressiveness, and soundness are often in conflict.
Adding a new type to the language affects both its soundness proof and its
 performance characteristics.

In this spirit, the following sections comment on the expressiveness, soundness,
 and overall usability of Reticulated.
Recall the three oddities in the evaluation:
@itemlist[
@item{
  the fully-typed configuration in @bm{spectralnorm} runs faster than many configurations;
}
@item{
  some configurations in @bm{call_method} and @bm{call_method_slots} run faster
   with additional type annotations; and
}
@item{
  four benchmarks require the dynamic type.
}
]
These drive the next subsections.

Throughout the paper we have said @emph{Reticulated} as an abbreviation for
 @emph{Reticulated Python, master branch, using the transient semantics}.
Lest remarks in this section be taken out of context, we will say
 Transient, and that is an abbreviation for @emph{the Transient Semantics
 for gradual typing as defined in @citet[vksb-dls-2014] and @citet[vss-popl-2017] and implemented in Reticulated Python master branch}.

@; SORRY prose is bad but lets just scaffoliding


@section{Transient Soundness}

Two functions in the @bm{spectralnorm} benchmark run considerably faster when
 typed.
These functions have the same general shape as this simplified function:

@python|{
  def i_times_u(i_u:(float, List(float)))->float:
    (i, u) = i_u
    total = 0
    for _ in u:
      total = (total + i)
    return total
}|

In other words, both functions accept a tuple as input,
 unpack the tuple outside of a loop, and
 reference the tuple's first component within the loop.
Configurations in which these functions are typed run significantly faster
 because Reticulated compiles them to functions that dynamically check their
 arguments' shape @emph{outside} the loop, and do not dynamically check the
 type of the tuple's first component inside the loop:@note{Run @exec{retic --print file.py} to generate a checked version of @tt{file.py}.}

@python|{
  def i_times_u(i_u):
    check_type_tuple(i_u, 2)
    (i, u) = i_u
    total = 0
    for _ in check_type_list(u):
      total = (total + i)
    return check_type_float(total)
}|

The above function is safe provided its input @tt{i_u} is always a well-typed
 tuple containing a @tt{float} and a @tt{List(float)}.
In general, this assumption is false.
The particular unsoundness is harmless.
If @tt{i_times_u} receives an ill-typed input, it will error.
But as they say, if you mix a barrel of wine and a teaspoon of sewage, you get
 a barrel of sewage.


@subsection{Cost of Unsound Types}
@; TODO
@; - is the same bug in the Big Types calculus?
@; - google for web apps

Many people build web applications with Python.
Many web applications need to deal with currency.
Hence many Python programs need to manipulate values representing real money.
Even brogrammers know not to use floating point numbers to represent money.
They will use integers, and perhaps a compound object like the @tt{Currency}
 object from @section-ref{sec:reticulated}.

Python will not flinch if you attempt to mix integers and floating points, so
 the state of the art is to insert tests and runtime assertions and hope
 nothing goes terribly wrong.
Reticulated has the potential to advance the state of the art.
Its type system can enforce, e.g., that a numeric function only returns integers:

@python|{
  def safe_add(i, j)->Int:
    return i + j

    safe_add(2, 2)     # OK
    safe_add(2, 3.14)  # Runtime error
}|

So far so good, but as @bm{spectralnorm} demonstrates, Reticulated offers
 shallow guarantees for compound objects.

@python|{
  def danger(x)->Currency:
    x.dollars += 0.00001
    return x
}|

The type checker accepts this function, and running it does not yield an error!
The error is delayed until the invalid field is accessed---provided the access
 happens on a type-annotated variable!

@python|{
  c0 = Currency(0, 0)
  c1 = danger(c0)

  def unsafe_ref(x)->Float:
    return x.dollars

  print(unsafe_ref(c1))
  # prints 3.14
}|

General lesson is that Transient types are not guarantees about values,
 they are guarantees about variables and last precisely as long as the variable
 remains in scope.

@section{Transient Error Message}

The @bm{call_method} and @bm{call_method_slots} benchmarks test the performance
 of method calls.
As such, they contain a few methods that (1) receive an object (2) repeatedly
 call methods on the given object.
These methods run slower when dynamically typed because Reticulated inserts
 a check around each use of the object to ensure it binds the correct method.

In principle, such checks are unnecessary because the Python runtime
 checks each attribute access.
Also in principle, such checks are unimportant; they add very little overhead.
In practice, however, the checks inserted by Reticulated are a serious issue for programmers.

As Felleisen said in his keynote, @bold{errors matter}.
@;@; In 2001, Felleisen used the slogan ``errors matter'' for his POPL
@;@; keynote. He meant that when systems work, everyone is happy, but when
@;@; systems break, developers really want to see high quality error messages. 

Here is some illustrative code:

@python|{
  "hello".unbound_method()
}|

Running in Python gives:

@verbatim|{
Traceback (most recent call last):
  File "attr.py", line 1, in <module>
    "hello".unbound_method()
AttributeError: 'str' object has no attribute 'unbound_method'
}|

Running in Reticulated prints the above message, and additionally:

@verbatim|{
Traceback (most recent call last):
  File "/usr/local/bin/retic", line 6, in <module>
    retic.main()
  File "/home/ben/code/gradual/reticulated/retic/retic.py", line 155, in main
    reticulate(program, prog_args=args.args.split(), flag_sets=args)
  File "/home/ben/code/gradual/reticulated/retic/retic.py", line 107, in reticulate
    utils.handle_runtime_error(exit=True)
  File "/home/ben/code/gradual/reticulated/retic/retic.py", line 102, in reticulate
    _exec(code, __main__.__dict__)
  File "/home/ben/code/gradual/reticulated/retic/exec3/__init__.py", line 2, in _exec
    exec (obj, globs, locs)
  File "attr.py", line 257, in <module>
  File "attr.py", line 8, in check0
retic.transient.CheckError: hello
}|

Errors matter.
@itemlist[
@item{
  The final @tt{CheckError} gives no indication of what went wrong; it is not
   even clear that @tt{hello} refers to a string.
}
@item{
  The stack trace references line numbers in the compiled code, not the source code.
}
]

The programmer needs to scroll up past 13 lines of noise to reach the helpful
 part of the message.

Another example, a typed wrapper around a built-in function:

@python|{
  def safe_sum(nums:List(Int))->Int:
    return sum(nums)
}|

The call @tt{safe_sum(["hello"])} passes the input list to the internal function
 @tt{sum}.
Thankfully @tt{sum} checks its input and throws an error message, but a client
 of @tt{safe_sum} needs to dig into the implementation to find out what's wrong.
The errors do not mirror the API.


@section{Transient Types}

Four benchmarks require the dynamic type because they use types that Reticulated
 cannot express.
@itemlist[
@item{
  @bm{go} contains a tree class, with a list of trees as a field.
  Reticulated produces a massive error message.
}
@item{
  @bm{pystone} has a class with a nullable field.
  @; https://github.com/mvitousek/reticulated/issues/28
  Reticulated has neither nullable types or untagged unions (though the second author worked on such a feature).
}
@item{
  @bm{take5} contains a function with optional arguments.
  When reticulated encounters such functions, it ignores their entire signature.
}
@item{
  @bm{stats} requires untagged union types and polymorphism
  Retic has no apparent syntax for polymorphism.
  (Hard to tell because the grammar is undocumented.)
}
]

@; -----------------------------------------------------------------------------

@;Implementation issues.
@;Small in relation, but hurt the user experience.
@;- import*
@;- set (syntax okay, but runtime error)
@;- cannot import types from other packages
@;  https://github.com/mvitousek/reticulated/issues/31
@;- wrong scope for builtin binary operators (only on RHS)
@;  tested with: + - * / // % **
@;  https://github.com/mvitousek/reticulated/issues/33
@;- calling `check_type_object` on a module
@;  https://github.com/mvitousek/reticulated/issues/34
@;- __init__ ignored
@;  https://github.com/mvitousek/reticulated/issues/35
@;
@;
@;There are @id[NUM-BETTER-WITH-TYPES] configurations that run faster that
@; at least one configuration with fewer typed components.
@;
@; https://blog.codinghorror.com/loose-typing-sinks-ships/
@;
@; The only errors that matter are runtime errors: until you have eliminated
@; those, you don't have a functional app. And those errors tend to be a hell of a
@; lot more subtle than "Oops, I called the .Bark method on a Cat!"
@;
@; Basically the value of compile time checking isn't that great, compared to the
@; overwhelming value of real world testing. That's what all these hardcore Java
@; figures are saying: they used to feel that way, too.. until experience taught
@; them otherwise. Just because your program compiles means basically nothing.
@;
@; Once you factor in the cost (both mental overhead and simple keyboard typing)
@; of all that "checking" in terms of programmer productivity (forced inheritance
@; model to get a .Bark method, cast cast cast) .. it's pretty clear that dynamic
@; typing is superior.
