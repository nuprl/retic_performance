#lang gm-dls-2017

@title[#:tag "sec:vs-tr"]{Why is Reticulated so Fast ...}

The worst slowdown we observe in Reticulated is within one order of magnitude.
By contrast, many partially typed Typed Racket programs are two orders of
 magnitude slower than their untyped counterparts@~cite[takikawa-popl-2016 greenman-jfp-2017].
While implementation technology and the peculiarities of the benchmarks
 affect performance, this order-of-magnitude gap suggests fundamental differences.

We have identified three factors that contribute to the relative
 performance of Reticulated.
First, Reticulated's type system lacks support for unions, recursive types,
 and variable-arity functions.
Second, Reticulated's error messages rarely provide actionable feedback.
Third, Reticulated guarantees an alternative notion of type soundness.
All three factors affect not only performance, but also Reticulated programmers.


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
First and second, the @bm{pystone} and @bm{stats} benchmarks require union types.
Third, the @bm{go} benchmark contains a recursive class type.
Fourth, one function in the @bm{take5} benchmark accepts optional arguments.@note{@url{https://github.com/mvitousek/reticulated/issues/32}}

If Reticulated cannot express such types, Python programmers will frequently
 need to rewrite their programs before they can try gradual typing.
In our own experience, we rewrote several benchmarks that used @tt{None} as
 a default value to use a well-typed sentinel value.
We also attempted to rewrite a shallowly-embedded Lisp interpreter to use a
 deep-embedding, but stopped for the lack of recursive types.

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
When systems work, everyone is happy, but when systems break, developers really
 want error messages that pinpoint the source of the fault.

Reticulated currently produces simple error messages that supply (1) a value
 that failed some check and (2) a stack trace.
For flat types, these clues often suffice to deduce the type
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

Improving the error messages will add performance overhead.
For example, @citet[vss-popl-2017] built an extension to Reticulated that improves these
 error messages by reporting all casts that may have led to the dynamic type error.
Their evaluation reports the @|t/p-ratio|s of
 @integer->word[(length vss-popl-2017-benchmarks)]
 programs from @|TPPBS|; in @integer->word[(length vss-2x-benchmarks)]
 programs, adding blame tracking to the fully-typed configuration
 at least doubled the @|t/p-ratio|.


@section{Alternative Soundness}

Sound type systems are useful because they provide guarantees.
If a static type system proves that a term has type @${\tau}, then @${\tau}
 specifies the term's behavior.
The type system can use this specification to find small logical errors throughout a program,
 the compiler can rely on this specification to generate efficient code,
 and the programmer can trust this specification as an API.

Gradual typing systems cannot provide exactly the same guarantees,
 but Typed Racket's soundness is quite similar to conventional soundness.
In Typed Racket, typed code is sound in the conventional sense; for example, the
 compiler may use the types to eliminate run-time tag-checks@~cite[sthff-padl-2012].
Untyped code is quarantined.
An untyped value @${v} can only cross the boundary into typed code via
 a type @${\tau}.
Typed Racket enforces the behavioral specification implied by @${\tau}
 by compiling the type to a contract; if @${v} does not satisfy the contract,
 the programmer receives an error message containing @${v}, @${\tau}, and
 the relevant boundary@~cite[tfffgksst-snapl-2017].

@; -------------------------------------------------------
@; MF: we should put a visual marker here, like a line 
@(define running 
  @exact{\par \noindent \hrulefill \par \noindent Running this program yields:})

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

Reticulated takes an alternative approach.
It guarantees tag-level soundness.
As @figure-ref{fig:magic} demonstrates, a Reticulated term with type @tt{List(String)} may evaluate to a list containing any kind of data.
On one hand, this fact is harmless since tag soundness implies that any read from a variable with type @tt{List(String)} is tag-checked.
On the other hand, Reticulated does not guard values that exit typed regions.
Thus, two interesting scenarios can arise:
@itemlist[#:style 'ordered
@item{
  (the @emph{typhoid mary} scenario) Typed code can create an ill-typed value,
  pass it to untyped code, and trigger an error by violating an implicit
  assumption in the untyped code.
  The source of such ``disguised'' type errors may be difficult to track down.
}
@item{
  (the @emph{sybil} scenario) Two typed contexts can safely reference the same value at incompatible types.
}
]@;
It remains to be seen whether these potential scenarios cause practical issues.
Developers may embrace the flexibility of tag-soundness and use Reticulated
 in combination with unit tests.
At the moment, the only conclusion our data supports is that Reticulated's
 alternative soundness imposes significantly less performance overhead than
 Typed Racket's behavioral contracts.
@;On one hand, Reticulated types cannot enforce datatype invariants, e.g.,
@; the class declaration in @section-ref{sec:reticulated} cannot guarantee that
@; all instances of the @tt{Cash} class have integer-valued fields.
@;On the other hand, developers may value the increased flexibility and pay-as-you-annotate
@; cost model.


@;@figure["fig:no-magic" 
@;        #:style @left-figure-style
@;	@list{An equivalent well-typed Typed Racket program}]{
@;@; MF: I'd really like 2-space indentation in all code displays 
@;@verbatim[#:indent 2]{
@;#lang racket
@;
@;(module add-one-module typed/racket
@;  (provide add-one)
@;  (define (add-one {los : [Listof Integer]})
@;    (append los (list 1))))
@;
@;(require 'add-one-module)
@;
@;(displayln (add-one '("a" "b")))
@;}
@;
@;@running 
@;
@;@verbatim[#:indent 2]{
@;add-one: contract violation
@;  expected: Integer
@;  given: "a"
@;}
@;}
