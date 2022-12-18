package array

import "testing"

func Test_array(t *testing.T) {
	var a [3]int
	arr1 := [3]int{1, 2, 3}
	t.Log(a[1], arr1[2])
}
