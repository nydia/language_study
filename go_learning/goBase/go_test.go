package main

import (
	"log"
	"testing"
)

func TestPrint(t *testing.T) {
	t.Log("nihao")

}

func Test1(t *testing.T) {
	t.Log("nihao")
}

func Test2(t *testing.T) {

	var _type string = "1"
	var ins interface{}
	if "1" == _type {
		ins = returnName1()
	} else {
		ins = returnName2()
	}
	log.Println("结束", ins)
}

type Name1 struct {
	Name1 string
}
type Name2 struct {
	Name2 string
}

func returnName1() *Name1 {
	_name1 := new(Name1)
	_name1.Name1 = "soll"
	return _name1
}
func returnName2() *Name2 {
	_name2 := new(Name2)
	_name2.Name2 = "soll"
	return _name2
}
