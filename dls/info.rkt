#lang info
(define collection "gm-dls-2017")
(define deps '(
  "base"
  "at-exp-lib"
  "math-lib"
  "pict-lib"
  "plot-lib"
  "scribble-lib"
  "with-cache"
))
(define build-deps '(
  "rackunit-abbrevs"
  "rackunit-lib"
))
(define pkg-desc "Source for _Performance Evaluation of Reticulated Python_")
(define version "0.1")
(define pkg-authors '(ben zeina))
(define raco-commands '(
  ("rp-info" (submod gm-dls-2017/script/benchmark-info main) "Print static benchmark info" #f)
  ("rp-plot" (submod gm-dls-2017/script/plot main) "Render overhead plot" #f)
  ("rp-perf" (submod gm-dls-2017/script/performance-info main) "Print performance statistics" #f)
  ("rp-python" (submod gm-dls-2017/script/python main) "Parse and query Python programs" #f)
  ("rp-sample" (submod gm-dls-2017/script/sample main) "Generate samples for a benchmark" #f)
))
