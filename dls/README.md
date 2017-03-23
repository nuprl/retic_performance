dls
===

**Deadline: 2017-05-26**


#### How to write a section

Begin every `.scrbl` file with the language:

```
#lang gm-dls-2017
```

This language _should_ import every library you need to start writing a Scribble
document using our flavor of `scribble/acmart`.

If you want a new import, edit `main.rkt` to provide it.


#### How to build the paper

```
  $ make
```

Installs necessary Racket packages, builds `dls.pdf`.


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


#### Dependencies

- racket (6.8 ?)
- scribble (6.8+)
- git
- LaTeX

