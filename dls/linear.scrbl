#lang gm-dls-2017
@title[#:tag "sec:linear"]{Linear Measurements Suffice, Again}

@figure*["fig:validate-sample" "Valdiating Linear Measurements"
  (parameterize ([*PLOT-HEIGHT* 100])
    @render-validate-samples-plot*[VALIDATE-BENCHMARKS])
]

@figure["fig:sample:static-benchmark" "Static summary of benchmarks"
  @render-static-information[SAMPLE-BENCHMARKS]]

@figure*["fig:sample" "Linear Measurements"
  (parameterize ([*PLOT-HEIGHT* 100])
    @render-samples-plot*[SAMPLE-BENCHMARKS])]


@; FIRST make these pretty!!!!!
@; next, tell the story
@; - evaluation method does not scale
@; - painfully obvious, see Evolution
@; - open question from Takikawa etal is HOW TO SCALE, especially howtoscale to micro
@; - well. We have an answer. Stems from the developer story.
@; - overhead plot is statement about expected values
@;   (except, don't actually use that sentence because it confuses everyoneeveryone)
@; - what's this mean, well if I take a random configuration it is N% chance of YOLO
@; - cool
@; - put this intuition to the test
@; - graphs for largest benchmarks, how to read, why CI

