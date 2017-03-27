#lang info
(define collection "gm-dls-2017")
(define deps '(
  "base"
  "at-exp-lib"
  "scribble-lib"
  "with-cache"
))
(define build-deps '(
  "math-lib"
  "rackunit-lib"
  "rackunit-abbrevs"
))
(define pkg-desc "Source for _Performance Evaluation of Reticulated Python_")
(define version "0.1")
(define pkg-authors '(ben zeina))
(define raco-commands '(
  ("rp-plot" (submod gm-dls-2017/script/plot main) "Render overhead plot" #f)
  ("rp-perf" (submod gm-dls-2017/script/performance-info main) "Print performance statistics" #f)
  ("rp-sample" (submod gm-dls-2017/script/sample main) "Generate samples for a benchmark" #f)
))
