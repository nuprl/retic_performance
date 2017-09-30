#lang gm-pepm-2018 @sigplan

@require[(for-syntax racket/base)]

@; You see, there are two kinds of people in this world: the workers and the
@; hustlers.  The hustlers never work and the workers never hustle.  And you,
@; my friend, are a worker.  God knows I've tried to beat that instinct out of
@; him... but it's there ingrained in your immigrant blood.  Look how tasty your
@; cocktails are.  Look how clean you keep your bar.  Why, man, you actually
@; take pride in your work. --- Cocktail, 1988

@title{On the Cost of Soundness for Gradual Typing}

@(define ANONU
   @affiliation[
     #:institution "Anonymous University"
     @;#:city "Boston"
     @;#:state "Massachusetts"
     @;#:postcode "02115"
     @;#:country "USA"
   ])

@(define NEU
   @affiliation[
     #:institution "Northeastern University"
     @;#:city "Boston"
     @;#:state "Massachusetts"
     @;#:postcode "02115"
     @;#:country "USA"
   ])

@author["Anonymous Author(s)" #:affiliation ANONU]

@;@author["Ben Greenman"
@;        #:email "benjaminlgreenman@gmail.com"
@;        #:orcid "0000-0001-7078-9287"
@;        #:affiliation NEU]
@;
@;@author["Zeina Migeed"
@;        #:email "migeed.z@outlook.com"
@;        #:affiliation NEU]

@acmConference["ACM Conference" "2018" "Washington, DC, USA"]
@acmYear{2018}

@; -----------------------------------------------------------------------------

@abstract{
  Gradual typing promises to reduce the cost of software maintenance for
   dynamically typed languages.
  In a language with a gradual typing system, developers
   can add type annotations to a portion of a code base after they
   reconstruct its type during some maintenance action.
  As Takikawa @|etal|'s recent work shows, however, the addition of type
   annotations comes at a large cost in performance.
  In particular, performance evaluations of Typed Racket suggest that a
   conventionally sound gradual typing system may slow down a working system by
   two orders of magnitude.


  Since different gradual typing systems satisfy different notions of
   soundness, the question then arises: what is the cost of such varying notions of soundness?
   This paper answers an instance of this question by applying Takikawa @|etal|'s evaluation
   method to Reticulated Python, which in contrast to Typed Racket, satisfies a more relaxed
   notion of soundness which we refer to as tag soundness. We find that the cost
   of soundness in Reticulated is at most one order of magnitude. Substantial user studies
   are needed to determine whether programmers will accept tag soundness.
  
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

@if-techrpt[@include-section{appendix.scrbl}]
