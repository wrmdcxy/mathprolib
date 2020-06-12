package mathprolib
import "math"

func gcd(x,y int64) int64,float64{
    if x != 0 && y != 0{
        tmp := x % y
        if tmp > 0 {
	        return gcd(y, tmp),200.0
        } else {
		    return y,200.0 // 此数为HTTP 200的意思
	    }
	}
	return 0,403.0
}
func lcm(x,y int64) int64 {
    tmp,code := gcd(x, y)
    if code==200.0 {
	    return x * y / gcd(x, y)
    }
    else{
        return 403
    }
}