from math import nan as NaN
from math import log10
from ctypes import Union


class Scientific_notation:
    def __abs__(self):
        return Scientific_notation(abs(self.num),self.exp)
    def __init__(self, num, exp):
        self.num = round(num*1e3/10**int(log10(abs(num))))/1e3
        self.exp = int(exp)+int(log10(abs(num)))

    def __str__(self):
        return "{} * 10^{}".format(self.num, self.exp)

    def __neg__(self):
        return Scientific_notation(-(self.num), self.exp)

    def __add__(self, other):
        if isinstance(other, Scientific_notation):
            if other.exp == self.exp:
                return Scientific_notation(self.num+other.num, self.exp)
            elif self.exp < other.exp:
                return Scientific_notation(self.num/10**(self.exp-other.exp)+other.num, self.exp)
            else:
                return Scientific_notation(self.num*10**(self.exp-other.exp)+other.num, other.exp)
        elif isinstance(other, int) or isinstance(other, float):
            return self.__add__(Scientific_notation(other, 0))


        raise TypeError(
                f"cannot add from type {str(type(other))[8:-2]} to Scientific_notation")

    def __sub__(self, other):
        return self+(-other)

    def __mul__(self,other):
        if isinstance(other, Scientific_notation):
            return Scientific_notation(self.num*other.num,self.exp+other.exp)
        elif isinstance(other,Union(int,float)):
            return Scientific_notation(self.num*other, self.exp*other.exp)
        raise TypeError(
                f"cannot mul from type {str(type(other))[8:-2]} to Scientific_notation")
    
    

if __name__ == "__main__":
    print(Scientific_notation(111,2)*Scientific_notation(111,4))
