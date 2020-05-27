# Version: Test
# Author:LAI-1048576,Toby-LAI
# -*- coding:utf-8 -*-

import math
from functools import total_ordering

REAL = float
Ф = (math.sqrt(5) - 1) / 2
γ = 0.5772156649015328

def deg(num):
    return num*180/math.pi
def rad(num):
    return num/180*math.pi


sin, cos, tan = lambda n: math.sin(rad(n)), lambda n: math.cos(rad(n)), lambda n: math.tan(rad(n))
sinh,cosh,tanh = math.sin,math.cos,math.tan
asin,acos,atan = math.asin,math.acos,math.atan
ln,log,log2 = math.log,math.log10,math.log2
π,e,fact = math.pi,math.e,math.factorial
def gcd(x, y):
    smaller = x if x < y else y
    g = [i for i in range(1,smaller+1) if x % i == 0 and y % i == 0][-1]
    return g

def lcm(x, y):
    return x*y//gcd(x,y)
@total_ordering
class INF:
    def __lt__(self, other):
        return False

    def __eq__(self, other):
        return isinstance(other, INF)

    def __str__(self):
        return "∞"

    def __neg__(self):
        return NEGINF()


@total_ordering
class NEGINF:
    def __lt__(self, other):
        return True

    def __eq__(self, other):
        return isinstance(other, NEGINF)

    def __str__(self):
        return "∞"


Infinity = INF()


def root(num: REAL, exp: REAL):
    """

    :rtype: REAL
    :param num: 开方底数
    :param exp: 开方指数
    :return: 结果

    """
    result = num ** (1 / exp)
    if not isinstance(result, complex):
        return num ** (1 / exp)
    else:
        return math.nan


def sqrt(num: REAL):
    """

    :param num:要开方的数
    :return: 结果
    """
    return root(num, 2)

