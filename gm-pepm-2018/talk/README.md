On the Cost of Type-Tag Soundness
===

Ben:
       Hi everyone.
       I'm Ben, this is Zeina, and our paper is titled _On the Cost of Type-Tag
        Soundness_. (Alt: and we're giving a joint talk)
       In the paper, we describe an experiment where we take 21 programs
        written in Reticulated, which is a gradual typing system for Python,
        and systematically measure the performance cost of soundness in each
        program.
       As the title suggests, Reticulated's soundness is not type soundness
        but rather a weaker property that we call type-tag soundness.
       And so, the plan for this talk is to first define type-tag soundness,
        then explain what it means for soundness to have a performance cost,
        and then share some details and conclusions from the experiment.


Zeina:
       To introduce type-tag soundness, let us first review a standard type
        soundness theorem.
       We say that a typing judgment is sound with respect to a reduction semantics if
        whenever the typing judgment proves that an expression `e` has the
        static type `\tau`, then the evaluation of `e` either: diverges,
        ends in a well-defined error, or ends in a well-typed value.
       This is a useful theorem for two reasons: it guarantees that evaluation
        never reaches an undefined state, and it guarantees that the type of the
        expression predicts the type of the value.
       Put another way, in a type-sound language you can use the types to reason
        about the behavior of a program.

       Type-tag soundness is a similar, but weaker theorem.
       A typing judgment is type-tag sound with respect to a semantics if whenever
        `e` has the static type `\tau`, the evaluation of `e` either: diverges,
        ends in a valid error, or ends in a value with the same type-tag as `e`.
       This last clause uses a map "floorof" from types to type-tags, and
        a "tagging" judgment analogous to the typing judgment.

       For example, if the language of types includes integers, pairs, and
        functions, then the language of type-tags might include the tags Integer,
        Pair, and Function.
       The idea is that type-tags express first-order properties of values.
       And the judgment that checks whether a value matches a type-tag should
        be decidable in near-constant time.

       Type-tag soundness guarantees that evaluation does not reach an undefined
        state, just like type soundness, but only weakly predicts the type of
        the value if evaluation terminates successfully.
       So whereas type soundness supports compositional reasoning, type tag
        soundness does not.


Ben:
       Now that we've seen type-tag soundness, let's say what it means for
        soundness to have a performance cost.
       The cost we have in mind "comes into play" when a type-correct program
        interacts with the outside world, with a source of values that is not
        necessarily type checked.

       One kind of source is user input ... a program might ask the program
        for an integer, and then get some kind of value in return --- maybe not
        an integer.
       Another, similar source is a serialize/deserialize API,
        in which you can write a value to a file in some compact format, and
        later read it back in at the same type (needs illustration on slide).
       A foreign function interface is a third kind of external source,
        and a special case of that is interactions with a runtime system through
        primops, such as arithmetic functions.

       These interactions pose a type soundness problem, which I like to call
        the "type safe FFI" problem.
       What can we do to safely and efficiently interact with values that don't
        come with a proof of type-correctness.

       There are essentially two solutions to the problem.
       One is to assume that the input is type-correct and trust that this
        assumption holds at runtime.
       This solution makes sense for a runtime library, or source that
        could be formally verified.
       Not so much for user input.
       A second is to check the input at runtime.
       We think of this as changing the semantics.
       Take `deserialize` for example,
        the standard "unsafe" deserialize steps to a non-deterministic value.
       A "safe" deserialize could take one step to a form that checks the
        deserialized value against the expected type.
       Checking will take further steps, and eventually return the value or an
        error.
       This second solution provides soundness at the cost of a runtime check.
       This is what we mean by the cost of type-tag soundness:
        the performance cost of these "extra" steps that check the type
        system's assumptions at runtime.

       Since we have a cost, the question is, how much?
       This is difficult to predict; it depends on the size of the value,
        size of the type, and number of values that need to be checked.

       (For example with size, to check the type `List(Int)` need to check every element of the list.)

       But in general, its faster to check type-tags than types.
       This is why type-tag soundness might be useful --- you might be running
        a program where the cost of type soundness is extreme, but the cost
        of type-tag soundness is more reasonable.


Zeina:
       Back to the paper.
       Reticulated is a gradual typing system for Python.
       A Reticulated program is a Python program with optional type annotations.
       Type-annotated parts of the program are type-checked,
        and their interactions with un-annotated parts poses a "type-safe FFI"
        problem.

       For example, this function that computes the distance between two cartesian
        coordinates.
       Reticulated statically checks the type annotations, then compiles the types
        to runtime tag checks.
       These checks solve the "FFI problem" at the level of type-tags.
       No matter what input this
        `distance` function receives, it will never segfault or give undefined
        behavior.

       The promise of Reticulated is that a programmer can use any combination
        of typed and untyped and the program will run.
       Our research question is how fast these configurations run relative to
        the untyped Python program; more precisely, for a program with N
        possible typed/untyped configurations, we ask what proportion of
        configurations run with at most Dx overhead.

       The method we use to answer this question is adapted from the method
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
      For programs with less than `2**22` configurations, we measure each
       configuration.
      For larger programs we use simple random sampling to approximate the
       performance --- the paper explains why we believe sampling gives a useful
       approximation.

Ben:
      After measuring, we are ready to answer questions like "what proportion
       of configurations have at most 5x overhead relative to Python".
      For the smaller benchmarks, we give a precise answer to this question.
      For the larger benchmarks, we give a confidence interval; here, the plot
       says we are 95% sure that the true proportion of "5-deliverable"
       configurations is between A% and B%.
      Then we plot a sequence of answers by varying the overhead along an
       x-axis and plotting a CDF.
      A large area under the curve means that a large proportion of
       configurations run with low overhead. (Say the ideal?)

      These plots give the results for two benchmarks.
      In the paper we have results for 21 benchmarks total; the results are
       encouraging ... in fact these 2 plots are "typical" examples.
      I want to share our high-level conclusions.

      First, the largest overhead we observed is under 10x; for any combination
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


#### Q. didn't Vitousek POPL 2017 evaluate Reticulated

they did not measure the performance of partially-typed programs

#### Q. Do you have data for the linear increase

Yes of course here are the graphs

#### Q. why not get the correlation, compute an R^2

no reason, I don't see who that helps besides people who don't want to read the plots


#### Q. tag soundness sounds horrible, lose type-based reasoning

Agree completely.
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
