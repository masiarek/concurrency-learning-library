// Four threads, a million additions each, and a load and a store that are each
// atomic but not atomic together. Prints how many additions were lost.
use std::sync::atomic::{AtomicU64, Ordering};
use std::thread;

const THREADS: u64 = 4;
const EACH: u64 = 1_000_000;

fn main() {
    let total = AtomicU64::new(0);
    thread::scope(|s| {
        for _ in 0..THREADS {
            s.spawn(|| {
                for _ in 0..EACH {
                    let seen = total.load(Ordering::SeqCst);
                    total.store(seen + 1, Ordering::SeqCst);
                }
            });
        }
    });
    println!("{}", THREADS * EACH - total.into_inner());
}
