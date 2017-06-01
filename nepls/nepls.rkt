#lang at-exp slideshow

;; Source for NEPLS 2017 talk

;; TODO
;; - highlight types
;; - highlight typ-os
;; - use same bib file for talk and paper
;; - keep checksum for python files, re-run and check Python 3.4 and retic

(require
  "bib.rkt"
  racket/runtime-path
  slideshow/code
  slideshow/text)

;; =============================================================================

(define-runtime-path PWD ".")

(define BLANK
  (blank 0 0))

(define PYTHON-KEYWORDS
  (map symbol->string '(def class return for in if elif else)))

(define GRIEF
  (pict->pre-render-pict
    (scale (bitmap (build-path PWD "src" "grief.jpg")) 1/4)))

(define (cite b)
  (t @~a{[@bib->venue[b] @bib->year[b]]}))

(define (python . arg*)
  (python* arg*))

(define (python* arg*)
  (parameterize ([current-keyword-list PYTHON-KEYWORDS]
                 [current-const-list PYTHON-KEYWORDS]
                 [code-colorize-quote-enabled #f]
                 [current-literal-color (current-id-color)])
    (codeblock-pict (string-join arg* ""))))

(define (pythonline . arg*)
  @item[#:align 'left #:bullet BLANK]{@python*[arg*]})

(define (closer . arg*)
  (apply vc-append (* (current-gap-size) 0.6) arg*))

(define (faded p)
  (cellophane p 0.5))

;; =============================================================================

;; TITLE
(slide
  @titlet{Measuring Reticulated Python}
  @closer[
    @small{@t{Ben Greenman, Northeastern University}}
    @small{@t{with Zeina Migeed}}]
  @comment{
    ok good morning
  })

(slide
  GRIEF
  @comment{
    Any here heard of the five stages of grief?
    Ok
    They're 5 five complex emotions that people often experience after the
     death of a loved one.
    ...
    I've been experiencing similar emotions in the context of this research,
     measuring Reticulated Python.
    My goal today is to share that journey with you.
  })

(slide
  #:title "Reticulated Python"
  @item{Gradual typing for Python @cite[vksb-dls-2014]}
  @item{Static type checking}
  @item{Dynamic type enforcement}
  @item{Type system is sound @cite[vss-popl-2017]} ;; Corollary 5.5.1
  @comment{
    This is reticulated

    see also @tt{github.com/mvitousek/reticulated}
  })

;; -----------------------------------------------------------------------------

(slide
  #:title "Example Program"
  #:layout 'top
  @python{
    def f(n):
      return n*(n+1) // 2

    def get_numbers(how_many):
      nums = []
      for i in range(1, 1 + how_many):
        nums.append(f(i))
      return nums
  }
  @comment{
    is a valid python program, also a valid retic program
  })

(slide
  #:title "Example Program, Fully-Typed"
  #:layout 'top
  @python{
    def f(n:Int)->Int:
      return n*(n+1) // 2

    def get_numbers(how_many:Int)->List(Int):
      nums = []
      for i in range(1, 1 + how_many):
        nums.append(f(i))
      return nums
  }
  @comment{
    valid Retic, fully annotated

    so happens, not a valid python program
  })

(slide
  #:title "Example Program, Partially Typed"
  #:layout 'top
  @python{
    def f(n:Int):
      return n*(n+1) // 2

    def get_numbers(how_many)->List(Int):
      nums = []
      for i in range(1, 1 + how_many):
        nums.append(f(i))
      return nums
  }
  'next
  ;; TODO show output?
  @pythonline{

    get_numbers(4)
  }
  'next
  @pythonline{
    get_numbers("not a number")
  }
  'next
  @pythonline{
    f("not a number")
  }
  @comment{
    anywhere you can have a type annotation, can also remove it. Anywhere.

    example semantics,
    - have successful call
    - dynamic type error
    - static type error
  })

;; -----------------------------------------------------------------------------

(slide
  #:title "Reticulated Python"
  @item{Gradual typing for Python @cite[vksb-dls-2014]}
  @item{Static type checking}
  @item{Dynamic type enforcement}
  @faded[@item{Type system is sound @cite[vss-popl-2017]}]
  @comment{
    okay so you see, we've checkced the 3 boxes via
    - gradual typing syntax
    - static "semantics"
    - dynamic "semantics"
  })

(slide
  @titlet{Grief}
  @comment{
    nice warmup now time for grief
  })

(slide
  #:title "Something Weird"
  #:layout 'top
  'alts~
  (list
    (list
      @python{
        def f(n:Int):
          return n*(n+1) // 2

        def get_numbers(how_many)->List(Int):
          nums = []
          for i in range(1, 1 + how_many):
            nums.append(f(i))
          return nums
      })
    (list
      @python{
        def f(n:Int):
          return n*(n+1) // 2

        def get_numbers(how_many)->List(Int):
          nums = []
          for i in range(1, 1 + how_many):
            nums.append(f)
          return nums
      }))
  'next
  @pythonline{

    get_numbers(4)
  }
  @pythonline{
    def apply_first(funs):
      return funs[0](42)

    apply_first(nums)
  }
  @comment{
    okay this is funny,

    lets take our partially typed program and add a type-O

    oh dear not a list of ints any more 
    but wait it still type checks

    it also runs, and you can apply the functions in the list,
    here's example doing so in untyped code
  })

(slide
  #:title "Another Something Weird"
  #:layout 'top
  @python|{
    @fields({"dollars": Int
            ,"cents": Int})
    class Cash:
      dollars = 0
      cents = 0

      def add_dollars(self, dollars):
        self.dollars += dollars

  }|
  'next
  @pythonline{
    def get_cash()->Cash:
      c = Cash()
      c.add_dollars(3.14159)
      return c

    print(get_cash())
  }
  @comment{
    another strange thing,
    suppose we have a class,
    suppose we also type its fields.
    Maybe representing currency and want to make sure fields are integers,
     and defininitely not integers mixed with floats.

    lo and behold you can write AND READ bad values to the field,
     doesn't even have to be floats
     retic doesn't care
  })

(slide
  @titlet{Denial}
  @comment{
    first time I saw this, thought it was very very strange
    thats not the soundness as I know and love
  })

(slide
  #:title "'Classic' Type Soundness"
  @item[#:bullet BLANK]{If @code[e] has type @code[T], then either:}
  @item{@code[e] reduces to a value @code[v] with type @code[T]}
  @item{@code[e] raises an error due to a partial primitive}
  @item{@code[e] diverges}
  @comment{
    useful in particular because the type works as an API
    if function returns list(int) that's money in the bank,
    guaranteed it will give list of ints no matter how composed in larger program
  })

(slide
  #:title "Reticulated Type Soundness"
  @item[#:bullet BLANK]{If @code[e] has type @code[T], then either:}
  @item{@code[e] reduces to a value @code[v] with type @code[⌊T⌋]}
  @item{@code[e] raises a blame error}
  @item{@code[e] diverges}
  'next
  @t{}
  ;; floor operation
  @comment{
    useful in particular because the type works as an API
    if function returns list(int) that's money in the bank,
    guaranteed it will give list of ints no matter how composed in larger program
  })
