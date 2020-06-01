package mathprolib
import (
    "math"
    "strconv"
    "strings"
)
const Pi = math.Pi
const E = math.E
var NaN = math.NaN()
var Infinity = math.Inf(1)
var NegtiveInfinity = math.Inf(-1)
var Ln = math.Log
var Log10 = math.Log10
var Log2 = math.Log2
func Pow(base float64,exp float64)(float64){
    return math.Pow(base,exp) 
}
func Root(base float64,exp float64)(float64){
    if(FloatMod(exp,2.0)==0.0&&base<0){return NaN}
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
}
func Higher(num1 float64,num2 float64)float64{
    if num1>num2{return num1}
    return num2
}
func Smaller(num1 float64,num2 float64)float64{
    if num1<num2{return num1}
    return num2
}
func FloatMod(dividend float64,divisor float64)interface{}{
    bs:=float64(math.Pow10(int(Higher(float64(len(strings.Split(strconv.FormatFloat(dividend,'f',-1,64),".")[1])),float64(len(strings.Split(strconv.FormatFloat(divisor,'f',-1,64),".")[1]))))))
    fdividend,fdivisor:=int(dividend*bs),int(divisor*bs)
    res:=fdividend%fdivisor
    return float64(res)/float64(bs)
}