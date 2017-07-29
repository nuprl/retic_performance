#lang gm-plateau-2017

@; TODO too many words ya know

@(define MAIN-BENCHMARKS (append EXHAUSTIVE-BENCHMARKS SAMPLE-BENCHMARKS))
@(define NUM-MAIN-BENCHMARKS (length MAIN-BENCHMARKS))

@title[#:tag "sec:evaluation"]{Performance Evaluation}


@figure["fig:static-benchmark" "Static summary of benchmarks"
  @render-static-information[MAIN-BENCHMARKS]]

To assess the run-time cost of gradual typing in Reticulated, we measured
 the performance of @integer->word[NUM-MAIN-BENCHMARKS] benchmark programs.
@(let* ([column-descr*
         (list
           @elem{lines of code (@bold{SLOC}), }
           @elem{number of modules (@bold{M}), }
           @elem{number of function and method definitions (@bold{F}), }
           @elem{and number of class definitions (@bold{C}).})]
        [num-col @integer->word[(length column-descr*)]]
       ) @elem{
  @Figure-ref{fig:static-benchmark} tabulates information about the size and
   structure of the @defn{experimental} portions of the benchmarks.
  The @|num-col| columns report the @|column-descr*| 
  For more information about the benchmarks' origin and purpose, see the appendix.
})

The following subsections present our results in three parts.
First, @section-ref{sec:ratio} reports the performance of the fully-untyped
 and fully-typed configurations.
Second, @section-ref{sec:overhead} plots the proportion of @deliverable{D}
 configurations for @${D} between @${1} and @${@id[MAX-OVERHEAD]}.
This is our main result.
Third, @section-ref{sec:exact} confirms that the number of type annotations
 in a configuration is correlated to its performance.


@section[#:tag "sec:ratio"]{Performance Ratios}

@(define RT (get-ratios-table MAIN-BENCHMARKS))
@figure["fig:ratio" "Performance ratios"
  @render-ratios-table[RT]
]

The table in @figure-ref{fig:ratio} lists the extremes of gradual typing in
 Reticulated.
From left to right, these are:
 the performance of the untyped Reticulated configuration relative to Python (the @emph[u/p-ratio]),
 the performance of the fully-typed configuration relative to the untyped Reticulated configuration (the @emph[t/u-ratio]),
 and the overall delta between fully-typed Reticulated and Python (the @emph[t/p-ratio]).

@(let* ([futen-row (ratios-table-row RT 'futen)]
        [futen-u/p (ratios-row-retic/python futen-row)]
        [futen-t/u (ratios-row-typed/retic futen-row)]) @elem{
  For example, the row for @bm{futen} reports a @|u/p-ratio| of @${@|futen-u/p|}.
  This means that the average time to run the untyped configuration of the
   @bm{futen} benchmark using Reticulated was @${@|futen-u/p|} times slower than the
   average time of running the same code using @|PYTHON|.
  Similarly, the @|t/u-ratio| for @bm{futen} states that the fully-typed configuration
   is @${@|futen-t/u|} times slower than the untyped configuration.
})

On one hand, these ratios demonstrate that migrating a benchmark to
 Reticulated, or from untyped to fully-typed, always adds performance overhead.
The migration never improves performance.
On the other hand, the overhead is always within an order-of-magnitude.
@(let* ([rp* (map ratios-row-retic/python RT)]
        [tr* (map ratios-row-typed/retic RT)]
        [count-< (λ (x* n) (length (filter (λ (str) (< (string->number str) n)) x*)))]
        [rp-<2 (count-< rp* 2)]
        [rp-<3 (count-< rp* 3)]
        [rp-<4.5 (count-< rp* 4.5)]
        [tr-<2 (count-< tr* 2)]
        [tr-<3 (count-< tr* 3)]
        [tr-<3.5 (count-< tr* 3.5)]
        [num-> (for/sum ([rp (in-list rp*)]
                         [tr (in-list tr*)]
                         #:when (> (string->number rp) (string->number tr)))
                 1)])
  (unless (= (length rp*) rp-<4.5)
    (raise-user-error 'performance-ratios
      "expected all retic/python ratios to be < 4.5, but only ~a of ~a are" rp-<4.5 (length rp*)))
  @elem{
    Regarding the @|u/p-ratio|s:
     @integer->word[rp-<2] are below @${2}x,
     @integer->word[(- rp-<3 rp-<2)] are between @${2}x and @${3}x, and
     the remaining @integer->word[(- rp-<4.5 rp-<3)] are below @${4.5}x.
    The @|t/u-ratio|s are typically lower:
      @integer->word[tr-<2] are below @${2}x,
      @integer->word[(- tr-<3 tr-<2)] is between @${2}x and @${3}x,
      and the final @integer->word[(- tr-<3.5 tr-<3)] are below @${3.5}x.
    In particular, @integer->word[num->] benchmarks
     have larger @|u/p-ratio|s than @|t/u-ratio|s.
    This data suggests that migrating an arbitrary
     Python program to Reticulated adds a relatively larger overhead
     than migrating the same program to a fully-typed configuration.
})

@section[#:tag "sec:overhead"]{Overhead Plots}

@figure*["fig:overhead" "Overhead plots"
  @render-overhead-plot*[MAIN-BENCHMARKS]
]

@Figure-ref{fig:overhead} summarizes the overhead of gradual typing in the
 benchmark programs.
Each plot reports the percent of @deliverable[] configurations (@|y-axis|)
 for values of @${D} between @${1} and @${@id[MAX-OVERHEAD]} (@|x-axis|).
The @|x-axes| are log-scaled to focus on low overheads;
 vertical tick marks appear at @${1.2}x, @${1.4}x, @${1.6}x, @${1.8}x, @${4}x, @${6}x, and @${8}x overhead.

The heading above the plot for a given benchmark states the benchmark's name
 and the nature of the underlying dataset.
If the data is exhaustive, the heading lists the number of configurations
 in the benchmark.
If the data is approximate, the heading lists the number of samples
 and the number of randomly-selected configurations in each sample.


@parag{How to Read the Plots}
Overhead plots are cumulative distribution functions.
As the value of @${D} increases along the @|x-axis|, the number of
 @deliverable{D} configurations is monotonically increasing.
The important question is how many configurations are @deliverable{D}
 for low values of @${D}.
If this number is large, then a developer who applies gradual typing to a
 similar program has a larger change of arriving at a @deliverable{D} configuration.
The area under the curve is the answer; in short, more is better.
A curve with a large shaded area below it implies that a large number
 of configurations have low performance overhead.

@(let ([d0 "a"]
       [d1 "b"]) @elem{
  After surveying the area under a curve, the second most important aspects of
   an overhead plot are the values of @${D} where the curve starts and ends.
  More precisely, if @${h : \mathbb{R}^+ \rightarrow \mathbb{N}} is a function
   that counts the number of @deliverable{D}
   configurations in a benchmark, the critical points are the smallest
   overheads @${@|d0|, @|d1|} such
   that @${h(@|d0|) > 0} and @${h(@|d1|) = 100}.
  An ideal start-value would lie between zero and one; if @${@|d0| < 1} then
   at least one configuration runs faster than the original Python code.
  The end-value @${@|d1|} is the overhead of the slowest-running configuration
   in the benchmark.
})

Lastly, the slope of a curve corresponds to the likelihood that
 accepting a small increase in performance overhead increases the number
 of deliverable configurations.
A flat curve (zero slope) suggests that the performance of a group of
 configurations is dominated by a common set of type annotations.
Such observations are no help to programmers facing performance issues,
 but can help language designers find inefficiencies.


@parag{Conclusions}

Curves in @figure-ref{fig:overhead} typically cover a large area and reach the
 top of the @|y-axis| at a low value of @${D}.
This value is always less than @${@id[MAX-OVERHEAD]}.
In other words, every configuration in the
 experiment is @deliverable[MAX-OVERHEAD].
For many benchmarks, the maximum overhead is significantly lower.
@(let ([num-2-deliv (length '(futen slowSHA fannkuch nbody nqueens pidigits
                              take5 stats))]) @elem{
  Indeed, @integer->word[num-2-deliv] benchmarks are @deliverable[2].})
@; TODO 'indeed' is awkward

None of the configurations in the experiment run faster than the Python baseline.
This is no surprise, because Reticulated adds run-time checks to Python code for
 each type annotation.

@(let ([smooth '(futen http2 slowSHA chaos fannkuch float nbody pidigits
                 pystone PythonFlow take5 sample_fsm aespython stats)])
  @elem{
    @Integer->word[(length smooth)] benchmarks have relatively smooth slopes.
    The plots for the other @integer->word[(- NUM-EXHAUSTIVE-BENCHMARKS (length smooth))]
     benchmarks have wide, flat segments because those benchmarks contain at
     least one function or method that is called frequently.
    For example, if a benchmark creates many instances of a class @tt{C},
     adding a type annotation to the method @tt{C.__init__} adds significant
     overhead.
})

@(let* ([NOT-tp '(http2 call_method spectralnorm)]
        [num-tp (- NUM-MAIN-BENCHMARKS (length NOT-tp))]) @elem{
  @Integer->word[num-tp] benchmarks are roughly @deliverable{T}, where @${T} is
   the @|t/p-ratio| listed in @figure-ref{fig:ratio}.
})
In these benchmarks, the fully-typed configuration is one of the slowest-running
 configurations.
The notable exception is @bm{spectralnorm}, in which the fully-typed configuration
 runs faster than @${@id[@percent-slower-than-typed{spectralnorm}]\%} of the configurations.
This speedup occurs because of an unsoundness in the implementation of Reticulated;
 in short, the implementation does not type-check the contents of tuples.@note{@url{https://github.com/mvitousek/reticulated/issues/36}}


@section[#:tag "sec:exact"]{Absolute Running Times}

@figure*["fig:exact" "Running time (in seconds) vs. Number of typed components"
  @render-exact-runtime-plot*[MAIN-BENCHMARKS]
]

Since changing the type annotations in a Reticulated program changes its
 performance, the language should provide a cost model to help developers
 predict the performance of a given configuration.
The plots in @figure-ref{fig:exact} demonstrate that a simple heuristic
 works well for these benchmarks; @emph{the performance of a configuration is
 proportional to the number of type annotations in the configuration}.

@parag{How to Read the Plots}
@Figure-ref{fig:exact} contains one green point for every run of every
 configuration in the experiment.@note{Recall from @section-ref{sec:protocol},
 the data for each configuration is @id[NUM-ITERATIONS] runs.}
Each point compares the number of typed functions, methods, and classes in a
 configuration (@|x-axis|) against its running time in seconds (@|y-axis|).

The plots contain many points with both the same number of typed components
 and similar performance.
To reduce the visual overlap between such points, the points for a given
 configuration are spread across the @|x-axis|.
The @id[NUM-ITERATIONS] points for a configuration with @math{N}
 typed components lie within the interval @${N \pm @id[EXACT-RUNTIME-XSPACE]}
 on the @|x-axis|.
For example, @bm{fannkuch} has two configurations: one untyped
 configuration with zero typed components and one fully-typed configuration
  with one typed component.
To determine whether a point @${(x,y)} in the plot for @bm{fannkuch} represents
 the untyped or fully-typed configuration, round @${x} to the nearest integer.


@parag{Conclusions}

There are four notable trends regarding how adding types can affect
 performance.
To illustrate the trends, suppose a programmer starts at some configuration
 and adds some type annotations.
Depending on the benchmark and the configuration, there are at most four
 possible outcomes.

@exact-runtime-category["types make things slow"
  '(futen slowSHA chaos float pystone PythonFlow take5 sample_fsm aespython stats)
  (λ (num-in-category) @elem{
    The plots for @|num-in-category| benchmarks show a gradual increase in
     performance as the number of typed components increases.
    Typing any function, class, or method adds a small performance overhead.
})]

@exact-runtime-category[@elem{types make things very slow}
  '(call_method call_simple go http2 meteor nqueens spectralnorm Espionage PythonFlow)
  (λ (num-in-category) @elem{
    @string-titlecase[num-in-category] plots have visible gaps between
     clusters of configurations with the same number of types.
    Configurations below the gap contain type annotations that impose relatively little
     run-time cost.
    Configurations above the gap have some common type annotations that
     add significant overhead.
    Each such gap corresponds to a flat slope in @figure-ref{fig:overhead}.
})]

@exact-runtime-category[@elem{types are free}
  '(fannkuch nbody pidigits)
  (λ (num-in-category) @elem{
    In @|num-in-category| benchmarks, all configurations have similar performance.
    The dynamic checks that enforce type soundness add insignificant overhead.
})]

@exact-runtime-category[@elem{types make things fast}
  '(call_method spectralnorm)
  (λ (num-in-category) @elem{
    In @|num-in-category| benchmarks, there are some configurations
     that run faster than similar configurations with fewer typed components.
    These speedups happen for one of two reasons: either because of duplicate
     checks on dynamically-typed receivers of method calls,
     or because of omitted checks on values annotated with tuple types.
    The former is due to an overlap between Reticulated's semantics and
     Python's dynamic typing@~cite[vksb-dls-2014].
    The latter is due to a bug in the implementation (see @section-ref{sec:overhead}).
})]

Overall, there is a clear trend that adding type annotations adds performance
 overhead.
The increase is typically linear.
