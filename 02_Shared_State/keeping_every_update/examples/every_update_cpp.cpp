// Keeping every update, two ways. Eight handlers each add the numbers 1 to
// 10,000 to one total: under a std::mutex, and with an atomic add.
//
//   c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -pthread every_update_cpp.cpp -o every_update_cpp && ./every_update_cpp

#include <atomic>
#include <functional>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

constexpr int handlers = 8;
constexpr long last = 10'000;

static void run_handlers(const std::function<void()>& handler) {
    std::vector<std::jthread> threads;
    for (int i = 0; i < handlers; ++i) {
        threads.emplace_back(handler);
    }
} // each std::jthread joins as it is destroyed

static long with_a_mutex() {
    std::mutex lock;
    long total = 0;
    run_handlers([&] {
        for (long n = 1; n <= last; ++n) {
            std::scoped_lock held{lock};
            total += n; // load, add and store, all while holding the lock
        }
    });
    return total;
}

static long with_an_atomic_add() {
    std::atomic<long> total{0};
    run_handlers([&] {
        for (long n = 1; n <= last; ++n) {
            total.fetch_add(n); // one indivisible operation
        }
    });
    return total.load();
}

int main() {
    std::cout << handlers << " handlers each add 1 to " << last << "; the total should be "
              << handlers * last * (last + 1) / 2 << "\n";
    std::cout << "with a std::mutex:    " << with_a_mutex() << "\n";
    std::cout << "with fetch_add:       " << with_an_atomic_add() << "\n";
}
