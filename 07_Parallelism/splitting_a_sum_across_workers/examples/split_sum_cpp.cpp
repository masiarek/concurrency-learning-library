// Splitting a sum across workers. Each thread adds its own run of values into a
// variable no other thread can see, and the partial sums are then combined two
// ways: one after another, and as a tree whose rounds add pairs at the same time.
// Then the same split, with doubles.
//
//   c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -pthread split_sum_cpp.cpp -o split_sum_cpp && ./split_sum_cpp

#include <cstddef>
#include <format>
#include <iostream>
#include <numeric>
#include <string>
#include <thread>
#include <tuple>
#include <utility>
#include <vector>

constexpr std::size_t workers = 8; // a power of two, so every round pairs everyone up
const std::vector<long> values{1, 4, 3, 9, 2, 8, 5, 1, 1, 6, 2, 7, 2, 5, 0, 4, 1, 8, 6, 5, 1, 2, 3, 9};

// Give each worker an equal run of values. Each adds its run, left to right, into
// its own my_sum, and stores the result in its own slot of sums.
template <typename T>
std::vector<T> partial_sums(const std::vector<T>& values, std::size_t workers) {
    std::size_t width = values.size() / workers;
    std::vector<T> sums(workers);
    {
        std::vector<std::jthread> threads;
        for (std::size_t w = 0; w < workers; ++w) {
            threads.emplace_back([&, w] {
                T my_sum = values[w * width];
                for (std::size_t i = w * width + 1; i < (w + 1) * width; ++i) {
                    my_sum += values[i];
                }
                sums[w] = my_sum;
            });
        }
    } // each std::jthread joins as it is destroyed
    return sums;
}

// The master adds every partial sum into its own, one at a time.
template <typename T>
std::pair<T, std::size_t> serial_combine(const std::vector<T>& sums) {
    T total = sums[0];
    for (std::size_t i = 1; i < sums.size(); ++i) {
        total += sums[i];
    }
    return {total, sums.size() - 1};
}

template <typename T>
std::string joined(const std::vector<T>& xs) {
    std::string out;
    for (const T& x : xs) {
        out += std::format("{}{}", out.empty() ? "" : " ", x);
    }
    return out;
}

// Each round adds neighbouring pairs, every pair on its own thread, until one
// value is left. Returns the total, the number of additions and of rounds.
template <typename T>
std::tuple<T, std::size_t, std::size_t> tree_combine(std::vector<T> level, bool show_rounds) {
    std::size_t additions = 0;
    std::size_t rounds = 0;
    while (level.size() > 1) {
        std::vector<T> next(level.size() / 2);
        {
            std::vector<std::jthread> threads;
            for (std::size_t i = 0; i < next.size(); ++i) {
                threads.emplace_back([&, i] { next[i] = level[2 * i] + level[2 * i + 1]; });
            }
        }
        additions += next.size();
        ++rounds;
        level = std::move(next);
        if (show_rounds) {
            std::cout << std::format("tree, round {}: {}\n", rounds, joined(level));
        }
    }
    return {level[0], additions, rounds};
}

int main() {
    std::cout << std::format("{} values, {} to each of {} workers\n", values.size(),
                             values.size() / workers, workers);
    auto partials = partial_sums(values, workers);
    std::cout << "partial sums: " << joined(partials) << "\n";
    auto [serial_total, serial_additions] = serial_combine(partials);
    std::cout << std::format("serial combine: {}, after {} additions in {} rounds\n", serial_total,
                             serial_additions, serial_additions);
    auto [tree_total, additions, rounds] = tree_combine(partials, true);
    std::cout << std::format("tree combine: {}, after {} additions in {} rounds\n", tree_total,
                             additions, rounds);

    std::vector<double> floats;
    for (long v : values) {
        floats.push_back(static_cast<double>(v) + 0.2);
    }
    std::cout << std::format("\nthe same {} values plus 0.2 each, as double (on paper, 99.8)\n",
                             floats.size());
    double loop_total = 0.0;
    for (double x : floats) {
        loop_total += x;
    }
    std::cout << std::format("one loop over all {}: {}\n", floats.size(), loop_total);
    auto float_partials = partial_sums(floats, workers);
    std::cout << std::format("partial sums, then serial: {}\n", serial_combine(float_partials).first);
    std::cout << std::format("partial sums, then tree: {}\n",
                             std::get<0>(tree_combine(float_partials, false)));
    std::cout << std::format("std::accumulate: {}\n",
                             std::accumulate(floats.begin(), floats.end(), 0.0));
}
