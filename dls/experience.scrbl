#lang scribble/acmart
@require[
  "common.rkt"
]
@title[#:tag "sec:experience"]{Experience}

  @; add code samples
  @; cite masked types (myers 2012?)

@section{import * }

Consider the following python program:

@python{
   from sys import *

   for line in stdin:
       print(line)
}

Running the program we get the following result

@verbatim{
   WARNING: Unable to import type definitions
   from sys due to *-import
}

Since Evolution had multiple types, all @pythoninline{*} imports had to be removed
and file name has to be explicitly imported. 


@section{Union Types,}
  @;can't use none to initialize fields (lisp interpreter)
  @;  Cite example from a standard python library


@section{Missing the set base type}
The following was a function in Espionage:

@python{
 def convert_to_set(res):
    res_tuple=set()
    for r in res:
        (e1, e2, w) = r
        res_tuple.add((e1, e2))
    return res_tuple
}

Since reticulated python was missing the set base type, the program had to
be modified to use lists.


@section{Error handling}
Issues with error messages for type errors (they do not point to the location of the error)
give an example. 



