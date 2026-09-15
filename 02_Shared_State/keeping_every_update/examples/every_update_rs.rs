//! Keeping every update, three ways. Eight handlers each add the numbers 1 to
//! 10,000 to one total: under a Mutex, with an atomic add, and by sending every
//! number to the one thread that owns the total.
//!
//!   rustc --edition 2024 every_update_rs.rs -o every_update_rs && ./every_update_rs

use std::sync::atomic::{AtomicU64, Ordering};
use std::sync::{Mutex, mpsc};
use std::thread;

const HANDLERS: u64 = 8;
const LAST: u64 = 10_000;

fn with_a_mutex() -> u64 {
    let total = Mutex::new(0);
    thread::scope(|s| {
        for _ in 0..HANDLERS {
            s.spawn(|| {
                for n in 1..=LAST {
                    // load, add and store, all while this thread holds the lock
                    *total.lock().unwrap() += n;
                }
            });
        }
    });
    total.into_inner().unwrap()
}

fn with_an_atomic_add() -> u64 {
    let total = AtomicU64::new(0);
    thread::scope(|s| {
        for _ in 0..HANDLERS {
            s.spawn(|| {
                for n in 1..=LAST {
                    total.fetch_add(n, Ordering::SeqCst); // one indivisible operation
                }
            });
        }
    });
    total.into_inner()
}

fn with_one_owner() -> u64 {
    let (numbers, received) = mpsc::channel();
    let owner = thread::spawn(move || {
        let mut total = 0; // no other thread can reach this variable
        for n in received {
            total += n;
        }
        total
    });
    thread::scope(|s| {
        for _ in 0..HANDLERS {
            let numbers = numbers.clone();
            s.spawn(move || {
                for n in 1..=LAST {
                    numbers.send(n).unwrap();
                }
            });
        }
    });
    drop(numbers); // the last sender is gone, so the owner's loop ends
    owner.join().unwrap()
}

fn main() {
    println!(
        "{HANDLERS} handlers each add 1 to {LAST}; the total should be {}",
        HANDLERS * LAST * (LAST + 1) / 2
    );
    println!("with a Mutex:         {}", with_a_mutex());
    println!("with fetch_add:       {}", with_an_atomic_add());
    println!("with one owner:       {}", with_one_owner());
}
