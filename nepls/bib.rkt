#lang racket/base

;; Poor man's bibliography for the DLS talk

(provide (all-defined-out))

(require
  racket/string)

;; =============================================================================

(define dls "DLS")
(define popl "POPL")

(define (make-bib #:author a #:title t #:location l #:date d)
  (list a t l d))

(define (authors . str*)
  (string-join str* " and "))

(define (proceedings-location l #:pages [p #f])
  l)

(define (bib->venue b)
  (caddr b))

(define (bib->year b)
  (cadddr b))

(define vksb-dls-2014
  (make-bib
   #:author (authors "Michael M. Vitousek" "Andrew Kent" "Jeremy G. Siek" "Jim Baker")
   #:title "Design and Evaluation of Gradual Typing for Python"
   #:location (proceedings-location dls #:pages '(45 56))
   #:date 2014))

(define vss-popl-2017
  (make-bib
    #:title "Big Types in Little Runtime: Open-World Soundness and Collaborative Blame for Gradual Type Systems"
    #:author (authors "Michael M. Vitousek" "Cameron Swords" "Jeremy G. Siek")
    #:location (proceedings-location popl #:pages '(762 774))
    #:date 2017))

