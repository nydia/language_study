package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

func main() {
	println('1')
	getData2()
}
func getData2() {
	db, _ := sql.Open("mysql", "root:123456@(localhost:3307)/test")
	defer db.Close() //关闭数据库
	err := db.Ping() //连接数据库
	if err != nil {
		fmt.Println("数据库连接失败")
		return
	} else {
		fmt.Println("数据库连接成功")
	}

	//多行查询
	rows, _ := db.Query("select * from test") //获取所有数据
	var ID int
	var Name, Code string
	for rows.Next() { //循环显示所有的数据
		rows.Scan(&ID, &Name, &Code)
		fmt.Println(ID, "--", Name, "--", Code)
	}
}
