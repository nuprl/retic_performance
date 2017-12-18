On the Cost of Type-Tag Soundness
===

Ben:
       Hello everyone, our goal today is to share what we have learned about the
        _performance cost_ of type-tag soundness in Reticulated, which is a
        gradual typing system for Python.
       In order to do that, first we'll define type-tag soundness, second we'll
        explain what it means for soundness to have a cost, and third we'll tell
        you about the experiment we conducted and our conclusions.

Zeina:
       To begin, let us review a standard type soundness theorem.
       We say that a typing judgment is sound with respect to a semantics if
        whenever the typing judgment proves that an expression `e` has the
        static type `\tau`, then the evaluation of `e` either: diverges,
        ends in a well-defined error, or ends in a well-typed value.
       This is a useful theorem for two reasons: it guarantees that evaluation
        never reaches an undefined state, and it guarantees that the type of the
        expression matches the type of the value.
       Put another way, in a type-sound language you can use the types to reason
        about the behavior of a program.

       Type-tag soundness is a similar, but weaker theorem.
       A typing judgment is type-tag sound with respect to a semantics, where
        "floor of" is a relation that maps a type to a type tag, if whenever
        `e` has the static type `\tau` the evaluation of `e` either: diverges,
        ends in a valid error, or ends in a value with the same type-tag as `e`
        (according to a type-tagging judgment).

       For example, if the language of types includes integers, pairs, and
        functions, the language of type-tags might include the tags Integer,
        Pair, and Function.
       The idea is that type-tags express first-order properties of values;
        the judgment that checks whether a value matches a type-tag should
        be decidable in near-constant time (`\Theta(\tau)`).

       Of course this is a weaker theorem.
       Next we will explain why you might want such a theorem.

Ben:
       Suppose the language includes a function `read` that prompts the user for
        a value and steps to the new value.
       So `read()` steps to `v`, where `v` is some non-deterministically-chosen
        value.
       I claim that it is not obvious how to give a sound typing rule for `read`.
       One idea is to say `read()` is well-typed in any context because it
        _might_ be well-typed depending on what it steps to, but this is
        clearly unsound.
       We don't know ahead of time what the value will be --- its coming from
        a source that it outside the scope of the static typing judgment.
       For `read`, the source is a programmer.
       Other possible sources are API server, program written in another language,
        the runtime library.
       In general, I call this a "type safe FFI" problem.

       There are essentially two solutions.
       One is to assume that the input is type-correct and trust that this
        assumption holds at runtime.
       This solution makes sense for a runtime library, or source that
        could be formally verified, but not so much for user input.
       A second is to check the input at runtime.
       We think of this as changing the semantics of `read` ... instead of
        the simple rule where `read()` steps directly to `v`, have `read()`
        step to a form that checks the value `check \tau v` and either returns
        `v` or signals an error.
       This second solution provides soundness at the cost of a runtime check;
        when we say "the cost of soundness" we mean the performance cost of
        these "extra" steps that check the type system's assumptions at
        runtime.

       The exact cost of soundness depends on the expected type, the size of
        the value, and the number of values that need to be checked.
       This is difficult to predict.
       But in general, its faster to check type-tags than types.
       This is why type-tag soundness might be useful --- you might be running
        a program where the cost of type soundness is extreme, but the cost
        of type-tag soundness is more reasonable.

Zeina:
       In the paper, we measure the cost of type-tag soundness in Reticulated,
        a gradual typing system for Python.


In this paper we measure the cost of type-tag soundness in Reticulated, a gradual typing system for Python.
The ingredients for Reticulated build on the ingredients for Python.
Python has a syntax, notion of errors, reduction relation,
Reticulated adds types, extends the syntax with optional type annotations,
 and adds a typing judgment.
Reticulated also adds the ingredients for tag soundness and "in essence" adds rules
 to the Python reduction relation to ensure tag soundness.
In fact, Reticualted is a source-to-source compiler from e+ to e that converts the types to runtime checks, but it's the same difference.
Here is a simple example, of a function that computes the distance between 2 points.
If both arguments are typed, Reticulated compiles this source to a Python function that checks the type tags.
If only 1 aragumnet is typed, or if the types include Dyn, then the checks are different.

Now the promise of Reticulated is that a programmer can use any combination of typed and untyped and the program will run.
The combinations will have different costs of soundness.
This leads to our research question: for a program with N configurations what percent of the configurations run with at most Dx overhead?

The method we used to answer this question is adapted from the method presented at POPL 2016
First pick a suite of Reticualted programs and get fully-typed versions ... make completely typed
Second systematically generate 2**N configurations by removing all types from one function or one class.
If 2 functions, then 4 configurations.
If these 2 functions are inside a class definition, then 8 configurations
You'll notice this gradularity is not as fine as the one Reticualted supports, but we believe its representative and also it was small enough that we could exhaustively measure some programs.
Third, we measure.
For programs with less than 23 functions we then measure the running time of each configuration and compare it to Python runing the untyped configuration.
This is important because Retic adds overhead even to untyped programs.
For larger programs we emply simple random sampling, which we hvae reason to believe gives an accurate answer to the same question

After measuring we are ready to answer questions like "what % of configurations hvae at most 5x overhead relative to Python"
We answer this question for a range of overehad values and geta  aCDF where the area under the curve shows the % of deliverable configurations
Thats the results for one benchmark, measured exhaustively
For the sampled data, our answer to the question of "what % ..." takes the form of a confidence inverval.
We are 95% confident that the true proportion is within the interval.
... we can plot a sequence of these intervals and get something that looks like a CDF

Findings!
THe 2 plots we've shown are the results for two benchmarks ... take5 + aes
Plots for 18 more benchmarks are in the paper
Rather than show them all, want to share some general observations.
First, the data typically starts between 1x and 4x
That meas the fastest Retic version is 1-4 times slower than Python
It was never faster, which is counter-intuitive if you expect type-driven optimizations.
Second the highest overhead is within 10x
This is the time for all our benchmarks, the worst-case overhead was 9xxx
So the slowdown is within one order of magnitude
Third, if we plot the overhead of the fully-typed configuration on the x axis we see its one of the slowest configurations
Fourth the gradually-typed configurations fall somewhere between performance is roughly a libear function of the number of type annotations.

All in one sentence, Reticulated's implementation of type-tag soundness seems to add between 1x and 10x overhead.
The overhead increases with the number of type annotations.

- - -

QUESTIONS
===

#### Q. wasn't this obvious? what's the point of the evaluation?

I don't think obvious is the right word.
We're doing science.
Had a prediction, and the data seems to confirm the prediction.

One interesting point we skipped --- 3 benchmarks got faster by adding type annotations.
All three were due to bugs, one was an unsoundness and the others were overlap where Retic and Python check the same thing.
Performance evaluation helped us find those issues.

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
