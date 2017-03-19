#lang scribble/acmart
@require[
  "common.rkt"
]
@title[#:tag "sec:reticulated"]{Reticulated}

This section introduces reticulated python and gradual typing

@; Is it a whole program analysis i.e if module a is prereq. of module b, does b get compiled again even if b has
@; already been type-checked?


@itemlist[
@item{
  Brief intro on reticulated and gradual typing
}
@item{
  Definition of type soundness
}
@item{
  Definition for transient mode
}
@item{
  Examples of what types we can write and where to put the annotations (ex: puting annotations on class fields/ functions)
}
@item{
  Examples on how transient catches type errors
}
@item{
  Examples on how errors could still get through
  despite having the wrong types
}
@item{
  Talk about blame
}
]




