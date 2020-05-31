package mathprolib
import (
	"math"
)
const pi = 3.14159265358979
const e = 2.718281828459045
const NaN = math.NaN
const Infinity = math.Inf()
const NegtiveInfinity = math.Inf(-1)
func Pow(base float64,exp float64)(float64){
	return math.Pow(base,exp) 
}
func Root(base float64,exp float64)(float64){
    if(exp%2==0&&base<0){return NaN}
	return Pow(base,1/exp)
}
func Sqrt(num float64)(float64){
	return Root(num,2.0)
}
func Round(num float64)(int64){
	return int64(math.Floor(num+0.5))
}
func Floor(num float64)(int64){
	return int64(math.Floor(num))
}
func Ceil(num float64)(int64){
	return int64(math.Ceil(num))
}
func Abs(num float64)(float64){
	if(num>0){return num}
	return -num
}
func Neg(num float64)float64{
    return -num//@1048576 是这个意思吗
}