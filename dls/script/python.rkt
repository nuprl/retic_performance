#lang racket/base

;; Racket interface to Python code
;;  for querying static characteristics

(require racket/contract)
(provide
  (contract-out
   [struct python-info (
     [name symbol?]
     [module* (listof module-info?)])]
   ;; Type information for a Python program

   [struct module-info (
     [name symbol?]
     [function* (listof function-info?)]
     [class* (listof class-info?)])]
   ;; Type information for a Python module

   [struct class-info (
     [name symbol?]
     [field* (listof field-info?)]
     [method* (listof function-info?)])]
   ;; Type information for a Python class

   [struct field-info (
     [name symbol?]
     [type string?])]
   ;; Type information for a Python function

   [python-path?
    (-> any/c boolean?)]
   ;; Return `#t` if the given path string ends in a `.py` suffix, and `#f` otherwise

   [python-sloc
    (-> python-path? exact-nonnegative-integer?)]
   ;; Count source lines of code in a python module

   [python->max-configuration
    (-> is-benchmark-directory? configuration?)]
   ;; Compute a benchmark's max configuration from its Python source code

   [python-info->max-configuration
    (-> python-info? configuration?)]
   ;; Compute a benchmark's max configuration from a summary of its Python
   ;;  source code.

   [benchmark-dir->python-info
    (-> is-benchmark-directory? python-info?)]
   ;; Summarize the Python modules in the given benchmark

))

(require
  "config.rkt"
  "system.rkt"
  "util.rkt"
  json
  file/glob
  with-cache
  (only-in racket/path
    path-get-extension)
  (only-in racket/list
    last)
  (only-in racket/string
    string-join
    string-split))

;; =============================================================================

(define *python-exe* (make-parameter "python3.4"))
(define EXPLODE.PY "explode_module.py")

;; TODO static call graph??

(struct python-info (
  name    ;; Symbol
  module* ;; (Listof module-info)
) #:prefab )

(struct module-info [
  name ;; Symbol
  function* ;; (Listof function-info)
  class* ;; (Listof class-info)
] #:prefab )

(struct function-info [
  name ;; Symbol
  dom* ;; (Listof field-info)
  cod ;; (U String #f)
] #:prefab )

(struct class-info [
  name ;; Symbol
  field* ;; (U #f (Listof field-info))
  method* ;; (Listof function-info)
] #:prefab )

(struct field-info [
  name ;; Symbol
  type ;; (U String #f)
] #:prefab )

;; -----------------------------------------------------------------------------

(define (python-path? ps)
  (and (path-string? ps)
       (equal? (path-get-extension ps) #".py")))

(define (python-sloc ps)
  (define ps-str (path-string->string ps))
  (define arg* (list "--details" "--wide" ps-str))
  (define all-output (shell "sloccount" arg*))
  (define cmd-str (string-join (cons "sloccount" arg*)))
  (define col* (string-split (last (string-split all-output "\n"))))
  (define-values [loc lang _src sloccount-ps]
    (if (= 4 (length col*))
      (apply values col*)
      (raise-user-error 'python-sloc
        "failed to parse output of 'sloccount ~a'~n  full output: ~a"
        ps
        all-output)))
  (unless (string=? lang "python")
    (raise-user-error 'python-sloc
      "expected SLOCCOUNT to return 'python' language, got '~a' instead.~n  original command: ~a"
      lang cmd-str))
  (unless (string=? sloccount-ps ps-str)
    (raise-user-error 'python-sloc
      "expected SLOCCOUNT to report path string '~a', got '~a' instead.~nSomething is very wrong!"
      ps-str
      sloccount-ps))
  (define n (string->number loc))
  (unless (exact-nonnegative-integer? n)
    (raise-user-error 'python-sloc
      "expected SLOCCOUNT to report a natural number of lines, got '~a'.~nSomething is very wrong."
      loc))
  n)

(define (python->max-configuration ps)
  (python-info->max-configuration (benchmark-dir->python-info ps)))

(define (python-info->max-configuration py)
  (for/list ([mi (in-list (python-info-module* py))])
    (expt 2 (module-info->max-configuration mi))))

(define (module-info->max-configuration mi)
  (+ (length (module-info-function* mi))
     (for/sum ([ci (in-list (module-info-class* mi))])
       (class-info->max-configuration ci))))

(define (class-info->max-configuration ci)
  (+ (length (class-info-method* ci))
     (if (class-info-field* ci) 1 0)))

(define (benchmark-dir->python-info x)
  (cond
   [(is-benchmark-directory? x)
    (define bm-name (benchmark-dir->name x))
    (define m* (glob (build-path (benchmark-dir->typed-dir x) "*.py")))
    (define md5* (map md5sum m*)) ;; keys for `with-cache`
    (if (null? m*)
      (raise-user-error 'benchmark-dir->python-info "benchmark ~a has no (typed) Python files" bm-name)
      (parameterize ([*current-cache-directory* "cache-python-info"]
                     [*current-cache-keys* (list (λ () (cons bm-name (map list m* md5*))))])
        (ensure-directory (*current-cache-directory*))
        (with-cache (cachefile (format "~a.rktd" bm-name))
          (λ () (python-info bm-name (map path-string->module-info m*))))))]
   [else
    (raise-user-error 'benchmark-dir->python-info "cannot coerce ~a into static info about a Python program" x)]))

(define (path-string->module-info ps)
  (define py-json (path-string->exploded-module ps))
  (module-json->module-info py-json))

(define (module-json->module-info j)
  (module-info (json-name j)
               (map function-json->function-info (hash-ref j 'function))
               (map class-json->class-info (hash-ref j 'class))))

(define (class-json->class-info j)
  (class-info (json-name j)
              (let ([f (hash-ref j 'field #f)])
                (if f (map field-json->field-info f) #f))
              (map function-json->function-info (hash-ref j 'method))))

(define (function-json->function-info j)
  (function-info (json-name j)
                 (map field-json->field-info (hash-ref j 'dom))
                 (hash-ref j 'cod)))

(define (field-json->field-info j)
  (field-info (json-name j)
              (hash-ref j 'type)))

(define (json-name j)
  (string->symbol (hash-ref j 'name)))

(define (path-string->exploded-module ps)
  (define py (*python-exe*))
  (check-python-exe! py)
  (check-python-file! EXPLODE.PY)
  (string->jsexpr (shell py (list EXPLODE.PY (path-string->string ps)))))

;; (-> string? void?)
;; Assert that the argument refers to a Python with the right version
(define (check-python-exe! str)
  (define v-str (shell str "--version"))
  (unless (valid-python-version? v-str)
    (raise-argument-error 'check-python-exe! (format "Python 3.4 (given '~a')" v-str) str))
  (void))

(define (check-python-file! fn)
  (unless (file-exists? fn)
    (raise-user-error 'check-python-file! "could not find Python file '~a'" fn))
  (void))

;; TODO can relax to "Python 3" ?
(define (valid-python-version? str)
  (regexp-match? #rx"^Python 3.4" str))

;; =============================================================================

(module+ test
  (require rackunit racket/runtime-path)

  (define-runtime-path sloc-example "test/sloc-example.py")
  (define-runtime-path parse-example "test/parse-example.py")
  (define-runtime-path bad-extension-example "test/bad-extension.md")
  (define-runtime-path Espionage-dir "../../benchmarks/Espionage")

  (define py-Espionage (benchmark-dir->python-info Espionage-dir))

  ;; -------------------------------------------------------

  (test-case "python-path?"
    (check-pred python-path? sloc-example)
    (check-false (python-path? "foo")))

  (test-case "python-sloc"
    (check-equal?
      (python-sloc sloc-example)
      2))

  (test-case "python->max-configuration"
    (check-equal? (python-info->max-configuration py-Espionage) '(128 32)))

  (test-case "check-python-file!"
    (check-pred check-python-file! sloc-example)
    (check-exn exn:fail:user?
      (λ () (check-python-file! "not-a-real-file.txt"))))

  (test-case "valid-python-version?"
    (check-true (valid-python-version? "Python 3.4"))
    (check-true (valid-python-version? "Python 3.4.4"))
    (check-false (valid-python-version? "Python 2.7.1")))

  (test-case "python-tests"
    ;; These tests depend on a working Python3.4 executable,
    (when (with-handlers ((exn:fail? (λ (e) #f)))
            (check-python-exe! (*python-exe*)))
      (define py-sloc (path-string->module-info sloc-example))
      (define py-parse (path-string->module-info parse-example))
        (check-equal? (python-info->max-configuration (python-info 'test (list py-sloc))) '(2))
        (check-equal? (python-info->max-configuration (python-info 'test (list py-parse))) '(512))
      (test-case "path-string->exploded-module"
        (check-pred jsexpr? (path-string->exploded-module sloc-example)))

      (test-case "path-string->module-info:basic"

        (define (name=? n1 n2)
          (unless (eq? n1 n2)
            (raise-user-error 'module-info=? "unequal names, ~a /= ~a" n1 n2)))

        (define (type=? t1 t2)
          (if (not t2)
            (when t1
              (raise-user-error 'type=? "got type ~a, expected #f" t1))
            (unless (string=? t1 t2)
              (raise-user-error 'type=? "got type ~a, expected ~a" t1 t2))))

        (define (field-info=? actual expected)
          (and (name=? (field-info-name actual) (field-info-name expected))
               (type=? (field-info-type actual) (field-info-type expected))))

        (define (module-info=? actual expected)
          (and (name=? (module-info-name actual) (module-info-name expected))
               (map function-info=? (module-info-function* actual) (module-info-function* expected))
               (map class-info=? (module-info-class* actual) (module-info-class* expected))))

        (define (function-info=? actual expected)
          (and (name=? (function-info-name actual) (function-info-name expected))
               (map field-info=? (function-info-dom* actual) (function-info-dom* expected))
               (type=? (function-info-cod actual) (function-info-cod expected))))

        (define (class-info=? actual expected)
          (and (name=? (class-info-name actual) (class-info-name expected))
               (if (not (class-info-field* expected))
                 (when (class-info-field* actual)
                   (raise-user-error 'class-info=? "got fields, did not expect fields ~a" actual))
                 (map field-info=? (class-info-field* actual) (class-info-field* expected)))
               (map function-info=? (class-info-method* actual) (class-info-method* expected))))

        (check module-info=?
          py-sloc
          (module-info 'sloc-example
            (list
              (function-info 'f
                (list (field-info 'x #f))
                #f))
            (list)))

        (check module-info=?
          py-parse
          (module-info 'parse-example
            (list
              (function-info 'untyped_function
                (list (field-info 'x #f) (field-info 'y #f))
                #f)
              (function-info 'typed_function
                (list (field-info 'x "int") (field-info 'y "List(Void)"))
                "Int")
              (function-info 'gradual_function
                (list (field-info 'x "int") (field-info 'y #f))
                #f))
            (list
              (class-info 'without_fields
                #f
                (list
                  (function-info 'untyped_method
                    (list (field-info 'self #f) (field-info 'x #f) (field-info 'y #f))
                    #f)
                  (function-info 'typed_method
                    (list (field-info 'self "without_fields") (field-info 'x "int") (field-info 'y "List(Void)"))
                    "Int")
                  (function-info 'gradual_method
                    (list (field-info 'self "without_fields") (field-info 'x "int") (field-info 'y #f))
                    #f)))
              (class-info 'with_fields
                (list (field-info 'f1 "List(List(Int))"))
                (list (function-info '__init__
                        (list (field-info 'self "with_fields"))
                        #f)
                      (function-info 'm
                        (list (field-info 'self "with_fields")
                              (field-info 'x "int"))
                        "int"))))))
      )))

)
