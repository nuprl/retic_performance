dls
===

Deadline: 



#### How to build the paper

```
  $ make
```

builds `dls.pdf`.


Running `make` has the same effect as running:

```
  $ make pdf
```

which has almost the same effect as running:

```
  $ make tex
  $ pdflatex dls.tex
```

except that the first command (`make tex`) builds the file `dls.tex`.
Also, `pdflatex` gives MUCH better error messages than `make` or `make pdf`.
