#lang gm-dls-2017
@require[racket/list]
@title[#:tag "sec:measurements"]{Measuring Reticulated Python}

@section{The Deliverable Count}

@section{Results}

@figure*["fig:overhead" "Proportion of D-deliverable configurations"
  @render-overhead-plot*[ALL-BENCHMARKS]
]

@figure*["fig:exact" "Exact running times (sec)"
  @render-exact-runtime-plot*[ALL-BENCHMARKS]
]
