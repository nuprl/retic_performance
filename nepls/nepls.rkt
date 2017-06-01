#lang at-exp slideshow

;; Source for NEPLS 2017 talk

;; TODO
;; - highlight types
;; - highlight typ-os
;; - vertically align "logically similar" picts
;; - horizontally align equations
;; - use same bib file for talk and paper
;;   - may be possible with `(define-cite #:style ....)`
;; - keep checksum for python files, re-run and check Python 3.4 and retic

(require
  "bib.rkt"
  racket/runtime-path
  slideshow/code
  slideshow/text)

;; =============================================================================

(define (do-show)
  (title)
  (intro)
  (grief-stage)
  (denial-stage)
  (anger-stage)
  (acceptance-stage)
  (moving-on-stage)
  (void))

;; -----------------------------------------------------------------------------

(define-runtime-path PWD ".")

(define NUM-EXHAUSTIVE 19)

(define NUM-TR 20)

(define BLANK
  (blank 0 0))

(define PYTHON-KEYWORDS
  (map symbol->string '(def class return for if in is elif else)))

(define GRIEF
  (pict->pre-render-pict
    (scale (bitmap (build-path PWD "src" "grief.jpg")) 1/4)))

(define POPL-1
  (pict->pre-render-pict (bitmap (build-path PWD "src" "popl-p1.png"))))

(define POPL-2
  (pict->pre-render-pict (bitmap (build-path PWD "src" "popl-p10.png"))))

(define POPL-3
  (pict->pre-render-pict (bitmap (build-path PWD "src" "popl-p5.png"))))

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

(define-syntax-rule (eitem arg* ...)
  (item #:bullet BLANK arg* ...))

(define (stage-slide str . arg*)
  (apply slide
    (titlet str)
    arg*))

;; =============================================================================

(define (title)
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
  (void))

(define (intro)
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
  (void))

(define (grief-stage)
  (stage-slide "Grief"
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

      x = get_numbers(4)
    }
    @pythonline{
      def apply_first(funs):
        return funs[0](42)

      apply_first(x)
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

      get_cash()
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
  (void))

(define (denial-stage)
  (stage-slide "Denial"
    @comment{
      first time I saw this, thought it was very very strange
      thats not the soundness as I know and love
    })
  (slide
    #:title "`Classic' Type Soundness"
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
    @eitem{}
    ;; floor operation
    @eitem{@code[⌊Int⌋ = Int]}
    'next
    @eitem{@code[⌊List(Int)⌋ = List]}
    @eitem{@code[⌊Int -> Int⌋ = ->]}
    @comment{
      first claim is the important one

      some examples of the floor operation,
       it just gets the top-most constructor

      soundness is skin-deep
    })
  (slide POPL-1)
  (slide POPL-2)
  (slide POPL-3
    @comment{
      and there we have it, type soundness
    })
  (void))

(define (anger-stage)
  (stage-slide "Anger? Bargaining? Depression?"
    @comment{
      at this point you too may be feeling some complex emotions
    })
  (slide
    @python{
      def get_numbers(how_many)->List(Int):
        ....
        return nums
    }
    'next
    @item{Cannot guarantee return type}
    @comment{
    })
  (slide
    @python|{
      @fields({"dollars": Int, "cents": Int})
      class Cash:
        ....
    }|
    'next
    @item{Cannot protect datatype invariants}
    @comment{
    })
  (slide
    #:title "Reticulated's `transient' types"
    @item{Cannot guarantee return type}
    @item{Cannot protect datatype invariants}
    @eitem{}
    @titlet{Any untyped code => No compositional reasoning!}
    @comment{
      ALL BETS ARE OFF
    })
  (void))

(define (acceptance-stage)
  (stage-slide "Acceptance"
    @comment{
      ... silence ...
    })
  (acceptance-stage:theory)
  (acceptance-stage:practice)
  (void))

(define (acceptance-stage:theory)
  (slide
    #:title "Two Good Reasons"
    @item{Interoperability}
    @item{Performance}
    @comment{
    })
  (slide
    #:title "Interoperability"
    'alts~
    (list
      (list
        @python{
          def get_numbers(how_many)->List(Int):
            ....
            return nums
        }
        @item{@code[List] is mutable, `classic' approach is to proxy})
      (list
        @python{
          def get_numbers(how_many)->List(Int):
            ....
            return proxy(nums, List(Int))
        }
        @item{@code[List] is mutable, `classic' approach is to proxy}
        @item{The proxy must be compatible with existing code}))
    'next
    @pythonline{nums.append(....)}
    @pythonline{len(nums)}
    @pythonline{nums is nums}
    @comment{
      since List is a mutable data structure,
       conventional wisdom is to proxy it and check future reads and writes.

      if you do that, need to be backwards-compatible

      Racket has chaperones, most languages don't
      (could they? at least it's "a thing")

      interop is trivial if you don't interpose!
    })
  (slide
    #:title "Performance"
    @python{
      def get_numbers(how_many)->List(Int):
        ....
        return proxy(nums, List(Int))
    }
    @eitem{}
    @item{Proxy has allocation cost}
    @item{Proxy adds overhead to future operations}
    @item{In general, need to recursively proxy @code[List] elements}
    @comment{
      (insert text here)

      without proxy, everything is unit-cost

    })
  (slide  ;; TODO really need this slide?
    #:title "Performance"
    'alts~
    (list
      (list
        @python{
          def get_numbers(how_many)->List(Int):
            ....
            return proxy(nums, List(Int))
        })
      (list
        @python{
          def get_numbers(how_many)->List(Int):
            ....
            return check(nums, List(Int))
        }))
    @item{Checking @code[List(Int)] is O(@code[how_many])}
    @item{Checking infinite objects is not possible (e.g., @code[Int -> Int])}
    @comment{
      okay proxy is expensive, suppose we just check
    })
  (void))

(define (acceptance-stage:practice)
  (slide
    #:title "Measuring Reticulated"
    @item{@~a[NUM-EXHAUSTIVE] benchmarks @cite[vksb-dls-2014] @cite[vss-popl-2017] (+ more)}
    @item{Ran all configurations at a @it{function and class fields} granularity}
    'next
    'alts~
    (list
      (list
        @python|{
          @fields({"x": Int, "y": Int})
          class Point:
            x = 0
            y = 0

            def get_x(self:Point)->Int:
              return self.x
        }|)
      (list))
    @item{20-deliverable? 100%}
    @item{10-deliverable? 100%}
    @comment{
      TODO use bar charts
      TODO append random sampling bars
    })
  (slide
    #:title "Worst-Case Overhead"
    'alts
    (list
      (list
        @item{worst-case for each benchmark})
      (list
        (titlet "``Within an order of magnitude''")))
    @comment{
      TODO make a table

      these range between TODO and TODO

      bottom-line / high-level-summary,
       these are within an order of magnitude
    })
  (slide
    #:title (hc-append 0 (t "vs. Typed Racket ")) ;; @cite[tfgnvf-popl-2016])
    'alts
    (list
      (list
        'alts
        (list
          (list
            @item{@~a[NUM-TR] @bt{different} benchmarks}
            @item{20-deliverable? TODO (much fewer)})
          (list
            @item{TODO table})))
      (list
        (titlet @~a{``Frequently worse than an order of magnitude''})))
    @comment{
      cannot directly compare these numbers
    })
  (void))

(define (moving-on-stage)
  (stage-slide "Moving On"
    @comment{
    })
  (slide
    #:title "Moving On" ;; Life After Transient
    @item{Is Reticulated's soundness practical?}
    @item{Can Typed Racket soundness be performant?}
    @item{Is Typed Racket soundness portable?}
    @item{Soundness 3.0}
    @comment{
      where do we go from here?
    })
  (void))

;; =============================================================================

(module+ test
  (require
    rackunit
    (prefix-in dls:
      (only-in gm-dls-2017
        NUM-EXHAUSTIVE-BENCHMARKS)))

  (test-case "constants"
    (check-equal? NUM-EXHAUSTIVE dls:NUM-EXHAUSTIVE-BENCHMARKS))
)

;; =============================================================================

(module+ main
  (do-show))
