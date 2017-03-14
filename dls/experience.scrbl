#lang scribble/acmart
@require[
  "common.rkt"
]
@section{Experience}

% add code samples
% site masked types (myers 2012?)

@subsection{import * }

Consider the following python program:

@; \begin{python}
@; from sys import *
@;
@; for line in stdin:
@;     print(line)
@; \end{python}

Running the program we get the following result

@; \begin{verbatim}
@; WARNING: Unable to import type definitions
@; from sys due to *-import
@; \end{verbatim}

@;     Since Evolution had multiple types, all @pythoninline{*} imports had to be removed
@;     and file name has to be explicitly imported. 
@;     
@; 
@;  \subsection{Union Types,}
@;  can't use none to initialize fields (lisp interpreter)
@; %  Site example from a standard python library
@; 
@;     
@; \subsection{ Missing the set base type}
@;  The following was a function in Espionage:
@; 
@;  \begin{python}
@;  def convert_to_set(res):
@;     res_tuple=set()
@;     for r in res:
@;         (e1, e2, w) = r
@;         res_tuple.add((e1, e2))
@;     return res_tuple
@;  \end{python}
@;  
@;     Since reticulated python was missing the set base type, the program had to
@;     be modified to use lists.
@; 
@; 
@;  \subsection{Error handling}   
@; Issues with error messages for type errors (they do not point to the location of the error)
@; give an example. 
@; 
@; 

