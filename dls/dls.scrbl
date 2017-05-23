#lang gm-dls-2017 @anonymous @sigplan @10pt

@; You see, there are two kinds of people in this world: the workers and the
@; hustlers.  The hustlers never work and the workers never hustle.  And you,
@; my friend, are a worker.  God knows I've tried to beat that instinct out of
@; him... but it's there ingrained in your immigrant blood.  Look how tasty your
@; cocktails are.  Look how clean you keep your bar.  Why, man, you actually
@; take pride in your work. --- Cocktail, 1988

@;title{Performance Evaluation of Reticulated Python}
@;title{Linear Samples Suffice}
@;title{You Get What you Pay For (Gradual Typing for Low, Low Prices)}
@;title{The Cost of Transient}
@title{Is Sound Gradual Typing Alive?}

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

@abstract{Gradual typing empowers developers to freely combine dynamically
  and statically typed code in a single program. A sound gradual
  typing system performs run-time checks to ensure the integrity of types
  at the boundary between typed and untyped code. The question is how much
  such checks affect the performance of gradually typed software systems.

This paper presents a systematic performance evaluation of Reticulated,
  a gradual typing system for Python.  Since Reticulated allows fine-grained
  mixing of typed and untyped code, our evaluation method is to establish a fixed-size
  unit for adding type annotations and measure the performance of all
  possible combinations of typed and untyped code.
  The paper also shows that this exponentially expensive performance evaluation
  method can be approximated with a linear sampling technique. In
  comparison to the performance of Typed Racket---the first gradual typing
  system to be evaluated in a comprehensive manner---the measurements look
  encouraging. On closer inspection, the low cost of run-time checks
  seem to be due to Reticulated's inexpressive type system,
  spartan error messages, and alternative notion of type soundness. }

@;terms{CS}
@;keywords{CS}

@include-section{introduction.scrbl}

@include-section{reticulated.scrbl}
@include-section{method.scrbl}
@include-section{exhaustive.scrbl}
@include-section{linear.scrbl}
@include-section{threats.scrbl}
@include-section{vs-tr.scrbl}
@include-section{conclusion.scrbl}

@acks{
  Matthias for all things.
  Mike for Reticulated, bugfixes.
  Sam for access to IU cluster.
  Spenser Bauman for advice about cluster.
  Tony GJ for insisting that overhead plots are CDFs.
  @;note{Computed using David A. Wheeler's @hyperlink["https://www.dwheeler.com/sloccount/"]{@tt{sloccount}} utility.}
}

@generate-bibliography[]
