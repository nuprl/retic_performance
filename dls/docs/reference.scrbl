#lang scribble/manual
@require[(for-label gm-dls-2017)]
@title{Reference}

@defmodulelang[gm-dls-2017]{
  The @racketmodname[gm-dls-2017] language provides the reader from
   @racketmodname[scribble/base] and all exports from the @racketmodname[gm-dls-2017] module.
}

@defproc[(render-benchmark-name [bm string?]) element?]{
  Render the name of a benchmark program.
}

@section{Static Benchmark Information}

@defmodule[gm-dls-2017/script/benchmark-info]{
}


@section{Reticulated Performance Data}

@defmodule[gm-dls-2017/script/performance-info]{
}

@;script/benchmark-info.rkt
@;script/performance-info.rkt
@;script/python.rkt
@;script/sample.rkt
@;script/util.rkt
@;script/config.rkt
@;script/plot.rkt
@;script/render.rkt
@;script/system.rkt
