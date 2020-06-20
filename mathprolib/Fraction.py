from functools import total_ordering
from logging import warning as warn
class CalculateError(Exception):
	pass

class Fraction(object):
	def __gongyue(self,a,b):
		while b!=0:
			temp=a%b
			a=b
			b=temp
		return a

	def __init__(self,_numerator,denominator):
		if denominator==0:
			raise CalculateError("fatal error:Denominator = 0")
		self._numerator=_numerator
		self.denominator=denominator

	def __float__(self):
		return self._numerator/self.denominator

	def general(self,factor):
		self._numerator*=factor
		self.denominator*=factor

	def all(self):
		return (self._numerator,self.denominator)

	def reduction(self,factor=None):
		if factor==None:
			factor=self.__gongyue(self._numerator,self.denominator)
		if self._numerator/factor!=int(str(self._numerator/factor).split('.')[0]) or self.denominator/factor!=int(str(self.denominator/factor).split('.')[0]):
			warn(f"Reduction failed.Cannot reduction by {factor}")
			return
		self._numerator//=factor
		self.denominator//=factor

	def common(self,other):
		if type(other)!=int and (not isinstance(other,Fraction)) and type(other)!=float:
			raise TypeError(f"can only concatenate Fraction (not {type(other)}) to Fraction")
		else:
			if type(other)==int:
				ofra=VulgarFraction(self.denominator*other,self.denominator)
			elif type(other)==float:
				l=10**len(str(other).split(".")[1])
				ofra=VulgarFraction(int(other*l),l)
				ofra.reduction()
				p=ofra.denominator*self.denominator//self.__gongyue(ofra.denominator,self.denominator)
				self._numerator*=p//self.denominator
				ofra._numerator*=p//ofra.denominator
				self.denominator,ofra.denominator=p,p
			else:
				ofra=VulgarFraction(other._numerator,other.denominator)
				p=ofra.denominator*self.denominator//self.__gongyue(ofra.denominator,self.denominator)
				self._numerator*=p//self.denominator
				ofra._numerator*=p//ofra.denominator
				self.denominator,ofra.denominator=p,p
			return ofra

@total_ordering
class VulgarFraction(Fraction):
	def toMixed(self):
		temp=MixedFraction(0,0,self.denominator)
		temp.numerator=self.numerator
		return temp

	@property
	def numerator(self):
		return self._numerator

	@numerator.setter
	def numerator(self,value):
		self._numerator=value
	
	def __str__(self):
		if self.numerator==self.denominator:
			return '1'
		if self.numerator==0:
			return '0'
		return f"{self.numerator}\n{'—' * len(str(max(self.numerator, self.denominator)))}\n{self.denominator}"

	def __add__(self,other):
		fra=VulgarFraction(self.numerator,self.denominator)
		if type(other)==int:
			fra.numerator+=other*fra.denominator
		elif type(other)==float or isinstance(other,Fraction):
			fra.numerator+=fra.common(other).numerator
		else:
			raise TypeError(f"can only concatenate Fraction (not {type(other)}) to Fraction")
		fra.reduction()
		return fra

	def __sub__(self,other):
		fra=VulgarFraction(self.numerator,self.denominator)
		if type(other)==int:
			fra.numerator-=other*fra.denominator
		elif type(other)==float or isinstance(other,Fraction):
			fra.numerator-=fra.common(other).numerator
		else:
			raise TypeError(f"can only concatenate Fraction (not {type(other)}) to Fraction")
		fra.reduction()
		return fra

	def __mul__(self,other):
		fra=VulgarFraction(self.numerator,self.denominator)
		if type(other)==int:
			fra.numerator*=other
		elif type(other)==float or isinstance(other,Fraction):
			temp=fra.common(other)
			fra.numerator*=temp.numerator
			fra.denominator*=temp.denominator
		else:
			raise TypeError(f"can only concatenate Fraction (not {type(other)}) to Fraction")
		fra.reduction()
		return fra

	def __truediv__(self,other):
		fra=VulgarFraction(self.numerator,self.denominator)
		if type(other)==int:
			fra.denominator*=other
		elif type(other)==float or isinstance(other,Fraction):
			temp=fra.common(other)
			fra.numerator*=temp.denominator
			fra.denominator*=temp.numerator
		else:
			raise TypeError(f"can only concatenate Fraction (not {type(other)}) to Fraction")
		fra.reduction()
		return fra

	def __eq__(self,other):
		fra=VulgarFraction(self.numerator,self.denominator)
		if type(other)==MixedFraction:
			otr=other.toVulgar()
			otr=fra.common(otr)
		else:
			otr=fra.common(other)
		return fra.numerator==otr.numerator

	def __lt__(self,other):
		fra=VulgarFraction(self.numerator,self.denominator)
		if type(other)==MixedFraction:
			otr=other.toVulgar()
			otr=fra.common(otr)
		else:
			otr=fra.common(other)
		return fra.numerator<otr.numerator

@total_ordering
class MixedFraction(Fraction):
	def __init__(self,integer,numerator,denominator):
		if numerator>=denominator:
			raise CalculateError("Numerator should be smaller than denominator")
		if integer<0:
			raise CalculateError("fatal error:Calculate failed.Cause integer < 0")
		super().__init__(numerator,denominator)
		self.integer=integer

	def __eq__(self,other):
		fra=MixedFraction(self.integer,self.numerator,self.denominator).toVulgar()
		otr=fra.common(other)
		return fra==otr

	def __lt__(self,other):
		fra=MixedFraction(self.integer,self.numerator,self.denominator).toVulgar()
		otr=fra.common(other)
		return fra<otr

	def toVulgar(self):
		num=self.integer*self.denominator+self.numerator
		f=VulgarFraction(num,self.denominator)
		return f

	def all(self):
		return (self.integer,self.numerator,self.denominator)

	@property
	def numerator(self):
		return self._numerator

	@numerator.setter
	def numerator(self,value):
		nm=value
		if nm>=self.denominator:
			def itg():
				nonlocal self
				nonlocal nm
				temp=nm//self.denominator
				if temp>0:
					nm-=self.denominator*temp
					self.integer+=temp
			itg()
		elif nm<0:
			nm+=self.integer*self.denominator
			self.integer=0
			itg()
		else:
			pass
		self._numerator=nm
		self.reduction()


	def __str__(self):
		if self.numerator==0:
			return str(self.integer)
		return f"{' '*len(str(self.integer)) if self.integer!=0 else ''}{self.numerator}\n{self.integer if self.integer!=0 else ''}{'—' * len(str(max(self.numerator, self.denominator)))}\n{' '*len(str(self.integer)) if self.integer!=0 else ''}{self.denominator}"

	def __add__(self,other):
		fra=MixedFraction(self.integer,self.numerator,self.denominator).toVulgar()
		return (fra+other).toMixed()

	def __sub__(self,other):
		fra=MixedFraction(self.integer,self.numerator,self.denominator).toVulgar()
		return (fra-other).toMixed()

	def __mul__(self,other):
		fra=MixedFraction(self.integer,self.numerator,self.denominator).toVulgar()
		return (fra*other).toMixed()

	def __truediv__(self,other):
		fra=MixedFraction(self.integer,self.numerator,self.denominator).toVulgar()
		return (fra/other).toMixed()