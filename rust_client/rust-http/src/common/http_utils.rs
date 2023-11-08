
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
}


