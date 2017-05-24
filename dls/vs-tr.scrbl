#lang gm-dls-2017

@title[#:tag "sec:vs-tr"]{Why is Reticulated so Fast ...}

Reticulated lacks support for unions, recursive types and variable-arity functions.
Additionally, Reticulated's error messages rarely provide actionable feedback. Finally, Reticulated guarantees an alternative notion of type soundness.
These factors contribute to the seemingly-improved relative performance of Reticulated.
The worst slowdown we observe in Reticulated is within one order of magnitude.
By contrast, many partially typed Typed Racket programs are two orders of
 magnitude slower than their untyped counterparts@~cite[takikawa-popl-2016 greenman-jfp-2017].
While implementation technology and the peculiarities of the programs
 affect performance, this order-of-magnitude gap suggests fundamental differences
 between Typed Racket and Reticulated. 

@section{Missing Types}
@(define pystone-union-fields
        @; grep for 'PtrComp = ' to find assignments
        @; It's initially `None`, and assigned away-from and back-to `None`
        @;  in `Proc1`
        '(PSRecord.PtrComp))
@(define stats-union-functions
        @; Most of these functions all have a dead-giveaway pair of lines:
        @; ```
        @;  if type(cols) not in [list,tuple]:
        @;      cols = [cols]
        @; ```
        '(abut simpleabut colex linexand recode))
@(define dyn* '(go pystone stats take5))
@; TODO add better in-file evidence

@Integer->word[(length dyn*)] of our benchmarks must resort to dynamic typing
 because Reticulated cannot express the desired type.
The @bm{pystone} and @bm{stats} benchmarks require union types.
The @bm{go} benchmark contains a recursive class type.
Fourth, one function in the @bm{take5} benchmark accepts optional arguments.@note{@url{https://github.com/mvitousek/reticulated/issues/32}}

If Reticulated cannot express such types, Python programmers will frequently
 need to rewrite their programs before they can try gradual typing.
We rewrote several benchmarks that used @tt{None} as
 a default value to use a well-typed sentinel value.

Such rewrites are both time-consuming and prone to introduce bugs.
Developers would benefit if Reticulated added support for these types.
Indeed, @|PEP-484| specifies syntax for generics, untagged union types,
 recursive types, optional arguments, and keyword arguments.

Enforcing these types at run-time, however, will impose a higher cost than
 the single-test types that Reticulated programmers must currently use.
A union type or (equi-)recursive type requires a disjunction of type tests, and
 a variable-arity procedure requires a sequence of type checks.
If, for example, every type annotation @${T} in our benchmarks was instead a
 union type with @${T} and @tt{Void}, then overall performance would be nearly
 2x worse.


@section{Uninformative Errors}
@(define vss-popl-2017-benchmarks
   '(callsimple nqueens pidigits meteor fannkuch nbody callmethod
     callmethodslots pystone float chaos go spectralnorm))
@(define vss-2x-benchmarks
   '(nqueens meteor fannkuch callmethod callmethodslots pystone float chaos go))

Errors matter@~cite[f-keynote-2002].
When systems work, everyone is happy, but when systems break, developers want error messages that pinpoint the source of the fault.
Two kinds of "faults" can occur in Reticulated. Static type errors and dynamic type errors.
While Reticulated produces decent error messages for static type errors, it fails to produce quality error messages for dynamic type errors.
For dynamic type errors the developer wants to know the value which caused the error, the type information related to the error and the type boundary where the code went wrong.

Consider the following error message obtained by calling @code{dyn_add_cash(20)} from section 2.

@python{
Traceback (most recent call last): File "Currency.py", line 4, in
  check0 self.dollars = d AttributeError: 'int' object has no
  attribute 'dollars'

During handling of the above exception, another exception occurred:

Traceback (most recent call last): File
  "/Library/Frameworks/Python.framework/Versions/3.4/bin/retic", line
  9, in <module> load_entry_point('retic==0.1.0', 'console_scripts',
  'retic')() File
  "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/retic-0.1.0-py3.4.egg/retic/retic.py",
  line 155, in main reticulate(program, prog_args=args.args.split(),
  flag_sets=args) File
  "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/retic-0.1.0-py3.4.egg/retic/retic.py",
  line 107, in reticulate utils.handle_runtime_error(exit=True) File
  "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/retic-0.1.0-py3.4.egg/retic/retic.py",
  line 102, in reticulate _exec(code, __main__.__dict__) File
  "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/retic-0.1.0-py3.4.egg/retic/exec3/__init__.py",
  line 2, in _exec exec (obj, globs, locs) File "Currency.py", line
  272, in <module> File "Currency.py", line 14, in dyn_add_cash
  c1.add_cash(amount) File "Currency.py", line 10, in check0
    
retic.transient.CheckError: 20
}

In this case, Reticulated does not give type information about the wrong
argument @code{20} or the expected value of @code{add_cash}, nor does
it point to the location of the error.  Instead, it supplies a stack
trace and a value that fails some check, leaving the programmar to
deduce the error without much aid from error message.

For flat types, these clues may suffice to deduce the type
 check that halted the program.
@;;;To illustrate, consider the following small program:
@;;;
@;;;@nested[@python|{
@;;;def id(x)->Int:
@;;;  return x
@;;;id(None)
@;;;}|]@;
@;;;running this program produces the following error message:
@;;;
@;;;@nested[@exact|{{\footnotesize\begin{verbatim}
@;;;Traceback (most recent call last):
@;;;  File "/usr/local/bin/retic", line 6, in <module>
@;;;    retic.main()
@;;;  File ".../reticulated/retic/retic.py", line 155, in main
@;;;    reticulate(program, prog_args=args.args.split(), flag_sets=args)
@;;;  File ".../reticulated/retic/retic.py", line 104, in reticulate
@;;;    utils.handle_runtime_error(exit=True)
@;;;  File ".../reticulated/retic/retic.py", line 102, in reticulate
@;;;    _exec(code, __main__.__dict__)
@;;;  File ".../reticulated/retic/exec3/__init__.py", line 2, in _exec
@;;;    exec (obj, globs, locs)
@;;;  File "test.py", line 3, in <module>
@;;;    id(None)
@;;;  File "test.py", line 2, in id
@;;;    return x
@;;;  File ".../reticulated/retic/runtime.py", line 91, in check_type_int
@;;;    return val if isinstance(val, int) else (check_type_bool(val) if not flags.FLAT_PRIMITIVES else rse(val))
@;;;  File ".../reticulated/retic/runtime.py", line 100, in check_type_bool
@;;;    return val if isinstance(val, bool) else rse(val)
@;;;  File ".../reticulated/retic/runtime.py", line 88, in rse
@;;;    raise Exception(x)
@;;;Exception: None
@;;;\end{verbatim}}}|]@;
For function types and parameterized types, the relevant annotation is
 slightly harder to find, but still possible via the stack trace.
Unfortunately, such annotations are useless if they are correct.
If the fault is due to a bad value, the programmer must inspect the program to
 find where it came from.

Refining the error messages will add performance overhead.
For example, @citet[vss-popl-2017] built an extension to Reticulated that improves these
 error messages by reporting all casts that may have led to the dynamic type error.
Their evaluation reports that @|t/p-ratio| may double"

@section{Alternative Soundness}

Sound type systems are useful because they provide guarantees.
If a static type system proves that a term has type @${\tau}, then @${\tau}
 specifies the term's behavior.
The type system can use this specification to find small logical errors throughout a program;
 the compiler can rely on this specification to generate efficient code;
 the programmer can trust this specification as an API.

Consider the following notion of soundness:

If a program type-checks, running it can result in one of the following outcomes:

@itemlist[#:style 'ordered
@item{
Execution terminates, returning and printing values of the predicted type.
}
@item{
Execution diverges.
}
@item{
Execution ends in one of a number of well-specified exception states.
}
@item{
Execution ends in an exceptional state and points to one of the boundaries between typed and untyped code.
}
]

The first three outcomes are from the soundness theorem, and apply to fully typed code. The four outcomes together are a generalization of the soundness theorem to include partially typed code.

Reticulated defines gradual typing soundness is to modify the first clause to only guarantee tag-level soundness. Reticulated also modifies the fourth clause so that it points to a number of boundaries between typed and untyped code.

@; -------------------------------------------------------
@; MF: we should put a visual marker here, like a line 
@(define running 
  @exact{\par \noindent \hrulefill \par \noindent Running this program yields:})

@;;;; maybe make one of these cases a nested list
@figure["fig:magic"
        @list{A well-typed Reticulated program}]{
@python|{
    def make_strings()->List(String):
      xs = []
      for i in range(3):
        if   i == 0: xs.append(i)
        elif i == 1: xs.append(True)
        else       : xs.append(make_strings)
      return xs

    make_strings()
}|}


As @figure-ref{fig:magic} demonstrates, a Reticulated term with type @tt{List(String)} may evaluate to a list containing any kind of data.
On one hand, this fact is harmless since tag soundness implies that any read from a variable with type @tt{List(String)} is tag-checked.
On the other hand, Reticulated does not guard values that exit typed regions.
Thus, two interesting scenarios can arise:
@itemlist[#:style 'ordered
@item{
  (the @emph{typhoid mary} scenario) Typed code can create an ill-typed value,
  pass it to untyped code, and trigger an error by violating an implicit
  assumption in the untyped code.
  The source of such ``disguised'' type errors is difficult to track down.
}
@item{
  (the @emph{sybil} scenario) Two typed contexts can safely reference the same value at incompatible types.
}
]@;
It remains to be seen whether these potential scenarios cause problems in practice.
Developers may embrace the flexibility of tag-soundness and use Reticulated
 in combination with unit tests.
At the moment, the only conclusion our data supports is that Reticulated's
 tag checks impose less performance overhead than Typed Racket's behavioral contracts.

