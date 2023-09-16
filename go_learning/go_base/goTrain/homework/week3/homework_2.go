package main

import (
	"database/sql"
	"errors"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

func main() {
	var val = wikidata2()
	fmt.Println(val)
}
func wikidata2() (err error) {
	db, _ := sql.Open("mysql", "root:123456@(localhost:3307)/test")
	defer db.Close()  //关闭数据库
	err2 := db.Ping() //连接数据库
	if err2 != nil {
		fmt.Println("数据库连接失败")
		return
	} else {
		fmt.Println("数据库连接成功")
	}

	var node WikiNode2
	err3 := db.QueryRow("select * from tbl_hezi_wiki_node where id  = 100").Scan(&node.ID, &node.ParentId, &node.Url, &node.Name)
	//错误处理，如果没找到对应的movie，Scan()将返回sql.ErrNoRows错误。
	if err3 != nil {
		switch {
		case errors.Is(err3, sql.ErrNoRows):
			return errors.New("错误查询")
		default:
			return err3
		}
	}

	return err3
}

type WikiNode2 struct {
	ID       int    `db:"id"`
	ParentId int    `db:"parent_id"`
	Url      string `db:"url"`
	Name     string `db:"name"`
}
