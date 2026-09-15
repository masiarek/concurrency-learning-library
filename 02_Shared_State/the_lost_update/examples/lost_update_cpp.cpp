// The lost update, forced. `total += 1` is three steps -- load, add, store --
// and nothing stops ten threads from all loading the same old total. A
// std::latch holds every thread between its load and its store, so every load
// happens before any store, on every run.
//
// `total` is a std::atomic<long>, so each load and each store is indivisible
// and the program has no data race. The pair of operations is not atomic.
//
//   c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -pthread lost_update_cpp.cpp -o lost_update_cpp && ./lost_update_cpp

#include <array>
#include <atomic>
#include <cstddef>
#include <iostream>
#include <latch>
#include <thread>
#include <vector>

constexpr std::size_t handlers = 10;

int main() {
    std::atomic<long> total{0};
    std::latch all_loaded{handlers};
    std::array<long, handlers> loaded{};

    {
        std::vector<std::jthread> threads;
        for (std::size_t i = 0; i < handlers; ++i) {
            threads.emplace_back([&, i] {
                long seen = total.load();  // 1. load
                loaded[i] = seen;
                all_loaded.count_down();
                all_loaded.wait();         // every handler has loaded
                total.store(seen + 1);     // 2. add, 3. store
            });
        }
    } // each std::jthread joins as it is destroyed

    std::cout << handlers << " handlers each added 1 to a total that started at 0\n";
    std::cout << "the totals they loaded:";
    for (long seen : loaded) {
        std::cout << ' ' << seen;
    }
    std::cout << "\nthe total is " << total.load() << ", not " << handlers << "\n";
}
