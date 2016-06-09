from retic.runtime import *
from retic.mgd_transient import *
from retic.typing import *

def check0(val, elim, act):
    try:
        val.bar
        val.__slots__
        val.qux
        val.baz
        val.quux
        val.foo
        add_blame_pointer(val, elim, act)
        return val
    except:
        blame(val, elim, act)

def cast3(val, src, b, trg):
    try:
        val.time
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast4(val, src, b, trg):
    try:
        val.num_runs
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

def cast1(val, src, b, trg):
    try:
        val.OptionParser
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])
gensym11 = Class('Foo', {'bar': Function(NamedParameters([('self', TypeVariable('Foo')), ('a', Int), ('b', Int), ('c', Int)]), Dyn), '__slots__': Dyn, 'qux': Function(NamedParameters([('self', Dyn)]), Dyn), 'baz': Function(NamedParameters([('self', TypeVariable('Foo')), ('a', Int), ('b', Int)]), Dyn), 'quux': Function(NamedParameters([('self', TypeVariable('Foo')), ('a', Int)]), Dyn), 'foo': Function(NamedParameters([('self', TypeVariable('Foo')), ('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn), }, {})
gensym15 = Function(AnonymousParameters([Int]), Dyn)
gensym52 = Object('', {'num_runs': Dyn, })
gensym18 = Dyn
gensym30 = Dyn
gensym23 = Function(AnonymousParameters([]), Dyn)
gensym43 = Dyn
gensym53 = Function(NamedParameters([('iterations', Int), ('timer', Dyn)]), Dyn)
gensym51 = Dyn
gensym21 = Function(AnonymousParameters([Int]), Dyn)
gensym54 = Dyn
gensym45 = Dyn
gensym34 = Dyn
gensym5 = Function(NamedParameters([('self', Object('Foo', {'bar': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int)]), Dyn), '__slots__': Dyn, 'qux': Function(NamedParameters([]), Dyn), 'baz': Function(NamedParameters([('a', Int), ('b', Int)]), Dyn), 'quux': Function(NamedParameters([('a', Int)]), Dyn), 'foo': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn), })), ('a', Int), ('b', Int)]), Dyn)
gensym42 = Function(DynParameters, Dyn)
gensym13 = Function(NamedParameters([('iterations', Int), ('timer', Dyn)]), Dyn)
gensym6 = Dyn
gensym17 = Function(AnonymousParameters([]), Dyn)
gensym14 = Dyn
gensym31 = Function(AnonymousParameters([Int]), Dyn)
gensym19 = Function(AnonymousParameters([]), Dyn)
gensym40 = Object('', {'OptionParser': Dyn, })
gensym2 = Dyn
gensym4 = Dyn
gensym33 = Function(AnonymousParameters([]), Dyn)
gensym20 = Dyn
gensym22 = Dyn
gensym41 = Dyn
gensym1 = Function(NamedParameters([('self', Object('Foo', {'bar': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int)]), Dyn), '__slots__': Dyn, 'qux': Function(NamedParameters([]), Dyn), 'baz': Function(NamedParameters([('a', Int), ('b', Int)]), Dyn), 'quux': Function(NamedParameters([('a', Int)]), Dyn), 'foo': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn), })), ('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn)
gensym8 = Dyn
gensym12 = Dyn
gensym44 = Object('', {'parse_args': Dyn, })
gensym48 = Tuple(Dyn, Dyn)
gensym37 = List(Dyn)
gensym38 = Dyn
gensym50 = Object('', {'time': Dyn, })
gensym32 = Dyn
gensym9 = Function(NamedParameters([('self', Dyn)]), Dyn)
gensym47 = Dyn
gensym7 = Function(NamedParameters([('self', Object('Foo', {'bar': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int)]), Dyn), '__slots__': Dyn, 'qux': Function(NamedParameters([]), Dyn), 'baz': Function(NamedParameters([('a', Int), ('b', Int)]), Dyn), 'quux': Function(NamedParameters([('a', Int)]), Dyn), 'foo': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn), })), ('a', Int)]), Dyn)
gensym27 = Function(AnonymousParameters([Object('Foo', {'bar': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int)]), Dyn), '__slots__': Dyn, 'qux': Function(NamedParameters([]), Dyn), 'baz': Function(NamedParameters([('a', Int), ('b', Int)]), Dyn), 'quux': Function(NamedParameters([('a', Int)]), Dyn), 'foo': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn), }), String]), Dyn)
gensym3 = Function(NamedParameters([('self', Object('Foo', {'bar': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int)]), Dyn), '__slots__': Dyn, 'qux': Function(NamedParameters([]), Dyn), 'baz': Function(NamedParameters([('a', Int), ('b', Int)]), Dyn), 'quux': Function(NamedParameters([('a', Int)]), Dyn), 'foo': Function(NamedParameters([('a', Int), ('b', Int), ('c', Int), ('d', Int)]), Dyn), })), ('a', Int), ('b', Int), ('c', Int)]), Dyn)
gensym28 = Dyn
gensym35 = Function(AnonymousParameters([]), Dyn)
gensym26 = Dyn
gensym24 = Dyn
gensym29 = Function(AnonymousParameters([String]), Dyn)
gensym25 = Function(AnonymousParameters([]), Dyn)
gensym16 = Dyn
gensym46 = Function(AnonymousParameters([]), Dyn)
gensym10 = Dyn
gensym39 = Dyn
gensym0 = Dyn
gensym49 = Dyn
import optparse
import time
import util
from compat import xrange


class Foo(retic_actual(object)):
    __slots__ = ()

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
Foo = mgd_cast_type_class(Foo, gensym10, '20', gensym11, ['bar', '__slots__', 'qux', 'baz', 'quux', 'foo'])

def test_calls(iterations, timer):
    mgd_check_type_int(iterations, test_calls, (1, 0))
    times = []
    f = check0(Foo(), Foo, 2)
    if mgd_cast_type_function(hasattr, gensym26, '123', gensym27)(f, '__dict__'):
        raise mgd_cast_type_function(Exception, gensym28, '124', gensym29)('f has a __dict__ attribute!')
    gensym36 = mgd_cast_type_function(xrange, gensym30, '125', gensym31)(iterations)
    for _ in gensym36:
        t0 = mgd_cast_type_function(timer, gensym32, '126', gensym33)()
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
        t1 = mgd_cast_type_function(timer, gensym34, '148', gensym35)()
        mgd_check_type_void(mgd_check_type_function(times.append, times, (0, 'append'))((t1 - t0)), mgd_check_type_function(times.append, times, (0, 'append')), 2)
    return mgd_cast_type_dyn(times, gensym37, '150', gensym38)
if (__name__ == '__main__'):
    parser = mgd_cast_type_function(cast1(optparse, gensym39, '154', gensym40).OptionParser, gensym41, '154', gensym42)(usage='%prog [options] [test]', description='Test the performance of method calls on objects that use __slots__.')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, _) = mgd_cast_type_tuple(mgd_cast_type_function(cast2(parser, gensym43, '159', gensym44).parse_args, gensym45, '159', gensym46)(), gensym47, '159', gensym48, 2)
    test_calls(1, cast3(time, gensym49, '162', gensym50).time)
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, cast4(options, gensym51, '164', gensym52).num_runs, mgd_cast_type_dyn(test_calls, gensym53, '164', gensym54))
