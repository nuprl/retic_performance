On the Cost of Type-Tag Soundness
===

Ben:
       Hi everyone.
       Our paper is titled _On the Cost of Type-Tag Soundness_.
       We're going to give this as a joint talk.
       The outline is in reverse-order of the title:
        first Zeina will introduce type-tag soundness,
        then I will talk about what it means for soundness to have a cost,
        and then together we'll talk about the cost of type-tag soundness in
        Reticulated.


Zeina:
       To introduce type-tag soundness, let us first review a standard type
        soundness theorem.
       Suppose we have an expression `e` with static type `\tau`,
        then the evaluation of `e` either:
        steps to a well-typed value,
        steps to a well-defined error,
        or diverges.
       This is a useful theorem for two reasons:
        it guarantees that evaluation never reaches an undefined state,
        and it guarantees that the type of the expression predicts the type of the value.
       Therefore in type-sound languages we can use the types to reason about
        the program.

       
       To move from Type soundness to tag soundness, we weaken the first clause. (switch slide)
       
	Instead of returning a well typed value, we return a well tagged value. 

	Now we will define what well-tagged means. 
      Consider this grammar with values integers pairs and functions
        and their corresponding types and tags. 
        
       The idea is that the tags express first-order properties of values.
       So, checking whether a value matches a tag should
        be decidable in near-constant time.
        
        Therefore, tag soundness also guarantees  that
        evaluation does not reach an undefined state but it only predicts the tag of the value.
        
       Suppose we have an expression whose type is a pair of integers. Then type soundness guarantees that e evaluates to a pair with integers components, 
       while tag soundness guarantees that e evaluates to a pair regardless of types of the components. 
        



Ben:
       Now that we've seen type-tag soundness, let's say what it means for
        soundness to have a performance cost.
       The cost we have in mind comes about when a well-typed program
        interacts with the outside world, with a source of
        values that may not be type correct.

       [[ This never happens in the lambda calculus, but happens all the time
        in a useful programming language. ]]

       (TODO fix animations)

       For example, one kind of unreliable source is user input.
       A program might ask the user for an integer, but its impossible to
        predict what the user will actually return.
       Another kind of unreliable source is an API for deserialization.
       A program might write a well-typed value to a file, and later expect
        to deserialize a value with the same type.
       But it's not guaranteed that the file contains the same data.

       A foreign function interface is a third kind of external source,
        where you ask another language to compute a value.
       One special case of this is interactions with a runtime system through
        primitive operations, such as arithmetic functions.
       When you call a function like + you ask a low-level language to compute
        a value; that value may not be well typed.

       These interactions pose a type soundness problem.
       What can we do to safely, conveniently, and efficiently interact with
        values that don't come with a proof of type-correctness.

       There are essentially two solutions to the problem.
       One is to assume that the input is type-correct and trust that this
        assumption holds at runtime; add to the trusted computing base.
       This solution makes sense for a runtime library, or source that
        could be formally verified.
       Not so much for user input.
       A second is to check the input at runtime.
       So this provides soundness at the cost of a runtime check.

       For example if the language is expecting an integer value, there needs
        to be a check that the value is actually an integer.
       For a more complicated example,
        if the language is expecting a pair of integers then we need three checks:
        that the value is a pair,
        and that the first and second component are both integers.

       This is what we mean by the cost of soundness:
        assuming you check external data at run time, it's
        the performance cost of these "extra" steps that check the type
        system's assumptions at runtime.

       [[We think of this as changing the semantics.]]

       The same question arises for tag soundness, and we can hypothesize that
        it should be much less costly to enforce.

       [[ need some transition here ]]


Zeina:
       So our question is, "what is the cost of tag soundness in Reticulated?"

       Reticulated is a gradual typing system for Python that enforces tag soundness. 
       A program in Reticulated is a Python program with optional type annotations,


	This distance function is an example of a fully-annotated reticulated program.	

       Python code can invoke this function with any kind of arguments. To prevent untyped code from violating the types on the distance function,
       At run-time, Reticulated inserts two kinds of checks. First, it checks that the arguments are of type tuple. Second it checks that each read from the tuple are integers. 
   
   So let's see some usages of this function. 
   This usage uses the correct types-- ok
   The first check will fail (not a tuple)
   The second check will fail  because the second component of the tuple is not an integer.

       That explains how this program works with one set of type annotations.
[22]   The promise of Reticulated is that a programmer can use any combination
        of typed and untyped and the program will run.
       For the distance function, that means we can remove the return type,
        remove the argument type,
        or remove both types.

       There are 4 possibilities in total; we like to think of these as a
        set and we call them configurations.
       We have 4 configurations on the slide.

So, for some program we have an exponential number of configurations relative 
to the number of typable components on the program

       Our research question is what proportion of
        these configurations run at most D times slower than Python.

       The method we use to answer this question is adapted from Takikawa et al. for Typed Racket.
       Starting from a fully-annotated program, we systematically generate
        `2**N` configurations 
        
       Then, we measure the performance either by running all configurations in that space or by sampling a linear number of them.
              
       Finally we compare the performance to Python,
        which is what programmers would get without gradual typing.

Ben:
      After measuring, we are ready to answer questions like "what proportion
       of configurations run at most 4 times slower than Python"

      For the smaller benchmarks, we give a precise answer to this question;
       in one of the benchmarks we measured, we found that half the configurations
       had at most 4x overhead.
      If we ask this question for multiple overheads, we get a histogram.
      In the paper we ask for over 200 overheads and draw the histogram as a line.

      This is the kind of plot we use in the paper,
       it considers a range of different overheads that we think a developer
       might accept, and reports the % of configurations that run within that
       overhead.
      [[ awkward but in the ballpark ]]

      For the larger benchmarks, we give an approximate answer to the question:
       with 95% confidence, what proportion of the configurations have at most
       4x overhead based on R samples of S configurations each.
      The shaded area on the bar here represents a 95% confidence interval;
       this one is between 8 and 10 %.

      Again for multiple overheads this generates a histogram, and we plot
       this as a line.

      These plots give the results for two benchmarks.
      In the paper we have results for 21 benchmarks total; the results are
       pretty good.
      These plots are typical results; rather than show all 21 plots I want
       to share our high-level conclusions.

[29]  First, the largest overhead we observed is under 10x; for any combination
       of typed and untyped, the worst-case performance is within one order
       of magnitude.
      This is far from perfect, but much better than the cost of type soundness
       in Typed Racket where 1 order of magnitude was typical,
       and we sometimes found 2 or more.
      So that's good news.
      Some bad news is the second point,
       the lowest overhead in each benchmark was between 1x and 4x.
       Reticulated is always slower than Python, even with zero type annotations.
       Adding types never improves performance.
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


- - -

4 examples, too many, almost forgot what the problem was
(remind what the problem is)
each example should have connection to the problem

how do measurements connect to the problem?
... need a slide for this!!!

compare to typed racket at end, perforamcne (why care about tag soundness)

more time on graphs, curve looks like this, why an S,
 knowing where the spike is, what conclusions from graph
