use core::num;
extern crate restaurant;//自己的库

fn main() {
    println!("Hello, world!");

    //基础语法
    basicSyntax_test();

    //数学运算
    math_test();

    //数据类型
    dataTypes_test();

    //Rust函数
    //fn <函数名> ( <参数> ) <函数体>
    function_test();

    //条件语句
    conditions_test();

    //for循环
    for_test();

    //所有权
    ownership_move_test();//所有权的移动
    ownership_copy_teset();//所有权的复制
    ownership_other_test(); 
    ownership_return_val_test(); //返回值
    ownership_ref_test();//引用
    ownership_slices_test();//slices
    
    //结构体
    struct_test();

    //枚举
    enum_test();
    enum_match_test();////枚举 match
    enum_match_option_test();////枚举 option 填补 Rust 不支持 null 引用的空白
    enum_match_other_test();//枚举 match 通配符
    enum_match_if_test();//枚举 match if

    //组织管理
    package_test();
    //组织管理 - 电商实训
    package_trai_test();

    //常见集合
    common_collections_test();

}

//基础语法
fn basicSyntax_test(){
    let mut a = 1; // rust可以不加;结&尾
    //let a: i32 = 1;
    a = 2;
    print!("你好， {}",a);
}

//数据类型
fn dataTypes_test(){
    //元组
    let tup = (10,23.22,true);
    let (x,y,z) = tup;
    println!("x:{},y:{},z:{}",x,y,z);
    //数组
    let a = [1,2,3,4,5,6];
    println!("a[1]: {}",a[1]);
}

//数学运算
fn math_test(){
    let sum = 5 + 10; // 加
    let difference = 95.5 - 4.3; // 减
    let product = 4 * 30; // 乘
    let quotient = 56.7 / 32.2; // 除
    let remainder = 43 % 5; // 求余
    println!("add is {}, diff is {}, product is {}, quo is {}, rem is {}", sum, difference, product, quotient, remainder);
}

//函数
fn function_test() {
    //内部函数
    fn math_1() {
        println!("Hello, china!");
    }
    math_1();

    //函数返回值
    fn fn_return(a: i32, b: i32) -> i32{
        let c = a + b;
        return c;
    }
    println!("return vale : {}", fn_return(100,200));
}

//条件语句
fn  conditions_test() {
    let number = 3;
    if number < 5{
        println!("条件为true")
    } else {
        println!("条件为false")
    }

    let a = 12;
    let b;
    if a > 0{
        b =1 ;
    }else if a < 0{
        b = -1;
    } else {
        b = 0;
    }
    println!("b is {}", b);
    
}

//for循环
fn for_test(){
    let mut number = 1;
    while number !=4 {
        print!("number is {},", number);
        number += 1;
    }
    println!("for Exit");
}

//所有权
//变量与数据交互的方式（一）：移动
/**
 * 1. 当变量离开作用域后，Rust 自动调用 drop 函数并清理变量的堆内存
 */
fn ownership_move_test(){
    let s1 = 1;
    let s2 = s1;
    println!("si: {}, s2:{}",s1,s2);

    let a1 = String::from("hello");
    println!("a1: {}",a1);

    //let a2 = a1;
    //println!("a1:{},a2:{}",a1,a2);//错误，s1已经被移动走了

}
//变量与数据交互的方式（二）：克隆
fn ownership_copy_teset(){
    let s1 = String::from("hello");
    let s2 = s1.clone();
    println!("s1 = {}, s2 = {}", s1, s2);
}
//涉及函数的所有权机制
//copy类型数据可以在赋值后继续时候，飞copy类型数据不可以
fn ownership_other_test(){
    let s = String::from("hello");  // s 进入作用域
    takes_ownership(s); // s 的值移动到函数里 ... 所以到这里不再有效
    let x = 5;                 // x 进入作用域
    makes_copy(x);     // x 应该移动函数里，但 i32 是 Copy 的，所以在后面可继续使用 x
    fn takes_ownership(some_string: String) { // some_string 进入作用域
        println!("{}", some_string);
    } // 这里，some_string 移出作用域并调用 `drop` 方法。占用的内存被释放
    
    fn makes_copy(some_integer: i32) { // some_integer 进入作用域
        println!("{}", some_integer);
    } // 这里，some_integer 移出作用域。没有特殊之处
    //println!("s:{},x:{}",s,x);
    println!("s:失效了,x:{}",x);
}

//函数返回值
fn ownership_return_val_test(){

    let s1 = gives_ownership();//gives_ownership()将返回值转移给s1
    let s2 = String::from("hello");//s2进入作用域
    let s3 = takes_and_gives_back(s2);//s2 被转移到方法里面，它也将返回值转移给s3
    
    //println!("s1: {}, s2: {}, s3: {}", s1, s2, s3);
    println!("s1:{}",s1);

    fn gives_ownership() -> String {//gives_ownership会将返回值移动给调用给他的函数
        let some_string = String::from("yours");//some_string 进入作用域
        some_string                                //返回some_string 并移出调用的函数
    } 
    //将传入字符串作为返回值
    fn takes_and_gives_back(a_string: String) -> String {//a_string 进入作用域
        a_string //返回 a_string 并移出调用的函数
    }

}
//所有权 -- 引用
//我们将创建一个引用的行为称为 借用（borrowing）
fn ownership_ref_test(){
    let s1 = String::from("helllo");
    let s2 = &s1;
    println!("s1:{},s2:{}",s1,s2);

    //引用计算长度
    fn calculate_lenth(s: &String) -> usize {
        s.len()
    }
    let len  = calculate_lenth(s2);
    println!("The length of '{}' is {}.", s2,len);
}
//所有权 -- slices
fn ownership_slices_test(){
    fn first_word(s: &str) -> &str {
        let bytes = s.as_bytes();
    
        for (i, &item) in bytes.iter().enumerate() {
            if item == b' ' {
                return &s[0..i];
            }
        }
    
        &s[..]
    }

    let my_string = String::from("hello world");

    // `first_word` 适用于 `String`（的 slice），整体或全部
    let word = first_word(&my_string[0..6]);
    println!("word : {}", word);
    let word = first_word(&my_string[..]);
    // `first_word` 也适用于 `String` 的引用，
    // 这等价于整个 `String` 的 slice
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // `first_word` 适用于字符串字面值，整体或全部
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // 因为字符串字面值已经 **是** 字符串 slice 了，
    // 这也是适用的，无需 slice 语法！
    let word = first_word(my_string_literal);
}

//结构体
fn struct_test(){
    struct User{
        id: i8,
        active: bool,
        username: String,
        email: String,
        sign_in_count: u64
    }

    let mut user1 = User {
        id: 1,
        active: true,
        username: String::from("nydia"),
        email: String::from("111@qq.com"),
        sign_in_count: 1,
    };
    user1.email = String::from("tt@qq.com");

    println!("user1's username : {}", user1.username);

    // ==========================

    struct_debug_test();

}
//struct debug
fn struct_debug_test(){
    #[derive(Debug)]
    struct Rectangle {
        width: u32,
        height: u32,
    }
    let scala = 2;
    let rect1 = Rectangle{
        width: dbg!(30 * scala),
        height: 50
    };
    dbg!(&rect1);

    //结构体关联函数

    impl Rectangle {
        fn are(&self) -> u32 {
            self.width * self.height
        }
    }
    impl Rectangle {
        fn can_hold(&self, other: &Rectangle) -> bool {
            self.width > other.width && self.height > other.height
        }
    }

}


//枚举
fn enum_test(){
    // =============================
    #[derive(Debug)]
    enum  IpAddrKind {
        V4,
        V6,
    }   
    struct IpAddr{
        kind: IpAddrKind,
        addres: String,
    }
    let home = IpAddr{
        kind: IpAddrKind::V4,
        addres: String::from("127.0.0.1"),
    };
    let loopback = IpAddr {
        kind: IpAddrKind::V6,
        addres: String::from("::1"),
    };
    println!("v4's kind: {:#?}, v6's kind: {:#?}", home.kind, loopback.kind);
    // =============================

    //可以存储多个类型
    enum Message {
        Quit,
        Move { x: i32, y: i32 },
        Write(String),
        ChangeColor(i32, i32, i32),
    }



}
//枚举 match
fn enum_match_test(){
    enum Coin{
        Penny,
        Nickel,
        Dime,
        Quarter(UsState),
    }
    #[derive(Debug)] // 这样可以立刻看到州的名称
    enum UsState {
        Alabama(u16),
        Alaska,
        // --snip--
    }
    fn value_in_cents(coin: Coin) -> u8 {
        match coin {
            Coin::Penny => 1,
            Coin::Nickel => 5,
            Coin::Dime => 10,
            Coin::Quarter(state) => {
                println!("State quarter from {:?}!", state);
                25
            },
        }
    }
    let usState = UsState::Alabama(100);
    let coin = Coin::Quarter(usState);
    println!("enum math : {}", value_in_cents(coin));

}
//枚举 option 填补 Rust 不支持 null 引用的空白
fn enum_match_option_test(){
    enum Option<T>{
        Some(T),
        None,
    }
    let opt = Option::Some("Hello");
    match opt {
        Option::Some(something) => {
            println!("enum option： {}", something);
        },
        Option::None => {
            println!("opt is nothing");
        }
    }

    // ============  
    let opt2:Option<&str> = Option::None;
    match opt2 {
        Option::Some(something) => {
            println!("{}", something);
        },
        Option::None => {
            println!("opt is nothing");
        }
    }
}
//枚举 match 通配符
fn enum_match_other_test(){
    let dice_roll = 9;
    match dice_roll {
        3 => add_fancy_hat(),
        7 => remove_fancy_hat(),
        other => move_player(other),
    }

    fn add_fancy_hat() {}
    fn remove_fancy_hat() {}
    fn move_player(num_spaces: u8) {
        println!("match 通配符号， 大于 9");
    }
}
//match if
fn enum_match_if_test(){
    enum Book{
        Papery(u32),
        Electronic(String),
    }
    let book = Book::Electronic(String::from("url"));
    if let Book::Papery(index) = book{
        println!("Papery {}", index);
    } else {
        println!("Not papery book");
    }
}

//组织管理
fn package_test(){
    //引入自己创建的lib
    restaurant::front_of_house::hosting::add_to_waitlist();
}

//组织管理 - 电商实训
fn package_trai_test(){
    //产生order_id
    let order_id = restaurant::front_of_house::serving::take_order();
    println!("order_id : {}", order_id);

    let trade_id = restaurant::front_of_house::serving::take_payment();
    println!("trade id : {}", trade_id);
}

//常见集合
fn common_collections_test(){
    //vector
    common_collections_vector_test();;
    //string
    common_collections_string_test();
    //hashmap
    common_collections_hashmap_test();


    //vector
    fn common_collections_vector_test(){
        //v的作用域仅限于这个方法
        let mut v:Vec<u32>  = Vec::new();
        v.push(1);
        v.push(2);
        v.push(3);
        v.push(4);
        print!("vector ");
        for i in v {
            print!("{}, ", i);
        }
        println!("");

        //使用宏创建集合
        let v2 = vec![1, 2, 3];
        print!("vector ");
        //我们可以遍历其所有的元素而无需通过索引一次一个的访问。
        for i in &v2 {
            print!("{}, ", i);
        }
        println!("");
        for i in v2 {
            print!("{}, ", i);
        }
        println!("");
    }

    //string
    fn common_collections_string_test(){
        let str = String::new();
        let str2 = String::from("it is str");

        let data = "initial contents";
        let s1 = data.to_string();

        let s2 = String::from("initial contents");

        let mut s3 = String::from("foo");
        let s4 = "bar";
        s3.push_str(s4);
        println!("s3 is {}", s3);

        let s4 = String::from("Hello, ");
        let s5 = String::from("world!");
        let s6 = s1 + &s2; // 注意 s1 被移动了，不能继续使用

        // 该方法也可直接用于字符串字面值：
        let s6 = "initial contents".to_string();
        }
    //hashmap
    use std::collections::HashMap;
    fn common_collections_hashmap_test(){
        let mut scores = HashMap::new();

        scores.insert(String::from("Blue"), 10);
        scores.insert(String::from("Yellow"), 50);
        
    }
   
}
