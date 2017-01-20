The Grand Unified Python Benchmark Suite
########################################

This project is intended to be an authoritative source of benchmarks for all
Python implementations. The focus is on real-world benchmarks, rather than
synthetic benchmarks, using whole applications when possible.

Bug tracker: http://bugs.python.org/issue?@template=item&components=Benchmarks


Quickstart Guide
----------------

Not all benchmarks are created equal: some of the benchmarks listed below are
more useful than others. If you're interested in overall system performance,
the best guide is this:

    $ python perf.py -r -b default /control/python /test/python

That will run the benchmarks we consider the most important headline indicators
of performance. There's an additional collection of whole-app benchmarks that
are important, but take longer to run:

    $ python perf.py -r -b apps /control/python /test/python


Notable Benchmark groups
------------------------

Like individual benchmarks (see "Available benchmarks" below), benchmarks
group are allowed after the `-b` option.

- 2n3 - benchmarks compatible with both Python 2 and Python 3
- apps - "high-level" applicative benchmarks
- serialize - various serialization libraries
- template - various third-party template engines


Available Benchmarks
--------------------

- 2to3 - have the 2to3 tool translate itself.
- calls - collection of function and method call microbenchmarks:
    - call_simple - positional arguments-only function calls.
    - call_method - positional arguments-only method calls.
    - call_method_slots - method calls on classes that use __slots__.
    - call_method_unknown - method calls where the receiver cannot be predicted.
- django - use the Django template system to build a 150x150-cell HTML table.
- fastpickle - use the cPickle module to pickle a variety of datasets.
- fastunnpickle - use the cPickle module to unnpickle a variety of datasets.
- float - artificial, floating point-heavy benchmark originally used by Factor.
- html5lib - parse the HTML 5 spec using html5lib.
- html5lib_warmup - like html5lib, but gives the JIT a chance to warm up by
                    doing the iterations in the same process.
- mako - use the Mako template system to build a 150x150-cell HTML table.
- nbody - the N-body Shootout benchmark. Microbenchmark for floating point
          operations.
- nqueens - small solver for the N-Queens problem.
- pickle - use the cPickle and pure-Python pickle modules to pickle and unpickle
           a variety of datasets.
- pickle_dict - microbenchmark; use the cPickle module to pickle a lot of dicts.
- pickle_list - microbenchmark; use the cPickle module to pickle a lot of lists.
- pybench - run the standard Python PyBench benchmark suite. This is considered
            an unreliable, unrepresentative benchmark; do not base decisions
            off it. It is included only for completeness.
- regex - collection of regex benchmarks:
    - regex_compile - stress the performance of Python's regex compiler, rather
                      than the regex execution speed.
    - regex_effbot - some of the original benchmarks used to tune mainline
                     Python's current regex engine.
    - regex_v8 - Python port of V8's regex benchmark.
- richards - the classic Richards benchmark.
- rietveld - macrobenchmark for Django using the Rietveld code review app.
- slowpickle - use the pure-Python pickle module to pickle a variety of
               datasets.
- slowspitfire - use the Spitfire template system to build a 1000x1000-cell
                 HTML table. Unlike the spitfire benchmark listed below,
                 slowspitfire does not use Psyco.
- slowunpickle - use the pure-Python pickle module to unpickle a variety of
                 datasets.
- spitfire - use the Spitfire template system to build a 1000x1000-cell HTML
             table, taking advantage of Psyco for acceleration.
- spambayes - run a canned mailbox through a SpamBayes ham/spam classifier.
- startup - collection of microbenchmarks focused on Python interpreter
            start-up time:
    - bzr_startup - get Bazaar's help screen.
    - hg_startup - get Mercurial's help screen.
    - normal_startup - start Python, then exit immediately.
    - startup_nosite - start Python with the -S option, then exit immediately.
- threading - collection of microbenchmarks for Python's threading support.
              These benchmarks come in pairs: an iterative version
              (iterative_foo), and a multithreaded version (threaded_foo).
    - threaded_count, iterative_count - spin in a while loop, counting down from a large number.
- unpack_sequence - microbenchmark for unpacking lists and tuples.
- unpickle - use the cPickle module to unpickle a variety of datasets.


Third-Party Modules
-------------------

We include snapshots of the following third-party projects:
- 2to3: r72994 from http://svn.python.org/projects/sandbox/trunk/2to3
- AppEngine Python SDK: release 1.2.3
- Bazaar: release 2.0.3
- Django: r9654 from http://code.djangoproject.com/svn/django/trunk
- htm5lib: rev 16b9dacec7 from https://html5lib.googlecode.com/hg/
- lockfile: release 0.3
- Mako: rev 9ca34926d830 from http://hg.makotemplates.org/mako
- Mercurial: release 1.2.1
- pathlib: rev 1438df2f2016 from https://bitbucket.org/pitrou/pathlib/
- Psyco: release 1.6
- PyBench: release 2.6.4
- Rietveld: r427 from http://rietveld.googlecode.com/svn/trunk
- Spambayes: r3256 http://spambayes.svn.sourceforge.net/svnroot/spambayes/trunk/spambayes
- Spitfire: release 0.7.4

