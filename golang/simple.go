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