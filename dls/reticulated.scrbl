
#lang gm-dls-2017
@title[#:tag "sec:reticulated"]{Gradual Typing}


A gradual typing system allows programmers to add type annotations to their programs incrementally while providing soundness guarantees for the program in runtime.

The granularity of such type system varies from language to language. For example, in Typed Racket we can only type modules as a whole but not smaller expressions, while Reticulated Python allows us to type individual function arguments, function return types and class fields. We cannot type statements like "x=4". The only expressions that are currently typable in Reticulated Python follow idiomatic Python the https://www.python.org/dev/peps/pep-0484/

Furthermore, Reticulated Python does not support generics http://homes.soic.indiana.edu/mvitouse/papers/dls14.pdf, which according to Vitousek et al. is a constraint for how typable some expressions in Reticulated Python are. For example, to annotate List[x], we would have to use Dyn.

Reticulated Python is implemented as a source-to-source translator, which means that it takes a Python program and generates Python code after adding the necessary checks to typecheck the program. The code is then executed as regular Python. paper@~cite[dls-2014]. It has three modes of implementation: Monotonic, Guarded and Transient, each with a different way of providing soundness guarantees. Our analysis uses Transient mode.

In transient type semantics, objects are wrapped with a cast containing a target type. In line 4, the target type would be int. During runtime that cast checks that the target type is consistent with the type the given object already has. In Transient semantics, the object does not permanently get wrapped in proxies to determine its target type which means that during runtime an object can be mutated with a value of a new type. Transient addresses this by inserting extra checks at various points of the code to insure that the object's current type did not change incorrectly as a result of mutation. 



1 def f(x:int)->str:
2 return str(x)
3
4 f(x)



