#lang scribble/acmart
@require[
  "common.rkt"
]

@title[#:tag "sec:introduction"]{Introduction}

Sound gradual typing allows us to safely combine typed and untyped code, but to accomplish soundness, gradual typing adds extra checks during runtime. There are currently a few implementations of sound gradual typing, but none of them seem to be efficient. Studies by  Takikawa et al on Typed Racket , a macro-gradual type system show a significant overhead of Typed Racket compared to Racket. The method used in this study explores the partial conversions from typed to untyped code by measuring the performance of 2^n configurations where n is the number of modules in a given benchmark. It also employs the linear sampling approach by generating a linear number of samples of random typed/untyped ratios over modules. It then uses a lattice oriented approach to interpret the results. 

Another study by Vitousek et al. on Reticulated Python, a micro-gradual type system studies the performance of fully annotated Reticulated Python programs versus Python programs and shows that Reticulated Python is 20x slower than Python. However, this study does not measure any of the configurations which represent the partial conversions from typed to untyped code. The reason why we want to measure these configurations is that they span the different ways the developer can use this system. A developer may want to only add types to certain parts of the code for debugging reasons, or may introduce types to a program in an incremental manner. Up till now, no studies conduct a proper evaluation of Reticulated Python. Furthermore, no studies conduct a proper evaluation on any micro-gradual type system. 

According to Siek et. al, "Programmers should be able to add or remove type annotations without any unexpected impacts on their program". However, so far, this hypothesis cannot be verified and one reasons for that is the absence of proper evaluations on micro-gradual type systems.

In this paper, we conduct a proper evaluation on a micro-gradual type system by adapting the  Takikawa et al. method for macro-gradual type systems to mico-gradual type systems in the following way:

Instead of testing every possible configuration over modules, we test every possible configuration over functions. In other words, we consider 2^n configurations obtained by choosing to annotate or to not annotate every function in the program and test their performance against python. Secondly, We select n random configurations but instead of annotating over modules, we annotate over atomic expressions. We then interpret the results according to the lattice-oriented approach from  Takikawa et al.

In summary, we make two main contributions: We test Siek's hypothesis by adapting the  Takikawa et al. method to measure the performance of a micro-gradual type system and we validate the linear sampling method by Takikawa et al.





