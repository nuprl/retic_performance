#lang scribble/manual
@title{Artifact: On the Cost of Type-Tag Soundness}
@author[
  @hyperlink["https://github.com/bennn"]{Ben Greenman}
  @hyperlink["https://github.com/migeed-z"]{Zeina Migeed}
]

This package is a supplement our paper @hyperlink["https://popl18.sigplan.org/event/pepm-2018-on-the-cost-of-type-tag-soundness"]{@emph{On the Cost of Type-Tag Soundness}}.
It contains code to process our datasets and generate the submitted paper.

Local copy: @url{http://www.ccs.neu.edu/home/types/resources/pdf/gm-pepm-2018.pdf}

Source code: @url{https://github.com/nuprl/retic_performance}



@bold{Note}: the code in this package assumes that certain relative paths exist.
 For example, it assumes the Karst datasets are in the folder @filepath{../data/karst}
 relative to the source for the @racketmodname[gm-pepm-2018] package.

@include-section{data.scrbl}
@include-section{reference.scrbl}

