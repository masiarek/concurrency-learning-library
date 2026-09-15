// Four threads, a million additions each, to a plain long with nothing guarding
// it. Prints how many additions were lost. This is a data race, which makes the
// program's behaviour undefined: the count is what one build happened to do.
#include <iostream>
#include <thread>
#include <vector>

constexpr int threads = 4;
constexpr int each = 1'000'000;

long total = 0;

int main() {
    {
        std::vector<std::jthread> pool;
        for (int i = 0; i < threads; ++i) {
            pool.emplace_back([] {
                for (int j = 0; j < each; ++j) {
                    total += 1;
                }
            });
        }
    }
    std::cout << long{threads} * each - total << "\n";
}
