// std::reduce may group the additions any way it likes; this prints what one
// standard library chose for the lesson's 24 values plus 0.2 each.
#include <format>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    const long values[] = {1, 4, 3, 9, 2, 8, 5, 1, 1, 6, 2, 7, 2, 5, 0, 4, 1, 8, 6, 5, 1, 2, 3, 9};
    std::vector<double> floats;
    for (long v : values) {
        floats.push_back(static_cast<double>(v) + 0.2);
    }
    std::cout << std::format("{}\n", std::reduce(floats.begin(), floats.end(), 0.0));
}
