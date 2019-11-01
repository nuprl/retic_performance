almost-free
===


Background
---

There's a paper in VMIL 2019 that uses configurations with 1 type annotation
 to explain configurations with N type annotations.
See figure 2.

```
  @inproceedings{grmhn-vmil-2019,
    title = {Which of My Transient Type Checks Are Not (Almost) Free?},
    author = {Gariano, Isaac Oscar and Roberts, Richard and Marr, Stefan and Homer, Michael and Noble, James},
    booktitle = {{VMIL}},
    pages = {58--66},
    year = {2019}
  }
```

They make a bar graph showing the performance of every configuration with
 exactly one type annotation.
In these graphs, only 1 or 2 bars are "interesting" ... i.e. far off from 1x
 overhead.
These interesting type annotation (bars) also appear in "interesting" groups
 of points in a set of randomly-sampled configurations.

None of this is made precise in the paper.

The question is: does our Transient Reticulated data ALSO have bar graphs with
 only 1 or 2 "interesting" bars?
If so, can we quantify "interesting" and make precise predictions about the
 configurations?

We have all the ground-truth data (except, probably, for the largest benchmarks)
 so lets see.


TODO
---

- [ ] read paper
- [ ] email authors for their code + benchmarks
- [ ] which 1-ann configurations do we have for our large benchmarks?
- [ ] make bar graphs
- [ ] spot-check for interesting groups of points
- [ ] 

