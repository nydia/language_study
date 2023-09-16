package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

func main() {
	var wikiNodeArr []WikiNode2
	wikiNodeArr, err := wikidata2()
	if err != nil {
		fmt.Println("查询错误")
	}
	fmt.Println(wikiNodeArr)
}
func wikidata2() ([]WikiNode2, error) {
	db, _ := sql.Open("mysql", "root:123456@(localhost:3307)/test")
	defer db.Close() //关闭数据库
	err := db.Ping() //连接数据库
	if err != nil {
		fmt.Println("数据库连接失败")
		return nil, err
	} else {
		fmt.Println("数据库连接成功")
	}

	var wikiNodeArr []WikiNode2
	//多行查询
	rows, err := db.Query("select * from tbl_hezi_wiki_node") //获取所有数据
	for rows.Next() {                                         //只能读取一次，之后数据rows.Next()数据为空
		var node WikiNode2
		err = rows.Scan(&node.ID, &node.ParentId, &node.Url, &node.Name)
		if err != nil {
			panic(err)
		}
		wikiNodeArr = append(wikiNodeArr, node)
	}
	return wikiNodeArr, nil
}

type WikiNode2 struct {
	ID       int    `db:"id"`
	ParentId int    `db:"parent_id"`
	Url      string `db:"url"`
	Name     string `db:"name"`
}
