use super::HttpUtilsBase;
use reqwest::header::HeaderMap;
use serde_json::value::Value;
use std::collections::HashMap;
use std::string::String;
type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

pub struct HttpUtils {}

impl HttpUtilsBase for HttpUtils {
    fn get() -> Result<HashMap<String, String>> {
        println!(">>>> enter get http");
        let resp = reqwest::blocking::get("http://127.0.0.1:8081/json")?
            .json::<HashMap<String, String>>()?;
        //println!("{:#?}", resp);
        Ok(resp)
    }
}

pub async fn get_handle() -> Result<HashMap<String, String>> {
    print!("enter get_handle >>>>>>>>");

    Ok(reqwest::get("http://127.0.0.1:8081/json")
        .await?
        .json::<HashMap<String, String>>()
        .await?)
}

pub async fn post_handle() -> Result<HashMap<String, Value>> {
    print!("enter post >>>>>>>>");

    // post 请求要创建client
    let client = reqwest::Client::new();

    // 组装header
    let mut headers = HeaderMap::new();
    headers.insert("Content-Type", "application/json".parse().unwrap());

    // 组装要提交的数据
    let mut data = HashMap::new();
    data.insert("user", "zhangsan");
    data.insert("password", "123");

    // 发起post请求并返回
    Ok(client
        .post("http://127.0.0.1:8081/json")
        .headers(headers)
        .json(&data)
        .send()
        .await?
        .json::<HashMap<String, Value>>()
        .await?)
}
