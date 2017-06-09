karst
===

Scripts for the cluster.

These scripts are not user-friendly.


### Main data collection

- `setup_karst.py` : given a benchmark folder, generate configurations and prepare to collect data
- `bnode.sh` : script for cluster nodes to follow
- `brun.py` : driver script, schedules `bnode.sh` on cluster nodes


### Performance ratio data collection

- `python-untyped.sh` : collect Python running times
- `retic-typed.sh` : collect Retic, fully-typed runtimes
- `retic-untyped.sh` : collect Retic, fully-untyped runtimes


### Sample data collection

- `make-sampler.sh` : driver for `sampler.sh`, if lists of configurations exist then generates copies of `sampler.sh`
- `sampler.sh` : a template for a cluster job


Details of main data collection
===

Usage
---

The scripts assume your Karst username is `zmahmoud`.

First do:
```
$ ./setup_karst.py
```

Then, and every day afterward, try:

```
$ ./brun.py
```

If jobs are still running, `brun.py` will do nothing.
If all nodes are finished, `brun.py` will organize their data and schedule new jobs.

Eventually `brun` will report:

```
All benchmarks finished! See results at:
<file> ...
```

Each `<file>` will have data in the format:

```
<cfg-id> <num-types> [<time> ....]
....
```

Except `<num-types>` is a placeholder value.


Advanced Usage
---

1. Clone/download
  - [Python-3.4.3](https://www.python.org/downloads/release/python-343/)
  - [reticulated](https://github.com/mvitousek/reticulated)
  - [retic_performance](https://github.com/migeed-z/retic_performance)
2. Edit the `#!` line of every script here with an absolute path to your
   `Python-3.4.3/python` executable.
   (Maybe someday, we can have a user-agnostic setup that doesn't require `sudo` access.)
3. Use `./brun.py` as described above.

