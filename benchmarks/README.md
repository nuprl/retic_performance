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

Install [Reticulated commit `e478343`](https://github.com/mvitousek/reticulated/commit/e478343).

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


### History

- `aespython`, `stats`, `futen`, `http2`, and `slowSHA` are based on case study programs reported in: [_Design and Evaluation of Gradual Typing for Python_](https://dl.acm.org/citation.cfm?id=2661101). Michael M. Vitousek, Andrew M. Kent, Jeremy G. Siek, and Jim Baker. DLS 2014.
- `call_method`, `call_method_slots`, `call_simple`, `chaos`, `fannkuch`, `float`, `go`, `meteor`, `nbody`, `nqueens`, `pidigits`, `pystone`, and `spectralnorm` are based on benchmarks from: [_Big Types in Little Runtime: Open-world Soundness and Collaborative Blame for Gradual Type Systems_](https://dl.acm.org/citation.cfm?id=3009849). Michael M. Vitousek, Cameron Swords, and Jeremy G. Siek. POPL 2017.
- `take5` and `sample_fsm` are inspired by Racket benchmarks: <https://github.com/bennn/gtp-benchmarks>
  **NOTE**: the performance of these Reticulated benchmarks is not directly comparable to the performance of the Racket benchmarks.
