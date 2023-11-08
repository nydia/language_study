pub use crate::common::http_utils::HttpUtils::post;

#[cfg(test)]
pub mod tests {
    #[test]
    fn test_handle(){
        get();
    }
}