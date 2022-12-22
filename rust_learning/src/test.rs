
extern "C" fn dummy_bytes<T, R>(_: T, _: R) -> cffi::Bytes { vec![].into() }

extern "C" fn bytes_drop(bytes: cffi::Bytes) { unsafe { bytes.local_drop() }; }

extern "C" fn dummy_drop<T>(_: T) {}

pub fn dummy_data_source() -> *mut cffi::DataSource {
	cffi::build_data_source(
		ptr::null_mut(),
		dummy_bytes,
		dummy_drop,
		ptr::null_mut(),
		dummy_bytes,
		dummy_drop,
		bytes_drop,
	)
}


fn main(){
    println!("hello");

    println!("你好");

}