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
 and why we think tag soundness might be a good "gateway drug" to get JavaScript
 developers to start caring about soundness.


#### Tag Soundness

To introduce type-tag soundness, let's first review type soundness.
A type soundness theorem says:
 if an expression is well-typed, then the evaluation of the expression will
 either end in a well-typed value,
 diverge,
 or end in an error state, where "Error" here represents
 a clearly-defined set of ways that a well-typed program can go wrong.

Type soundness is useful because it provides two guarantees:
 (1) a well-typed program never has undefined behavior,
 and (2) the static type of an expression predicts the type of the value
 that it reduces to.
This second point makes it possible to use types to reason about complex program behaviors.

To move from type soundness to tag soundness, we weaken the first clause.
Instead of returning a well typed value, tag soundness guarantees a well-tagged
 value, where a tag expresses a basic property about the shape of value.
I think of it as, the tag of a type is its top-level type constructor.

The rest of the statement of type-tag soundness is similar:
 a well-typed program might diverge
 and it might end in some kind of acceptable error.

To give an example of the difference between types and tags,
 if an expression is statically typed as a pair of integers,
 type soundness guarantees that the expression can only reduce to
 a pair of integers.
Tag soundness guarantees a pair, but nothing more.
It might be a pair of integers, and it might be any other kind of pair.

Clearly tag soundness is a weaker theorem.
It is less clear why you would want such a theorem.
The reason is performance, to illustrate we need to focus on the reduction
 relation that so far we've glossed over.

Suppose instead of one true reduction relation
 you have two arrows where one is more efficient than the other (so of course the faster one is better),
 and suppose you don't know how to prove type soundness for the efficient
 reduction relation.
In this case tag soundness lets you trade safety for speed.

I should point out that the static type checking for type soundness
 and tag soundness can be the same.
You can use the same static type checker for each;
 moving to tag soundness just affects the quality of runtime errors
 and your ability to use types to reason about behavior.

Next: I want to go into detail about how this scenario can come about.
To do that I need to explain what I mean by the performance cost of soundness.


#### Performance cost of soundness

So the cost I have in mind comes about when a statically typed program interacts,
 at runtime, with some thing that is outside the domain of the static type checker.
Here "e-tau" is a statically typed program
 and the question-mark represents an external source of values.

Gradual typing is a perfect example of this kind of interaction.
A statically typed expression might receive a dynamically typed value at runtime.

But this "outside world" problem is not unique to gradually typed languages,
 it affects almost any language with a notion of type soundness.

For example, if the language includes a function `read` that accepts keyboard input
 from a user, the user acts an un-checked source of data.
Similarly, if the language has a function for de-serializing a value from a file
 or a port, that byte stream is an un-checked source of values.
Another example, of course, is calls through a foreign function interface,
 and this includes calls to the runtime system.
When you invoke a primitive operation, like addition, you're interacting
 with a low-level language and hoping that it returns a well-typed value.

All these examples are instances of the same general problem,
 this "outside world" problem that static typing makes some assumption
 about an external source of values.

There are essentially two solutions to this problem.
One is to trust the outside world, trust that it returns well-typed values.
This makes sense in some special cases.
The alternative is to check the incoming value at runtime.
Instead of assuming the value is type-correct,
 we take some additional reduction steps to check that assumption,
 and either approve the value or halt the program.

These extra steps are the performance cost of soundness.
The cost is the number of reduction steps that the program takes to
 validate static typing assumptions at runtime.

Now I can illustrate my point from earlier about the relative cost of
 types versus tags.
Suppose the program expects a pair of integers, and receives a value from
 an untrusted source.
To check type soundness, we need three steps:
 check that the value is a pair,
 check that the first component is an integer,
 and check that the second component is an integer
To check tag soundness, we need only one step:
 to check that the value is a pair.

That's one example where the cost of tag soundness is lower,
 and depending on the types and data flow in a program, it could add up to
 a big performance difference.


#### Reticulated

In the paper, we measure the cost of tag soundness in Reticulated,
 which is a gradual typing system for Python.

Statically typed code in a Reticulated program can receive input from Python
 code, so Reticulated has an "outside world" problem like we've just discussed.

As a concrete example, here is a typed Reticulated function that computes
 the Manhattan distance from a point to the origin.
If we call this function with a pair of integers, then all goes well and
 it returns an integer.
If we call this function with something that is not a pair,
 then Reticulated raises a tag error before entering the body of the function.
And if we call the function with a pair that contains a string,
 then Reticulated raises a tag error on the line where it tries to extract
 an integer from the pair.

Our method for measuring the cost of soundness in Reticulated is as follows.
First, we start with a Python program and add type annotations to get a
 fully-typed Reticulated program.
This blue rectangle represents one program with 4 type annotations.
Second, we take the fully typed program and generate a powerset of gradually
 typed programs.
We call elements of this set "configurations" of the original program.
Third, we measure performance.
Depending on the number of configurations, we might measure
 performance exhaustively, as shown on the slide,
 or we use simple random sampling to get an approximate measure.
Fourth, we ask you the reader to choose an cutoff for "good performance"
 and compare the overhead relative to Python.
If you are willing to accept a 4x slowdown relative to Python, then
 we count the configurations that meet your requirement.

This box at the top is very important.
We evaluate performance by counting the proportion of configurations that
 run within some overhead.

Here's the method all on one slide:
 fully typed program,
 generate all configurations,
 measure performance exhaustively or by sampling,
 and compare performance to Python.


#### Experiment & Results

Next up, our experiment and results.

We apply the method to 21 Reticulated programs.
The programs in the first two columns come from prior work by Michael Vitousek
 at Indiana University.
The programs in the third column are programs that we added.

To give a sense of size, this table gives `N`, the number of type annotations,
 for each benchmark.
You can see, size ranges from 1 to 79.
Three of these numbers have asterisks, and they correspond to the benchmarks
 that we do not have exhaustive results for --- only sampling data.

For each benchmark that we measure exhaustively,
 we can answer questions like we saw before: what % of configurations in this benchmark
 run with at most 4x overhead relative to Python.
If we ask the same question for different overheads we obtain a histogram,
 and for the paper we build a very dense histogram and plot it as a line.

For each benchmark with sampling data, we can answer a similar question:
 what % of configurations in this benchmark run with at most 4x overhead
 based on R samples of S configurations each.
In this case our answer is a confidence interval.
The shaded area on this bar represents a 95% confidence inverval,
 this one happens to fall between 8% and 10%.
Again we can ask a similar question for other overheads to obtain a histogram,
 and in the paper we plot a dense histogram as a function interval.

Ok.
We've shown two plots so far, and these are results for two benchmarks.
To read plots like these, you want to look for the shaded area,
 a larger shaded area is better.
Ideally the shading starts early on the x-axis, far to the left, meaning some configurations
 run with very low overhead.
If there is a y-intercept, that demonstrates a speedup relative to Python.
Also ideally this monotonically-increasing line quickly reaches the top of
 the y-axis.
Wherever it does, that is the worst-case overhead for the benchmark.

So that's your crash-course on reading the plots you can find in the paper.
Here they all are, and you can see there's a fair amount of shaded area.

Our main conclusions are the following.
First, the worst-case overhead out of all configurations was within 10x.

Now 10x is a fairly large number, but this is very good news compared to
 what we've seen for the cost of type soundness.
Here's a very high level comparison.
On the right, these are the worst-case overheads for tag soundness in Reticulated.
On the left, these are the worst-case overheads for type soundness in Typed Racket.
This is an apples-to-oranges comparison: different programs, different languages,
 and different guarantees, but its also an order-of-magnitude improvement.
That's why we say 10x is good news.

Maybe, an implementation of tag soundness for TypeScript would give programmers
 some kind of soundness at a reasonable overhead.

Second, some bad news, the best-case overhead in Reticulated was between 1x and 4x.
This means that for all ways of gradual typing, moving from Python to
 Reticulated made the program run slower.
Third, "how much slower" appears to be a linear function of the number of
 type annotations.
In fact the fully-typed configuration was among the slowest in all benchmarks.

This raises an open question: whether it is possible to have a more performant
 implementation of tag soundness, ideally one where fully-typed programs
 have very little overhead.

Also in the paper, we compare the sampling method to the exhaustive
 evaluation method.
Here are plots for the six largest benchmarks that we have exhaustive data for,
 in blue.
The orange intervals are based on a linear number of samples,
 and you can see that the intervals give an accurate and precise approximation
 for these benchmarks.

So that's good news, here again are our conclusions
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
