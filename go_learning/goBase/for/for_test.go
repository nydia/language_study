package _for

import (
	"fmt"
	"testing"
)

func Test_for(t *testing.T) {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}
}
