#lang scribble/manual
@title{Artifact: Is Sound Gradual Typing Alive?}
@author[
  @hyperlink["https://github.com/bennn"]{Ben Greenman}
  @hyperlink["https://github.com/migeed-z"]{Zeina Migeed}
]

This package is a supplement to our PLATEAU 2017 submission.
It contains code to process our datasets and generate the submitted paper.

Source code: @url{https://github.com/nuprl/retic_performance}



@bold{Note}: the code in this package assumes that certain relative paths exist.
 For example, it assumes the Karst datasets are in the folder @filepath{../data/karst}
 relative to the source for the @racketmodname[gm-pepm-2018] package.

@include-section{data.scrbl}
@include-section{reference.scrbl}

