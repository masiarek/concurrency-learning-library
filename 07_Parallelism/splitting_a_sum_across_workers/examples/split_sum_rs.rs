//! Splitting a sum across workers. Each worker adds its own run of values into a
//! variable no other thread can see, and the partial sums are then combined two
//! ways: one after another, and as a tree whose rounds add pairs at the same time.
//! Then the same split, with floats.
//!
//!   rustc --edition 2024 split_sum_rs.rs -o split_sum_rs && ./split_sum_rs

use std::fmt::Display;
use std::ops::Add;
use std::thread;

const WORKERS: usize = 8; // a power of two, so every round of the tree pairs everyone up
const VALUES: [i64; 24] = [1, 4, 3, 9, 2, 8, 5, 1, 1, 6, 2, 7, 2, 5, 0, 4, 1, 8, 6, 5, 1, 2, 3, 9];

/// Give each worker an equal run of `values`. Each worker adds its run, left to
/// right, into its own `my_sum`; the thread hands the result back through `join`.
fn partial_sums<T>(values: &[T], workers: usize) -> Vec<T>
where
    T: Copy + Add<Output = T> + Send + Sync,
{
    thread::scope(|s| {
        let handles: Vec<_> = values
            .chunks(values.len() / workers)
            .map(|run| {
                s.spawn(move || {
                    let mut my_sum = run[0];
                    for &x in &run[1..] {
                        my_sum = my_sum + x;
                    }
                    my_sum
                })
            })
            .collect();
        handles.into_iter().map(|h| h.join().unwrap()).collect()
    })
}

/// The master adds every partial sum into its own, one at a time.
fn serial_combine<T: Copy + Add<Output = T>>(sums: &[T]) -> (T, usize) {
    let mut total = sums[0];
    for &s in &sums[1..] {
        total = total + s;
    }
    (total, sums.len() - 1)
}

/// Each round adds neighbouring pairs, every pair on its own thread, until one
/// value is left. Returns the total, the number of additions and of rounds.
fn tree_combine<T>(sums: &[T], show_rounds: bool) -> (T, usize, usize)
where
    T: Copy + Add<Output = T> + Send + Sync + Display,
{
    let mut level = sums.to_vec();
    let (mut additions, mut rounds) = (0, 0);
    while level.len() > 1 {
        level = thread::scope(|s| {
            let handles: Vec<_> = level
                .chunks(2)
                .map(|pair| s.spawn(move || pair[0] + pair[1]))
                .collect();
            handles.into_iter().map(|h| h.join().unwrap()).collect()
        });
        additions += level.len();
        rounds += 1;
        if show_rounds {
            println!("tree, round {rounds}: {}", joined(&level));
        }
    }
    (level[0], additions, rounds)
}

fn joined<T: Display>(xs: &[T]) -> String {
    xs.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(" ")
}

fn main() {
    println!("{} values, {} to each of {WORKERS} workers", VALUES.len(), VALUES.len() / WORKERS);
    let partials = partial_sums(&VALUES, WORKERS);
    println!("partial sums: {}", joined(&partials));
    let (total, additions) = serial_combine(&partials);
    println!("serial combine: {total}, after {additions} additions in {additions} rounds");
    let (total, additions, rounds) = tree_combine(&partials, true);
    println!("tree combine: {total}, after {additions} additions in {rounds} rounds");

    let floats: Vec<f64> = VALUES.iter().map(|&v| v as f64 + 0.2).collect();
    println!();
    println!("the same {} values plus 0.2 each, as f64 (on paper, 99.8)", floats.len());
    let mut loop_total = 0.0;
    for &x in &floats {
        loop_total += x;
    }
    println!("one loop over all {}: {loop_total}", floats.len());
    let partials = partial_sums(&floats, WORKERS);
    println!("partial sums, then serial: {}", serial_combine(&partials).0);
    println!("partial sums, then tree: {}", tree_combine(&partials, false).0);
    println!("iter().sum(): {}", floats.iter().sum::<f64>());
}
