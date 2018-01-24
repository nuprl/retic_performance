#lang info
(define collection 'multi)
(define deps '(
  "at-exp-lib"
  "base"
  "html-parsing"
  "math-lib"
  "pict-lib"
  "plot-lib"
  "scribble-lib"
  "slideshow-lib"
  "sxml"
  "with-cache"
))
(define build-deps '(
  "pict-doc"
  "racket-doc"
  "rackunit-abbrevs"
  "rackunit-lib"
  "scribble-doc"
))
(define pkg-desc "A performance evaluation of Reticulated Python")
(define version "0.2")
(define pkg-authors '(ben zeina))
(define raco-commands '(
  ("plateau-info" (submod gm-pepm-2018/script/benchmark-info main) "Print static benchmark info" #f)
  ("plateau-plot" (submod gm-pepm-2018/script/plot main) "Render overhead plot" #f)
  ("plateau-perf" (submod gm-pepm-2018/script/performance-info main) "Print performance statistics" #f)
  ("plateau-python" (submod gm-pepm-2018/script/python main) "Parse and query Python programs" #f)
  ("plateau-sample" (submod gm-pepm-2018/script/sample main) "Generate samples for a benchmark" #f)
))
(define scribblings '(("docs/gm-pepm-2018.scrbl" () (omit))))
(define compile-omit-paths '("benchmarks" "data" "karst" "pre-benchmarks" "script"))
(define test-omit-paths '("benchmarks" "data" "karst" "pre-benchmarks" "script"))
