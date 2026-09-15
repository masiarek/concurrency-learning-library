//! Not an example: CI does not run this, because it prints something different
//! from one run to the next. `tally.sh` beside it runs it many times and counts
//! the transcripts.
//!
//! The shape of the first program in chapter 1 of Mara Bos's "Rust Atomics and
//! Locks", with the messages changed.

use std::thread;

fn main() {
    thread::spawn(worker);
    thread::spawn(worker);
    println!("main: hello");
}

fn worker() {
    println!("worker: hello");
    let id = thread::current().id();
    println!("worker: my id is {id:?}");
}
