# retic_performance

Performance evaluation for [Reticulated Python](https://github.com/mvitousek/reticulated) commit [`e478343`](https://github.com/mvitousek/reticulated/commit/e478343).

### Summary

- `benchmarks/` benchmark programs
- `pre-benchmarks/` programs that _aspire_ to be benchmark programs
- `data/` raw results of experiments
- `plateau/` writeup of results, as of Spring 2017
- `karst/` scripts for running experiments on Indiana University's Karst cluster
- `script/` data processing scripts

For more info, see the `README.md` files in each folder.

Thank you Senxi Li for discovering that Reticulated made big changes between commit `e478343` and the present. The latest version cannot run these benchmarks as-is because it requires types on all imports. It also optimizes transient code using the strategy from [Vitousek, Siek, Chaudhuri DLS 2019](https://dl.acm.org/doi/10.1145/3359619.3359742).
