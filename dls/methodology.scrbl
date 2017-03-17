#lang scribble/acmart
@require[
  "common.rkt"
]
@title[#:tag "sec:methodology"]{Methodology}

In this section we introduce the method used to evaluate the performance. Since we do not want to run all possible program configurations, we only type functions as a whole, yielding 2^n configurations per benchmark, for n = the number of functions in a benchmark. Using this methods means we assume this is an approximation to how the programmer introduces type annotations to a program. 

@itemlist[
@item{
  Find programs, port to reticulated
}
@item{
  Run against program which generates all possible configurations of the
  program by typing/untyping each function
}
@item{
  Run each configuration for x iterations, recording the time using python's
  system timer
}
@item{
  Machine used was KARST CLUSTER
}

]
