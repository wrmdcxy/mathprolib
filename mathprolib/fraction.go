package mathprolib
import "math"

func gcd(x,y uint64) uint64,float64{
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
func lcm(x,y uint64) uint64 {
    tmp,code := gcd(x, y)
    if code==200.0 {
	    return x * y / gcd(x, y)
    }
    else{
        return 403
    }
}
type Fraction struct{
    uint64 son //分子
    uint64 mum //分母
}
func (f Fraction) add(F Fraction){
    tmp1,tmp2,tmp3 := f.mum*F.mum,f.son*F.mum,F.son*f.mum
    tmp4 := tmp2+tmp3
    mum := tmp1 / gcd(tmp1,tmp4)
    son := tmp4 / gcd(tmp1,tmp4)    
    result := Fraction {
        "mum":mum
        "son":son
    }
    return result
    //golang咩有分好就是方便
}