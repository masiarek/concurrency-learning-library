// Who waits when main returns? In C++ it depends on the class: a std::jthread
// joins in its destructor, and a detached std::thread is ended with the process.
//
//   c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -pthread who_waits_cpp.cpp -o who_waits_cpp && ./who_waits_cpp

#include <chrono>
#include <iostream>
#include <thread>

using namespace std::chrono_literals;

int main() {
    {
        std::jthread waited([] {
            std::this_thread::sleep_for(1s);
            std::cout << "std::jthread:          finished\n";
        });
    }  // ~jthread() asks the thread to stop, then joins it

    std::thread detached([] {
        std::this_thread::sleep_for(3s);
        std::cout << "detached std::thread:  finished\n";
    });
    detached.detach();  // without this, ~thread() would call std::terminate

    std::cout << "main:                  returning\n";
}
