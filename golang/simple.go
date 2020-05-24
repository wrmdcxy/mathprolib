package mathprolib
import (
    _ "fmt"
    "math"
)
func pow(base float64,exp float64)(float64){
    return math.Pow(base,exp) 
}
func root(base float64,exp float64)(float64){
    return pow(base,1/exp)
}
func sqrt(num float64)(float64){
    return root(num,2.0)
}