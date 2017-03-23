#lang gm-dls-2017
@title[#:tag "sec:method"]{Adapting Takikawa et al.'s Method}

For each benchmark, we aimed to choose a set of configurations that represent the overall performance of Reticulated Python, and had size less than x. In our method, we type functions as a whole, yielding 2^n configurations per benchmark, where n is the number of functions in a benchmark. 

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
