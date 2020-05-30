package mathprolib
func Fibonacci(num int16) []int64{
    var b int64 = 0
    var temp int64 = 1  //防止认为不是int64
    var a int64
    var result []int64 = {}[:]
    for i:=0;i<num;i++{
        result = append(result,temp)
        a = b 
        b = temp
        temp = a+b
    }
}
func IsOdd(int64 num) bool{
    return num%2 == 1
}
func IsEven(int64 num) bool{
    return num%2 == 0
}
func Map(type T,type ftype)(array []T,function ftype) []T{ 
    //静态类型，没办法
    var result []T = {}[:]
    for _,v := range array{ 
        result = append(result,function(result))
    }
    return result
}