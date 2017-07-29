#lang gm-plateau-2017 @sigplan @10pt

@; You see, there are two kinds of people in this world: the workers and the
@; hustlers.  The hustlers never work and the workers never hustle.  And you,
@; my friend, are a worker.  God knows I've tried to beat that instinct out of
@; him... but it's there ingrained in your immigrant blood.  Look how tasty your
@; cocktails are.  Look how clean you keep your bar.  Why, man, you actually
@; take pride in your work. --- Cocktail, 1988

@title{On the Cost of Soundness for Gradual Typing}

@(define NEU
   @affiliation[
     #:institution "Northeastern University"
     @;#:city "Boston"
     @;#:state "Massachusetts"
     @;#:postcode "02115"
     @;#:country "USA"
   ])

@author["Ben Greenman"
        #:email "benjaminlgreenman@gmail.com"
        #:orcid "0000-0001-7078-9287"
        #:affiliation NEU]

@author["Zeina Migeed"
        #:email "migeed.z@outlook.com"
        #:affiliation NEU]

@; -----------------------------------------------------------------------------

@abstract{
  Gradual typing promises to reduce the cost of software maintenance for
  scripts. In a scripting language with a gradual typing system, developers
  can add type annotations to the untyped portion of a code base after they
  reconstruct the type during some maintenance action.  As Takikawa et
  al.'s recent work shows, however, the addition of type annotations comes
  at a large cost in performance. In particular, performance evaluations of
  Typed Racket suggest that a conventionally sound gradual typing system
  may slow down a working system by one to two orders of magnitude.

  Since different gradual typing systems satisfy different notions of
  soundness, the question arises how much the relaxation of soundness
  benefits a program's performance. This paper answers this question by
  applying Takikawa et al.'s evaluation method to Reticulated Python, which
  in contrast to Typed Racket, merely satisfies tag soundness not type
  soundness. Numerically, Reticulated is at least one order of magnitude
  better than Typed Racket in terms of performance. Sadly, the evaluation
  still suggests that the performance degradation is still intolerable for
  most developers. 
}

@;terms{CS}
@;keywords{CS}

@include-section{introduction.scrbl}
@include-section{reticulated.scrbl}
@include-section{method.scrbl}
@include-section{evaluation.scrbl}
@include-section{threats.scrbl}
@include-section{conclusion.scrbl}

@generate-bibliography[]
@;@include-section{appendix.scrbl}
