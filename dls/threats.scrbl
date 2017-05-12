#lang gm-dls-2017
@title[#:tag "sec:threats"]{Threats to Validity}

There are several threats to the validity of the overhead plots in
 @figure-ref["fig:overhead" "fig:sample:overhead"].
These threats question the accuracy of the data
 and the soundness of the experimental protcol.


@section{Measurement Error}
@; - did some preliminary measurements to see if different nodes or
@;   different usage patterns
@; - ran 40 iterations to control

The data are timings recorded on the Karst at Indiana University cluster
 using the Python function @hyperlink["https://docs.python.org/3/library/time.html#time.process_time"]{@tt{time.process_time()}}.
Assuming @tt{process_time()} is accurate, the cluster infrastructure is prone
 to at least two sources of error.
First, cluster nodes may have non-uniform performance (despite being identical
 servers).
Second, the load on other nodes in the cluster may affect the latency of
 system calls.
These measurement biases@~cite[mdhs-asplos-2009] may explain the outliers evident in @figure-ref{fig:exact}.


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
                        library contains over @id[(cadr ld)]@;
                        @(if long-style? " functions and methods" "")}))]
       ) @elem{
  First, the experiment includes very few benchmarks, and these benchmarks are
   rather small.
  For example, an ad-hoc sample of the @|rank-info| reveals that even small
   packages have many functions and methods.
  @|lib-info|.
})

Second, the experiment considers one fully-typed configuration per benchmark;
 however there are many ways of typing a given program.
The types in this experiment may differ from types inferred by another Python
 programmer, and may lead to different performance overhead.

@(let ([missing-fields '(futen Evolution)]
       [retic-limited '(go pystone take5 stats)]
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
       @; - Evolution is missing some type annotation(s)
       @;   - none of classes have @fields
       @; - take5 is missing some type annotation(s)
       @;   - `create_deck`, argument 'deck_size' is unannotated
       @;   - same function has optional arguments, so the types ignored
       @; - stats is missing some type annotation(s)
       @;   - only on the print function
       @; - stats uses the Dyn type
       @;   - for polymorphism, "rank polymorphism", and union types
      ) @elem{
  Third, some benchmarks are either missing annotations or use the dynamic type.
  @Integer->word[(length missing-fields)]
   benchmarks (@format-bm*[missing-fields]) have
   classes with untyped fields due to an oversight on our part.
  @Integer->word[(length retic-limited)]
   benchmarks (@format-bm*[retic-limited]) use the
   dynamic type (@tt{Dyn}) to overcome limitations in Reticulated's type theory.
})

Fourth, Reticulated supports a finer granularity of type annotations than the
 experiment considers.
Partially-typed function signatures or classes with some typed fields and some
 untyped fields may have interesting performance characteristics.
More importantly, such combinations of typed and untyped code may be more
 representative of what Python programmers eventually use in practice.

