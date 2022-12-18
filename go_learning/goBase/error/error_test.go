package error

import (
	"errors"
	"fmt"
	"testing"
)

//斐波那契数列
func fibonacci(n int) ([]int, error) {
	if n < 0 {
		fmt.Println("error ....")
		return nil, errors.New("n is forbbiden small zero")
	}
	fibList := []int{1, 1}
	for i := 2; i < n; i++ {
		fibList = append(fibList, fibList[i-2]+fibList[i-1])
	}
	return fibList, nil
}

func Test_error(t *testing.T) {
	a, err := fibonacci(10)
	if err != nil {
		fmt.Println("错误")
	}
	fmt.Println(a)

	a2, err2 := fibonacci(-1)
	if err2 != nil {
		fmt.Print("错误信息:")
		fmt.Println(err2)
		return
	}
	fmt.Println(a2)

}
