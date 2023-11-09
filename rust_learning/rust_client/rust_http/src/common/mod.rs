pub mod http_utils;
use std::collections::HashMap;
type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

pub trait HttpUtilsBase {

    fn get() -> Result<HashMap<String, String>>;

}