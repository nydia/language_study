/**
 crate
 └── front_of_house
     ├── hosting
     │   ├── add_to_waitlist
     │   └── seat_at_table
     └── serving
         ├── take_order
         ├── serve_order
         └── take_payment
  
 */

mod gateway;
pub use crate::gateway::order;

pub mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {
            println!("add_to_waitlist................");
        }

        pub fn seat_at_table() {}
    }

    pub mod serving {
        pub fn take_order() -> String{
            let order_id = order::create_order();
            order_id
        }

        pub fn serve_order() {}

        pub fn take_payment() {}
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}