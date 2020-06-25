from functools import total_ordering
from math import log10

@total_ordering
class Scientific_notation:

    def __abs__(self):

        return Scientific_notation(abs(self.num), self.exp)

    def __init__(self, num, exp):

        self.num = round(num * 1e3 / 10 ** int(log10(abs(num)))) / 1e3

        self.exp = int(exp) + int(log10(abs(num)))

    def __str__(self):

        return "{} * 10^{}".format(self.num, self.exp)

    def __neg__(self):

        return Scientific_notation(-(self.num), self.exp)

    def __add__(self, other):

        if isinstance(other, Scientific_notation):

            if other.exp == self.exp:

                return Scientific_notation(self.num + other.num, self.exp)

            elif self.exp < other.exp:

                return Scientific_notation(self.num / 10 ** (self.exp - other.exp) + other.num, self.exp)

            else:

                return Scientific_notation(self.num * 10 ** (self.exp - other.exp) + other.num, other.exp)

        elif isinstance(other, int) or isinstance(other, float):

            return self.__add__(Scientific_notation(other, 0))

        raise TypeError(

            f"cannot add from type {str(type(other))[8:-2]} to Scientific_notation")

    def __sub__(self, other):

        return self + (-other)

    def __mul__(self, other):

        if isinstance(other, Scientific_notation):

            return Scientific_notation(self.num * other.num, self.exp + other.exp)

        elif isinstance(other, (int, float)):

            return Scientific_notation(self.num * other,self.exp)

        raise TypeError(

            f"cannot mul from type {str(type(other))[8:-2]} to Scientific_notation")

    def __truediv__(self, other):
        if isinstance(other,Scientific_notation):
            return Scientific_notation(self.num/other.num,self.exp-other.exp)
        elif isinstance(other,(int,float)):
            return Scientific_notation(self.num/other,self.exp)
        raise  TypeError(f"cannot div from type {str(type(other))[8:-2]} to Scientific_notation")

    def __int__(self):
        print("Warning: the number can be too large!")
        return int(self.num * 10 ** self.exp)

    def __float__(self):
        return float(self.num * 10 ** self.exp)

    def __eq__(self, other):
        if isinstance(other,Scientific_notation):
            return abs(self.num - other.num) < 1e-3 and self.exp == other.exp
        elif isinstance(other,(int,float)):
            return abs(float(self)-other) < 1e-3
        raise TypeError(f"cannot get equal from type {str(type(other))[8:-2]} to Scientific_notation")
        
        
    def __lt__(self, other):
        if isinstance(other, Scientific_notation):
            return -(self.num - other.num) >= 1e-3 and self.exp == other.exp
        elif isinstance(other, (int, float)):
            return -(float(self) - other) > 1e-3
        raise TypeError(f"cannot get less than from type {str(type(other))[8:-2]} to Scientific_notation")
 
    def __mod__(self, other):
        if isinstance(other,Scientific_notation):
            if self.exp != 0:
                tmp = self
                if tmp.num > float(other):
                    tmp.num -= float(other)
                else:
                    tmp.num *= 10
                    tmp.exp -= 1
                return tmp%other
            else:
                return self.num%int(float(other))

    def __pow__(self, power, modulo=None):
        power = float(power)
        if modulo is None:
            return Scientific_notation(self.num**power,self.exp*power)

