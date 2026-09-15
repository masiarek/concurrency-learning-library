//! Who waits when main returns? In Rust, nothing waits for a spawned thread:
//! returning from main ends the process. `thread::scope` is the construct that waits.
//!
//!   rustc --edition 2024 who_waits_rs.rs -o who_waits_rs && ./who_waits_rs

use std::thread;
use std::time::Duration;

fn main() {
    // `scope` does not return until every thread started inside it has finished.
    thread::scope(|s| {
        s.spawn(|| {
            thread::sleep(Duration::from_secs(1));
            println!("thread in a scope:  finished");
        });
    });

    // `spawn` hands back a JoinHandle. Dropping it detaches the thread; nothing waits.
    thread::spawn(|| {
        thread::sleep(Duration::from_secs(3));
        println!("spawned thread:     finished");
    });

    println!("main:               returning");
}
