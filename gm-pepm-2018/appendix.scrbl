#lang gm-pepm-2018

@title[#:style 'unnumbered #:tag "sec:appendix"]{Appendix}

@section[#:tag "sec:appendix:validating"]{Validating the Approximation Method}

@Section-ref{sec:method} proposes a so-called @emph{simple random approximation}
 method for guessing the number of @deliverable{D} configurations in a benchmark:

@|DEF-APPROX|@;
@;
@Section-ref{sec:evaluation} instantiates this method using @${r\!=\!@id[NUM-SAMPLE-TRIALS]}
 samples each containing @${@id[SAMPLE-RATE]\!*\!(F + C)} configurations,
 where @${F} is the number of functions and methods in the benchmark and
 @${C} is the number of class definitions.
The intervals produced by this method
 (for the @bm*[SAMPLE-BENCHMARKS] benchmarks) are thin,
 but the paper does not argue that the intervals are very likely to be accurate.
This appendix provides the missing argument.

@subsection{Statistical Argument}

Let @${d} be a predicate that checks whether a configuration from
 a fixed program is @deliverable{D}.
Since @${d} is either true or false for every configuration,
 this predicate defines a Bernoulli random variable @${X_d} with parameter
 @${p}, where @${p} is the true proportion of @deliverable{D} configurations.
Consequently, the expected value of this random variable is @${p}.
The law of large numbers therefore states that the average of infinitely
 many samples of @${X_d} converges to @${p}, the true proportion
 of deliverable configurations.
Convergence suggests that the average of ``enough'' samples is ``close to'' @${p}.
The central limit theorem provides a similar guarantee---any sequence of
 such averages is normally distributed around the true proportion.
A @${95\%} confidence interval generated from sample averages is therefore
 likely to contain the true proportion.


@;@subsection{Back-of-the-Envelope Argument}
@;
@;Suppose a few developers independently apply gradual typing to a program.
@;For a fixed overhead tolerance @${D}, some proportion of the developers have
@; @deliverable{D} configurations.
@;There is a remote chance that this proportion coincides with the true proportion
@; of @deliverable{D} configurations.
@;Intuitively, the chance is less remote if the number of developers is large.
@;But even for a small number of developers, if they repeat this experiment
@; multiple times, then the average proportion of @deliverable{D} configurations
@; should tend towards the true proportion.
@;After all, if the true proportion of @deliverable{D} configurations is
@; @${10\%} then approximately @${1} in @${10} randomly sampled configurations is
@; @deliverable{D}.


@subsection{Empirical Illustration}

@Figure-ref{fig:sample:validate} superimposes the results of simple random
 sampling upon the exhaustive data for three benchmarks.
Specifically, these plots are the result of a two-step recipe:
@itemlist[
@item{
  First, we plot the true proportion of
   @deliverable{D} configurations for @${D} between @${1}x and @${10}x.
  This data is represented by a blue curve; the area under the curve is shaded
   blue.
}
@item{
  Second, we plot a
   @approximation[NUM-SAMPLE-TRIALS (format "[~a(F+C)]" SAMPLE-RATE) "95"]
   as a brown interval.
  This is a 95% confidence interval generated from @integer->word[NUM-SAMPLE-TRIALS]
   samples each containing @$[(format "~a(F+C)" SAMPLE-RATE)] configurations
   chosen uniformly at random.
}
]

@;The intervals accurately enclose the true proportions of @deliverable{D} configurations.

@figure["fig:sample:validate" @elem{Simple random approximations}
  (parameterize ([*PLOT-HEIGHT* 100]
                 [*SINGLE-COLUMN?* #true])
    @render-validate-samples-plot*[VALIDATE-BENCHMARKS])
]

@section[#:tag "sec:appendix:benchmarks"]{Benchmark Descriptions}

@(let ([total @integer->word[NUM-EXHAUSTIVE-BENCHMARKS]]
       [num1 @Integer->word[(length (list* 'aespython 'stats DLS-2014-BENCHMARK-NAMES))]]
       [num2 @Integer->word[(length POPL-2017-BENCHMARK-NAMES)]]
       [num3 @integer->word[(length '(Espionage PythonFlow take5 sample_fsm))]]
      ) @elem{
   @|num1| benchmarks originate from case studies by @citet[vksb-dls-2014].
   @;@note{@|dls-names|.}
   @|num2| are from the evaluation by @citet[vss-popl-2017] on programs from
   the Python Performance Benchmark Suite.
   The remaining @|num3| originate from open-source programs.
})

The following descriptions credit each benchmark's original author,
 state whether the benchmark depends on any fixed modules,
 and briefly summarize its purpose.

@; -----------------------------------------------------------------------------
@; --- WARNING: the order of benchmarks matters!
@; ---  Do not re-order without checking ALL PROSE in this file
@; -----------------------------------------------------------------------------

@bm-desc["futen"
@hyperlink["http://blog.amedama.jp/"]{@tt{momijiame}}
@url{https://github.com/momijiame/futen}
@list[
  @lib-desc["fnmatch"]{Filename matching}
  @lib-desc["os.path"]{Path split, path join, path expand, getenv}
  @lib-desc["re"]{One regular expression match}
  @lib-desc["shlex"]{Split host names from an input string}
  @lib-desc["socket"]{Basic socket operations}
]]{
  Converts an @hyperlink["https://www.openssh.com/"]{OpenSSH} configuration
  file to an inventory file for the
  @hyperlink["https://www.ansible.com/"]{@emph{Ansiable}} automation framework.
  @; 1900 iterations
}

@bm-desc["http2"
@authors[@hyperlink["https://github.com/httplib2/httplib2"]{Joe Gregorio}]
@url{https://github.com/httplib2/httplib2}
@list[
  @lib-desc["urllib"]{To split an IRI into components}
]]{
  Converts a collection of @hyperlink["https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier"]{Internationalized Resource Identifiers}
  to equivalent @hyperlink["http://www.asciitable.com/"]{ASCII} resource
  identifiers.
  @; 10 iterations
}

@bm-desc["slowSHA"
@authors["Stefano Palazzo"]
@url{http://github.com/sfstpala/SlowSHA}
@list[
  @lib-desc["os"]{path split}
]]{
  Applies the SHA-1 and SHA-512 algorithms to English words.
  @; 1 iteration
}

@bm-desc["call_method"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Microbenchmarks simple method calls;
  the calls do not use argument lists,
  keyword arguments, or tuple unpacking.
  @; Consists of @${32*10^5} calls to trivial functions.
  @; 1 iteration
}

@bm-desc["call_simple"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Same as @bm{call_method}, using functions rather than methods.
}

@bm-desc["chaos"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[
  @lib-desc["math"]{Square root}
  @lib-desc["random"]{randrange}
]]{
  Creates fractals using the @hyperlink["https://en.wikipedia.org/wiki/Chaos_game"]{@emph{chaos game}} method.
  @; 1 iteration
}

@bm-desc["fannkuch"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Implements Anderson and Rettig's microbenchmark.
  @;@~cite[ar-lp-1994].
  @; 1 iteration
}

@bm-desc["float"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[
  @lib-desc["math"]{Sin, Cos, Sqrt}
]]{
  Microbenchmarks floating-point operations.
  @; 1 iteration (200,000 points)
}

@bm-desc["go"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[
  @lib-desc["math"]{sqrt log}
  @lib-desc["random"]{randrange random}
  "two untyped modules"
]]{
  Implements the game @hyperlink["https://en.wikipedia.org/wiki/Go_(game)"]{Go}.
  This benchmark is split across three files: an @defn{experimental} module that implements
  the game board, a @defn{fixed} module that defines constants, and a @defn{fixed} module
  that implements an AI and drives the benchmark.
  @; 2 iterations
}

@bm-desc["meteor"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Solves the Shootout benchmarks meteor puzzle.
  @note{@url{http://benchmarksgame.alioth.debian.org/u32/meteor-description.html}}
  @; 1 iterations (finds at most 6,000 solutions)
}

@bm-desc["nbody"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Models the orbits of Jupiter, Saturn, Uranus, and Neptune.
  @; 1 iteration
}

@bm-desc["nqueens"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Solves the @hyperlink["https://developers.google.com/optimization/puzzles/queens"]{@math{8}-queens} problem by a brute-force algorithm.
  @; 10 iterations
}

@bm-desc["pidigits"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Microbenchmarks big-integer arithmetic.
  @; 1 iteration (5,000 digits)
}

@bm-desc["pystone"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Implements Weicker's @emph{Dhrystone} benchmark.
  @note{@url{http://www.eembc.org/techlit/datasheets/ECLDhrystoneWhitePaper2.pdf}}
  @; 50,000 iterations
}

@bm-desc["spectralnorm"
@authors["The Python Benchmark Suite"]
@url{https://github.com/python/performance}
@list[]]{
  Computes the largest singular value of an infinite matrix.
  @; 10 iterations
}

@bm-desc["Espionage"
@authors["Zeina Migeed"]
""
@list[
  @lib-desc["operator"]{itemgetter}
]]{
  Implements Kruskal's spanning-tree algorithm.
  @; 1 iteration
}

@bm-desc["PythonFlow"
@authors["Alfian Ramadhan"]
@url{https://github.com/masphei/PythonFlow}
@list[
  @lib-desc["os"]{path join}
]]{
  Implements the Ford-Fulkerson max flow algorithm. 
  @; no longer needs citation
  @;@~cite[ff-cjm-1956].
  @; 1 iteration
}

@bm-desc["take5"
@authors["Maha Alkhairy" "Zeina Migeed"]
""
@list[
  @lib-desc["random"]{randrange shuffle random seed}
  @lib-desc["copy"]{deepcopy}
]]{
  Implements a card game and a simple player AI.
  @; 500 iterations
}

@bm-desc["sample_fsm"
@authors["Linh Chi Nguyen"]
@url{https://github.com/ayaderaghul/sample-fsm}
@list[
  @lib-desc["itertools"]{cycles}
  @lib-desc["os"]{path split}
  @lib-desc["random"]{random randrange}
]]{
  Simulates the interactions of economic agents modeled as finite-state automata.
  @;@~cite[n-mthesis-2014].
  @; 100 iterations
}

@bm-desc["aespython"
@authors[@hyperlink["http://caller9.com/"]{Adam Newman}
         @hyperlink["https://github.com/serprex"]{Demur Remud}]
@url{https://github.com/serprex/pythonaes}
@list[
  @lib-desc["os"]{random stat}
  @lib-desc["struct"]{pack unpack calcsize}
]]{
  @; Second sentence is a little awkward. I just want to say, "this is really
  @;  a Python implementation of AES, not just a wrapper to some UNIX implementation"
  Implements the @hyperlink["http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf"]{Advanced Encryption Standard}.
  @;Uses the @tt{os} library only to generate random bytes and invoke the
  @; @hyperlink["http://man7.org/linux/man-pages/man2/stat.2.html"]{@tt{stat()}}
  @; system call.
  @; 1 iteration, encrypts the book of Leviticus (2800 lines)
}

@bm-desc["stats"
@authors[@hyperlink["https://connects.catalyst.harvard.edu/Profiles/display/Person/12467"]{Gary Strangman}]
@url{https://github.com/seperman/python-statlib/blob/master/statlib/pstat.py}
@list[
  @lib-desc["copy"]{deepcopy}
  @lib-desc["math"]{pow abs etc.}
]]{
  Implements first-order statistics functions; in other words, transformations
   on either floats or (possibly-nested) lists of floats.
  The original program consists of two modules.
  The benchmark is modularized according to comments in the program's source
   code to reduce the size of each module's configuration space.
  @; 1 iteration
}

@subsection[#:style 'unnumbered]{Acknowledgments}
  This paper is supported by @hyperlink["https://www.nsf.gov/awardsearch/showAward?AWD_ID=1518844"]{NSF grant CCF-1518844}.
  Part of this work was completed while the second author was an REU under Jeremy Siek at Indiana University.
  We thank
   Spenser Bauman,      @; advice about Karst
   Matthias Felleisen,  @; advisor
   Tony Garnock-Jones,  @; insisting that overhead plots are CDFs
   Sam Tobin-Hochstadt, @; access to Karst
   Michael Vitousek,    @; making retic, working with Zeina, fixing bugs
   Ming-Ho Yee, and     @; reading a draft
   the PEPM review committee.
@; DLS reviews sort of, @; sad reviews, but helped
@; PLATEAU reviews sort of @; we were off-topic for them, but reviews tried to help anyway
@;}

@generate-bibliography[#:sec-title "References"]
