from retic.runtime import *
from retic.mgd_transient import *
from retic.typing import *

def check0(val, elim, act):
    try:
        val.bar
        val.quux
        val.baz
        val.foo
        val.qux
        add_blame_pointer(val, elim, act)
        return val
    except:
        blame(val, elim, act)

def cast4(val, src, b, trg):
    try:
        val.num_runs
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast1(val, src, b, trg):
    try:
        val.OptionParser
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast3(val, src, b, trg):
    try:
        val.time
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast2(val, src, b, trg):
    try:
        val.parse_args
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])
gensym14 = Dyn
gensym37 = Dyn
gensym10 = Dyn
gensym36 = Object('', {'OptionParser': Dyn, })
gensym24 = Dyn
gensym1 = Function(NamedParameters([('self', Object('Foo', {'bar': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int)]), Dyn), 'quux': Function(NamedParameters([('a', Int)]), Dyn), 'baz': Function(NamedParameters([('a', Int), ('b', Int)]), Dyn), 'foo': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn), 'qux': Function(NamedParameters([]), Dyn), })), ('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn)
gensym11 = Class('Foo', {'bar': Function(NamedParameters([('self', TypeVariable('Foo')), ('a', Int), ('b', Int), ('c', Int)]), Dyn), 'quux': Function(NamedParameters([('self', TypeVariable('Foo')), ('a', Int)]), Dyn), 'baz': Function(NamedParameters([('self', TypeVariable('Foo')), ('a', Int), ('b', Int)]), Dyn), 'foo': Function(NamedParameters([('self', TypeVariable('Foo')), ('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn), 'qux': Function(NamedParameters([('self', Dyn)]), Dyn), }, {})
gensym7 = Function(NamedParameters([('self', Object('Foo', {'bar': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int)]), Dyn), 'quux': Function(NamedParameters([('a', Int)]), Dyn), 'baz': Function(NamedParameters([('a', Int), ('b', Int)]), Dyn), 'foo': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn), 'qux': Function(NamedParameters([]), Dyn), })), ('a', Int)]), Dyn)
gensym6 = Dyn
gensym12 = Dyn
gensym42 = Function(AnonymousParameters([]), Dyn)
gensym16 = Dyn
gensym13 = Function(NamedParameters([('iterations', Int), ('timer', Dyn)]), Dyn)
gensym2 = Dyn
gensym41 = Dyn
gensym17 = Function(AnonymousParameters([]), Dyn)
gensym34 = Dyn
gensym23 = Function(AnonymousParameters([]), Dyn)
gensym35 = Dyn
gensym3 = Function(NamedParameters([('self', Object('Foo', {'bar': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int)]), Dyn), 'quux': Function(NamedParameters([('a', Int)]), Dyn), 'baz': Function(NamedParameters([('a', Int), ('b', Int)]), Dyn), 'foo': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn), 'qux': Function(NamedParameters([]), Dyn), })), ('a', Int), ('b', Int), ('c', Int)]), Dyn)
gensym26 = Dyn
gensym30 = Dyn
gensym27 = Function(AnonymousParameters([Int]), Dyn)
gensym47 = Dyn
gensym22 = Dyn
gensym38 = Function(DynParameters, Dyn)
gensym28 = Dyn
gensym5 = Function(NamedParameters([('self', Object('Foo', {'bar': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int)]), Dyn), 'quux': Function(NamedParameters([('a', Int)]), Dyn), 'baz': Function(NamedParameters([('a', Int), ('b', Int)]), Dyn), 'foo': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn), 'qux': Function(NamedParameters([]), Dyn), })), ('a', Int), ('b', Int)]), Dyn)
gensym0 = Dyn
gensym8 = Dyn
gensym9 = Function(NamedParameters([('self', Dyn)]), Dyn)
gensym29 = Function(AnonymousParameters([]), Dyn)
gensym25 = Function(AnonymousParameters([]), Dyn)
gensym19 = Function(AnonymousParameters([]), Dyn)
gensym33 = List(Dyn)
gensym46 = Object('', {'time': Dyn, })
gensym50 = Dyn
gensym48 = Object('', {'num_runs': Dyn, })
gensym45 = Dyn
gensym20 = Dyn
gensym15 = Function(AnonymousParameters([Int]), Dyn)
gensym49 = Function(NamedParameters([('iterations', Int), ('timer', Dyn)]), Dyn)
gensym21 = Function(AnonymousParameters([Int]), Dyn)
gensym4 = Dyn
gensym44 = Tuple(Dyn, Dyn)
gensym43 = Dyn
gensym39 = Dyn
gensym40 = Object('', {'parse_args': Dyn, })
gensym31 = Function(AnonymousParameters([]), Dyn)
gensym18 = Dyn
import optparse
import time
import util
from compat import xrange


class Foo(retic_actual(object)):

    def foo(self, a, b, c, d):
        check0(self, self.foo, (1, 0))
        mgd_check_type_int(a, self.foo, (1, 1))
        mgd_check_type_int(b, self.foo, (1, 2))
        mgd_check_type_int(c, self.foo, (1, 3))
        mgd_check_type_int(d, self.foo, (1, 4))
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)
        mgd_check_type_function(self.bar, self, (0, 'bar'))(a, b, c)

    def bar(self, a, b, c):
        check0(self, self.bar, (1, 0))
        mgd_check_type_int(a, self.bar, (1, 1))
        mgd_check_type_int(b, self.bar, (1, 2))
        mgd_check_type_int(c, self.bar, (1, 3))
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)
        mgd_check_type_function(self.baz, self, (0, 'baz'))(a, b)

    def baz(self, a, b):
        check0(self, self.baz, (1, 0))
        mgd_check_type_int(a, self.baz, (1, 1))
        mgd_check_type_int(b, self.baz, (1, 2))
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)
        mgd_check_type_function(self.quux, self, (0, 'quux'))(a)

    def quux(self, a):
        check0(self, self.quux, (1, 0))
        mgd_check_type_int(a, self.quux, (1, 1))
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()
        mgd_check_type_function(self.qux, self, (0, 'qux'))()

    def qux(self):
        pass
Foo = mgd_cast_type_class(Foo, gensym10, '18', gensym11, ['bar', 'quux', 'baz', 'foo', 'qux'])

def test_calls(iterations, timer):
    mgd_check_type_int(iterations, test_calls, (1, 0))
    times = []
    f = check0(Foo(), Foo, 2)
    gensym32 = mgd_cast_type_function(xrange, gensym26, '119', gensym27)(iterations)
    for _ in gensym32:
        t0 = mgd_cast_type_function(timer, gensym28, '120', gensym29)()
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        mgd_check_type_function(f.foo, f, (0, 'foo'))(1, 2, 3, 4)
        t1 = mgd_cast_type_function(timer, gensym30, '142', gensym31)()
        mgd_check_type_void(mgd_check_type_function(times.append, times, (0, 'append'))((t1 - t0)), mgd_check_type_function(times.append, times, (0, 'append')), 2)
    return mgd_cast_type_dyn(times, gensym33, '144', gensym34)
if (__name__ == '__main__'):
    parser = mgd_cast_type_function(cast1(optparse, gensym35, '148', gensym36).OptionParser, gensym37, '148', gensym38)(usage='%prog [options] [test]', description='Test the performance of simple Python-to-Python method calls.')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, _) = mgd_cast_type_tuple(mgd_cast_type_function(cast2(parser, gensym39, '153', gensym40).parse_args, gensym41, '153', gensym42)(), gensym43, '153', gensym44, 2)
    test_calls(1, cast3(time, gensym45, '156', gensym46).time)
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, cast4(options, gensym47, '158', gensym48).num_runs, mgd_cast_type_dyn(test_calls, gensym49, '158', gensym50))
