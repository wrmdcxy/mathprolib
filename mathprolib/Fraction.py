
from functools import total_ordering


def gcd(x, y):
    smaller = x if x < y else y
    g = [i for i in range(1, smaller + 1) if x % i == 0 and y % i == 0][-1]
    return g


@total_ordering
class Fraction:

    def __lt__(self, other):
        if isinstance(other,Fraction):
            numerator1 = self.numerator*other.denominator
            numerator2 = self.denominator*other.numerator
            return numerator1 < numerator2
        else:
            return float(self) < other

    def __eq__(self, other):
        if isinstance(other,Fraction):
            numerator1 = self.numerator*other.denominator
            numerator2 = self.denominator*other.numerator
            return numerator1 == numerator2
        else:
            return abs(float(self) - other) <= 1e-5

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}\n{'—' * len(str(max(self.numerator, self.denominator)))}\n{self.denominator}"

    def __add__(self, other):
        if isinstance(other, Fraction):
            tmp1, tmp2 = other.denominator * self.denominator, other.numerator * self.denominator + self.numerator * other.denominator
            tmp3 = tmp1 // gcd(tmp1, tmp2)
            tmp2 = tmp2 // (tmp1 // tmp2)
            del tmp1
            return Fraction(tmp2, tmp3)
        elif isinstance(other, int):
            return self + Fraction(other, 1)
        elif isinstance(other, float):
            float_str = str(other)
            numbers = len(float_str) - float_str.find(".") - 1
            return self + Fraction(int(float_str.strip("i")), 10 ** numbers)
        raise TypeError(
                f"cannot add from type {str(type(other))[8:-2]} to Fraction")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            tmp1, tmp2 = other.denominator * self.denominator, other.numerator * self.denominator - self.numerator * other.denominator
            tmp3 = tmp1 // gcd(tmp1, tmp2)
            tmp2 = tmp2 // (tmp1 // tmp2)
            del tmp1
            return Fraction(tmp2, tmp3)
        elif isinstance(other, int):
            return self - Fraction(other, 1)
        elif isinstance(other, float):
            float_str = str(other)
            numbers = len(float_str) - float_str.find(".") - 1
            return self - Fraction(int(float_str.strip("i")), 10 ** numbers)
        
        raise TypeError(
                f"cannot sub from type {str(type(other))[8:-2]} to Fraction")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            tmp1, tmp2 = other.denominator * self.denominator, self.numerator * self.numerator
            tmp3 = tmp1 // gcd(tmp1, tmp2)
            tmp2 = tmp2 // (tmp1 // tmp2)
            del tmp1
            return Fraction(tmp2, tmp3)
        elif isinstance(other, int):
            return self * Fraction(other, 1)
        elif isinstance(other, float):
            float_str = str(other)
            numbers = len(float_str) - float_str.find(".") - 1
            return self * Fraction(int(float_str.strip("i")), 10 ** numbers)        
        raise TypeError(
                f"cannot mul from type {str(type(other))[8:-2]} to Fraction")

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return self * Fraction(other.denominator, other)
        elif isinstance(other, int):
            return self * Fraction(1, other)
        elif isinstance(other, float):
            float_str = str(1 / other)
            numbers = len(float_str) - float_str.find(".") - 1
            return self * Fraction(int(float_str.strip("i")), 10 ** numbers)
        raise TypeError(
                f"cannot div from type {str(type(other))[8:-2]} to Fraction")

    def reciprocal(self):
        return Fraction(self.denominator,self.numerator)

    def to_ffraction(self):
        num = self.numerator // self.denominator
        numerator = self.numerator - (self.numerator // self.denominator)*self.denominator
        denominator = self.denominator
        return FFraction(num=num,numerator=numerator,denominator=denominator)

    def __int__(self):
        return int(self.numerator / self.denominator)

    def __float__(self):
        return self.numerator / self.denominator

class FFraction:
    def __init__(self,num,numerator,denominator):
        self.fraction = Fraction.__init__(num*denominator+numerator,denominator)
        self.num = num
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(other,FFraction):
            tmp1 = self.fraction + other.fraction
            tmp2 = tmp1.denominator
            tmp3 = tmp1.numerator
            tmp4 = tmp3//tmp2
            tmp3 -= tmp4*tmp2
            return FFraction(tmp4,tmp3,tmp2)
        elif isinstance(other,Fraction):
            return self+FFraction(0,other.numerator,other.denominator)
        elif isinstance(other,int):
            return self+FFraction(other,0,1)
        elif isinstance(other,float):
            return self+(Fraction(0,1)+other)
        raise TypeError


    def __sub__(self, other):
        if isinstance(other,FFraction):
            tmp1 = self.fraction - other.fraction
            tmp2 = tmp1.denominator
            tmp3 = tmp1.numerator
            tmp4 = tmp3//tmp2
            tmp3 -= tmp4*tmp2
            return FFraction(tmp4,tmp3,tmp2)
        elif isinstance(other,Fraction):
            return self-FFraction(0,other.numerator,other.denominator)
        elif isinstance(other,int):
            return self-FFraction(other,0,1)
        elif isinstance(other,float):
            return self-(Fraction(0,1)+other)
        raise TypeError


    def __mul__(self, other):
        if isinstance(other,FFraction):
            tmp1 = self.fraction * other.fraction
            tmp2 = tmp1.denominator
            tmp3 = tmp1.numerator
            tmp4 = tmp3//tmp2
            tmp3 -= tmp4*tmp2
            return FFraction(tmp4,tmp3,tmp2)
        elif isinstance(other,Fraction):
            return self*FFraction(0,other.numerator,other.denominator)
        elif isinstance(other,int):
            return self*FFraction(other,0,1)
        elif isinstance(other,float):
            return self*(Fraction(0,1)+other)
        raise TypeError

     

if __name__ == '__main__':
    fr = Fraction(1, 2)
    print(fr)
