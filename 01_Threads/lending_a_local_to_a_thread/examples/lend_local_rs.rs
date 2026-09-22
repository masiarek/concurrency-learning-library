//! Eight numbers on one function's stack, summed by two threads that borrow
//! halves of them. Nothing is cloned, nothing is reference-counted, and no
//! lifetime is written down: `thread::scope` cannot return until both threads
//! have finished, which is what makes borrowing a local sound.
//!
//!   rustc --edition 2024 lend_local_rs.rs -o lend_local_rs && ./lend_local_rs

use std::thread;

fn sum_on_two_threads() -> i64 {
    let samples: [i64; 8] = [3, 1, 4, 1, 5, 9, 2, 6]; // on this function's stack
    let (left, right) = samples.split_at(4);

    let (a, b) = thread::scope(|s| {
        let a = s.spawn(|| left.iter().sum::<i64>()); // borrows `samples`
        let b = s.spawn(|| right.iter().sum::<i64>());
        (a.join().unwrap(), b.join().unwrap())
    }); // `scope` has joined both threads; only now may this frame go away

    println!("left half {a} + right half {b}");
    a + b
}

fn main() {
    println!("the total is {}", sum_on_two_threads());
}
