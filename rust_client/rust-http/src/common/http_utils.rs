
use std::collections::HashMap;
use reqwest::header::HeaderMap;
use serde_json::value::Value;

pub struct HttpUtils {}

impl HttpUtils {
    
    pub fn get() -> String{
        let body = reqwest::get("http://127.0.0.1:8081/demo")
        .await?
        .text()
        .await?;
        
        //println!("body = {:?}", body);
        return body;
        
    }

    async fn post() -> Result<HashMap<String, Value>, reqwest::Error>{
        // post 请求要创建client
        let client = reqwest::Client::new();
    
        // 组装header
        let mut headers = HeaderMap::new();
        headers.insert("Content-Type", "application/json".parse().unwrap());
    
        // 组装要提交的数据
        let mut data = HashMap::new();
        data.insert("user", "tangjz");
        data.insert("password", "dev-tang.com");
    
        // 发起post请求并返回
        Ok(client.post("http://127.0.0.1:8081/demo").headers(headers).json(&data).send().await?.json::<HashMap<String, Value>>().await?)
    }
}


