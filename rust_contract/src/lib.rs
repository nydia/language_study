use ink_lang as ink;

#[ink::contract]
mod my_smart_contract {
    #[ink(storage)]
    pub struct MySmartContract {
        value: i32,
    }

    impl MySmartContract {
        #[ink(constructor)]
        pub fn new(initial_value: i32) -> Self {
            Self { value: initial_value }
        }

        #[ink(message)]
        pub fn get(&self) -> i32 {
            self.value
        }

        #[ink(message)]
        pub fn set(&mut self, new_value: i32) {
            self.value = new_value;
        }
    }
}
