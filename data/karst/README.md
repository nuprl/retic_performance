karst
===

Data from the _Karst at Indiana University_ high-throughput computing cluster.

Karst home: <https://kb.iu.edu/d/bezu>


### Summary

This directory contains _exhaustive_ data.

- `sample/` randomly-sampled data
- `*_tab.gz` contains data for one benchmark,
  the un-zipped `.tab` file has 1 line for each configuration,
  and each line has the format `CONFIG-ID	NUM-TYPES	[TIME, ...]`
  where `CONFIG-ID` is a hypen-separated string of natural numbers (e.g. 0-0)
  and `NUM-TYPES` is a natural number
  and `TIME` is a positive float
- `*_python.tab` contains Python data for one benchmark, i.e. how many seconds
  did it take to run the _untyped_ configuration using Python
- `*_retic-untyped.tab` runtimes for the untyped configuration run via Retic
- `*_retic-typed.tab` runtimes for the fully-typed configuration (run via Retic)
