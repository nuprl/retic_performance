#lang at-exp slideshow

;; Source for NEPLS 2017 talk

;; TODO
;; - use same bib file for talk and paper
;; - keep checksum for python files, re-run and check Python 3.4 and retic

(require
  "bib.rkt"
  racket/runtime-path
  slideshow/code
  slideshow/text)

;; =============================================================================

(define-runtime-path PWD ".")

(define PYTHON-KEYWORDS
  (map symbol->string '(def class return for in if elif else)))

(define GRIEF
  (pict->pre-render-pict
    (scale (bitmap (build-path PWD "src" "grief.jpg")) 1/4)))

(define (cite b)
  (t @~a{[@bib->venue[b] @bib->year[b]]}))

(define-syntax-rule (python x ...)
  (parameterize ([current-keyword-list PYTHON-KEYWORDS]
                 [current-const-list PYTHON-KEYWORDS]
                 [code-colorize-quote-enabled #f]
                 [current-literal-color (current-id-color)])
    (codeblock-pict (string-append x ...))))

(define-syntax-rule (closer arg* ...)
  (parameterize ([current-gap-size (* (current-gap-size) 0.6)])
    arg* ...))

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
  ;; 'next
  @item{Static type checking}
  @item{Dynamic type enforcement}
  @item{Type system is sound @cite[vss-popl-2017]} ;; Corollary 5.5.1
  @comment{
    This is reticulated

    see also @tt{github.com/mvitousek/reticulated}
  })

(slide
  #:title "Example Program"
  @python{
    def f(n):
      return n*(n+1) // 2
  }
  @comment{
  })
