#lang gm-dls-2017
@title[#:tag "sec:conclusion"]{Is Sound Gradual Typing Alive?}

Reticulated Python is an experimental language that uses programmer-supplied
 type annotations to perform some static type checks, and furthermore compiles the
 annotations to first-order runtime assertions.
The data in this paper suggests that the performance overhead imposed by the
 runtime assertions will not exceed 10x in typical Python programs, no
 matter how many functions and class definitions the programmer chooses to
 annotate with types.

Reticulated is a research prototype.
Its type system is able to express the types in basic Python programs
 and may catch some of the errors typically thought of as ``type errors'',
 but Reticulated is not an implementation of @|PEP-484|
 and does not guarantee type soundness in the SML, Haskell, or Typed Racket sense@~cite[tfffgksst-snapl-2017].
For example, if a Reticulated function is declared with the return type @pythoninline{List(Int)},
 Reticulated inserts a tag check that ensures the function returns a @pythoninline{List} of some sort, but ignores the contents.@note{@citet[vss-popl-2017] give a similar example at the end of @hyperlink["http://homes.soic.indiana.edu/mvitouse/papers/popl17.pdf"]{section 2.2.2}. Their function @emph{avg} expects a list of floating-point numbers, but will not error if given a list of integers. If @emph{avg} is given a list of strings, the call will terminate in an error raised by the Python function @tt{sum}.}

Nevertheless, Reticulated's integration with Python and its low performance
 overhead due to type annotations are promising.
 If the implementation can address the concerns raised in @section-ref{sec:vs-tr}
 (e.g., lack of polymorphism, cryptic error messages) while maintaining its
 current level of performance, then it will be interesting to see how developers
 react to its unique notion of type soundness.
