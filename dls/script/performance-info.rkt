#lang racket/base

;; TODO
;; - make sure "alphabetical in Racket" matches configuration order

(require racket/contract)
(provide
  (contract-out
   [benchmark->performance-info
    (-> benchmark-info? performance-info?)]
  )
)

(require
  "benchmark-info.rkt"
  "util.rkt"
  (only-in math/statistics
    mean)
  (only-in racket/string
    string-split
    string-replace))

(define-syntax-rule (TODO) (raise-user-error "not implemented"))

;; =============================================================================

(struct performance-info (
  name ;; Symbol, a benchmark name
  src  ;; Path-String, data from Karst
  num-configs
  configs/module*
  python-runtime
  untyped-runtime
  typed-runtime
) #:transparent )

(define (make-performance-info name #:src k
                                    #:num-configurations num-configs
                                    #:configurations/module* configs/module*
                                    #:untyped-retic-runtime base-retic
                                    #:typed-retic-runtime typed-retic)
  ;; TODO python runtime
  (performance-info name k num-configs configs/module* #f base-retic typed-retic))

(define (benchmark->performance-info bm)
  (define k (benchmark->karst-data bm))
  (define name (benchmark->name bm))
  (unless k
    (raise-user-error 'benchmark->performance-info
      "cannot find Karst data for benchmark '~a'" name))
  (define-values [num-configs configs/module* base-retic typed-retic]
    (scan-karst-file k))
  (make-performance-info name
    #:src k
    #:num-configurations num-configs
    #:configurations/module* configs/module*
    #:untyped-retic-runtime base-retic
    #:typed-retic-runtime typed-retic))

;; scan-karst-file : Path-String -> (Values Natural (Listof Natural) Natural Natural)
;; Take a "first glance" pass over a data file
;; Return
;; - the number of configurations
;; - the max. number of types per module (in alphabetical order)
(define (scan-karst-file k)
  (define-values [num-configs num-configs++]
    (let ([nc (box 0)])
      (values nc
              (λ ()
                (set-box! num-configs (+ 1 (unbox num-configs)))))))
  (define-values [configs/module* update-configs/module*]
    (let ([cm (box #f)])
      (values cm
              (λ (cfg/mod*)
                (set-box! cm
                  (if (unbox cm)
                    (for/list ([v-old (in-list (unbox cm))]
                               [v-new (in-list cfg/mod*)])
                      (max v-old v-new))
                    cfg/mod*))))))
  (define-values [base-retic typed-retic update-base-retic update-typed-retic]
    (let ([ur (box #f)]
          [tr (box #f)])
      (values ur
              tr
              (λ (times-str)
                (set-box! ur
                  (mean (parse-times-string times-str))))
              (λ (times-str)
                (when (not (unbox tr))
                  (set-box! tr
                    (mean (parse-times-string times-str))))))))
  (with-input-from-file k
    (λ ()
      (for ([ln (in-lines)])
        (define-values [cfg-str times-str]
          (let ([ln-info (parse-line ln)])
            (values (car ln-info) (caddr ln-info))))
        (num-configs++)
        (define cfg/mod* (parse-config-string cfg-str))
        (define prev-cfg* (unbox configs/module*))
        (update-configs/module* cfg/mod*)
        (when (typed-configuration? cfg/mod*)
          (update-typed-retic times-str))
        (unless (equal? prev-cfg* (unbox configs/module*))
          (update-base-retic times-str))
        (void))))
  (values (unbox num-configs)
          (unbox configs/module*)
          (unbox base-retic)
          (unbox typed-retic)))

(define (typed-configuration? cfg/mod*)
  (andmap zero? cfg/mod*))

(define/contract (parse-line str)
  (-> string? (list/c string? string? string?))
  (tab-split str))

;; parse-config-string : String -> (Listof Natural)
;; Parse a string like `0-0-3` into a list of numbers `'(0 0 3)`
(define/contract (parse-config-string cfg-str)
  (-> string? (listof exact-nonnegative-integer?))
  (map string->number (string-split cfg-str "-")))

(define/contract (parse-times-string times-str)
  (-> string? (listof (and/c flonum? (>=/c 0))))
  (let ([sp (open-input-string (string-replace times-str "," ""))])
    (begin0 (read sp) (close-input-port sp))))

(define (num-configurations pf)
  (performance-info-num-configs pf))

(define (overhead pf v)
  (/ v (performance-info-untyped-runtime pf)))

(define (min-overhead pf)
  (overhead pf (fold/mean (performance-info-src pf) min)))

(define (max-overhead pf)
  (overhead pf (fold/mean (performance-info-src pf) max)))

(define (average-overhead pf)
  ;; TODO how is the average less than the min?
  (define 1/N (/ 1 (num-configurations pf)))
  (define (avg acc v)
    (+ acc (* 1/N v)))
  ;(overhead pf
  (fold/mean (performance-info-src pf) avg #:init (λ (v) (* 1/N v))))

(define fold/mean
  (let ([line->mean (λ (ln)
                      (let ([times-str (caddr (parse-line (read-line)))])
                        (mean (parse-times-string times-str))))])
    (λ (filename f #:init [init-f #f])
      (with-input-from-file filename
        (λ ()
          (define init (line->mean (read-line)))
          (for/fold ([acc (if init-f (init-f init) init)])
                    ([ln (in-lines)])
            (f acc (line->mean ln))))))))

(define ((deliverable D) pf)
  (TODO))

(define ((usable D U) pf)
  (TODO))

(define (typed/python-ratio pf)
  (TODO))

(define (typed/retic-ratio pf)
  (/ (performance-info-typed-runtime pf)
     (performance-info-untyped-runtime pf)))

(define (python-runtime pf)
  (TODO))

(define (quick-performance-info bm-name)
  (define bm (->benchmark-info bm-name))
  (define pf (benchmark->performance-info bm))
  (printf "~a~n" bm-name)
  (printf "- num configs  : ~a~n" (performance-info-num-configs pf))
  (printf "- Python  time : ~a~n" "???")
  (printf "- untyped time : ~a~n" (performance-info-untyped-runtime pf))
  (printf "-   typed time : ~a~n" (performance-info-typed-runtime pf))
  (printf "- min overhead : ~a~n" (min-overhead pf))
  (printf "- max overhead : ~a~n" (max-overhead pf))
  (printf "- avg overhead : ~a~n" (average-overhead pf))
  (void))

;; =============================================================================

(module+ test
  (require rackunit)

  (test-case "performance-info"
    #;(let* ([bm (->benchmark-info 'Espionage)]
           [pf (benchmark->performance-info bm)]
          )
      (check-true (performance-info? pf))
      (void))
    (quick-performance-info 'Espionage)
  )
)

(module+ main

)

