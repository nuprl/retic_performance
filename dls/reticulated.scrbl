#lang gm-dls-2017
@title[#:tag "sec:reticulated"]{Gradual Typing}

Outline:

@section{Purpose of the section:Why is gradual typing useful for the programmer?}
Allows them to incrementally type their programs. The reason they want their programs to be gradually typed is that gradual typing provides guarantees about soundness during runtime.


@section{What is soundness for partially typed programs?}
In order to see why soundness is important for the programmer in partially typed programs, we need to define it.

Soundness:

We use the similarity relation from SNAPL sim(a,b), which states that a and b are the same with a possibly having more types or casts.

The definition states that given two programs P and P_M which are similar and where M is a typed module:

1- if P evaluates to v then P_M evaluates to v' where sim(v,v') or it outputs an (runtime/static)? error where g != M. (not sure what that means)

 ** what about when typing M catches a static type error in M?**

2- If P results in an error, then P_M also results in an error and g != M

3- If P does not terminate then P_M does not terminate, or outputs an error.


Mention why this definition allows the programmer to produce less error prone programs and helps catch errors, possibly give an example.


@section{Reticulated Python design}

- Mention that we can type smaller expressions in the program within a module.

- Those expressions are limited to those typable according to idiomatic python
@note{@url{https://www.python.org/dev/peps/pep-0484/}}

- Reticulated Python does not support generics @~cite[vksb-dls-2014], which means we use type Dyn instead (some of our benchmarks had generics, so this point can be postponed to the benchmark section)

@section{Transient semantics}
- Explain what transient semantics are, using the definition in DLS2014 "Design and Evaluation of Gradual Typing for Python".

- Explain soundness in Reticulated Python and talk about the gradual guarantee


@section{Is reticulated Python sound?}
Does reticulated python actually follow the definition of soundness?

