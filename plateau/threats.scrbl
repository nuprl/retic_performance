#lang gm-plateau-2017
@title[#:tag "sec:threats"]{Threats to Validity}

Our work may suffer from two problems: measurement error and systematic bias.
This section spells out the details.


@section{Measurement Error}
@; - did some preliminary measurements to see if different nodes or
@;   different usage patterns

The data are timings recorded on the Karst at Indiana University cluster
 using the Python function @|time.process_time|.
Assuming @tt{process_time()} is accurate, the cluster infrastructure is prone
 to at least two sources of error.
First, cluster nodes may have non-uniform performance despite being identical
 servers.
Second, the load on other nodes in the cluster may affect the latency of
 system calls.
These measurement biases may explain the outliers evident in @figure-ref{fig:exact}.
@;@~cite[mdhs-asplos-2009]


@section{Systematic Bias}

@(let* ( @; See `src/PyPI-ranking/README.md` to reproduce these claims
        [lib-data* '((simplejson 50 "https://github.com/simplejson/simplejson")
                     (requests 200 "https://github.com/kennethreitz/requests")
                     (Jinja2 600 "https://github.com/pallets/jinja/tree/master/jinja2"))]
        [rank-info @elem{PyPI Ranking@note{@url{http://pypi-ranking.info/alltime}}}]
        [lib-info (authors*
                    (for/list ([ld (in-list lib-data*)]
                               [long-style? (in-sequences '(#t)
                                                          (in-cycle '(#f)))])
                      @elem{
                        @(if long-style? "The" "the")
                        @hyperlink[(caddr ld)]{@tt[@symbol->string[(car ld)]]}
                        library contains over @${@id[(cadr ld)]}@;
                        @(if long-style? " functions and methods" "")}))]
       ) @elem{
  First, the experiment consists of a small suite of benchmarks, and these
   benchmarks are rather small.
  For example, an ad-hoc sample of the @|rank-info| reveals that even small
   packages have many functions and methods.
  @|lib-info|.
})

Second, the experiment considers one fully-typed configuration per benchmark;
 however there are many ways of typing a given program.
The types in this experiment may differ from types ascribed by another Python
 programmer, which, in turn, may lead to different performance overhead.

@(let ([missing-types '(take5)]
       [retic-limited '(go pystone stats)]
       [format-bm* (lambda (bm*) (authors* (map bm bm*)))]
       @; see also https://github.com/nuprl/retic_performance/issues/55
       @;
       @; - futen is missing some type annotation(s)
       @;   - LazyFqdn missing @fields
       @; - call_method is missing some type annotation(s)
       @;   - missing @fields, but actually empty
       @; - call_method_slots is missing some type annotation(s)
       @;   - missing @fields, but actually empty
       @; - go uses the Dyn type
       @;   - to avoid circular reference
       @; - pystone uses the Dyn type
       @;   - union type, (U PSRecord None)
       @; - take5 is missing some type annotation(s)
       @;   - `create_deck`, argument 'deck_size' is unannotated
       @;   - same function has optional arguments, so the types ignored
       @; - stats is missing some type annotation(s)
       @;   - only on the print function
       @; - stats uses the Dyn type
       @;   - for polymorphism, "rank polymorphism", and union types
      ) @elem{
  Third, some benchmarks use dynamic typing.
  The @bm{take5} benchmark contains one effectively-untyped function.@note{This function accepts an optional argument. Reticulated ignores the types of such functions, see @url{https://github.com/mvitousek/reticulated/issues/32}.}
  This is due to a mistake our our part, but we later typed the function, repeated the random sampling experiment, and observed no significant change in performance.
  @Integer->word[(length retic-limited)] other
   benchmarks (@format-bm*[retic-limited]) use
   dynamic typing to overcome limitations in Reticulated's types.
})

@(let ([use-io* '(aespython futen http2 slowSHA)]) @elem{
  Fourth, the @(authors* (map bm use-io*)) benchmarks read from a file
   within their timed computation.
  We nevertheless consider our results representative.
})

Fifth, Reticulated supports a finer granularity of type annotations than the
 experiment considers.
Partially-typed functions and classes may come with entirely different performance.
We leave this as an open question.


@section{TBA: Leftovers}
@(define pystone-union-fields
        @; grep for 'PtrComp = ' to find assignments
        @; It's initially `None`, and assigned away-from and back-to `None`
        @;  in `Proc1`
        '(PSRecord.PtrComp))
@(define stats-union-functions
        @; Most of these functions all have a dead-giveaway pair of lines:
        @; ```
        @;  if type(cols) not in [list,tuple]:
        @;      cols = [cols]
        @; ```
        '(abut simpleabut colex linexand recode))
@(define dyn* '(go pystone stats take5 lisp))
@; TODO add better in-file evidence

Reticulated currently lacks union types, recursive types, and types for variable-arity functions.
Consequently, Reticulated cannot fully-type some programs in our experiment.
One common issue is Python code that uses @tt{None} as a default value.
The benchmark versions of such code use well-typed defaults instead.
Other benchmark versions resort to dynamic typing.
Both @bm{pystone} and @bm{stats} suffer from the lack of union types,
 and @bm{go} contains a recursive class type.
Lastly, we tried typing a Lisp interpreter, but the program made too-heavy use of union and recursive types.


@; ===

@(define vss-popl-2017-benchmarks
   '(callsimple nqueens pidigits meteor fannkuch nbody callmethod
     callmethodslots pystone float chaos go spectralnorm))
@(define vss-2x-benchmarks
   '(nqueens meteor fannkuch callmethod callmethodslots pystone float chaos go))

Refining the dynamic error messages will add performance overhead.
For example, @citet[vss-popl-2017] built an extension to Reticulated that reports a set of potentially-guilty casts when a dynamic type error occurs.
They report that tracking these casts can double a program's @|t/p-ratio|.


@; ===

The performance implications of @${1'} are substantial.
A gradual type system that enforces traditional soundness must exhaustively traverse
 data structures before they leave typed code, and must monitor functional values
 to ensure their future applications are well-typed.
Enforcing @${1'} requires a tag check, nothing more.

