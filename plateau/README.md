dls
===

**Deadline: 2017-08-01**

8 page limit


#### How to write a section

Begin every `.scrbl` file with the language:

```
#lang gm-plateau-2017
```

This language imports every library you need to start writing a Scribble
 document using our flavor of `scribble/acmart`.

If you want more, edit `main.rkt` to provide it.


#### How to build the paper

- _For the first time_ : `make all`
- _After the first time, for a faster build_: `make`
- _Just the LaTeX_ : `make tex`


#### Dependencies

- racket (6.8 ?)
- scribble (6.8+)
- git
- LaTeX

