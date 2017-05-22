#lang gm-dls-2017
@title[#:tag "sec:conclusion"]{Is Sound Gradual Typing Alive?}

The application of Takikawa et al.'s method to Reticulated appears to
 indicate that at least one sound, gradually typed language comes with a
 performant implementation. In particular, the overhead plots for
 Reticulated look an order of magnitude better than those for Typed
 Racket. Appearances are deceiving, however.  Reticulated's type system is
 far less expressive than Typed Racket's. Furthermore, its error messages,
 especially for higher-order values, are seldom actionable.
 Most importantly, though, Reticulated guarantees an alternative soundness.
 A program of type @tt{List(Int)} may print a list of
 strings---without signaling any violation.

Our evaluation effort thus confirms a widely held conjecture and leaves us
 with an open research problem. While the sacrifice of soundness improves
 the performance of gradual typing systems, it remains unclear how
 pervasive the problem is and whether programmers accept such compromises if
 they want to reason with types.
 Finally, the research community must
 continue to search for ways to improve the performance of sound, gradually
 typed languages.
