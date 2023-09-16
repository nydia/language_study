package _map

import (
	"fmt"
	"testing"
)

func Test_map(t *testing.T) {
	user := make(map[string]int)
	fmt.Println(user["test"])

	user["test"] = 3
	fmt.Println(user["test"])

	user2 := map[string]int{
		"name1": 1,
		"name2": 2,
	}

	fmt.Println(user2["name2"])
}
