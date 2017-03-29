#lang racket/base

;; Utility functions.
;; Maybe these should be somewhere more public.

(require racket/contract)
(provide
  configuration?

  (contract-out
    [tab-split
     (-> string? (listof string?))]
    ;; Split a list of string by its tab characters

    [path-string->string
     (-> path-string? string?)]
    ;; Convert a string or a path to a string

    [ensure-directory
     (-> path-string? void?)]
    ;; If given directory exists, do nothing. Else create it.

    [rnd
     (-> real? string?)]
    ;; Render a number as a string, round to 2 decimal places.

    [pct
     (-> real? real? real?)]
    ;; `(pct 1 4)` returns 25

    [log2
     (-> exact-nonnegative-integer? exact-nonnegative-integer?)]

    [file-remove-extension
     (-> path-string? path-string?)]
    ;; Removes a Racket-added extension from a filename.
    ;; `(file-remove-extension "foo_tab.gz")` returns "foo.tab"

    [add-commas
     (-> real? string?)]
    ;; Convert a decimal number to a string, adding commas in the normal English
    ;;  places.
    ;; Example: 1234.5678 ==> 1,234.5678

    [save-pict
     (-> path-string? pict? boolean?)]
    ;; Save the given pict to the given filename (in .png format)

    [columnize
     (-> list? exact-nonnegative-integer? (listof list?))]
    ;; Split a list into almost-equally-sized components.
    ;; Order / partitioning of elements is unspecified.

    [force/cpu-time
     (-> (-> any/c) (values any/c exact-nonnegative-integer?))]

))

(require
  (only-in racket/format
    ~r)
  (only-in racket/class
    send)
  (only-in pict
    pict?
    pict->bitmap)
  (only-in racket/set
    set-union
    list->set)
  (only-in racket/list
    make-list)
  (only-in racket/string
    string-join
    string-split))

;; =============================================================================

(define configuration?
  (non-empty-listof exact-nonnegative-integer?))

(define TAB "\t")

(define (tab-split str)
  (string-split str TAB))

(define (path-string->string ps)
  (if (string? ps) ps (path->string ps)))

(define (rnd n)
  (~r n #:precision 2))

(define (ensure-directory d)
  (unless (path-string? d)
    (raise-argument-error 'ensure-directory "path-string?" d))
  (unless (directory-exists? d)
    (make-directory d)))

(define (pct part total)
  (* 100 (/ part total)))

(define (string-last-index-of str c)
  (for/fold ([acc #f])
            ([c2 (in-string str)]
             [i (in-naturals)])
    (if (eq? c c2) i acc)))

(define (file-remove-extension fn)
  (define str (path-string->string fn))
  (define no-ext (path->string (path-replace-extension str #"")))
  (define i (string-last-index-of no-ext #\_))
  (string-append (substring no-ext 0 i) "." (substring no-ext (+ i 1))))

(define (log2 n)
  (if (= n 1)
    0
    (let loop ([k 1])
      (if (= n (expt 2 k))
        k
        (loop (+ k 1))))))

(define (add-commas n)
  (define str (number->string n))
  (define str* (string-split str "."))
  (string-append (add-commas/integer (car str*))
                 (if (or (null? (cdr str*)) (< (string-length str) 4))
                   ""
                   (string-append "." (cadr str*)))))

(define (add-commas/integer str)
  (define L (string-length str))
  (string-join
    (let loop ([i L]
               [acc '()])
      (let ([i-3 (- i 3)])
        (cond
         [(<= i-3 0)
          (cons (substring str 0 i) acc)]
         [else
          (loop i-3 (cons "," (cons (substring str i-3 i) acc)))]))) ""))

(define (save-pict fn p)
  (define bm (pict->bitmap p))
  (send bm save-file fn 'png))

(define (safe-take x* n)
  (cond
   [(zero? n)
    (values '() x*)]
   [(null? x*)
    (values '() '())]
   [else
    (define-values [hd tl] (safe-take (cdr x*) (- n 1)))
    (values (cons (car x*) hd) tl)]))

(define (columnize x* n)
  (let loop ([x* x*])
    (define-values [hd tl] (safe-take x* n))
    (define l (length hd))
    (cond
     [(< l n)
      (append (map list hd) (make-list (- n l) '()))]
     [else
      (define y** (loop tl))
      (for/list ([h (in-list hd)]
                 [y* (in-list y**)])
        (cons h y*))])))

(define (force/cpu-time t)
  (let-values ([(r* cpu real gc) (time-apply t '())])
    (values (car r*) cpu)))

;; =============================================================================

(module+ test
  (require rackunit rackunit-abbrevs)

  (test-case "path-string->string"
    (check-equal? (path-string->string "hi") "hi")
    (check-equal? (path-string->string (string->path "hi")) "hi"))

  (test-case "tab-split"
    (check-equal? (tab-split "hello") '("hello"))
    (check-equal? (tab-split "dr racket") '("dr racket"))
    (check-equal? (tab-split "dr\tracket") '("dr" "racket")))

  (test-case "rnd"
    (check-equal? (rnd 2) "2")
    (check-equal? (rnd 1/3) "0.33"))

  (test-case "pct"
    (check-equal? (pct 1 2) 50)
    (check-equal? (rnd (pct 1 3)) "33.33"))

  (test-case "string-last-index-of"
    (check-equal? (string-last-index-of "hello" #\h) 0)
    (check-equal? (string-last-index-of "hello" #\o) 4)
    (check-equal? (string-last-index-of "hello" #\l) 3)
    (check-equal? (string-last-index-of "hello" #\Q) #f))

  (test-case "file-remove-extension"
    (check-equal? (file-remove-extension "foo_tab.gz") "foo.tab")
    (check-equal? (file-remove-extension "a_b.c") "a.b"))

  (test-case "log2"
    (check-equal? (log2 1) 0)
    (check-equal? (log2 2) 1)
    (check-equal? (log2 8) 3)
    (check-equal? (log2 4096) 12))

  (test-case "add-commas"
    (check-apply* add-commas
     [1
      => "1"]
     [10
      => "10"]
     [100
      => "100"]
     [1000
      => "1,000"]
     [999999
      => "999,999"]
     [12
      => "12"]
     [1234.56789
      => "1,234.56789"]
     [123456789
      => "123,456,789"]
     [12456789
      => "12,456,789"]))

  (test-case "halve"
    (define (check-columnize x* n)
      (define y** (columnize x* n))
      (define L (length (car y**)))
      (check-true (for/and ([y* (in-list (cdr y**))])
                    (define m (length y*))
                    (or (= L m) (= L (+ m 1)))))
      (check-equal? (list->set x*) (apply set-union (map list->set y**))))

    (check-columnize '() 2)
    (check-columnize '(1) 2)
    (check-columnize '(1 2) 2)
    (check-columnize '(1 2 3) 2)
    (check-columnize '(1 2 3 4 5 6 7) 3))

  (test-case "force/cpu-time"
    (let-values ([(v c) (force/cpu-time (λ () 42))])
      (check-equal? v 42)
      (check-true (< c 10))))
)