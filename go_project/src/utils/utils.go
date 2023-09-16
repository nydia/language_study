package utils

import (
	"encoding/json"
	"log"
)

func LogInfo(obj interface{}) {
	reqMsg, _ := json.Marshal(obj)
	log.Println("文件：" + string(reqMsg))
}
