On the Cost of Type-Tag Soundness
===

Ben:
[00]   Hi everyone.
       I'm Ben, this is Zeina, and our paper is titled _On the Cost of Type-Tag
        Soundness_. (Alt: and we're giving a joint talk)
       In the paper, we describe an experiment where we take 21 programs
        written in Reticulated, which is a gradual typing system for Python,
        and systematically measure the performance cost of soundness in each
        program.
       As the title suggests, Reticulated's soundness is not type soundness
        but rather a weaker property that we call type-tag soundness.
[01]   And so, the plan for this talk is to first define type-tag soundness,
        then explain what it means for soundness to have a performance cost,
        and then share some details and conclusions from the experiment.


Zeina:
[02]   To introduce type-tag soundness, let us first review a standard type
        soundness theorem.
       We say that a typing judgment is sound with respect to a reduction semantics if
        whenever the typing judgment proves that an expression `e` has the
        static type `\tau`, then the evaluation of `e` either:
        steps to a well-typed value,
        steps to a well-defined error,
        or diverges.
       This is a useful theorem for two reasons:
[03]    it guarantees that evaluation never reaches an undefined state,
        and it guarantees that the type of the expression predicts the type of the value.
       Put another way, in a type-sound language you can use the types to reason
        about the behavior of a program.

       Type-tag soundness is a similar, but weaker theorem.
[04]   A typing judgment is type-tag sound with respect to a semantics if whenever
        `e` has the static type `\tau`, the evaluation of `e` either:
         steps to a value with the same type-tag as `e`,
         steps to a valid error,
         or diverges.
       In this theorem statement we use two auxiliary notions:
        a map "floorof" from types to type-tags, and
        a judgment that decides if a value matches, or models, a type-tag.

[05]   For example, if the language of types includes integers, pairs, and
        functions, then the language of type-tags might include the tags Integer,
        Pair, and Function.
       The idea is that type-tags express first-order properties of values.
       And the judgment that checks whether a value matches a type-tag should
        be decidable in near-constant time.

[06]   So that is type-tags, and here again is type-tag soundness.

[07]   Type-tag soundness guarantees that
        evaluation does not reach an undefined state, just like type soundness,
        but only predicts the type-tag of the value.
       So whereas type soundness supports compositional type-based reasoning,
        type tag soundness is only compositional at a superficial level.
       Compared to type soundness this is a much weaker guarantee,
        but notice that it may be easier to prove for certain typing systems
        and reduction semantics.


Ben:
[08]   Now that we've seen type-tag soundness, let's say what it means for
        soundness to have a performance cost.
       The cost we have in mind comes about when a well-typed program
        interacts with the outside world; more precisely, with a source of
        values that may not be type correct.

       [[ This never happens in the lambda calculus, but happens all the time
        in a useful programming language. ]]

[09]   For example, one kind of unreliable source is user input.
       A program might ask the user for an integer, and then get some kind of
        value in return --- maybe not an integer.
[10]   Another, similar source is a serialize/deserialize API,
        in which you can write a value to a file in some compact format, and
        later read it back in at the same type.
       I like this example because it reminds me of OCaml's marshalling API,
        which uses polymorphic types for convenience and comes with a warning
        that deserialization is not type safe.
[11]   A foreign function interface is a third kind of external source,
[12]    and a special case of that is interactions with a runtime system through
        primops, such as arithmetic functions.

[13]   These interactions pose a type soundness problem, which I like to call
        the "type safe FFI" problem.
       What can we do to safely, conveniently, and efficiently interact with
        values that don't come with a proof of type-correctness.

[14]   There are essentially two solutions to the problem.
       One is to assume that the input is type-correct and trust that this
        assumption holds at runtime; add to the trusted computing base.
       This solution makes sense for a runtime library, or source that
        could be formally verified.
       Not so much for user input.
       A second is to check the input at runtime.
       This second solution provides soundness at the cost of a runtime check.
       And this is what we mean by the cost of type-tag soundness:
        assuming you take solution 2, it's
        the performance cost of these "extra" steps that check the type
        system's assumptions at runtime.
       We think of this as changing the semantics.

[15]   As a concrete example, suppose we have a call to `deserialize` that
        expects an integer.
       A safe deserialize function will read the value from the outside world
        and then check that it's actually an integer.
       So there is one extra step to ensure type soundness.

[16]   If the expected type is more complex, for instance a list of integers,
        then the check to ensure type soundness will be more expensive.
       Naturally the question arises how expensive these checks are in
        your "average" program.

[17]   The same question arises for tag soundness, and we can hypothesize that
        it should be much less costly to enforce.


Zeina:
[18]   Back to the paper, we ask "what is the cost of type-tag soundness in Reticulated?"

[19]   Reticulated is a gradual typing system for Python.
       A Reticulated program is a Python program with optional type annotations,
        as the function on the slide demonstrates.
       Type-annotated parts of the program are type-checked,
        in this case, the body of this "Manhattan distance" function is
        statically type-checked.
       Typed and untyped code can interact, and these interactions pose a
        "type-safe FFI" problem as Ben just described.
[20]   Python code can invoke the `distance` function with any kind of arguments.
       To solve the problem, Reticulated checks that the arguments are type-tag correct
        at run-time.
[21]   Similarly, Reticulated checks the reads from the first and second component
        of each pair --- again to preserve tag soundness.

       That explains how this program works with one set of type annotations.
[22]   The promise of Reticulated is that a programmer can use any combination
        of typed and untyped and the program will run.
       For the distance function, that means we can remove the return type,
        remove the argument type,
        or remove both types.

[23]   There are 4 possibilities in total; we like to think of these as a lattice.
       In a larger program, there are exponentially more possibilities.

[24]   Our research question is how fast these configurations run relative to
        the untyped Python program; more precisely, for a program with N
        possible typed/untyped configurations, we ask what proportion of
        configurations run with at most D times slower than Python.

[25]   The method we use to answer this question is adapted from the method
        presented at POPL 2016 for Typed Racket.
       Starting from a fully-annotated program, we systematically generate
        `2**N` configurations by toggling the types on each function and class
        declaration.
       For example if the program has 2 functions, there are 4 configurations.
       If the program has 2 functions within one class, there are 8
        configurations because each method can be typed and the class's fields
        can be typed.

       Note: in principle we could get `2**8` configurations from this
        program by toggling each function parameter, function return type,
        and individual class field.
       We picked the coarser granularity to make the evaluation tractable.
       (Sampling experiment coming up)

      Second, we measure the performance.
      For programs with less than `2**17` configurations, we measure each
       configuration.
[26]  For larger programs we use simple random sampling to approximate the
       performance --- the paper explains why we believe sampling gives a useful
       approximation.

Ben:
[27]  After measuring, we are ready to answer questions like "what proportion
       of configurations have at most 5x overhead relative to Python".
      For the smaller benchmarks, we give a precise answer to this question.
      For the larger benchmarks, we give a confidence interval; here, the plot
       says we are 95% sure that the true proportion of "5-deliverable"
       configurations is between A% and B%.
[28]  Then we plot a sequence of answers by varying the overhead along an
       x-axis and plotting a CDF.
      A large area under the curve means that a large proportion of
       configurations run with low overhead. (Say the ideal?)

      These plots give the results for two benchmarks.
      In the paper we have results for 21 benchmarks total; the results are
       encouraging ... in fact these 2 plots are "typical" examples.
      I want to share our high-level conclusions.

[29]  First, the largest overhead we observed is under 10x; for any combination
       of typed and untyped, the worst-case performance is within one order
       of magnitude.
      This is far from perfect, but much better than the cost of type soundness
       in Typed Racket where 1 order of magnitude was typical, and on the low end.
      (On a more sober note)
      Second, the lowest overhead in each benchmark was between 1x and 4x
       --- Reticulated is always slower than Python, even with zero type annotations.
      Third, we found that the fully-typed configuration was normally one of
       the slowest.
      In fact, the performance overhead we observed, across the board, is
       roughly a linear function of the number of type annotations.

      All in one sentence, Reticulated's implementation of type-tag soundness
       appears to cost between 1x to 10x performance overhead.
      The overhead increases with the number of type annotations.

      With that, we can take questions.

- - -

QUESTIONS + ANSWERS
===

#### Q. wasn't this obvious? what's the point of the evaluation?

I don't think obvious is the right word.
We're doing science.
Had a prediction, and the data seems to confirm the prediction.

One interesting point we skipped --- 3 benchmarks got faster by adding type annotations.
All three were due to bugs, one was an unsoundness and the others were overlap where Retic and Python check the same thing.
Performance evaluation helped us find those issues.

This is science, not enlightened prediction.


#### Q. didn't Vitousek POPL 2017 evaluate Reticulated

they did not measure the performance of partially-typed programs


#### Q. Do you have data for the linear increase

Yes of course here are the graphs


#### Q. why not get the correlation, compute an R^2

Because we don't see how that could be useful, and we're worried it might
 be harmful.
If we show an R**2, there's danger that readers will think it is more precise.

This paper is not really about prediction & extrapolation, just trying to report
 what we saw.


#### Q. tag soundness sounds horrible, lose type-based reasoning

Agreed.
With tags only get top-level compositional reasoning which is basically nothing.
Coming from type soundness tag is really bad.

But coming from no soundness (typescript), tag soudness is a huge improvement.
I hope that with some performance tuning then tag soundness could be pure victory
 for unsound gradual typing, just get more guaratees for "zero" runtime cost.

Note that static checking is the same, the weak interface is just with the outside world


#### Q. where did the benchmarks come from?

The literature on Retic, mostly.
We have the programs from DLS 2014 and POPL 2017.
Four programs that Zeina wrote


#### Q. how many samples on the X-axis?

200


#### Q. how many runs, how ran?

see paper for details,
40 runs, ran on Karst cluster


#### Q. retic has Dyn, why don't you mention that?

it's orthogonal, that's a detail of `\vdash e : \tau`, not really important

Dyn is useful for describing some programs, but it also weakens the static typing
 judgment ... I just don't like implicit coercions
