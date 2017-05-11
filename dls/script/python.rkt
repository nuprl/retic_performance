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

   [struct function-info (
     [name symbol?]
     [dom* (listof field-info?)]
     [cod (or/c string? #f)])]

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

   [python-info->max-configuration
    (-> python-info? configuration?)]
   ;; Compute a benchmark's max configuration from a summary of its Python
   ;;  source code.

   [benchmark-dir->python-info
    (-> is-benchmark-directory? python-info?)]
   ;; Summarize the Python modules in the given benchmark

   [python-info->module*
    (-> python-info? (listof string?))]
   ;; Return all module names

   [python-info->num-modules
    (-> python-info? natural?)]
   ;; Count modules

   [python-info->function*
    (-> python-info? (listof string?))]
   ;; Return all function names

   [python-info->num-functions
    (-> python-info? natural?)]
   ;; Count functions

   [python-info->class*
    (-> python-info? (listof string?))]
   ;; Return all class names

   [python-info->num-classes
    (-> python-info? natural?)]
   ;; Count classes

   [python-info->method*
    (-> python-info? (listof string?))]
   ;; Return all method names

   [python-info->num-methods
    (-> python-info? natural?)]
   ;; Count methods

   [python-info->domain*
    (-> python-info? (listof (listof field-info?)))]
   ;; Return all parameter names (across functions and methods)

   [python-info->num-parameters
    (-> python-info? natural?)]
   ;; Count all function/method parameters

   [python-info->return*
    (-> python-info? (listof string?))]
   ;; Return all function / method return types

   [python-info->num-returns
    (-> python-info? natural?)]
   ;; Count the number of function / method return types

   [python-info->field*
    (-> python-info? (listof field-info?))]
   ;; Return all class field names

   [python-info->num-fields
    (-> python-info? natural?)]
   ;; Count the number of class fields

   [python-info->all-types
    ;; TODO codomain should not include #f
    (-> python-info? (set/c (or/c #f string?)))]
   ;; Return a set of all types used in the program

   [python-info->num-types
    (-> python-info? natural?)]
   ;; Count the number of type annotations

))

(require
  "config.rkt"
  "system.rkt"
  "util.rkt"
  file/glob
  json
  racket/runtime-path
  with-cache
  (only-in racket/set
    list->set
    for/set
    for*/set
    set/c
    set-union)
  (only-in racket/list
    append*)
  (only-in racket/math
    natural?)
  (only-in racket/path
    file-name-from-path
    path-get-extension)
  (only-in racket/list
    last)
  (only-in racket/string
    string-join
    string-split))

;; =============================================================================

(define *python-exe* (make-parameter "python3.4"))
(define-runtime-path EXPLODE.PY "explode_module.py")
(define-runtime-path PYTHON-INFO-CACHE "cache-python-info") ;; directory

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

(define (python-info->max-configuration py)
  (for/list ([mi (in-list (python-info-module* py))])
    (expt 2 (module-info->max-configuration mi))))

(define (module-info->max-configuration mi)
  (+ (length (module-info-function* mi))
     (for/sum ([ci (in-list (module-info-class* mi))])
       (class-info->max-configuration ci))))

(define (class-info->max-configuration ci)
  (+ 1 (length (class-info-method* ci))))

(define (benchmark-dir->python-info x)
  (cond
   [(is-benchmark-directory? x)
    (define bm-name (benchmark-dir->name x))
    (define m* (glob (build-path (benchmark-dir->typed-dir x) "*.py")))
    (define filename+md5* (for/list ([m (in-list m*)]) (list (path-string->string (file-name-from-path m)) (md5sum m))))
    (if (null? m*)
      (raise-user-error 'benchmark-dir->python-info "benchmark ~a has no (typed) Python files" bm-name)
      (parameterize ([*current-cache-directory* PYTHON-INFO-CACHE]
                     [*current-cache-keys* (list (λ () (cons bm-name filename+md5*)))]
                     [*with-cache-fasl?* #f])
        (ensure-directory (*current-cache-directory*))
        (with-cache (cachefile (format "~a.rktd" bm-name))
          (λ () (python-info bm-name (map path-string->module-info m*))))))]
   [else
    (raise-user-error 'benchmark-dir->python-info "cannot coerce ~a into static info about a Python program" x)]))

(define (directory->python-info ps)
  (define-values [_base name _mbd] (split-path ps))
  (define m* (glob (build-path ps "*.py")))
  (if (null? m*)
    (raise-user-error 'directory->python-info "directory ~a has no Python files")
    (python-info name (map path-string->module-info m*))))

(define (path-string->python-info ps)
  (python-info (file-name-from-path ps) (path-string->module-info ps)))

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

(define (python-info->module* py)
  (for/list ([mi (in-list (python-info-module* py))])
    (string-append (symbol->string (module-info-name mi)) ".py")))

(define (python-info->num-modules py)
  (length (python-info->module* py)))

(define (python-info->function* py)
  (for*/list ([mi (in-list (python-info-module* py))]
              [fi (in-list (module-info-function* mi))])
    (symbol->string (function-info-name fi))))

(define (python-info->num-functions py)
  (length (python-info->function* py)))

(define (python-info->class* py)
  (for*/list ([mi (in-list (python-info-module* py))]
              [fi (in-list (module-info-class* mi))])
    (symbol->string (class-info-name fi))))

(define (python-info->num-classes py)
  (length (python-info->class* py)))

(define (python-info->method* py)
  (for*/list ([mi (in-list (python-info-module* py))]
              [ci (in-list (module-info-class* mi))]
              [fi (in-list (class-info-method* ci))])
    (symbol->string (function-info-name fi))))

(define (python-info->num-methods py)
  (length (python-info->method* py)))

(define (python-info->domain* py)
  (append*
    (for/list ([mi (in-list (python-info-module* py))])
      (append (for/list ([fi (in-list (module-info-function* mi))])
                (function-info-dom* fi))
              (for*/list ([ci (in-list (module-info-class* mi))]
                          [fi (in-list (class-info-method* ci))])
                (function-info-dom* fi))))))

(define (python-info->num-parameters py)
  (for/sum ([d (in-list (python-info->domain* py))])
    (length d)))

(define (python-info->return* py)
  (append*
    (for/list ([mi (in-list (python-info-module* py))])
      (append (for/list ([fi (in-list (module-info-function* mi))])
                (function-info-cod fi))
              (for*/list ([ci (in-list (module-info-class* mi))]
                          [fi (in-list (class-info-method* ci))])
                (function-info-cod fi))))))

(define (python-info->num-returns py)
  (length (python-info->return* py)))

(define (python-info->field* py)
  (define missing-field* (list (field-info 'missing-field #f)))
  (for*/list ([mi (in-list (python-info-module* py))]
              [ci (in-list (module-info-class* mi))]
              [f (in-list (or (class-info-field* ci)
                              (list (field-info (string->symbol (format "missing-fields:~a" (class-info-name ci))) #f))))])
    f))

(define (python-info->num-fields py)
  (length (python-info->field* py)))

(define (python-info->all-types py)
  (set-union
    (list->set (python-info->return* py))
    (for/set ([f (in-list (python-info->field* py))])
      (field-info-type f))
    (for*/set ([d (in-list (python-info->domain* py))]
               [f (in-list d)])
      (field-info-type f))))

(define (python-info->num-types py)
  (+ (python-info->num-functions py)
     (python-info->num-classes py)
     (python-info->num-methods py)))

;; -----------------------------------------------------------------------------
;; search

(define (get-method-by-name n ci)
  (for/first ([fi (in-list (class-info-method* ci))]
              #:when (eq? n (function-info-name fi)))
    fi))

(define (get-class-by-name n mi)
  (for/first ([c (in-list (module-info-class* mi))]
              #:when (eq? n (class-info-name c)))
    c))

(define (is-typed-function? m)
  (and (function-info-cod m)
       (for/and ([d (in-list (function-info-dom* m))])
         (field-info-type d))))

;; -----------------------------------------------------------------------------
;; Scan command

(define (scan fd*)
  (for ((fd (in-list fd*)))
    (define pi
      (cond
       [(file-exists? fd)
        (path-string->python-info fd)]
       [(directory-exists? fd)
        (directory->python-info fd)]
       [else
        (printf "WARNING: expected path to file or directory, given '~a'~n" fd)]))
    (and pi (print-python-info pi))))

(define (print-python-info pi)
  (printf "~a~n" (python-info-name pi))
  (printf "- ~a modules~n" (python-info->num-modules pi))
  (printf "- ~a functions~n" (python-info->num-functions pi))
  (printf "- ~a classes~n" (python-info->num-classes pi))
  (printf "- ~a methods~n" (python-info->num-methods pi))
  (void))

;; =============================================================================

(module+ main
  (require racket/cmdline racket/set racket/pretty)
  (define scan-mode? (box #f))
  (command-line
   #:program "rp-python"
   #:once-any
   [("-s" "--scan") "Scan a Python file (or flat directory of Python files)" (set-box! scan-mode? #t)]
   #:args ARG*
   (cond
    [(unbox scan-mode?)
     (scan ARG*)]
    [else
     (raise-user-error 'die)])
   #;(pretty-print (benchmark-dir->python-info p))
   #;(for ((PAT (in-list PAT*)))
     (when (set-member? (python-info->all-types (benchmark-dir->python-info PAT)) #f)
       (printf "MISSING TYPE IN ~a~n" PAT)))
   #;(for ([fn (in-glob PAT)])
     (define mi (path-string->module-info fn))
     (when (is-typed-function? (get-method-by-name '__init__ (get-class-by-name 'SSHConfig mi)))
       (displayln (path-replace-extension (file-name-from-path fn) #""))))))

;; =============================================================================

(module+ test
  (require rackunit racket/runtime-path)

  (define-runtime-path sloc-example "test/sloc-example.py")
  (define-runtime-path parse-example "test/parse-example.py")
  (define-runtime-path bad-extension-example "test/bad-extension.md")
  (define-runtime-path Espionage-dir "../../benchmarks/Espionage")
  (define-runtime-path futen-dir "../../benchmarks/futen")

  (define py-Espionage (benchmark-dir->python-info Espionage-dir))
  (define py-futen (benchmark-dir->python-info futen-dir))

  ;; -------------------------------------------------------

  (test-case "python-path?"
    (check-pred python-path? sloc-example)
    (check-false (python-path? "foo")))

  (test-case "python-sloc"
    (check-equal?
      (python-sloc sloc-example)
      2))

  (test-case "python-info->max-configuration"
    (check-equal? (python-info->max-configuration py-Espionage) '(128 32))
    (check-equal? (python-info->max-configuration py-futen) '(16 2 1024)))

  (test-case "check-python-file!"
    (check-pred check-python-file! sloc-example)
    (check-exn exn:fail:user?
      (λ () (check-python-file! "not-a-real-file.txt"))))

  (test-case "valid-python-version?"
    (check-true (valid-python-version? "Python 3.4"))
    (check-true (valid-python-version? "Python 3.4.4"))
    (check-false (valid-python-version? "Python 2.7.1")))

  (test-case "selectors"
    (check-equal?
      (python-info->module* py-Espionage)
      '("main.py" "union_find.py"))
    (check-equal?
      (python-info->function* py-Espionage)
      '("main" "output_result" "convert_to_set" "create_nodes" "make_tuple" "make_set" "kruskal"))
    (check-equal?
      (python-info->class* py-Espionage)
      '("UnionFind"))
    (check-equal?
      (python-info->method* py-Espionage)
      '("__init__" "add_node" "find" "union"))
    (check-equal?
      (python-info->field* py-Espionage)
      (list (field-info 'my_dict "Dict(Int,Tuple(Int,Int))")))
    (check-equal?
      (length (python-info->domain* py-Espionage))
      (+ (python-info->num-functions py-Espionage)
         (python-info->num-methods py-Espionage)))
    (check-equal?
      (python-info->num-parameters py-Espionage)
      (+ 10 9))
    (check-equal?
      (python-info->num-returns py-Espionage)
      (+ 7 4))
    (check-equal?
      (python-info->all-types py-Espionage)
      (list->set '("UnionFind" "Tuple(Int,Int)" "Tuple(Int,Int,Int)" "String" "Void" "Int" "Dict(Int,Tuple(Int,Int))" "List(String)" "List(Tuple(Int,Int))" "List(Tuple(Int,Int,Int))" "List(Int)")))
    (check-equal?
      (python-info->num-types py-Espionage)
      (+ 7 1 4)))

  (test-case "python-tests"
    ;; These tests depend on a working Python3.4 executable,
    (when (with-handlers ((exn:fail? (λ (e) #f)))
            (check-python-exe! (*python-exe*)))
      (define mi-sloc (path-string->module-info sloc-example))
      (define mi-parse (path-string->module-info parse-example))
      (define py-sloc (python-info 'test (list mi-sloc)))
      (define py-parse (python-info 'test (list mi-parse)))

      (test-case "max-configuration"
        (check-equal? (python-info->max-configuration py-sloc) '(2))
        (check-equal? (python-info->max-configuration py-parse) '(1024)))

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
          mi-sloc
          (module-info 'sloc-example
            (list
              (function-info 'f
                (list (field-info 'x #f))
                #f))
            (list)))

        (check module-info=?
          mi-parse
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
      )

      (test-case "python-info->module*"
        (check-equal? (python-info->module* py-sloc) '("sloc-example.py"))
        (check-equal? (python-info->module* py-parse) '("parse-example.py")))

      (test-case "python-info->num-modules"
        (check-equal? (python-info->num-modules py-sloc) 1)
        (check-equal? (python-info->num-modules py-parse) 1))

      (test-case "python-info->function*"
        (check-equal? (python-info->function* py-sloc) '("f"))
        (check-equal? (python-info->function* py-parse)
                      '("untyped_function" "typed_function" "gradual_function")))

      (test-case "python-info->num-functions"
        (check-equal? (python-info->num-functions py-sloc) 1)
        (check-equal? (python-info->num-functions py-parse) 3))

      (test-case "python-info->class*"
        (check-equal? (python-info->class* py-sloc) '())
        (check-equal? (python-info->class* py-parse) '("without_fields" "with_fields")))

      (test-case "python-info->num-classes"
        (check-equal? (python-info->num-classes py-sloc) 0)
        (check-equal? (python-info->num-classes py-parse) 2))

      (test-case "python-info->method*"
        (check-equal? (python-info->method* py-sloc) '())
        (check-equal? (python-info->method* py-parse)
                      '("untyped_method" "typed_method" "gradual_method" "__init__" "m")))

      (test-case "python-info->num-methods"
        (check-equal? (python-info->num-methods py-sloc) 0)
        (check-equal? (python-info->num-methods py-parse) 5))

      (test-case "python-info->domain*"
        (check-equal? (python-info->domain* py-sloc) (list (list (field-info 'x #f))))
        (check-equal?
          (python-info->domain* py-parse)
          (list (list (field-info 'x #f) (field-info 'y #f))
                (list (field-info 'x "int") (field-info 'y "List(Void)"))
                (list (field-info 'x "int") (field-info 'y #f))
                (list (field-info 'self #f) (field-info 'x #f) (field-info 'y #f))
                (list (field-info 'self "without_fields") (field-info 'x "int") (field-info 'y "List(Void)"))
                (list (field-info 'self "without_fields") (field-info 'x "int") (field-info 'y #f))
                (list (field-info 'self "with_fields"))
                (list (field-info 'self "with_fields") (field-info 'x "int")))))

      (test-case "python-info->num-parameters"
        (check-equal? (python-info->num-parameters py-sloc) 1)
        (check-equal? (python-info->num-parameters py-parse) 18))

      (test-case "python-info->return*"
        (check-equal? (python-info->return* py-sloc) '(#f))
        (check-equal? (python-info->return* py-parse) '(#f "Int" #f #f "Int" #f #f "int")))

      (test-case "python-info->num-returns"
        (check-equal? (python-info->num-returns py-sloc) 1)
        (check-equal? (python-info->num-returns py-parse) 8))

      (test-case "python-info->field*"
        (check-equal? (python-info->field* py-sloc) '())
        (check-equal? (python-info->field* py-parse) (list (field-info 'f1 "List(List(Int))"))))

      (test-case "python-info->num-fields"
        (check-equal? (python-info->num-fields py-sloc) 0)
        (check-equal? (python-info->num-fields py-parse) 1))

      (test-case "python-info->all-types"
        (check-equal? (python-info->all-types py-sloc) (list->set '(#f)))
        (check-equal? (python-info->all-types py-parse) (list->set '(#f "int" "without_fields" "with_fields" "List(Void)" "List(List(Int))" "Int"))))

      (test-case "python-info->num-types"
        (check-equal? (python-info->num-types py-sloc) 1)
        (check-equal? (python-info->num-types py-parse) 10))
      ))

)
