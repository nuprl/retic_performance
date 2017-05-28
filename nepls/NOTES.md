Is Sound GT Alive?
===

Let's talk about gradual typing
- promise --- as you know --- what static typing and dynamic typing, design system that supports both, moreover smooth integration between static and dynamic
- what does that mean? informallly "no unexpected consequences" formall "no new behaviors" `\sqle`
- examples: 2 modules, at least 4 ways to type
  - depending on the gradual type system may be finer granularity but that's not a super important distinction
- back to informal promise of GT, "no enexpected" says I can pick anything and get roughly the same program.
 And this, it's implied , is useful foundation for developers
- SNAPL'15 does not talk about performance except in passing, but if I'm a working programmer then I care very much about performance.
  If I move from A to B and my program is 5x slower then I will be very upset
- whether or not 5x is "unexpected" isn't important. If GT going to be more than theoretical artifact neesd to deliver performance

the word of the day is performance
- how to express performance of a type system?
  - how can types possibly affect performance?
- if t/u contexts share values, the t needs to check some types on the u at runtime
  - t : int -> int, called in u context, need to check domain
  - u : int -> listof int called in t context, need to check codomain
- GT systems insert checks automatically, these have cost, the affect on performance is what we mean by the performance impact of GT
- so
  - we have exponentially many configurations mixing t/u contexts in a unique way, each with performance
  - overall performance, is performance of each
  - ok but does not scale past like 6 things
  - if you have 10 things hard to judge performance
- idea from takikawa etal is how to present,
  paper with flash title, the important contribution is the evaluation method
  - plots are "what % is fast" as I relax definition of "fast" think CDF
- by example, project with 2 boxes, suppose absolute perfs are .... TODO ....
  - example graph, to summarize
  - lessno, if programmers can tolerate 2x can see what % are 2x to estimate whether GT will perform for you
  that is the idea of the method

experimetal setup
- no comprehensive eval of reticulated (hey Ben are you going to show the eval of TR?)
- sent zeina to IU, got programs, started measuing, long time,
- here is results
- N0 benchmarks, N1 sources, frange from N2 to N3 configurations
  - more details in paper
- foreach benchmark ran all configs UP TO CF granularity
- observations
  - 10x worst case
  - N4 at 100% by 2x
  - pretty god

conclusions
- small benchmarks significant overhead
- compare to TR unbelievably slow
- difference in first-order vs. higher-order
- other usability concerns

one more thing: sampling
- graph presentation scales but collecting does not
- paper confirms a SRS technique
- one example 

questsions
- add t/p ratios
- show exact runtimes
