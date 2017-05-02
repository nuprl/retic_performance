#lang gm-dls-2017
@title[#:tag "sec:linear"]{Scaling the Evaluation Method}

@; TODO s,t is way way way too general,
@;  should at least bring across we're doing LINEAR sampling,
@;  and why can't you test whether constant-factor works?

@; -----------------------------------------------------------------------------

Linear measurements suffice to approximate the results of an exhaustive
 performance evaluation.
This section presents a modified evaluation method, and provides both
 theoretical and empirical justification of its validity.


@section{Motivation}

The benchmark programs in @section-ref{sec:exhaustive} are rather small.
Any experienced Python programmer could infer type annotations for these
 programs in a matter of hours.
Widely-used Python programs are typically much larger.
For example @TODO{examples}.
@; "jumping" to fully-typed makes even less sense for reticualted,
@;  since number-of-types is a decent predictor of performance
In theory, gradual typing offers important engineering benefits to such projects;
 designers can choose the precise amount of typing that best suits the project
 and developers can run end-to-end tests on the program at each stage of the
 migration.
It is not clear, however, that the resuts of @section-ref{sec:exhaustive} will hold
 for significantly larger programs.


@section{Method}

To approximate the number of @deliverable[] configurations in a configuration
 space @cspace[]:
@itemlist[
@item{
  Choose a confidence level @${L \in [0,1]} for the approximation.
}
@item{
  Define two functions @${s} and @${t} such that @${n_s = s(@cspace[])}
  and @${n_t = t(@cspace[])}
  and both @${n_s} and @${n_t} are small natural numbers.
}
@item{
  Sample @${n_s} configurations from @cspace[] uniformly at random
   and count the proportion of @deliverable[] configurations in the sample.
}
@item{
  Repeat the previous step @${n_t} times to compute a sequence of
   proportions @$|{y_0 \ldots y_{n_t - 1}}|.
}
@item{
  Report the @${L}% confidence interval determined by the sample proportions.
}
]

@bold{Definition} a @approximation["s" "t" "P"] is a @${P}% confidence interval
 computed through the above protocol.

@; TODO need this?
@;  well it's not about us, it's about future communication

If @${P} is clear from context we may say @approximation["s" "t"].
If @cspace[] is also clear, we may say @approximation[@${n_s} @${n_t}].

@bold{Definition} a @emph[sra] is an @approximation["s" "t" "P"] for some
 values @${P}, @${s}, and @${t}.


@section{Justification}

Let @cspace{C} be a configuration space,
 let @emph{D} be a small natural number,
 and let @${y} be the true number of @deliverable{D} configurations in @cspace{C}.

A @emph{sample} from the space @cspace{C} is a sequence @cspace{S} of
 configurations in @cspace{C}.
Some proportion @${y_{\bf S}} of configurations in @cspace{S} are @deliverable{D}.@note{
 More formally, the predicate @tt{D? : @cspace{C} -> Boolean} defines a
 Bernoulli random variable.}

In general, there is no useful relation between @${y} and @${y_{\bf S}};
 thus assume there exist functions @${s} and @${t} such that:
@itemlist[
@item{
 @$|{|{\bf S}| = s({\bf C})}|,
}
@item{
 there are @$|{t({\bf C})}| such samples,
}
@item{
 the @$|{y_{\bf S_i}}| are normally distributed around @${y}.
}
]

Given such functions @${s} and @${t}, the @${P}% confidence interval of the
 sample proportions @$|{y_{\bf S_i}}| is an interval @${[y_{lo}, y_{hi}]} with
 the desired property.
In other words, repeating this process @${k} times will yield a sequence of
 intervals @$|{[y_{lo}, y_{hi}]_0 \ldots [y_{lo}, y_{hi}]_{k-1}}| and @${P}% of these
 intervals will contain the true proportion @${y}.

The formal intuition for why the function @${s} should exist is the Law of Large
 Numbers.
@TODO{explain}.
The formal intuition for why @${t} should exist is the Central Limit Theorem.
@TODO{explain}.

@figure*["fig:validate-sample" "Valdiating Linear Measurements"
  (parameterize ([*PLOT-HEIGHT* 100])
    @render-validate-samples-plot*[VALIDATE-BENCHMARKS])
]

@Figure-ref{fig:validate-sample} provides empirical justification.
Specifically, the figure demonstrates that the functions:
@itemlist[
@item{
  @$|{s = \lambda\,{\bf C}.\,10 * \mathsf{log}_2(|C|)}|
}
@item{
  @$|{t = \lambda\,{\bf C}.\,10}|
}
]
produced samples that formed correct, tight bounds on the
 @integer->word[NUM-VALIDATE-SAMPLES] largest benchmarks from
 @section-ref{sec:exhaustive}.
    @; TODO  emphasize "LINEAR" !!!
Note that each plot in @figure-ref{fig:validate-sample} represents two datasets:
@itemlist[
@item{
  the solid blue line in each plot is from @figure-ref{fig:overhead}, and
}
@item{
  the orange intervals around these lines are the @approximation["s" "t" 95]
  for consecutive values of @math{D}.
}
]
For further evidence, the artifact for this paper contains scripts to reproduce
 this experiment.


@section{Inexhaustive Evaluation}
@; TODO need a slogan!

@figure["fig:sample:static-benchmark" "Static summary of benchmarks" #:style center-figure-style
  @(parameterize ([*CACHE-SUFFIX* "-linear"])
    @render-static-information[SAMPLE-BENCHMARKS])]

@figure*["fig:sample" "Linear Measurements"
  (parameterize ([*PLOT-HEIGHT* 100])
    @render-samples-plot*[SAMPLE-BENCHMARKS])]

The table in @figure-ref{fig:sample:static-benchmark} and plots in @figure-ref{fig:sample}
 present an inexhaustive evaluation of @integer->word[NUM-NEW-SAMPLES] benchmark programs.
@TODO{benchmark descriptions}
The results confirm the trends in @figure-ref{fig:overhead}.

