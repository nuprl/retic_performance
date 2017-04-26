
#lang gm-dls-2017
@title[#:tag "sec:reticulated"]{Gradual Typing}


A gradual typing system allows programmers to add type annotations to their code incrementally while providing soundness guarantees for the code in runtime.

The granularity of such type systems vary from language to language. For example, in Typed Racket we can only type modules as a whole but not smaller expressions, while Reticulated Python allows us to type individual function arguments, function return types and class fields. The only expressions that are currently typable in Reticulated Python follow idiomatic Python @note{@url{https://www.python.org/dev/peps/pep-0484/}} therefore we cannot expect to annotate assignment statements or any statements in general. 

Furthermore, Reticulated Python does not support generics @~cite[vksb-dls-2014], which according to Vitousek et al. is a constraint for how typable some expressions are in Reticulated Python. Expressions that would require generic types are annotated using type Dyn.


Reticulated Python has three modes of implementation: Monotonic, Guarded and Transient, each with a different way of providing soundness guarantees. Our analysis uses Transient mode.

In transient type semantics, objects are wrapped with a cast containing a target type. In line 4, the target type would be int. During runtime that cast checks that the target type is consistent with the type the given object already has. In Transient semantics, the object does not permanently get wrapped in proxies to determine its target type which means that during runtime an object can be mutated with a value of a new type. Transient addresses this by inserting extra checks at various points of the code to insure that the object's current type did not change incorrectly as a result of mutation. 

@python{
1 def f(x:int)->str:
2 return str(x)
3
4 f(x)
}


