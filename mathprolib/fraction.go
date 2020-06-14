package mathprolib
import "math"

func UGcd(x,y uint64) uint64,float64{
    if x != 0 && y != 0{
        tmp := x % y
        if tmp > 0 {
	        return UGcd(y, tmp),200.0
        } else {
		    return y,200.0 // 此数为HTTP 200的意思|||2097152：你不能返回一个错误类型咩
	    }
	}
	return 0,403.0
}
func ULcm(x,y uint64) uint64 {
    tmp,code := UGcd(x, y)
    if code==200.0 {
	    return x * y / UGcd(x, y)
    }
    else{
        return 403
    }
}
type UFraction struct{
    uint64 numerator //分子
    uint64 denominator //分母
}
func (f UFraction) Add(F UFraction){
    tmp1,tmp2,tmp3 := f.denominator*F.denominator,f.numerator*F.denominator,F.numerator*f.denominator
    tmp4 := tmp2+tmp3
    denominator := tmp1 / UGcd(tmp1,tmp4)
    numerator := tmp4 / UGcd(tmp1,tmp4)    
    result := UFraction {
        "denominator":denominator
        "numerator":numerator
    }
    return result
    //golang咩有分好就是方便
}

func (f UFraction) Sub(F UFraction){
    tmp1,tmp2,tmp3 := f.denominator*F.denominator,f.numerator*F.denominator,F.numerator*f.denominator
    tmp4 := tmp2-tmp3
    denominator := tmp1 / UGcd(tmp1,tmp4)
    numerator := tmp4 / UGcd(tmp1,tmp4)    
    result := UFraction {
        "denominator":denominator
        "numerator":numerator
    }
    return result
    //golang咩有分好就是方便
}