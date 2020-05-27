package mathprolib
import "math"
func Deg(num float64)(float64){
    return num*180/math.Pi
}
func Rad(num float64)(float64){
    return num/180*math.Pi
}

Sinh:=m.Sin
Cosh:=m.Cos
Tanh:=m.Tan
Asinh:=m.Asin
Acosh:=m.Acos
Atanh:=m.Atan
Sincosh:=m.Sincos
Sin:=func(float64 num)(float64){return Sinh(Rad(num))}
Cos:=func(float64 num)(float64){return Cosh(Rad(num))}
Tan:=func(float64 num)(float64){return Tanh(Rad(num))}