//! The lost update, forced. `total += 1` is three steps -- load, add, store --
//! and nothing stops ten threads from all loading the same old total. A Barrier
//! holds every thread between its load and its store, so the interleaving that
//! loses updates happens on every run instead of one run in a thousand.
//!
//! Each load and each store is atomic, and this is safe Rust. The pair is not.
//!
//!   rustc --edition 2024 lost_update_rs.rs -o lost_update_rs && ./lost_update_rs

use std::sync::Barrier;
use std::sync::atomic::{AtomicU64, Ordering};
use std::thread;

const HANDLERS: usize = 10;

fn main() {
    let total = AtomicU64::new(0);
    let all_loaded = Barrier::new(HANDLERS);

    let loaded: Vec<u64> = thread::scope(|s| {
        let handlers: Vec<_> = (0..HANDLERS)
            .map(|_| {
                s.spawn(|| {
                    let seen = total.load(Ordering::SeqCst); // 1. load
                    all_loaded.wait(); // every handler has loaded
                    total.store(seen + 1, Ordering::SeqCst); // 2. add, 3. store
                    seen
                })
            })
            .collect();
        handlers.into_iter().map(|h| h.join().unwrap()).collect()
    });

    println!("{HANDLERS} handlers each added 1 to a total that started at 0");
    println!("the totals they loaded: {loaded:?}");
    println!("the total is {}, not {HANDLERS}", total.load(Ordering::SeqCst));
}
