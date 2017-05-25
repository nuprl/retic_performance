#lang gm-dls-2017
@title[#:style 'unnumbered]{Appendix}

@figure-here["fig:badcode" @elem{Reticulated program @tt{myfile.py}}
@python|{
def make_strings()->List(String):
    xs = []
    for i in range(3):
        if   i == 0: xs.append(i)
        elif i == 1: xs.append(True)
        else       : xs.append(make_strings)
    return xs

def get_lengths(los:List(String))->List(Int):
    return [strlen(s) for s in los]

def strlen(s:String)->Int:
    return len(s)

strs = make_strings()
get_lengths(strs)
}|]

@figure["fig:errmsg" @elem{Reticulated's error message for @figure-ref{fig:badcode}}
@exact|{\footnotesize\raggedright\begin{verbatim}
Traceback (most recent call last):
  File "/.../retic", line 9, in <module>
    load_entry_point('retic==0.1.0',
                     'console_scripts',
		     'retic')()
  File "/.../retic/retic.py", line 155, in main
    reticulate(program,
               prog_args=args.args.split(),
	       flag_sets=args)
  File /.../retic/retic.py", line 104, in reticulate
    utils.handle_runtime_error(exit=True)
  File "/.../retic/retic.py", line 102, in reticulate
    _exec(code, __main__.__dict__)
  File "/.../retic/exec3/__init__.py", line 2, in _exec
    exec (obj, globs, locs)
  File "myfile.py", line 16, in <module>
    get_lengths(strs)
  File "myfile.py", line 10, in get_lengths
    return [strlen(s) for s in los]
  File "myfile.py", line 10, in <listcomp>
    return [strlen(s) for s in los]
  File "myfile.py", line 12, in strlen
    def strlen(s:String)->Int:
  File "/.../retic/runtime.py", line 109, in
      check_type_string
    return val if isinstance(val, str) else rse()
  File "/.../retic/runtime.py", line 88, in rse
    raise Exception(x)
Exception: None
\end{verbatim}}|]

@Figure-ref{fig:badcode} is a small Reticulated program that commits a dynamic type error. This program produces the error message in @figure-ref{fig:errmsg}. The message consists of a stack trace and the name of a failing check, as described in @section-ref{sec:vs-tr:errors}.
