#lang scribble/acmart @anonymous @; @review
@; @9pt ???
@require[
  "common.rkt"
]


@title{Performance Evaluation of Reticulated Python}
@author{Ben Greenman}
@email|{types@ccs.neu.edu}|
@affiliation{
  @department{College of Computer and Information Science}
  @institution{Northeastern University}
  @city{Boston}
  @state{Massachusetts}}
@orcid{0000-0001-7078-9287}

@author{Zeina Migeed}
@email|{abdelmigeed.z@husky.neu.edu}|
@affiliation{
  @department{College of Computer and Information Science}
  @institution{Northeastern University}
  @city{Boston}
  @state{Massachusetts}}

@copyrightyear{2017}

@; -----------------------------------------------------------------------------
@abstract{
  Gradual typing promises to combine the benefits of dynamic and static typing
  disciplines in a single language, giving developers freedom to use type
  information only where it proves useful for catching bugs, documenting
  interfaces, or enabling optimizations.  Reticulated Python is one such
  @emph{gradually typed} language; it gives Python programmers the ability to
  incrementally add sound, optional type annotations to critical parts of their
  programs.  Reticulated preserves type soundness by adding dynamic type tests
  to a program.  These tests can arbitrarily degrade the performance of
  programs, but their effect on partially-typed variations of realistic
  programs is unknown.

  This paper studies the overhead of gradual typing in Reticulated Python.  We
  examine @|NUM-BENCHMARKS| programs taken from a variety of areas including
  Python libraries, implementations of common algorithms, and games.  For each
  program we systematically measure all partially-typed @emph{configurations}
  obtained by assigning full type signatures to a subset of functions in the
  program.  For a program with @${n} functions we obtain  @${2^n} configurations.
  We additionally sample random configurations in which any subset of class
  fields, function parameters, or function return types may be typed.  Finally
  we attempt to explain which functions or types are responsible for the
  greatest overhead and generalize common patterns.
}
@terms{CS}
@keywords{CS}
@maketitle[]

@include-section{introduction.scrbl}
@include-section{reticulated.scrbl}
@include-section{benchmarks.scrbl}
@include-section{methodology.scrbl}
@include-section{threats.scrbl}
@include-section{experience.scrbl}
@include-section{conclusion.scrbl}

@acks{
  Hidden for double-blind review.
}
@;{
  Matthias for all things.
  Mike for Reticulated, bugfixes.
  Sam for access to IU cluster.
  Spenser Bauman for advice about cluster.
}
