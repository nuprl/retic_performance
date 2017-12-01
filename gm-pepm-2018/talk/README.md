talk outline 0.0 for PEPM
===

Ben: Hello I am Ben

Zeina: Hello I am Zeina. We're going to talk about type-tag soundness.

Ben: First, some background.

Ben: ... gradual typing dream ... dynamically-typed codebase, add types,
     mixed codebase with typed and untyped code

Ben: great because
     - statically-typed code gets compile-time checks
     - (type soundness) use types to reason about program behavior
       * bonus: compiler can use types to optimize
     - mixed program will "work" just like before

Ben: well not exactly "works", two caveats
     - might error, b/c bug in type annotations or in untyped code
       this is probably a good thing --- help find problems
     - performance cost of extra checks

Ben: so we have a dilemma, type soundness vs. performance

Zeina: take a closer look at Typed Racket, its type soundness promises
       if `e : \tau` then either:
       - e reduces to a value of type `\tau`
       - e diverges
       - e reduces to an OK exception
       - e reduces to a typed/untyped error

Zeina: (a typed/untyped error is something like "expected v to have type `\tau`
       but it doesn't because here's `C[]` where `C[] : \tau'` but `C[v]` doesn't
       give a `\tau'`)

Zeina: the first clause is definitely going to affect performance
       let `f = (\lambda x : \tau . x)` and suppose we call `f` with untyped
       arguments. If `\tau = List[Int]` then need to check every element
       in the untyped list. ... other examples

Zeina: clearly _can_ be expensive, question is how bad in practice

Ben: Takikawa etal gave one answer. Their method:
     - pick some TR programs
     - get all typed/untyped configurations
     - measure overhead relative to Racket (no gradual typing)

Ben: for example ... 2 module program ... right

Ben: they did this for `K` programs. Surprising how slow.
     One question they answered: how many configurations have 10x overhead or less?
     Some, but not many. Another question: how many 100x overhead or less?
     Many, but not all.

Ben: "frequently order-of-magnitude, sometimes 2 or more"

Zeina: we have been measuring Reticulated

Zeina: Retic is gradual typing for Python, its soundness is very different.
       If `e : \tau` then either:
       - e reduces to value with same type-tag
       - e diverges
       - e -> error
       - e -> boundary error

Zeina: here're some example type-tags ... just the top-level type constructor

Zeina: let `f = \lambda x : \tau x` then cost of checking argument is O(1)
       for any type

Zeina: on the other hand, could return argument that doesn't match `\tau`
       so other typed functions need to check reads from data structures

Zeina: ... no monitors? ... subtle performance differences ?

Ben: we applied the Takikawa method to Reticulated. Complications:
     - baseline is Python, not untyped Retic
     - can annotate any function parameter, we do whole functions at once
     - some programs too large, so we do SRS and justify that method empirically

Ben: we grabbed some retic programs from the literature, here are results
     very impressive for 10x
     still pretty good for 2x or 5x

Zeina: where does this leave us?
       have 2 observations ... TR soundness with apparently high cost,
       Retic soundness with far lower cost by this "apples to oranges" comparison

Zeina: this is interesting, wonder if there's other useful soundnesses (or how
       useful the current ones are), wonder about the performance of other
       gradual typing systems

MORE:
  - error messages
  - compositional reasoning
  - linear slowdown
  - retic expressiveness
