#lang gm-dls-2017
@title[#:tag "sec:threats"]{Threats to Validity}

There are several threats to the validity of the overhead plots in
 @figure-ref["fig:overhead" "fig:sample:overhead"].
These threats question the accuracy of the data
 and the soundness of the experimental protcol.


@section{Measurement Error}

The data are timings recorded on the Karst at Indiana University cluster
 using the Python function @hyperlink["https://docs.python.org/3/library/time.html#time.process_time"]{@tt{time.process_time()}}.
Assuming @tt{process_time()} is accurate, the cluster infrastructure is prone
 to at least two sources of error.
First, cluster nodes may have non-uniform performance despite being identical
 servers.
Second, the load on other nodes in the cluster may affect the latency of
 system calls.
These measurement biases@~cite[mdhs-asplos-2009] may explain the outliers evident in @figure-ref{fig:exact}.


@section{Systematic Bias}

The first and most significant threat is that the experiment considers only one
 fully-typed configuration per benchmark.
In general there are many ways of typing a given program.
The types in this experiment may differ from types inferred by another Python
 programmer, and the different types may lead to different performance overhead.

Second, a few benchmarks are either missing annotations or use the dynamic type.

Third, the benchmarks are relatively small compared to widely-used Python libraries.
TODO data

Fourth, Reticulated supports a finer granularity of type annotations than the
 experiment considers.
Partially-typed function signatures or classes with some typed fields and some
 untyped fields might have interesting performance characteristics.
More importantly, such combinations of typed and untyped code might be more
 representative of what Python programmers use in practice.

