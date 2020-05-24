package mathprolib
import (
	_ "fmt"
	"math"
)
func Pow(base float64,exp float64)(float64){
	return math.Pow(base,exp) 
}
func Root(base float64,exp float64)(float64){
	return Pow(base,1/exp)
}
func Sqrt(num float64)(float64){
	return Root(num,2.0)
}
func Round(num float64)(float64){
	return math.Floor(num+0.5)
}
func Floor(num float64)(float64){
	return math.Floor(num)
}
func Ceil(num float64)(float64){
	return math.Ceil(num)
}