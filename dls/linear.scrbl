#lang gm-dls-2017
@title[#:tag "sec:linear"]{Linear Measurements Suffice, Again}

@(define TO-SAMPLE
   '(Espionage Evolution PythonFlow chaos futen pystone sample_fsm_python slowSHA take5))
@(define BENCHMARKS-TO-SAMPLE
   (filter (λ (bm) (memq (benchmark->name bm) TO-SAMPLE)) ALL-BENCHMARKS))

@figure["fig:sample" "Valdiating Linear Measurements"
  @render-validate-samples-plot*[BENCHMARKS-TO-SAMPLE]
]
