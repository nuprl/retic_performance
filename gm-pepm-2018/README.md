pepm
===

#### How to write a section

Begin every `.scrbl` file with the language:

```
#lang gm-pepm-2018
```

This language imports every library you need to start writing a Scribble
 document using our flavor of `scribble/acmart`.

If you want more, edit `main.rkt` to provide it.


#### How to build the paper

- For the first time : `make all`
- After the first time, for a faster build: `make`
- Just the LaTeX : `make tex`


#### Dependencies

- racket (6.8+)
- scribble (6.8+)
- LaTeX
