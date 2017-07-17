#lang gm-plateau-2017
@title[#:tag "sec:conclusion"]{Is Sound Gradual Typing Alive?}

The application of Takikawa et al.'s method to Reticulated appears to
 indicate that at least one sound, gradually typed language comes with a
 performant implementation. In particular, the overhead plots for
 Reticulated look an order of magnitude better than those for Typed
 Racket. Appearances are deceiving, however.  Reticulated's type system is
 far less expressive than Typed Racket's. Furthermore, its error messages,
 especially for higher-order values, are seldom actionable.
 Most importantly, though, Reticulated guarantees an alternative soundness.
 A program of type @tt{List(String)} may evaluate to a list of
 integers---without signaling any violation.

Our evaluation effort thus confirms a widely held conjecture and leaves us
 with an open research problem. While the sacrifice of traditional soundness improves
 the performance of gradual typing systems, it remains unclear whether programmers
 will accept what remains if they want to reason with types.
 @; NOTE from matthias: "may wish to investigate how each weakening of Reticulated
 @;  affects the performance profile of gradual typing; our method of linear
 @;  sampling provides a thorough evaluation framework.
 @;Finally, the research community must
 @;continue to search for ways to improve the performance of sound, gradually
 @;typed languages.

@acks{
  This paper is supported by @hyperlink["https://www.nsf.gov/awardsearch/showAward?AWD_ID=1518844"]{NSF grant CCF-1518844}.
@;  Matthias for all things.
@;  Mike for Reticulated, bugfixes.
@;  Sam for access to IU cluster.
@;  Spenser Bauman for advice about cluster.
@;  Tony GJ for insisting that overhead plots are CDFs.
@;  @;note{Computed using David A. Wheeler's @hyperlink["https://www.dwheeler.com/sloccount/"]{@tt{sloccount}} utility.}
}

