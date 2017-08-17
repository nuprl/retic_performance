benchmarks
===

The benchmark programs

### Summary

Each benchmark folder contains (at least) the following directories:

- `both/` Python code or input data
- `typed/` fully-typed Reticulated modules

The idea is, there are `2**N` ways to remove types from the `typed` modules.
Each of these `2**N` gradually-typed programs might need to process some
 (common) input data.
The files under `both` are this input.


### How to Test-Run a Benchmark

```
$ cp -r typed/ test-run/
$ cp -r both/* test-run/.
$ cd test-run/
$ retic main.py
```

In other words, (1) take the files from `typed/`, (2) add the files from `both/`,
 and (3) use Reticulated to run the `main.py` file.

The `typed/` program will not run using Python.
See `../scripts/README.md` for help converting a benchmark to valid Python code.


### How to run the benchmarks

See `../scripts/README.md`
