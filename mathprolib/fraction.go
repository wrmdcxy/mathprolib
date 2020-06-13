package mathprolib
import "math"

func UGcd(x,y uint64) uint64,float64{
    if x != 0 && y != 0{
        tmp := x % y
        if tmp > 0 {
	        return UGcd(y, tmp),200.0
        } else {
		    return y,200.0 // 此数为HTTP 200的意思
	    }
	}
	return 0,403.0
}
func ULcm(x,y uint64) uint64 {
    tmp,code := gcd(x, y)
    if code==200.0 {
	    return x * y / UGcd(x, y)
    }
    else{
        return 403
    }
}
type UFraction struct{
    uint64 son //分子
    uint64 mum //分母
}
func (f UFraction) add(F UFraction){
    tmp1,tmp2,tmp3 := f.mum*F.mum,f.son*F.mum,F.son*f.mum
    tmp4 := tmp2+tmp3
    mum := tmp1 / UGcd(tmp1,tmp4)
    son := tmp4 / UGcd(tmp1,tmp4)    
    result := UFraction {
        "mum":mum
        "son":son
    }
    return result
    //golang咩有分好就是方便
}

func (f UFraction) sub(F UFraction){
    tmp1,tmp2,tmp3 := f.mum*F.mum,f.son*F.mum,F.son*f.mum
    tmp4 := tmp2-tmp3
    mum := tmp1 / UGcd(tmp1,tmp4)
    son := tmp4 / UGcd(tmp1,tmp4)    
    result := UFraction {
        "mum":mum
        "son":son
    }
    return result
    //golang咩有分好就是方便
}