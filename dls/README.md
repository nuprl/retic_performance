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

- _For the first time_ : `make`
- _After the first time, for a faster build_: `make pdf`
- _Just the LaTeX_ : `make tex`


#### Dependencies

- racket (6.8 ?)
- scribble (6.8+)
- git
- LaTeX

