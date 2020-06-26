package mathprolib
func Map(type T,type RT)(array []T,function (func(T) RT)) []T{ 
    //静态类型，没办法
    var result []T = {}[:]
    for _,v := range array{ 
        result = append(result,function(result))
    }
    return result
}
func Reduce(type T,type RT)(array T,function (func(T,T) RT)) RT{
    //泛型就是别扭
}
