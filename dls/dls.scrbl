#lang gm-dls-2017 @anonymous @sigplan @10pt

@;title{Performance Evaluation of Reticulated Python}
@title{Is Gradual Typing Alive?}

@(define NEU
   @affiliation[
     #:institution "Northeastern University"
     #:city "Boston"
     #:state "Massachusetts"
     #:postcode "02115"
     #:country "USA"])

@author["Ben Greenman"
        #:email "types@ccs.neu.edu"
        #:orcid "0000-0001-7078-9287"
        #:affiliation NEU]

@author["Zeina Migeed"
        #:email "abdelmigeed.z@husky.neu.edu"
        #:affiliation NEU]

@; -----------------------------------------------------------------------------

@terms{CS}
@keywords{CS}

@include-section{introduction.scrbl}
@include-section{reticulated.scrbl}
@include-section{methodology.scrbl}
@include-section{benchmarks.scrbl}
@include-section{measuring.scrbl}
@include-section{threats.scrbl}
@include-section{vs-tr.scrbl}
@include-section{linear.scrbl}
@include-section{experience.scrbl}
@include-section{conclusion.scrbl}

@acks{
  Matthias for all things.
  Mike for Reticulated, bugfixes.
  Sam for access to IU cluster.
  Spenser Bauman for advice about cluster.
}

@generate-bibliography[]
