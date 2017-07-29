#lang gm-plateau-2017
@title[#:tag "sec:threats"]{Threats to Validity}

We have identified five sources of systematic
 bias that question the validity of our conclusions.
@(let* ( @; See `src/PyPI-ranking/README.md` to reproduce these claims
        [lib-data* '((simplejson 50 "https://github.com/simplejson/simplejson")
                     (requests 200 "https://github.com/kennethreitz/requests")
                     (Jinja2 600 "https://github.com/pallets/jinja/tree/master/jinja2"))]
        [rank-info @hyperlink["http://pypi-ranking.info/alltime"]{PyPI Ranking}]
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
 however, there are many ways of typing a given program.
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
  The @bm{take5} benchmark contains one function that accepts optional arguments,
   and is therefore untyped.@note{Bug report: @url{https://github.com/mvitousek/reticulated/issues/32}.}
  @Integer->word[(length retic-limited)] other
   benchmarks (@format-bm*[retic-limited]) use
   dynamic typing to overcome limitations in Reticulated's type system,
   such as the lack of untagged union types.
})

@(let ([use-io* '(aespython futen http2 slowSHA)]) @elem{
  Fourth, the @(authors* (map bm use-io*)) benchmarks read from a file
   within their timed computation.
  We nevertheless consider our results representative.
})

Fifth, Reticulated supports a finer granularity of type annotations than the
 experiment considers.
Partially-typed functions may come with entirely different performance.
We leave this as an open question.


