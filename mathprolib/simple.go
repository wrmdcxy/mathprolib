package mathprolib
import (
	"math"
)
const Pi = math.Pi
const E = math.E
var NaN = math.NaN//bug1
var Infinity = math.Inf(1)//bug1 and bug2
var NegtiveInfinity = math.Inf(-1)//bug1
var Ln = math.Log//bug1
var Log10 = math.Log10//bug1
var Log2 = math.Log2//bug1
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
    return -num
}
func Exp(num float64) float64{
    return Pow(E,num)
}
func Log(base float64,exp float64) float64{ 
    return (1/Log10(base))*Log10(exp)
} // @2097152,自己研究的对数公式    回复@1048576:ok