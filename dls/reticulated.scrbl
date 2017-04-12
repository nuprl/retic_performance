
#lang gm-dls-2017
@title[#:tag "sec:reticulated"]{Gradual Typing}


A gradual typing system aims to let programmers add type annotations to their programs incrementally. Unlike optional typing, gradual typing provides soundness guarantees by imposing type checks on the program in runtime. 
The granularity of such type system varies according to the language. We currently have micro-level gradually typed languages such as Reticulated Python and macro-level gradually typed languages such as Typed Racket.
We give a brief overview of micro-gradual typing and macro-gradual typing in sections 2.1 and 2.2 respectively. In section 2.3 we give an overview of Reticulated Python. Reticulated Python has three modes of implementation: transient, monotonic and guarded. We define the transient mode, which is the subject of our measurements.


@section{Macro-Gradual Typing}
In macro-gradual typing, a programmer must annotate an entire module. Therefore, it relies on behavioral contracts between the typed and untyped modules to enforce soundness. Typed Racket is an example of such system. (citation)

We note that the number of different ways in which we can annotate a program with n modules in such a system is @${2^n}.

@section{Micro-Gradual Typing}
Macro-graual typing allows the programmer to add type annotations to every expression that can be typed in the program. It does not rely on behavioral contracts. Instead annotates all untyped parts of the program with type Dyn (citation) and adds casts to these parts during runtime.

Here, we note that there are many more different ways we can annotate a program compared to micro-gradual typing. For a program with n atomic expressions, we can annotate it in @${2^n} different ways.

@section{Reticulated Python}
Reticulated Python is a micro-gradual typing system. It's implemented as a source-to-source translator, which means that it takes a Python program and generates Python code after adding the necessary checks to typecheck the program. The code is then executed as regular Python. paper@~cite[vksb-dls-2014]
There focus of our measurements is on transient semantics. The main idea is that during runtime, we check that the target type of a given value is consistent with its current type. We achieve that by inserting casts at the points of interaction between typed and untyped code in our program. The formal definition of consistency can be found in [?], but in the context of micro-gradual typing, we can think of two types as being consistent if they are the same up to Dyn.

