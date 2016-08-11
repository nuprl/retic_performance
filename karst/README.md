karst
===

Scripts for the cluster.

Usage
---

If your karst username is `zmahmoud` then these scripts are for you.
(If not, see __Advanced Usage__ below.)

First do:
```
$ ./setup_karst.py
```

Then, and every day afterward, try:

```
$ ./brun.py
```

Eventually `brun` will report:

```
All benchmarks finished! See results at:
<file> ...
```

Each `<file>` will have data in the old established format:

```
<cfg-id> <num-types> [<time> ...]
```

Except `<num-types>` is a placeholder value.
Enjoy.


Advanced Usage
---

1. Clone/download
  - [Python-3.4.3](https://www.python.org/downloads/release/python-343/)
  - [reticulated](https://github.com/mvitousek/reticulated)
  - [benchmark_tools](https://github.com/migeed-z/benchmark_tools)
  - [retic_performance](https://github.com/migeed-z/retic_performance)
2. Edit the `#!` line of every script here with an absolute path to your
   `Python-3.4.3/python` executable.
   (Maybe someday, we can have a user-agnostic setup that doesn't require `sudo` access.)
3. Use `./brun.py` as described above.


Details
---

- `brun.py` Control script for the karst benchmarks.
   Running this script schedules new nodes.
- `bnode.sh` Protocol for cluster nodes.
  Basically, loop forever running new configs.
- `setup_karst.py` Configures all benchmark directories for `brun.py`.
  After running the setup you are ready to `brun.py`.
