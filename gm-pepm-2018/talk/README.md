On the Cost of Type-Tag Soundness
===

#### Intro

Hello everyone.
Right, so the title of our paper is "On the Cost of Type-Tag Soundness",
 and the plan for this talk is to go in reverse-order of the title.
First I'll define type-tag soundness,
 then I'll explain what it means for soundness to have a cost,
 and finally I'll share what we learned about the cost of type-tag
 soundness in Reticulated, which is a gradual typing system for Python,
 and why we think tag soundness might be a good "gateway drug" to get TypeScript
 developers to start caring about soundness.


#### Tag Soundness

To introduce type-tag soundness, let's first review type soundness.
A type soundness theorem usually reads like the following:
 if an expression is well-typed, then the evaluation of the expression will
 either end in a well-typed value,
 diverge,
 or end in an error state, where "Error" is a clearly-defined set of ways that
 a well-typed program can go wrong.

This is a useful theorem for two reasons:
 (1) a well-typed program never exhibits undefined behavior,
 and (2) the type of an expression predicts the type of the value.

To move from type soundness to tag soundness, we weaken the first clause.
Instead of returning a well typed value, tag soundness guarantees a well-tagged
 value, where a tag is basically the top-level type constructor of a type.

Otherwise, the statement of type-tag soundness is similar:
 a well-typed program might diverge
 and it might end in some kind of error.

That's the main idea behind tag soundness.
To give an example of the difference,
 if an expression is statically typed as a pair of integers,
 type soundness guarantees that the expression can only reduce to
 a pair of integers.
Tag soundness guarantees a pair, but nothing more.
It might be a pair of integers, and it might be any other kind of pair.

Clearly tag soundness is a weaker theorem.
It is less clear why you would want such a theorem, especially given a choice
 between type soundness and tag soundness.
The reason is performance, it lies in the choice of reduction relation.         ANIMATION
You might have a very efficient reduction relation for which you can prove      SLIDE
 tag soundness, but not type soundness.

In other words, the performance cost of tag soundness is lower.
Lets go into detail.


#### Cost of soundness

So the cost I have in mind comes about when a statically typed program interacts,
 at runtime, with some thing that is outside the domain of the static type checker.

Gradual typing is a perfect example:
 you often have the case where a statically typed expression receives a
 dynamically typed value as input.

But this "outside world" problem comes up in many statically typed languages.

For example, if the language includes a function `read` that accepts keyboard input
 from a user, the user acts an un-checked source of data.
Similarly, if we deserialize a value from a file or a port, that's another
 un-checked source of data.
Another example, of course, is calls through a foreign function interface,
 and also calls to the runtime system fall under this category.
When you invoke a primitive operation, like addition, you're interacting
 with a low-level language and hoping that it returns a well-typed value.

All these examples are instances of the same general problem,
 this "outside world" problem that static typing makes some assumption
 that may not hold at runtime.

There are essentially two solutions to this problem.
One is to trust the outside world, trust that it returns well-typed values.
This makes sense in some special cases.
The alternative is to check the incoming value at runtime.
Instaed of assuming the value is type-correct,
 we take some additional reduction steps to check that assumption,
 and either approve the value or halt the program.

These extra steps, the black arrows on the slide, are the performance
 cost of soundness.
The cost is the number of reduction steps that the program takes to
 validate the static typing assumptions.

At this point I can give an example comparing type soundness and tag            SLIDE
 soundness.
Suppose the program expects a pair of integers, and receives some value.
To check type soundness, we need three steps:
 check that the value is a pair, and check that its components are integers.
To check tag soundness, we need only one step,
 to check that the value is a pair.

That's one example, depending on the types and the program, it might add up
 to a big difference.


#### Reticulated

In the paper, we measure the cost of tag soundness in Reticulated,
 which is a gradual typing system for Python.

Our method for measuring performance is as follows.
First, we start with a Python program and add type annotations to get a
 fully-typed Reticulated program.
This blue rectangle represents one program with 4 type annotations.
Second, we take the fully typed program and generate all gradually typed
 configurations.
Third, we measure performance.
Depending on the size of this set of configurations, we either measure
 performance of every configuration, or we use simple random sampling and
 look at a linear number of configurations, more on that in a minute.
Fourth, we compare performance to Python --- which is the performance a programmer
 would get with no gradual typing at all --- and report the overhead.
Specifically we ask you the reader to decide what overhead you think is acceptable,
 and we count the configurations that run with at most that overhead.

Here's the method all on one slide:
 fully typed program,
 generate all configurations,
 measure performance exhaustively or by sampling,
 and compare performance to Python.


#### Experiment & Results

Finally, lets talk about the experiment and results.

We apply the method to 21 reticulated programs.
Most programs are from prior work on Reticulated; four programs are our own.

To give a sense of size, this table gives `N` for each benchmark.
That is, the number of type annotations.
You can see, they range from 1 to 79.
Three of these numbers have asterisks, and they correspond to the benchmarks
 that we do not have exhaustive results for --- only sampling data.

For each benchmark that we measure exhaustively,
 we can answer questions like: what % of configurations in this benchmark
 run with at most 4x overhead relative to Python.
If we ask the same question for different overheads we obtain a histogram,
 and for the paper we build a very dense histogram and plot it as a line.

For each benchmark with sampling data, we can answer a similar question:
 what % of configurations in this benchmark run with at most 4x overhead
 based on R samples of S configurations each.
In this case our answer is a confidence interval.
The shaded area on this bar represents a 95% confidence inverval
 between 8% and 10%.
Again we can ask a similar question for other overheads to obtain a histogram,
 and in the paper we plot a dense histogram as a function interval.

Ok.
We've shown two plots so far, and these are results for two benchmarks.
The high-level takeaway from these figures is that a large shaded area
 is better.
Ideally the shading starts early on the x-axis, meaning some configurations
 run with very low overhead.
And ideally this monotonically-increasing line quickly reaches the top of
 the y-axis.
Wherever it does, that is the worst-case overhead for the benchmark.

So that's a crash-course on reading the plots you can find in the paper.
Here they all are, and you can see there's a fair amount of shaded area.
Performance is "good".

Our main conclusions are the following.
First, the worst-case overhead in all our benchmarks was within 10x.
10x is a fairly large number, but this is very good news --- it's an order
 of magnitude improvement over what's been reported for the cost of type
 soundness in Typed Racket.
Second, some bad news, the best-case overhead was between 1x and 4x.
This means that for all ways of gradual typing, moving from Python to
 Reticulated made the program run slower.
Third, "how much slower" appears to be a linear function of the number of
 type annotations.
In fact the fully-typed configuration was among the slowest in all benchmarks.

Also in the paper, we quickly compare the sampling method to the exhaustive
 evaluation method.
Here are plots for the six largest benchmarks that we have exhaustive data for,
 in blue.
We applied the sampling method to these benchmarks and found that the intervals
 based on a linear number of measurements provide an accurate and precise
 approximation to the true data.

So that's good news, here again is the cost of tag soundness,
 and I'm happy to take questions.

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
