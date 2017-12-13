On the Cost of Type-Tag Soundness
===

Hello, we are Ben and Zeina.
We're here to tell you three things:

1 what is type-tag soundness
2 what does it mean for "soundness" to have a cost
3 share what we've learned about the cost of type-tag soundness for gradual
  typing in the context of Reticulated

- - -

To begin lets review classic type soundness.
The ingredients are a language of expressions `e`, a set of errors `\Omega`,
 a reduction relation `->`, a language of types `\tau`, and a type checking
 judgment `\vdash e : \tau`.
Type soundness of \vdash with respect to `->` is the theorem:
   \vdash e t implies:
    - e diverges
    - e error
    - e v, \vdash v:t

This is useful because (1) no undefined behavior and (2) predicts type of
 result.

Type-tag soundness is a theorem in the same spirit, but weaker.
A few more ingredients, add `K` and `\tagof{\tau}`.
Theorem is similar, but the final clause is weaker:
  ....
  - e v, \vdash v:\tagof{t}

As before< no undefined states.
But the result could be "many things".

With type soundness, if expecting a List(Int) then possible values include
 empty list and lists of any length with any kinds of **integers**.
With tag soundness, if expecting List(Int) can get any kind of list,
 including lists of integers and lists of strings and lists of integers
 and other stuff.

Then again, if expecting `Int` and read from such a list, type-tag soundness
 will halt the program.

- - -

That is type soundness and type-tag soundness.
Now lets talk about costs, what it means for soundness to have a cost.

For a "given" set of "ingredients" it may not be possible to prove
 soundness, may not be able to show `\vdash e : \tau` is sound WRT to the runtime.
May need to add some kind of cost.

As a specific instance of the general problem, suppose we have a function
 read that gets input from a user.
Type signature `read : \forall A . () -> A`
Clearly unsound.
Can prove `\vdash read() : IntxInt`
 but evaluate to `5` or something.

In general, the problem is dealing with values from an "untyped" source.
The source isn't checked against the expected type --- source could be users,
 FFI, or the language runtime.

General solutions are:
- do nothing, hope for the best
- restrict the source, guarantee "good" inputs
- widen the expected type, push type-checking burden on programmer (Abadi Cardelli Pierce Plotkin)
- check value against type at runtime

Last solution is the one we care about ... also the others are basically "runtime check"
 anyway.

So this is what we mean by cost of soundness, it's the cost of changing `->`
 to include extra checking steps.

- - -

Reticulated ...  in this paper we measure the cost of type-tag soundness in Reticulated.
Reticulated is a gradual typing system for Python (cite)
What this means is, starts with Python, adds types, extends syntax, adds type checker.

Effectively extends Python runtime, but does so indirectly as source-to-source
 translator.
This is a very good idea, we can defend it offline.
Compiles typed syntax to Python syntax with checks to enforce type-tag soundness.

As example, here is type-annotated program and its compiled result.
The checks in this example are (1) access (2) addition (3) return (4) input.
No check on writes.

If the prorgammers uses different type annotations then the program will have
 exponentially many different type-tag checks.
Obviously these checks add a cost to a running program, cost depends on the annotations.

Research question: given a fully-typed program, what % of all configurations
 have at most Dx performance overhead?

- - -

Method adapted from Takikawa (cite).
Three important details:
 1. function * class-fields
 2. baseline is Python
 3. simple random sampling

small programs from the literature

- - -

one result, all configs one benchmark one D

full results from 1 to 10 D

Findings ... N% are D-deliverable

What does this mean
- compare to TR
- examples, will programmers accept this?
- blame
- Pyret

Arguments:
1. huge step backwards from type-soundness, this is ridiculous, no compositional reasoning
2. better than unsound! can enable soundness for debugging


- - -

linear slowdown?
