// Getting a result back. In C++, std::thread::join() returns void. The value
// comes back through something else: a captured variable, or a std::future.
//
//   c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -pthread result_back_cpp.cpp -o result_back_cpp && ./result_back_cpp

#include <future>
#include <iostream>
#include <stdexcept>
#include <thread>
#include <type_traits>
#include <utility>

static long sum_to_100() {
    long total = 0;
    for (long i = 1; i <= 100; ++i) {
        total += i;
    }
    return total;
}

int main() {
    std::cout << std::boolalpha;
    std::cout << "join() returns void: "
              << std::is_void_v<decltype(std::declval<std::thread&>().join())> << "\n";

    long total = 0;
    std::thread t([&total] { total = sum_to_100(); });
    t.join();
    std::cout << "after join(), the variable the lambda captured holds " << total << "\n";

    std::future<long> future = std::async(std::launch::async, sum_to_100);
    std::cout << "std::async handed back a std::future<long>, and get() returned "
              << future.get() << "\n";

    std::future<long> failing = std::async(std::launch::async, []() -> long {
        throw std::runtime_error("no total today");
    });
    try {
        failing.get();
    } catch (const std::runtime_error& e) {
        std::cout << "get() rethrew the thread's std::runtime_error: " << e.what() << "\n";
    }
}
