package mathprolib
import (
	"math"
)
const Pi = math.Pi
const E = math.E
const NaN = math.NaN
const Infinity = math.Inf()
const NegtiveInfinity = math.Inf(-1)
const Ln = math.Log  // 白嫖math包的函数太香了（滑稽）
const Log10 = math.Log10
const Log2 = math.Log2
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
}/*@2097152，对哒*/
func Exp(num float64) float64{
    return Pow(E,num)
}
func Log(base float64,exp float64) float64{ 
    return (1/Log10(base))*Log10(exp)
} // @2097152,自己研究的对数公式