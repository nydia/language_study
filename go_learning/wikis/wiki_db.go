package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

func main() {
	wikidata()
}
func wikidata() {
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
	rows, _ := db.Query("select * from tbl_hezi_wiki_node") //获取所有数据
	var ID, ParentId int
	var Url, Name string

	//fmt.Println("长度： ", rows.)
	for rows.Next() { //只能读取一次，之后数据rows.Next()数据为空
		rows.Scan(&ID, &ParentId, &Url, &Name)
		fmt.Println(ID, "--", ParentId, "--", Url, "--", Name)
	}

}

type WikiNode struct {
	ID       int    `db:"id"`
	ParentId int    `db:"parent_id"`
	Url      string `db:"url"`
	Name     string `db:"name"`
}
