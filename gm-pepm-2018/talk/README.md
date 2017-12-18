On the Cost of Type-Tag Soundness
===

Hello I'm Ben this is Zeinna we're here to talk about the cost of type-tag soundness.
There are 3 things we want to share with you today
 (1) define type-tag soundness
 (2) what mean for soundness to have a cost and
 (3) share what we've learned about the cost of type-tag soundness for gradual tying in Reticulated

To begin lets review classic type soudnness.
There are N ingredients:
 expression language e
 errors \Omega
 reduction relation -->
 types \tau
 typing judgment \vdash
Type soundness is a theorem that connects the typing judgment to the reduction relation.
If can express e well typed then running e has three possible outcomes [[ so many 3's ]]
 either diverges,
 reduces to a well-defined error state,
 or reduces to a well-typed value.
That is type soundness.
This is a useful theorem for two reasons,
 (1) guarantees that reduction never reaches an undefined state and
 (2) "states that the type of the expression predicts the type of value it can reduce to"
That second part enables a kind of compositional reasoning about programs.
Ok so that is soundness, type-tag soundness is similar but weaker.

Again the ingredients include e \Omega --> \tau \vdash,
We add to that a notion of type-tags K, a map from types to tags, and a typing judgment \vdash e : K
The idea is, \vdash v : K decidable in constant time, kind-of canonical forms.
Now the statement of type-tag soundness connects the typing judgment to the reduction relation (same as before) if \vdash e : \tau then either
 evalution diverges,
 reduces to error,
 or reduces to a value with the same type tag as the input
There we are type-tag soundness

Next we need to explain what it means for soundness to have a cost.
Lets start with an example
Suppose the language e includes a function 'read' that gets a value from the outside world.
We'll say read : \forall a . () -> a and give a non-deterministic reduction semantics
 read() -> v where v is any value.
Clearly this typing rule is not sound with respect to the reduction relation.
Can prove \vdash read() : Int x Int but might produce an integer instead of a
 pair value.
We have a problem.
And in general, this is a problem for any kind of expression that interacts
 "with stuff outside the language, any external interface", that receives input
 that is not type-checked.
Could be input from a user, input from another language, or input from the runtime.
"Correct me if I'm wrong byt I think even Haskell and SML have untyped runtime"
We have a type-safe FFI problem.
Possible solutions are to
 (1) do nothing ignore the unsoundness hope for the best
 (2) restrict the outside world so it only produces good values (either by typing it,
     or by other verification)
 (3) widen the type, read : () -> Any, make user check & verify
 (4) automatically check at runtime
If you take solution 4 -- which is what we are interested in -- then you effectively
 add rules to --> to make it a type-safe reduction relation.
In the case of read, the idea is check against the expected type.
Of course the runtime checks have a cost'
This is what we mean by the cost of soundness, it's the cost of running -->t
 relative to --> 
Clearly the cost of (check t v) depends on size of t (and v) and (chck K v) probably
 has lower cost because of \vdash v : K being decidable and all that 
"you get what you pay for"

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
