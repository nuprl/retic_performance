#lang scribble/manual

@title{Using the Datasets}

The @racketmodname[gm-dls-2017] package includes command-line tools for
 interacting with a dataset.

These tools are defined in modules under the @filepath{script/} folder and are
 declared in the @filepath{info.rkt} file for @racketmodname[gm-dls-2017].

@itemlist[
@item{
  @tt{rp-info} : print static information about a given benchmark
}
@item{
  @tt{rp-plot} : render a plot, similar to plots in the paper
}
@item{
  @tt{rp-perf} : print summary information about a benchmark's performance
}
@item{
  @tt{rp-python} : analyze Python and Reticulated programs
}
@item{
  @tt{rp-sample} : choose random configurations to sample
}
]

Example: to generate an overhead plot for @tt{Espionage}, run:

@nested[#:style 'inset
  @exec{raco rp-plot Espionage}
]

For more information about a command @tt{CMD}, run:

@nested[#:style 'inset
  @exec{raco CMD --help}
]
