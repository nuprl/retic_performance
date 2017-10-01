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
  Gradual typing systems ensure type soundness by transforming static type
   annotations into run-time checks.
  These checks provide semantic guarantees, but may come at a large cost in
   performance.
  In particular, recent work by Takikawa @|etal| suggests that enforcing a
   conventional form of type soundness may slow a program by two orders of magnitude.

  Since different gradual typing systems satisfy different notions of
   soundness, the question then arises: what is the cost of such varying
   notions of soundness?
  This paper answers an instance of this question by applying
   Takikawa @|etal|'s evaluation method to Reticulated Python, which satisfies
   a notion of type-tag soundness.
  We find that the cost of soundness in Reticulated is at most one order of
   magnitude.
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
