#lang scribble/acmart
@require[
  "common.rkt"
]

@title[#:tag "sec:introduction"]{Introduction}

Sound gradual typing allows us to safely combine typed and untyped code, but to accomplish soundness, gradual typing adds extra runtime checks which impact the performance. Studies on Typed Racket, a macro-gradual type system show a significant overhead of Typed Racket compared Racket. Another study on Reticulated Python, a micro-gradual type system studies the performance of fully annotated Reticulated Python programs versus Python programs. However no studies conduct a proper evaluation of a micro-gradual type system.

A proper evaluation for a gradual type system should capture the practicality of that system to the programmer, by not only measuring a fully annotated configuration of the program versus the original language, but by also measuring various other configurations of the program that would reflect his/her usage of the system. For example, a programmer may want to insert types only in certain parts of the code for debugging purposes, or would like to gradually transition from fully untyped code to fully typed code while avoiding a large performance overhead.

According to Siek et. al, "Programmers should be able to add or remove type annotations without any unexpected impacts on their program". One of our goals is to test this hypothesis on a micro-gradual type system.

In this paper, we consider Reticulated Python, a micro-gradual type system for Python. We port 8 benchmarks to Python, and measure the performance using the Takikawa et al method, which we adapt to micro-gradual typing. Consider a program with n functions. We take 2^n configurations obtained by choosing to annotate or to not annotate every function in the program. This method allows us to capture as many varied configurations over types as possible in 2^n configurations. Secondly we select n random configurations. This method annotates each atomic expression in the program randomly. We interpret the results according to the lattice-oriented approach from Takikawa et al.

In summary, we make two main contributions: We test Siek's hypothesis by applying the Takikawa et al. method to measure the performance of a micro-gradual type system and we validate the linear sampling method.







