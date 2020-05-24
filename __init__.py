# Version: Test
# Author:LAI-1048576,Toby-LAI
# -*- coding:utf-8 -*-

import math
from functools import total_ordering


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


