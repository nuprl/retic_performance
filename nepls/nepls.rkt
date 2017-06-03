#lang at-exp slideshow

;; Source for NEPLS 2017 talk

;; TODO
;; - use same bib file for talk and paper
;;   - may be possible with `(define-cite #:style ....)`
;; - keep checksum for python files, re-run and check Python 3.4 and retic
;; - uncomment the extra `require`

(require
  "bib.rkt"
  file/glob
  (only-in math/statistics
    mean)
  (only-in racket/runtime-path
    define-runtime-path)
  plot/no-gui
  plot/utils
  slideshow/code
  slideshow/text
  with-cache)
#;(require ; for the cache
  gm-dls-2017/script/benchmark-info
  gm-dls-2017/script/performance-info)

;; =============================================================================

(define (do-show)
  (parameterize ([current-main-font "Roboto"])
    (title)
    (intro)
    (grief-stage)
    (denial-stage)
    (anger-stage)
    (acceptance-stage)
    (moving-on-stage)
    #;(back-that-slides-up)
    (void)))

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
    (scale-to-fit (bitmap (build-path PWD "src" "grief.jpg")) full-page)))

(define BLACK
  (pict->pre-render-pict
    (filled-rectangle (pict-width GRIEF) (pict-height GRIEF) #:color "black" #:draw-border? #f)))

(define POPL-1
  (pict->pre-render-pict
    (scale-to-fit (bitmap (build-path PWD "src" "popl-p1.png")) GRIEF)))

(define POPL-2
  (pict->pre-render-pict
    (scale-to-fit (bitmap (build-path PWD "src" "popl-p10.png")) GRIEF)))

(define POPL-3
  (let ([b (scale-to-fit (bitmap (build-path PWD "src" "popl-p5.png")) GRIEF)])
    (pict->pre-render-pict
      (pin-over b
        0 (/ (pict-height b) 4)
        (cellophane (filled-rectangle (pict-width b) (inexact->exact (floor (* 0.55 (pict-height b)))) #:draw-border? #f #:color "white") 0.6)))))

(define (cite b)
  (t @~a{[@bib->venue[b] @bib->year[b]]}))

(define (python #:min-width [w 0] . arg*)
  (python* arg*))

(define (python* #:min-width [w 0] arg*)
  (vl-append
    (blank w 0)
    (codeblock-pict #:keep-lang-line? #f
      (string-append "#lang python\n" (string-join arg* "")))))

(define (pythonline . arg*)
  @item[#:align 'left #:bullet BLANK]{@python*[arg*]})

(define (closer . arg*)
  (apply vc-append (* (current-gap-size) 0.6) arg*))

(define (faded p)
  (cellophane p 0.5))

(define-syntax-rule (eitem arg* ...)
  (item #:bullet BLANK arg* ...))

(define stage-slide
  (let* ([stage-counter (box 0)]
         [stage-counter++ (λ ()
                            (set-box! stage-counter (+ 1 (unbox stage-counter)))
                            (unbox stage-counter))]
         [rm (λ (i)
               (case i
                [(1) "I"]
                [(2) "II"]
                [(3) "III"]
                [(4) "IV"]
                [(5) "V"]
                [else "VI"]))])
    (λ (str comment)
      (slide
        (cc-superimpose
          BLACK
          (colorize
            (bebas-bold (format "Stage ~a:  ~a" (rm (stage-counter++)) str))
            "white"))
        comment))))

(define (bebas-bold str)
  (text str "Bebas Neue, Bold" 72))

(define (tr-data->name filename)
  (define-values [_base pre-name _d] (split-path filename))
  (define name (if (string? pre-name) pre-name (path->string pre-name)))
  (define pre-hyphen (car (string-split name "-")))
  (define pre-dot (car (string-split pre-hyphen ".")))
  pre-dot)

(define (rnd n)
  (string->number (~r n #:precision '(= 2))))

(define (tr-overhead-fold f init fn)
  (define v (file->value fn))
  (define overhead
    (let ([u (mean (vector-ref v 0))])
      (λ (t*)
        (rnd (/ (mean t*) u)))))
  (for/fold ([acc init])
            ([t* (in-vector v)])
    (f acc (overhead t*))))

(define-syntax-rule (define-symbol* s ...)
  (begin (define s (quote s)) ...))

(define-symbol*
  retic-20-deliverable
  retic-10-deliverable
  retic-worst-case
  tr-20-deliverable
  tr-worst-case)

(define performance-data
  (with-cache (build-path PWD "with-cache" "performance.rktd")
    #:fasl? #f
    #:keys #f
    (lambda () (error 'die))
    #;(λ ()
      (define RETIC-PI
        (map benchmark->performance-info
             (filter benchmark->karst-data (all-benchmarks))))
      (define (retic-count-deliverable D)
        (for/list ([pi (in-list RETIC-PI)])
          (list (performance-info->name pi)
                ((deliverable D) pi)
                (num-configurations pi))))
      (define (retic-count-worst-case)
        (for/list ([pi (in-list RETIC-PI)])
          (cons (performance-info->name pi)
                (max-overhead pi))))
      (define TR-DATA (glob (build-path PWD "src" "tr-data" "*.rktd")))
      (define (tr-count-deliverable D)
        (define (add-if-good? acc o)
          (if (<= o 20) (+ acc 1) acc))
        (for/list ([fn (in-list TR-DATA)])
          (list (tr-data->name fn)
                (tr-overhead-fold add-if-good? 0 fn)
                (tr-overhead-fold (λ (acc t) (+ 1 acc)) 0 fn))))
      (define (tr-count-worst-case)
        (for/list ([fn (in-list TR-DATA)])
          (cons (tr-data->name fn)
                (tr-overhead-fold max 0 fn))))
      (make-immutable-hash
        (list
          (cons retic-20-deliverable (retic-count-deliverable 20))
          (cons retic-10-deliverable (retic-count-deliverable 10))
          (cons retic-worst-case (retic-count-worst-case))
          (cons tr-20-deliverable (tr-count-deliverable 20))
          (cons tr-worst-case (tr-count-worst-case)))))))

(define (render-retic-20-deliverable)
  (render-deliverable 20 (hash-ref performance-data retic-20-deliverable) #:tag "retic"))

(define (render-retic-10-deliverable)
  (render-deliverable 10 (hash-ref performance-data retic-10-deliverable) #:tag "retic"))

(define (render-retic-worst-case)
  (render-worst-case (hash-ref performance-data retic-worst-case)))

(define (render-tr-20-deliverable)
  (render-deliverable 20 (hash-ref performance-data tr-20-deliverable) #:tag "tr"))

(define (render-tr-worst-case)
  (render-worst-case (hash-ref performance-data tr-worst-case)))

(define (render-deliverable D bv* #:tag tag)
  (parameterize ([plot-font-size (- (current-font-size) 8)]
                 [plot-y-ticks (make-overhead-y-ticks)])
    (plot-pict
      (discrete-histogram
        (for/vector #:length (length bv*)
                    ([bv (in-list bv*)]
                     [i (in-naturals)])
          (vector "" (* 100 (/ (cadr bv) (caddr bv))))))
      #:x-label "Benchmark"
      #:y-label ""
      #:y-min 0
      #:y-max 100
      #:height (inexact->exact (round (* 0.6 (current-para-width))))
      #:width (current-para-width))))

(define (make-overhead-y-ticks)
  (define NUM-TICKS 3)
  (define UNITS "%")
  (ticks (λ (ax-min ax-max)
           (for/list ([y (in-list (linear-seq ax-min ax-max NUM-TICKS #:end? #t))])
             (pre-tick (exact-floor y) #t)))
         (ticks-format/units UNITS)))

(define ((ticks-format/units units) ax-min ax-max pre-ticks)
  (for/list ([pt (in-list pre-ticks)])
    (define v (pre-tick-value pt))
    (if (= v ax-max)
      (format "~a~a" (rnd v) units)
      (format "~a" (rnd v)))))

(define (render-worst-case bv*)
  (parameterize ([current-font-size (- (current-font-size) 4)])
    (define-values [hd tl] (split-at bv* 10))
    (vc-append 10
      (bt "Worst-Case Overhead")
      (ht-append 80 (overhead-table hd) (overhead-table tl)))))

(define (overhead-table bv*)
  (table 2
    (append*
      (for/list ([bv (in-list bv*)])
        (list (t (~a(car bv))) (t (~a (inexact->exact (floor (rnd (cdr bv)))))))))
    (list lc-superimpose rc-superimpose)
    cc-superimpose
    30 10))

;; =============================================================================

(define (title)
  (slide
    'alts~
    (list
      (list)
      (list
        (bebas-bold "Measuring Reticulated Python")
        @closer[
          @t{Ben Greenman, Northeastern University}
          @t{with Zeina Migeed}]))
    @comment{
      ok good morning
    })
  (slide
    GRIEF
    @comment{
      has anyone heard of the 5 stages of grief?
      These are stages that people often go through when coping with a
       traumatic incident.

      I've been coping with reticulated python and having similar experiences.
      My goal today is to share that journey with you

      (this is my outline slide)
    })
  (void))

(define (intro)
  (slide
    #:title "Reticulated Python"
    @item{Gradual typing for Python @cite[vksb-dls-2014]}
    @item{Static type checking}
    @item{Dynamic type enforcement}
    @item{Formal model is type is sound @cite[vss-popl-2017]} ;; Corollary 5.5.1
    @comment{
      This is reticulated

      see also @tt{github.com/mvitousek/reticulated}
    })
  (slide
    #:title "Example Program"
    #:layout 'top
    @pythonline{
      def f(n):
        return n*(n+1) // 2

      def get_numbers(count):
        nums = []
        for i in range(1, 1+count):
          nums.append(f(i))
        return nums

      get_numbers(4)
      # [1, 3, 6, 10]
    }
    @comment{
      is a valid python program, also a valid retic program
    })
  (slide
    #:title "Example Program, Fully-Typed"
    #:layout 'top
    @pythonline{
      def f(n:Int)->Int:
        return n*(n+1) // 2

      def get_numbers(count:Int)->List(Int):
        nums = []
        for i in range(1, 1+count):
          nums.append(f(i))
        return nums

      get_numbers(4)
      # [1, 3, 6, 10]
    }
    @comment{
      valid Retic, fully annotated

      so happens, not a valid python program
    })
  (slide
    #:title "Example Program, Partially Typed"
    #:layout 'top
    @pythonline{
      def f(n:Int):
        return n*(n+1) // 2

      def get_numbers(count)->List(Int):
        nums = []
        for i in range(1, 1+count):
          nums.append(f(i))
        return nums

      get_numbers(4)
      # [1, 3, 6, 10]
    }
    'next
    @pythonline{
      f("not a number")
      # Static type error
    }
    'next
    @pythonline{
      get_numbers("not a number")
      # Dynamic type error
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
    @faded[@item{Formal model is type is sound @cite[vss-popl-2017]}]
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
      Now you've got an idea of the syntax and semantics.
      Let's do a more interesting example.
    })
  (slide
    #:title "Something Weird"
    #:layout 'top
    'alts~
    (list
      (list
        @pythonline{
          def f(n:Int):
            return n*(n+1) // 2

          def get_numbers(count)->List(Int):
            nums = []
            for i in range(1, 1+count):
              nums.append(f(i))
            return nums

          get_numbers(4)
        })
      (list
        @pythonline{
          def f(n:Int):
            return n*(n+1) // 2

          def get_numbers(count)->List(Int):
            nums = []
            for i in range(1, 1+count):
              nums.append(f)  # typo!
            return nums

          get_numbers(4)
        }))
    'next
    @pythonline{
      # [<fun>, <fun>, <fun>, <fun>]
    }
    'next
    @pythonline{
      def apply_first(funs):
        return funs[0](10)
      apply_first(get_numbers(4))
      # 55
    }
    @comment{
      lets start with the same partially-typed program as before
      and add a typo
      instead of calling `f` inside the loop, we just put `f`.

      This is the sort of thing that I would call a "type error".
      Reticulated disagrees. This program type checks.
      So we can run it, any guesses to what happens if we run this program?
      ....
      Right we get a list of functions. Of course.
      Nothing goes wrong.

      We can even take one of the functions and apply it.
      Hey man, nothing goes wrong.
    })
  (slide
    #:title "Another Something Weird"
    #:layout 'top
    @pythonline|{
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
      # Cash(3.14159, 0)
    }
    @comment{
      another strange thing,
      suppose we have a class to represent money, US currency.

      and we want to make sure its fields are integer-valued,
      so we add a type annotation.

      The annotation doesn't stop a program from writing a float to the
       field. Or reading a float for that matter.
      The function `get_cash` claims to return a Cash object, but
       really what you get is some nonsense object that superficially looks
       like an instance of Cash.
      You get a forgery.
    })
  (void))

(define (denial-stage)
  (stage-slide "Denial"
    @comment{
      clearly theres some kind of misunderstanding
      I said Retic was based on a type-sound model, but this is not your
      typical type soundness.
    })
  (slide
    #:title "Type Soundness"
    @item[#:bullet BLANK]{If @code[e] has type @code[T], then either:}
    @item{@code[e] reduces to a value @code[v] with type @code[T]}
    @item{@code[e] raises an error due to a partial primitive}
    @item{@code[e] diverges}
    @comment{
      a classic "strong" type soundness theorem would guarantee that
      if a well-typed term reduces to a value, the value has the predicted type

      clearly not what's happening in Reticulated.
      Maybe the implementation has a bug?
    })
  (slide
    #:title "Reticulated Type Soundness"
    @item[#:bullet BLANK]{If @code[e] has type @code[T], then either:}
    @item{@code[e] reduces to a value @code[v] with type @code[⌊T⌋]}
    @subitem{e.g. @code[⌊Int->Int⌋ = ->]}
    ;;@subitem{@code[⌊Int -> Int⌋ = ->]}
    @item{@code[e] raises a blame error}
    @item{@code[e] diverges}
    @comment{
      no, there's no bug
      Reticulated's type soundness guarantees that if a well-typed term
       reduces to a value, the value has the expected TAG.
      Not type, it's a shallow soundness.
    })
  (slide POPL-1)
  (slide POPL-2)
  (slide POPL-3
    @comment{
      of course you don't have to take my word for it,
      can open the paper from POPL, this year,
      and Corollary 5.5.1 spells it out. Type Soudness.
      If a well-typed term reduces to a value, that value has the right tag.

      and here's the definition of the ``floor'' operation, from Figure 3
      ...
    })
  (void))

(define (anger-stage)
  (stage-slide "Anger, Bargaining, Depression"
    @comment{
      *shrug*
    })
  (slide
    #:title "What are Reticulated Types Good For?"
    'next
    @item{Protect invariants?  No}
    'next
    @item{Reliable documentation?  No}
    'next
    @item{Enable optimizations?  No}
    'next
    @eitem{}
    (t "Any untyped code")
    (t "=>")
    (t "No compositional reasoning!")
    @comment{
      compared to a normal type system, this is pretty useless.
      Retic types don't protect invariants,
       don't work as trustworthy documentation,
       and can't be used for standard type-based optimizations
      As soon as you mix in untyped code, all bets are off

      certainly, this is not a "real" type system as you know and love,
       not going to keep you from going wrong, just going to tell you there's
       a "possiblity" of going right.
      So then what, if anything, are retic types good for???!
    })
  (void))

(define (acceptance-stage)
  (stage-slide "Acceptance"
    @comment{
      *short silence*
    })
  (acceptance-stage:theory)
  (acceptance-stage:practice)
  (void))

(define (acceptance-stage:theory)
  (slide
    (titlet "Interoperability & Performance")
    @comment{
      They're good for two things.
      Interoperability and performance.
    })
  (slide
    #:title "Interoperability"
    #:layout 'top
    'alts~
    (list
      (list
        @python{
          def get_numbers(count)->List(Int):
            ....
            return nums
        }
        @item{@code[List] is mutable, standard approach is to proxy})
      (list
        @python{
          def get_numbers(count)->List(Int):
            ....
            return proxy(nums, List(Int))
        }
        'next
        @eitem{}
        @item{The proxy must be compatible with existing code}))
    'next
    @python|{
      nums.append(....)

      len(nums)

      nums is nums
    }|
    @comment{
      lets go back to the list example.
      a Python list is a mutable data structure,
      so the conventional wisdom is to proxy a typed list before leaves a
       typed function, to protect against bad writes from untyped contexts

      If you do so, add the proxy, the proxy needs to be observationally
       equivalent to the original list
      same methods, same functions, same object identity

      I know exactly one language that attempts to do this, Typed Racket,
       its a lot of work to get right.

      If you don't add the proxy ... interop is trivial if you don't interpose
    })
  (slide
    #:title "Performance"
    #:layout 'top
    @python{
      def get_numbers(count)->List(Int):
        ....
        return proxy(nums, List(Int))
    }
    'next
    @eitem{}
    @item{Allocation cost}
    'next
    @item{Traverse, recursively proxy}
    'next
    @item{Interpose on future operations}
    @comment{
      the other aspect is that proxies are not free
      need to allocate,
      traverse and recursively proxy components,
      and once installed a proxy affects future operations,
      may also defeat JIT optimizations

      cost may seem small, but it adds up ...
    })
  (void))

(define (acceptance-stage:practice)
  (slide
    #:title "Measuring Typed Racket"
    'alts
    (list
      (list
        @item{20 programs}
        @item{Measured all gradually-typed configurations}
        @item{How many 20-deliverable?}
        'next
        @render-tr-20-deliverable[])
      (list
        @render-tr-worst-case[]))
    @comment{
      ... to give you an idea, we can do a high level comparison between
      Retic and typed racket

      in 2016 we published some numbers on the performance of typed racket.
      One of the things reported was number of 20-deliverable configurations
      --- if you try all ways of gradually typing some programs, how many
      ways have less than 20x overhead relative to untyped?

      turns out, many of the benchmarks have configurations with MORE THAN 20x
      overhead. 20x is a lot.

      if you look at the worst-case overheads,
      there are triple-digit numbers in there
    })
  (slide
    #:title "Measuring Typed Racket"
    (titlet "Frequently an order-of-magnitude slowdown"))
  (slide
    #:title "Measuring Reticulated"
    'alts
    (list
      (list
        @item{@~a[NUM-EXHAUSTIVE] @bt{different} programs}  ; @cite[vksb-dls-2014] @cite[vss-popl-2017]
        @item{Measured all@it{function-level} configurations}
        'alts
        (list
          (list
            @item{How many 20-deliverable?}
            'next
            @render-retic-20-deliverable[])
          (list
            @item{How many 10-deliverable?}
            'next
            @render-retic-10-deliverable[])))
      (list
        @render-retic-worst-case[]))
    @comment{
      Apply same method to retic,
      using very different benchmarks

      Again asked how many 20-deliverable. Answer: all of them.

      Also asked, how many 10-deliverable. All of them.

      worst-case slowdown we observed was TODOx

      Clearly there's some secret sauce involved.
      I believe most of this gap is due to Reticulated's alternative soundness.
    })
  (slide
    #:title "Measuring Reticulated"
    (titlet "Never an order-of-magnitude slowdown"))
  (void))

(define (moving-on-stage)
  (stage-slide "Moving On"
    @comment{
    })
  (slide
    #:title "Moving On" ;; Life After Transient
    @item[#:bullet (t "Q1.")]{Is Reticulated's soundness practical?}
    @item[#:bullet (t "Q2.")]{Can Typed Racket soundness be performant?}
    @item[#:bullet (t "Q3.")]{Is Typed Racket soundness portable?}
    @item[#:bullet (t "Q4.")]{Is there a useful, ``efficient'' Soundness 3.0?}
    @comment{
      where do we go from here?
      In my mind there are four important, open questions.

      The fourth is the important question for you all,
       is there possibly a third notion of soundness, in between
       Typed Racket and Reticulated, that has strong guarantees
       and yields an efficient implementation.

      That's my talk.
    })
  (slide)
  (void))

(define (back-that-slides-up)
  (slide
    #:title "Granularity"
    @python|{
      @fields({"x": Int, "y": Int})
      class Point:
        x = 0
        y = 0

        def get_x(self:Point)->Int:
          return self.x
    }|
    @comment{
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
