package mathprolib
import "testing"

//Tests


//Tested.ok
//1:Fail,3.326s
//2:ok,3.369s
//3:ok,3.332s
func TestPowandSqrtandRoot(t *testing.T){
	if pr:=Pow(2.0,3.0);pr!=8.0{
		t.Fatal("Failed,result=",pr,".The result should be 4.")
	}else{
		t.Log("Success.",pr)
	}
	if sr:=Sqrt(64.0);sr!=8.0{
		t.Fatal("Failed,result=",sr,".The result should be 8.")
	}else{
		t.Log("Success.",sr)
	}
	if rr:=Root(27.0,3.0);!(2.999999<rr && rr<3.0){
		t.Fatal("Failed,result=",rr,".The result should be 3.")
	}else{
		t.Log("Success.",rr)
	}
}


//Tested.ok
//2:ok,3.369s
//3:ok,3.332s
func TestRound(t *testing.T){
	if res:=Round(0.56772981827312897716);res!=1.0{
		t.Fatal("Failed,result=",res,".The result should be 1.")
	}else{
		t.Log("Success.",res)
	}
}


//Tested.ok
//3:ok,3.332s
func TestFloorandCeil(t *testing.T){
	if res,res2:=Floor(2.361237633772981827312897716),Ceil(1.129376215362789127888827763663287);res!=2.0 || res2!=2.0{
		t.Fatal("Failed,result=",res,res2,".The result should be 2,2.")
	}else{
		t.Log("Success.",res,res2)
	}
}