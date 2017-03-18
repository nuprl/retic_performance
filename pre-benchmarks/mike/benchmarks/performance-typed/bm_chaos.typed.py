from __future__ import division
from retic.runtime import *
from retic.transient import *
from retic.typing import *

def check6(val):
    try:
        val.points
        val.__len__
        val.knots
        val.__repr__
        val.__call__
        val.GetIndex
        val.degree
        val.GetDomain
        return val
    except:
        raise CheckError(val)

def check10(val):
    try:
        val.maxx
        return val
    except:
        raise CheckError(val)

def check11(val):
    try:
        val.minx
        return val
    except:
        raise CheckError(val)

def check24(val):
    try:
        val.thickness
        return val
    except:
        raise CheckError(val)

def check27(val):
    try:
        val.parse_args
        return val
    except:
        raise CheckError(val)

def check18(val):
    try:
        val.num_total
        val.maxy
        val.minx
        val.truncate
        val.splines
        val.width
        val.thickness
        val.get_random_trafo
        val.maxx
        val.miny
        val.num_trafos
        val.transform_point
        val.height
        val.create_image_chaos
        return val
    except:
        raise CheckError(val)

def check4(val):
    try:
        val.y
        return val
    except:
        raise CheckError(val)

def check14(val):
    try:
        val.dist
        return val
    except:
        raise CheckError(val)

def check9(val):
    try:
        val.miny
        return val
    except:
        raise CheckError(val)

def check20(val):
    try:
        val.get_random_trafo
        return val
    except:
        raise CheckError(val)

def check17(val):
    try:
        val.add
        return val
    except:
        raise CheckError(val)

def check22(val):
    try:
        val.GetDomain
        return val
    except:
        raise CheckError(val)

def check13(val):
    try:
        val.height
        return val
    except:
        raise CheckError(val)

def check7(val):
    try:
        val.points
        return val
    except:
        raise CheckError(val)

def check16(val):
    try:
        val.append
        return val
    except:
        raise CheckError(val)

def check26(val):
    try:
        val.OptionParser
        return val
    except:
        raise CheckError(val)

def check8(val):
    try:
        val.maxy
        return val
    except:
        raise CheckError(val)

def check3(val):
    try:
        val.x
        return val
    except:
        raise CheckError(val)

def check25(val):
    try:
        val.truncate
        return val
    except:
        raise CheckError(val)

def check28(val):
    try:
        val.num_runs
        return val
    except:
        raise CheckError(val)

def check21(val):
    try:
        val.splines
        return val
    except:
        raise CheckError(val)

def check15(val):
    try:
        val.num_trafos
        return val
    except:
        raise CheckError(val)

def check12(val):
    try:
        val.width
        return val
    except:
        raise CheckError(val)

def check1(val):
    try:
        val.__rmul__
        val.linear_combination
        val.z
        val.__repr__
        val.__sub__
        val.x
        val.__mul__
        val.y
        val.Mag
        val.dist
        val.__add__
        val.__str__
        return val
    except:
        raise CheckError(val)

def check19(val):
    try:
        val.randrange
        return val
    except:
        raise CheckError(val)

def check5(val):
    try:
        val.z
        return val
    except:
        raise CheckError(val)

def check0(val):
    try:
        val.seed
        return val
    except:
        raise CheckError(val)

def check23(val):
    try:
        val.Mag
        return val
    except:
        raise CheckError(val)

def check2(val):
    try:
        val.sqrt
        return val
    except:
        raise CheckError(val)
import operator
import optparse
import random
check_type_function(check0(random).seed)(1234)
import math
import os
import sys
import time
from compat import print_, reduce, xrange


class GVector(retic_actual(object)):

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    __init__ = check_type_function(__init__)

    def Mag(self):
        check1(self)
        return check_type_float(check_type_function(check2(math).sqrt)((((check_type_float(self.x) ** 2) + (check_type_float(self.y) ** 2)) + (check_type_float(self.z) ** 2))))
    Mag = check_type_function(Mag)

    def dist(self, other):
        check1(self)
        check1(other)
        return check_type_float(check_type_function(check2(math).sqrt)(((((check_type_float(self.x) - check_type_float(other.x)) ** 2) + ((check_type_float(self.y) - check_type_float(other.y)) ** 2)) + ((check_type_float(self.z) - check_type_float(other.z)) ** 2))))
    dist = check_type_function(dist)

    def __add__(self, other):
        check1(self)
        check1(other)
        if (not check_type_function(isinstance)(other, GVector)):
            raise check_type_function(ValueError)(("Can't add GVector to " + check_type_function(str)(check_type_function(type)(other))))
        v = check1(GVector((check_type_float(self.x) + check_type_float(other.x)), (check_type_float(self.y) + check_type_float(other.y)), (check_type_float(self.z) + check_type_float(other.z))))
        return v
    __add__ = check_type_function(__add__)

    def __sub__(self, other):
        check1(self)
        check1(other)
        return check1((self + (other * (- 1))))
    __sub__ = check_type_function(__sub__)

    def __mul__(self, other):
        check1(self)
        check_type_float(other)
        v = check1(GVector((check_type_float(self.x) * other), (check_type_float(self.y) * other), (check_type_float(self.z) * other)))
        return v
    __mul__ = check_type_function(__mul__)
    __rmul__ = __mul__

    def linear_combination(self, other, l1, l2=None):
        if (l2 is None):
            l2 = (1 - l1)
        v = check1(GVector(((check3(self).x * l1) + (check3(other).x * l2)), ((check4(self).y * l1) + (check4(other).y * l2)), ((check5(self).z * l1) + (check5(other).z * l2))))
        return v
    linear_combination = check_type_function(linear_combination)

    def __str__(self):
        check1(self)
        return ('<%f, %f, %f>' % (check_type_float(self.x), check_type_float(self.y), check_type_float(self.z)))
    __str__ = check_type_function(__str__)

    def __repr__(self):
        check1(self)
        return ('GVector(%f, %f, %f)' % (check_type_float(self.x), check_type_float(self.y), check_type_float(self.z)))
    __repr__ = check_type_function(__repr__)
GVector = check_type_class(GVector, ['__rmul__', 'linear_combination', '__init__', '__repr__', '__sub__', '__mul__', 'Mag', 'dist', '__add__', '__str__'])

def GetKnots(points, degree):
    check_type_list(points)
    check_type_int(degree)
    knots = (([0] * degree) + check_type_function(range)(1, (check_type_function(len)(points) - degree)))
    knots = (knots + ([(check_type_function(len)(points) - degree)] * degree))
    return check_type_list(knots)
GetKnots = check_type_function(GetKnots)


class Spline(retic_actual(object)):

    def __init__(self, points, degree=3, knots=None):
        if (knots == None):
            self.knots = check_type_list(GetKnots(check_type_list(points), check_type_int(degree)))
        else:
            if (check_type_function(len)(points) > ((check_type_function(len)(knots) - degree) + 1)):
                raise check_type_function(ValueError)('too many control points')
            elif (check_type_function(len)(points) < ((check_type_function(len)(knots) - degree) + 1)):
                raise check_type_function(ValueError)('not enough control points')
            last = knots[0]
            for cur in knots[1:]:
                if (cur < last):
                    raise check_type_function(ValueError)('knots not strictly increasing')
                last = cur
            self.knots = knots
        self.points = points
        self.degree = degree
    __init__ = check_type_function(__init__)

    def GetDomain(self):
        check6(self)
        return (check_type_int(check_type_list(self.knots)[(check_type_int(self.degree) - 1)]), check_type_int(check_type_list(self.knots)[check_type_int((check_type_function(len)(check_type_list(self.knots)) - check_type_int(self.degree)))]))
    GetDomain = check_type_function(GetDomain)

    def __call__(self, u):
        check6(self)
        check_type_float(u)
        dom = check_type_tuple(check_type_function(self.GetDomain)(), 2)
        if ((u < dom[0]) or (u > dom[1])):
            raise check_type_function(ValueError)('Function value not in domain')
        if (u == dom[0]):
            return check1(check_type_list(self.points)[0])
        if (u == dom[1]):
            return check1(check_type_list(self.points)[(- 1)])
        I = check_type_int(check_type_function(self.GetIndex)(u))
        d = check_type_list([check1(check_type_list(self.points)[check_type_int((((I - check_type_int(self.degree)) + 1) + ii))]) for ii in check_type_function(range)((check_type_int(self.degree) + 1))])
        U = check_type_list(self.knots)
        for ik in check_type_function(range)(1, (check_type_int(self.degree) + 1)):
            for ii in check_type_function(range)((((I - check_type_int(self.degree)) + ik) + 1), (I + 2)):
                ua = check_type_int(U[check_type_int(((ii + check_type_int(self.degree)) - ik))])
                ub = check_type_int(U[check_type_int((ii - 1))])
                co1 = ((ua - u) / (ua - ub))
                co2 = ((u - ub) / (ua - ub))
                index = ((((ii - I) + check_type_int(self.degree)) - ik) - 1)
                d[check_type_int(index)] = check1(check_type_function(check1(d[check_type_int(index)]).linear_combination)(check1(d[check_type_int((index + 1))]), co1, co2))
        return check1(d[0])
    __call__ = check_type_function(__call__)

    def GetIndex(self, u):
        check6(self)
        check_type_float(u)
        dom = check_type_tuple(check_type_function(self.GetDomain)(), 2)
        for ii in check_type_function(range)((check_type_int(self.degree) - 1), (check_type_function(len)(check_type_list(self.knots)) - check_type_int(self.degree))):
            if ((u >= check_type_int(check_type_list(self.knots)[check_type_int(ii)])) and (u < check_type_int(check_type_list(self.knots)[check_type_int((ii + 1))]))):
                I = ii
                break
        else:
            I = (dom[1] - 1)
        return check_type_int(I)
    GetIndex = check_type_function(GetIndex)

    def __len__(self):
        check6(self)
        return check_type_int(check_type_function(len)(check_type_list(self.points)))
    __len__ = check_type_function(__len__)

    def __repr__(self):
        check6(self)
        return ('Spline(%r, %r, %r)' % (check_type_list(self.points), check_type_int(self.degree), check_type_list(self.knots)))
    __repr__ = check_type_function(__repr__)
Spline = check_type_class(Spline, ['GetIndex', '__len__', '__init__', '__repr__', '__call__', 'GetDomain'])


class Chaosgame(retic_actual(object)):

    def __init__(self, splines, thickness=0.1):
        self.splines = splines
        self.thickness = thickness
        self.minx = check_type_function(min)(check_type_list([check3(p).x for spl in splines for p in check7(spl).points]))
        self.miny = check_type_function(min)(check_type_list([check4(p).y for spl in splines for p in check7(spl).points]))
        self.maxx = check_type_function(max)(check_type_list([check3(p).x for spl in splines for p in check7(spl).points]))
        self.maxy = check_type_function(max)(check_type_list([check4(p).y for spl in splines for p in check7(spl).points]))
        self.height = (check8(self).maxy - check9(self).miny)
        self.width = (check10(self).maxx - check11(self).minx)
        self.num_trafos = []
        maxlength = ((thickness * check12(self).width) / check13(self).height)
        for spl in splines:
            length = 0
            curr = check_type_function(spl)(0)
            for i in check_type_function(range)(1, 1000):
                last = curr
                t = ((1 / 999) * i)
                curr = check_type_function(spl)(t)
                length = (length + check_type_function(check14(curr).dist)(last))
            check_type_function(check16(check15(self).num_trafos).append)(check_type_function(max)(1, check_type_function(int)(((length / maxlength) * 1.5))))
        self.num_total = check_type_function(reduce)(check17(operator).add, check15(self).num_trafos, 0)
    __init__ = check_type_function(__init__)

    def get_random_trafo(self):
        check18(self)
        r = check_type_function(check19(random).randrange)((check_type_function(int)(check_type_int(self.num_total)) + 1))
        l = 0
        for i in check_type_function(range)(check_type_function(len)(check_type_list(self.num_trafos))):
            if ((r >= l) and (r < (l + check_type_int(check_type_list(self.num_trafos)[check_type_int(i)])))):
                return check_type_tuple((i, check_type_function(check19(random).randrange)(check_type_int(check_type_list(self.num_trafos)[check_type_int(i)]))), 2)
            l = (l + check_type_int(check_type_list(self.num_trafos)[check_type_int(i)]))
        return check_type_tuple(((check_type_function(len)(check_type_list(self.num_trafos)) - 1), check_type_function(check19(random).randrange)(check_type_int(check_type_list(self.num_trafos)[(- 1)]))), 2)
    get_random_trafo = check_type_function(get_random_trafo)

    def transform_point(self, point, trafo=None):
        x = ((check3(point).x - check11(self).minx) / check12(self).width)
        y = ((check4(point).y - check9(self).miny) / check13(self).height)
        if (trafo is None):
            trafo = check_type_function(check20(self).get_random_trafo)()
        (start, end) = check_type_tuple(check_type_function(check22(check21(self).splines[trafo[0]]).GetDomain)(), 2)
        length = (end - start)
        seg_length = (length / check15(self).num_trafos[trafo[0]])
        t = ((start + (seg_length * trafo[1])) + (seg_length * x))
        basepoint = check_type_function(check21(self).splines[trafo[0]])(t)
        if ((t + (1 / 50000)) > end):
            neighbour = check_type_function(check21(self).splines[trafo[0]])((t - (1 / 50000)))
            derivative = (neighbour - basepoint)
        else:
            neighbour = check_type_function(check21(self).splines[trafo[0]])((t + (1 / 50000)))
            derivative = (basepoint - neighbour)
        if (check_type_function(check23(derivative).Mag)() != 0):
            basepoint.x = (check3(basepoint).x + (((check4(derivative).y / check_type_function(check23(derivative).Mag)()) * (y - 0.5)) * check24(self).thickness))
            basepoint.y = (check4(basepoint).y + ((((- check3(derivative).x) / check_type_function(check23(derivative).Mag)()) * (y - 0.5)) * check24(self).thickness))
        else:
            print_('r', end='')
        check_type_function(check25(self).truncate)(basepoint)
        return check1(basepoint)
    transform_point = check_type_function(transform_point)

    def truncate(self, point):
        check18(self)
        check1(point)
        if (check_type_float(point.x) >= check_type_float(self.maxx)):
            point.x = check_type_float(self.maxx)
        if (check_type_float(point.y) >= check_type_float(self.maxy)):
            point.y = check_type_float(self.maxy)
        if (check_type_float(point.x) < check_type_float(self.minx)):
            point.x = check_type_float(self.minx)
        if (check_type_float(point.y) < check_type_float(self.miny)):
            point.y = check_type_float(self.miny)
    truncate = check_type_function(truncate)

    def create_image_chaos(self, timer, w, h, n):
        check18(self)
        check_type_int(w)
        check_type_int(h)
        check_type_int(n)
        im = check_type_list([([1] * h) for i in check_type_function(range)(w)])
        point = check1(GVector(((check_type_float(self.maxx) + check_type_float(self.minx)) / 2), ((check_type_float(self.maxy) + check_type_float(self.miny)) / 2), 0))
        colored = 0
        times = []
        for _ in check_type_function(range)(n):
            t1 = check_type_function(timer)()
            for i in check_type_function(xrange)(5000):
                point = check1(check_type_function(self.transform_point)(point))
                x = (((check_type_float(point.x) - check_type_float(self.minx)) / check_type_float(self.width)) * w)
                y = (((check_type_float(point.y) - check_type_float(self.miny)) / check_type_float(self.height)) * h)
                x = check_type_function(int)(x)
                y = check_type_function(int)(y)
                if (x == w):
                    x = (x - 1)
                if (y == h):
                    y = (y - 1)
                check_type_list(im[check_type_int(x)])[check_type_int(((h - y) - 1))] = 0
            t2 = check_type_function(timer)()
            check_type_void(check_type_function(times.append)((t2 - t1)))
        return times
    create_image_chaos = check_type_function(create_image_chaos)
Chaosgame = check_type_class(Chaosgame, ['get_random_trafo', 'transform_point', 'create_image_chaos', 'truncate', '__init__'])

def main(n, timer):
    splines = [check6(Spline([check1(GVector(1.59735, 3.30446, 0.0)), check1(GVector(1.57581, 4.12326, 0.0)), check1(GVector(1.31321, 5.28835, 0.0)), check1(GVector(1.6189, 5.32991, 0.0)), check1(GVector(2.88994, 5.5027, 0.0)), check1(GVector(2.37306, 4.38183, 0.0)), check1(GVector(1.662, 4.36028, 0.0))], 3, [0, 0, 0, 1, 1, 1, 2, 2, 2])), check6(Spline([check1(GVector(2.8045, 4.01735, 0.0)), check1(GVector(2.5505, 3.52523, 0.0)), check1(GVector(1.97901, 2.62036, 0.0)), check1(GVector(1.97901, 2.62036, 0.0))], 3, [0, 0, 0, 1, 1, 1])), check6(Spline([check1(GVector(2.00167, 4.01132, 0.0)), check1(GVector(2.33504, 3.31283, 0.0)), check1(GVector(2.3668, 3.23346, 0.0)), check1(GVector(2.3668, 3.23346, 0.0))], 3, [0, 0, 0, 1, 1, 1]))]
    c = check18(Chaosgame(splines, 0.25))
    return check_type_list(check_type_function(c.create_image_chaos)(timer, 1000, 1200, check_type_int(n)))
main = check_type_function(main)
if (__name__ == '__main__'):
    import util
    parser = check_type_function(check26(optparse).OptionParser)(usage='%prog [options]', description='Test the performance of the Chaos benchmark')
    check_type_function(util.add_standard_options_to)(parser)
    (options, args) = check_type_tuple(check_type_function(check27(parser).parse_args)(), 2)
    check_type_function(util.run_benchmark)(options, check28(options).num_runs, main)
