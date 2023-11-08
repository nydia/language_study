
fn get(){
    let body = reqwest::get("http://127.0.0.1:8081/demo")
    .await?
    .text()
    .await?;

    println!("body = {:?}", body);
}

#[cfg(test)]
pub mod tests {
    #[test]
    fn test_handle(){
        get();
    }
}