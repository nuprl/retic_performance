karst
===

Scripts for the Karst high-throughput computing cluster.

<https://kb.iu.edu/d/bezu>


### Summary

There are 3 categories of scripts, based on their purpose.

#### 1. Main data collection

- `setup_karst.py` : given a benchmark folder, generate configurations and prepare to collect data
- `bnode.sh` : script for cluster nodes to follow
- `brun.py` : driver script, schedules `bnode.sh` on cluster nodes


#### 2. Performance ratio data collection

- `python-untyped.sh` : collect Python running times
- `retic-typed.sh` : collect Retic, fully-typed runtimes
- `retic-untyped.sh` : collect Retic, fully-untyped runtimes


#### 3. Sample data collection

- `make-sampler.sh` : driver for `sampler.sh`, if lists of configurations exist then generates copies of `sampler.sh`
- `sampler.sh` : a template for a cluster job


### More about "Main data collection"

#### Before running the scripts:

1. Clone/download the following to your Karst home directory:
  - [Python-3.4.3](https://www.python.org/downloads/release/python-343/)
  - [reticulated](https://github.com/mvitousek/reticulated)
  - [retic_performance](https://github.com/migeed-z/retic_performance)
2. Edit the `#!` line of every script here with an absolute path to your
   `Python-3.4.3/python` executable.


#### To collect all data:

First, run:
```
$ ./setup_karst.py
```

This should finish in a few hours, at most.


Second, run:
```
$ ./brun.py
```
This should finish in a few seconds.

Third, wait for the sceduler to start running the jobs that `brun.py` registered.
THis should take a week at most.

Fourth, wait 24 hours and go back to step 2.

Eventually, running `brun.py` will report:

```
All benchmarks finished! See results at:
<file> ...
```

Then you're done.
