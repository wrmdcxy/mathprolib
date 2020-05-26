from tkinter import *
import easygui
import math
w = Tk()
equation,final = StringVar(),StringVar()
def func_set(name):
    a = easygui.integerbox("数1？")
    b = easygui.integerbox("数2？")
    equation.set(f"{name}("+equation.get()+f"{a},{b})")
def lcm(x, y):
    return x*y//gcd(x,y)
def gcd(x, y):
    smaller = x if x < y else y
    hcf = [i for i in range(1,smaller+1) if x % i == 0 and y % i == 0][-1]
    return hcf
def num(n):
    equation.set(equation.get() + str(n))
sin,cos,tan = lambda n: math.sin(math.radians(n)),lambda n: math.cos(math.radians(n)),lambda n: math.tan(math.radians(n))
sinh,cosh,tanh = math.sin,math.cos,math.tan
asin,acos,atan = math.asin,math.acos,math.atan
deg,rad,sqrt = math.degrees,math.radians,math.sqrt
binary,october,hexadecimal = lambda n: bin(n)[2:],lambda n: oct(n)[2:],lambda n: hex(n)[2:]
ln,log,log2 = math.log,math.log10,math.log2
π,e,fact = math.pi,math.e,math.factorial
decimal_fraction = lambda n: n - int(n)
def ce():
    equation.set('')
    final.set('')
def calculate():
    try:
        final.set(f"={str(eval(equation.get().replace('×','*').replace('÷','/').replace('^','**').replace('mod','%')))}")
    except Exception:
        easygui.exceptionbox()
        ce()
def function(name):
    equation.set(name + '(' + equation.get() + ')')
w.geometry('1500x1000')
Button(w, text=0, command=lambda: num(0), width=7, height=2, font=('Arial',20)).grid(row=1,column=0)
Button(w, text=1, command=lambda: num(1), width=7, height=2, font=('Arial',20)).grid(row=1,column=1)
Button(w, text=2, command=lambda: num(2), width=7, height=2, font=('Arial',20)).grid(row=1,column=2)
Button(w, text=3, command=lambda: num(3), width=7, height=2, font=('Arial',20)).grid(row=2,column=0)
Button(w, text=4, command=lambda: num(4), width=7, height=2, font=('Arial',20)).grid(row=2,column=1)
Button(w, text=5, command=lambda: num(5), width=7, height=2, font=('Arial',20)).grid(row=2,column=2)
Button(w, text=6, command=lambda: num(6), width=7, height=2, font=('Arial',20)).grid(row=3,column=0)
Button(w, text=7, command=lambda: num(7), width=7, height=2, font=('Arial',20)).grid(row=3,column=1)
Button(w, text=8, command=lambda: num(8), width=7, height=2, font=('Arial',20)).grid(row=3,column=2)
Button(w, text=9, command=lambda: num(9), width=7, height=2, font=('Arial',20)).grid(row=4,column=1)
Button(w, text='.', command=lambda: num('.'), width=7, height=2, font=('Arial',20)).grid(row=5,column=3)
Button(w, text='+', command=lambda: num('+'), width=7, height=2, font=('Arial',20)).grid(row=1, column=3)
Button(w, text='-', command=lambda: num('-'), width=7, height=2, font=('Arial',20)).grid(row=2, column=3)
Button(w, text='×', command=lambda: num('×'), width=7, height=2, font=('Arial',20)).grid(row=3, column=3)
Button(w, text='÷', command=lambda: num('÷'), width=7, height=2, font=('Arial',20)).grid(row=4, column=3)
Button(w, text='^', command=lambda: num('^'), width=7, height=2, font=('Arial',20)).grid(row=4, column=2)
Button(w, text='(', command=lambda: num('('), width=7, height=2, font=('Arial',20)).grid(row=5, column=1)
Button(w, text=')', command=lambda: num(')'), width=7, height=2, font=('Arial',20)).grid(row=5, column=2)
Button(w, text='阶乘', command=lambda: function('fact'), width=7, height=2, font=('Arial',20)).grid(row=5, column=0)
Button(w, text='sin(角度)', command=lambda: function('sin'), width=7, height=2, font=('Arial',20)).grid(row=6, column=0)
Button(w, text='cos(角度)', command=lambda: function('cos'), width=7, height=2, font=('Arial',20)).grid(row=6, column=1)
Button(w, text='tan(角度)', command=lambda: function('tan'), width=7, height=2, font=('Arial',20)).grid(row=6, column=2)
Button(w, text='sin(弧度)', command=lambda: function('sinh'), width=7, height=2, font=('Arial',20)).grid(row=7, column=0)
Button(w, text='cos(弧度)', command=lambda: function('cosh'), width=7, height=2, font=('Arial',20)).grid(row=7, column=1)
Button(w, text='tan(弧度)', command=lambda: function('tanh'), width=7, height=2, font=('Arial',20)).grid(row=7, column=2)
Button(w, text='asin', command=lambda: function('asin'), width=7, height=2, font=('Arial',20)).grid(row=8, column=0)
Button(w, text='acos', command=lambda: function('acos'), width=7, height=2, font=('Arial',20)).grid(row=8, column=1)
Button(w, text='atan', command=lambda: function('atan'), width=7, height=2, font=('Arial',20)).grid(row=8, column=2)
Button(w, text='平方根', command=lambda: function('sqrt'), width=7, height=2, font=('Arial',20)).grid(row=10, column=0)
Button(w, text='弧度-角度', command=lambda: function('deg'), width=7, height=2, font=('Arial',20)).grid(row=9, column=0)
Button(w, text='角度-弧度', command=lambda: function('rad'), width=7, height=2, font=('Arial',20)).grid(row=9, column=1)
Button(w, text='绝对值', command=lambda: function('abs'), width=7, height=2, font=('Arial',20)).grid(row=9, column=2)
Button(w, text='二进制', command=lambda: function('binary'), width=7, height=2, font=('Arial',20)).grid(row=10, column=1)
Button(w, text='八进制', command=lambda: function('october'), width=7, height=2, font=('Arial',20)).grid(row=10, column=2)
Button(w, text='十六进制', command=lambda: function('hexadecimal'), width=7, height=2, font=('Arial',20)).grid(row=10, column=3)
Button(w, text='log2', command=lambda: function('log2'), width=7, height=2, font=('Arial',20)).grid(row=1, column=4)
Button(w, text='log10', command=lambda: function('log'), width=7, height=2, font=('Arial',20)).grid(row=1, column=5)
Button(w, text='ln', command=lambda: function('ln'), width=7, height=2, font=('Arial',20)).grid(row=1, column=6)
Button(w, text='π', command=lambda: num('π'), width=7, height=2, font=('Arial',20)).grid(row=2, column=6)
Button(w, text='e', command=lambda: num('e'), width=7, height=2, font=('Arial',20)).grid(row=2, column=4)
Button(w, text='CE', command=ce, width=7, height=2, font=('Arial',20)).grid(row=3, column=5)
Button(w, text='取余', command=lambda: num(' mod '), width=7, height=2, font=('Arial',20)).grid(row=1, column=7)
Button(w, text='取整', command=lambda: function('int'), width=7, height=2, font=('Arial',20)).grid(row=2, column=7)
Button(w, text='取小', command=lambda: function('decimal_fraction'), width=7, height=2, font=('Arial',20)).grid(row=2, column=5)
Button(w, text='←', command=lambda: equation.set(equation.get()[:-1]), width=7, height=2, font=('Arial',20)).grid(row=2, column=6)
Button(w, text='=', command=calculate, width=7, height=2, font=('Arial',20)).grid(row=4,column=0)
Button(w, text='最小公倍数', command=lambda: func_set('lcm'), width=7, height=2, font=('Arial',20)).grid(row=3,column=4)
Button(w, text='最大公约数', command=lambda: func_set('gcd'), width=7, height=2, font=('Arial',20)).grid(row=3,column=5)

Label(w, textvar=final, font=('Arial',30)).grid(row=0,column=6)
Label(w, textvar=equation, font=('Arial',30)).grid(row=0,column=2)
w.title('计算器')
w.mainloop()
