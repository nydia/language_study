package slice

import (
	"fmt"
	"testing"
)

//数组切片
func Test_slice(t *testing.T) {
	var a = [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	//a数组 2到3，包括2不包括3
	a1 := a[2:3]
	t.Log(len(a1))
	t.Log(a1[0])

	fmt.Println("-------------")

	//2代表从下表2开始（0，1，2），到下表9不包括10
	a2 := a[2:10]
	for i := 0; i < len(a2); i++ {
		fmt.Print(a2[i])
		fmt.Println(",")
	}
	t.Log(len(a2))
}
