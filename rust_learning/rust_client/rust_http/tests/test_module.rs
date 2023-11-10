//extern 导入外部模块
extern crate rust_http;

#[cfg(test)]
pub mod tests {
    use rust_http::common::{http_utils, HttpUtilsBase};

    #[test]
    #[warn(unused_must_use)]
    fn test_get() {
        let resp = http_utils::HttpUtils::get();
        println!("{:#?}", resp.is_ok());
        println!("{:#?}", resp.ok());
    }

    #[test]
    fn test_post() {
        let res = post();
        println!(">>>>>>{:#?}", res);
    }

    #[test]
    #[warn(unused_must_use)]
    fn test_post_handle() {
        request();
    }



    use std::collections::HashMap;
    type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

    async fn request() {
        if let Ok(res) = http_utils::get_handle().await {
            println!("{:#?}", res);
        }
    }

    fn post() -> Result<HashMap<String, String>> {
        let resp = reqwest::blocking::get("http://127.0.0.1:8081/json")?
            .json::<HashMap<String, String>>()?;
        println!("{:#?}", resp);
        Ok(resp)
    }

}
