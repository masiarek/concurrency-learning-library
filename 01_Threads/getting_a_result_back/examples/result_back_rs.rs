//! Getting a result back. In Rust, `join` returns what the thread returned --
//! or, if it panicked, the panic payload -- as a Result.
//!
//!   rustc --edition 2024 result_back_rs.rs -o result_back_rs && ./result_back_rs

use std::thread;

fn main() {
    let handle = thread::spawn(|| (1..=100u64).sum::<u64>());
    let joined = handle.join(); // Result<u64, Box<dyn Any + Send>>
    println!("join() returned {joined:?}");

    // A panicking thread prints its message to stderr through the panic hook.
    // This silences the hook so the transcript holds only what join() hands back.
    std::panic::set_hook(Box::new(|_| {}));

    let failing = thread::spawn(|| -> u64 { panic!("no total today") });
    match failing.join() {
        Ok(total) => println!("join() returned Ok({total})"),
        Err(payload) => {
            let message = payload.downcast_ref::<&str>().copied().unwrap_or("?");
            println!("join() returned Err, and the payload is the panic message: {message:?}");
        }
    }
}
