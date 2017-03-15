#lang scribble/acmart
@require[
  "common.rkt"
]
@title[#:tag "sec:methodology"]{Methodology}

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
