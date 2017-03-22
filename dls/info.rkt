#lang info
(define collection "gm-dls-2017")
(define deps '(
  "base"
  "scribble-lib"
  "with-cache"
))
(define build-deps '(
  "rackunit-lib"
  "rackunit-abbrevs"
))
(define pkg-desc "Source for _Performance Evaluation of Reticulated Python_")
(define version "0.1")
(define pkg-authors '(ben zeina))
(define raco-commands '(
  ("rp-perf" (submod gm-dls-2017/script/performance-info main) "Print performance statistics" #f)
))
