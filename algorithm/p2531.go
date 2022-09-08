package main

import "fmt"

func main() {
	fmt.Println(fib(0))
}

func fib(n int) int {
	var mod int = 1000000007
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	} else {
		var i int = 0
		var j int = 0
		var m int = 1
		for k := 2; k <= n; k++ {
			i = j
			j = m
			m = (i + j) % mod
		}
		return m
	}
}
