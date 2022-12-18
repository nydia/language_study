package expression

import (
	"fmt"
	"testing"
)

func Test_expression(t *testing.T) {
	//变量的类型和初始值必须保留一个
	var name1 = 1
	fmt.Print(name1)

	var name2 string
	fmt.Println(name2)

	//短变量声明
	name3 := "1"
	fmt.Println(name3)

	name4 := "4" //声明
	name4 = "5"  //赋值
	fmt.Println(name4)
}
