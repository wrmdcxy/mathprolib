from math import nan as NaN
from simple import log10
class Scientific_notation:
    def __init__(self,num,exp):
        self.num = round(num*1e3)/1e3/10**int(log(num))
        self.exp = int(exp)+int(log(num))
    
    def __str__(self):
        return "{} * 10^{}".format(self.num,self.exp)

    def __add__(self,other):
        if isinstance(other,Scientific_notation):
            if other.exp == self.exp:
                return Scientific_notation(self.num+other.num,self.exp)
            elif self.exp < other.exp:
                return Scientific_notation(self.num/10**(self.exp-other.exp)+other.num,self.exp)
            else:
                return Scientific_notation(self.num*10**(self.exp-other.exp)+other.num, other.exp)
        elif isinstance(other,int) or isinstance(other,float):
            return self.__add__(Scientific_notation(other,0))
        
        else:
            raise TypeError(
                f"cannot add from type {str(type(other))[8:-2]} to Scientific_notation")



if __name__ == "__main__":
    print(Scientific_notation(2,7)+Scientific_notation(1,6))
