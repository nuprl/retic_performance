sample
===

Randomly-sampled data from Karst


### Summary

Each folder in this directory contains files with the name:

- `sample*.txt`

These files have the same format as the exhaustive data,
 but fewer lines.
Instead of data for _all_ configurations, there's only data for some
 randomly selected configurations.


### How did we sample?

Picked `10*N` configurations uniformly at random,
 where `N` is the maximum number of types in the benchmark.
For us, `N` equals the number of functions + number of methods + number of class definitions.
