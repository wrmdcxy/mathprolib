# Version: Test
# Author:LAI-1048576,Toby-LAI
# -*- coding:utf-8 -*-

import math
from functools import total_ordering

REAL = float

e = math.e
π = math.pi
Ф = (math.sqrt(5)-1)/2
γ = 0.5772156649015328
@total_ordering
class INF:
    def __lt__(self, other):
        return False

    def __eq__(self, other):
        return isinstance(other,INF)

    def __str__(self):
        return "∞"

Infinity = INF()

def root(num:REAL,exp:REAL):
    """
    
    :rtype: REAL
    :param num: 开方底数
    :param exp: 开方指数
    :return: 结果
    
    """
    result = num**(1/exp)
    if not isinstance(result,complex):
        return num**(1/exp)
    else:
        return math.nan

def sqrt(num:REAL):
    """
    
    :param num:要开方的数 
    :return: 结果
    """
    return root(num,2)

