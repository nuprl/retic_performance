#lang gm-dls-2017
@title[#:tag "sec:linear"]{Scaling the Evaluation Method}

@; TODO s,t is way way way too general,
@;  should at least bring across we're doing LINEAR sampling,
@;  and why can't you test whether constant-factor works?

@; -----------------------------------------------------------------------------

Simple random sampling is a viable technique for approximating the number
 of @deliverable{D} configurations in a benchmark.
In particular, a sampling protocol based on elementary
 statistics (@section-ref{sec:sampling:protocol})
 is able to reproduce the largest overhead plots in @figure-ref{fig:overhead}
 with a fraction of the measurements (@section-ref{sec:sampling:overhead}).
The protocol scales to significantly larger benchmarks than the exhaustive
 technique presented in @section-ref{sec:method} (@section-ref{sec:sampling:new}).
Whereas exhaustive evaluation cannot feasibly be applied to programs containing
 hundreds of functions, the main bottleneck applying the sampling technique
 is the human cost of inferring fully-typed configurations.


@section[#:tag "sec:sampling:protocol"]{Sampling Protocol}

Counting the proportion of @deliverable{D} configurations is a useful way to
 measure the performance overhead of gradual typing because it addresses two
 forms of uncertainty.
First, the parameter @${D} addresses the fact that different software applications
 have different performance requirements.
Second, the proportion quantifies over the entire configuration space of a program
 because it is impossible to predict how developers will apply gradual
  typing.@note{ @; TODO: the note needs work, but it needs to be here.
    The promise of gradual typing is @emph{any configuration}. At
    present, there is no data to suggest that developers choose @emph{particular
    configuration}.}
For an arbitrary configuration, the proportion of @deliverable{D} configurations
 @emph{is} the probability that this configuration is @deliverable{D}.

There is, however, a natural way to approximate the same conclusion.
Suppose a few developers independently apply gradual typing to a program.
Each arrives at some configuration and observes some performance overhead.
Therefore, for a given value of @${D} some proportion of the developers have
 @deliverable{D} configurations.
There is a remote chance that this proportion coincides with the true proportion
 of @deliverable{D} configurations.
Intuitively, the chance is less remote if the number of developers is very
 large.
But even for a small number of developers, if they repeat this experiment
 multiple times then the average proportion of @deliverable{D} configurations
 should tend towards the true proportion.
After all, if the true proportion of @deliverable{D} configurations is
 10% then approximately 1 in 10 randomly sampled configurations will be
 @deliverable{D}.

The following definition capture the informal sampling protocol outlined above:

@definition[@approximation["r" "s" "95"]]{
  A @approximation["r" "s" "95"] of the proportion of @deliverable{D} configurations is
   a 95% confidence interval generated from @${r} samples, each made of @${s}
   configurations.
  (Informally: a @emph{simple random approximation}.)
  @; ^^^ to disambiguate from other approximations
}

A given sample of @${s} randomly-selected configurations contains some
 number @${n} of @deliverable{D} configurations.
The proportion @${n/s} is the proportion of @deliverable{D} configurations
 in the sample.
Repeating the sampling process @${r} times yields a sequence of proportions;
 the 95% confidence interval of such a sequence is a @approximation["r" "s" "95"].

The theoretical justification for why this protocol should yield a useful
 estimate requires some basic statistics.
Let @${d} be a predicate that checks whether a particular configuration of
 a fixed program is @deliverable{D}.
This predicate defines a Bernoulli random variable @${X_d} with parameter
 @${p}, where @${p} is the true proportion of @deliverable{D} configurations.@note{
  In particular, @${X_d = } @racket[(lambda () (if (@${d} (random-config)) 1 0))]}
Consequently, the expected value of this random variable is @${p}.
The law of large numbers therefore states that the average of infinitely
 many samples of @${X_d} converges to @${p}, the true proportion
 of deliverable configurations.
Convergence suggests that the average of ``enough'' samples will be ``close to''
 @${p}.
The central limit theorem provides a similar guarantee---any sequence of
 such averages will be normally distributed around the true proportion.
Hence a 95% confidence interval generated from such averages is likely
 to contain the true proportion.

@; Taken alone, this observation is useless; the protocol in @section-ref{sec:method}
@;  finds the same proportion @${p} in finite time.
@; The CLT turns the suggestion into a guarantee

@; TODO cite sources


@section[#:tag "sec:sampling:overhead"]{Empirical Validation}

In principle, a @approximation["r" "s" "95"] should give precise and accurate
 bounds.
It remains to be seen whether the data from a small number of samples (@${r})
 each containing a small number of configurations (@${s}) actually do so in
 practice.
@; The bounds might be wide, and the bounds might not contain the true proportion
@;  of @deliverable{D} configurations.
Fortunately, the data from the exhaustive evaluation of @section-ref{sec:exhaustive}
 is an adequate source-of-truth to test against.

@figure*["fig:sample:validate" @elem{Validating the @emph{simple random approximation} method}
  (parameterize ([*PLOT-HEIGHT* 100])
    @render-validate-samples-plot*[VALIDATE-BENCHMARKS])
]

@Figure-ref{fig:sample:validate} demonstrates that linear samples
 suffice to approximate the performance overhead in the
 @integer->word[NUM-VALIDATE-SAMPLES] largest benchmarks from
 @section-ref{sec:exhaustive}.
For a benchmark containing @${F} functions and @${C} classes,
 the figure plots the confidence interval generated by
 @integer->word[NUM-SAMPLE-TRIALS] samples of @${@id[SAMPLE-RATE]*(F+C)}
 configurations selected at random @emph{with replacement}.@note{The theoretical
  justification in @section-ref{sec:sampling:protocol} assumes random sampling
  without replacement, but (to paraphrase Knuth@~cite[k-cs-1974] out of context)
  the chance of drawing the same configuration twice is quite small, and removing
  this chance slightly increases the odds of drawing an extreme outlier.}
These intervals are superimposed on the overhead plots from @figure-ref{fig:overhead}.

These particular @approximation[NUM-SAMPLE-TRIALS @smaller{@${[@id[SAMPLE-RATE](F+C)]}} "95"]s
 @; ... could just say "simple random approximation"
 all contain the the true number of @deliverable{D} configurations for values of
 @${D} between 1 and @id[MAX-OVERHEAD].
The intervals are futhermore small, and thus practical substitutes for the overhead plots.
@; TODO I mean, the message they give to USERS is the same, more-or-less.
@;      the added benefit of collecting all the data is small

The online supplement to this paper contains scripts for generating new samples
 and reproducing this experiment.


@section[#:tag "sec:sampling:new"]{Approximate Evaluation}

@figure["fig:sample:static-benchmark" "Static summary of benchmarks"
  @(parameterize ([*CACHE-SUFFIX* "-linear"])
    @render-static-information[SAMPLE-BENCHMARKS])]

The simple random approximation method scales to large programs.
Given any fully-typed program, a @approximation["r" "s" 95] can estimate its
 performance in reasonable time.
The exact amount of time, as well as the quality of the estimate, depends
 on the chosen values of @${r} (number of repetitions) and @${s} (sample size).

@; continues the evaluation started in section 4
@(let* ([DLS '(aespython stats)]
        [NEW '(Evolution sample_fsm)]) @elem{
   This section presents the results of an @defn{approximate} performance
    evaluation of @integer->word[NUM-NEW-SAMPLES] benchmark programs.
   @string-titlecase[@integer->word[(length DLS)]] of these programs,
    @bm*[DLS], originate from case studies by @citet[vksb-dls-2014].
   The other @integer->word[(length NEW)], @bm*[NEW], originate from open-source
    programs.
   @Figure-ref{fig:sample:static-benchmark} and the following descriptions
    provide more information about the benchmarks' size and purpose.
})

@; -----------------------------------------------------------------------------
@; --- WARNING: the order of benchmarks matters!
@; ---  Do not re-order without checking ALL PROSE in this file
@; -----------------------------------------------------------------------------

@bm-desc["Evolution"
@authors["Maha Elkhairy" "Kevin McDonough" "Zeina Migeed"]
""
@list[
  @(let ([num-python-files-in-both-dir 90] @;; ./find "../benchmarks/Evolution/both" -name "*.py" | wc -l
         [num-test-files 21]) @;; ./find "../benchmarks/Evolution/both/evo_test" -name "*.py" | wc -l
    @elem{@id[(- num-python-files-in-both-dir num-test-files)] untyped modules})
]]{
  Implements a card game.
  The experimental modules represent the possible actions
   that a player can take on each turn.
  The control modules encode the players, cards, and game logic.
  @; 20 iterations
}

@bm-desc["sample_fsm"
@authors["Linh Chi Nguyen"]
@url{https://github.com/ayaderaghul/sample-fsm}
@list[
  @lib-desc["itertools"]{cycles}
  @lib-desc["os"]{path split}
  @lib-desc["random"]{random randrange}
]]{
  Simulates the interactions of economic agents via finite-state automata@~cite[n-mthesis-2014].
  This benchmark is adapted from a similar Racket program called @tt{fsmoo}@~cite[greenman-jfp-2017].
  @; 100 iterations
}

@bm-desc["aespython"
@authors[@hyperlink["http://caller9.com/"]{Adam Newman}
         @hyperlink["https://github.com/serprex"]{Demur Remud}]
@url{https://github.com/serprex/pythonaes}
@list[
  @lib-desc["os"]{random stat}
  @lib-desc["struct"]{pack unpack calcsize}
]]{
  @; Second sentence is a little awkward. I just want to say, "this is really
  @;  a Python implementation of AES, not just a wrapper to some UNIX implementation"
  Implements the @hyperlink["http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf"]{Advanced Encryption Standard}.
  Uses the @tt{os} library only to generate random bytes and invoke the
   @hyperlink["http://man7.org/linux/man-pages/man2/stat.2.html"]{@tt{stat()}}
   system call.
  @; 1 iteration, encrypts the book of Leviticus (2800 lines)
}

@bm-desc["stats"
@authors[@hyperlink["https://connects.catalyst.harvard.edu/Profiles/display/Person/12467"]{Gary Strangman}]
@url{https://github.com/seperman/python-statlib/blob/master/statlib/pstat.py}
@list[
  @lib-desc["copy"]{deepcopy}
  @lib-desc["math"]{pow abs etc.}
]]{
  Implements first-order statistics functions; in other words, transformations
   on either floats or (possibly-nested) lists of floats.
  The original program consists of two modules.
  The benchmark is modularized according to comments in the program's source
   code to reduce the size of each module's configuration space.
  @; 1 iteration
}


@subsection{Results}

@figure*["fig:sample:overhead" "Simple random approximation plots"
  (parameterize ([*PLOT-HEIGHT* 100])
    @render-samples-plot*[SAMPLE-BENCHMARKS])]

@Figure-ref{fig:sample:overhead} plots the results of applying the protocol
 in @section-ref{sec:protocol} to randomly sampled configurations.
These results confirm many trends in earlier data; in particular,
@itemlist[
@item{
  The @|u/p-ratio|s are relatively low.
  @; TODO compute these, call functions
  The smallest is 1.1x and the largest is 4x.
}
@item{
  All configurations are @deliverable[MAX-OVERHEAD].
}
@item{
  The curves typically have smooth slopes, implying the cost of annotating
   a single function or class is low.
}
@item{
  @TODO{plot and address typed/untyped ratios}
}
@item{
  The intervals are tight.
}
]



@; -----------------------------------------------------------------------------

@; @; This belongs in one of three places:
@; @; 1. Intro
@; @; 2. Conclusion
@; @; 3. Trash
@; @section{Motivation}
@; 
@; The benchmark programs in @section-ref{sec:exhaustive} are rather small.
@; Any experienced Python programmer could infer type annotations for these
@;  programs in a matter of hours.
@; Widely-used Python programs are typically much larger.
@; For example @TODO{examples}.
@; @; "jumping" to fully-typed makes even less sense for reticualted,
@; @;  since number-of-types is a decent predictor of performance
@; In theory, gradual typing offers important engineering benefits to such projects;
@;  designers can choose the precise amount of typing that best suits the project
@;  and developers can run end-to-end tests on the program at each stage of the
@;  migration.
@; It is not clear, however, that the resuts of @section-ref{sec:exhaustive} will hold
@;  for significantly larger programs.


