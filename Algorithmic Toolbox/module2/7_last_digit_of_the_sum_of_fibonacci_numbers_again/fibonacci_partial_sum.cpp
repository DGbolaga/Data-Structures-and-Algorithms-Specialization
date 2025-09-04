#include <iostream>
#include <vector>
using namespace std;


long long get_fibonacci_partial_sum_naive(long long from, long long to) {
    long long sum = 0;

    long long current = 0;
    long long next  = 1;

    for (long long i = 0; i <= to; ++i) {
        if (i >= from) {
            sum += current;
        }

        long long new_current = next;
        next = next + current;
        current = new_current;
    }

    return sum % 10;
}

int last_digit_fib(long long val) {
    val %= 60;
    if (val == 0) return 0;
    if (val == 1) return 1;
    int prev = 0;
    int curr = 1;
    for (int i = 2; i <= val; i++) {
        int temp = prev;
        prev = curr;
        curr = (curr + temp) % 10;
    }

    return curr;
}

long long get_fibonacci_partial_sum_fast(long long m, long long n) {
    // sum of fib numbers from "from" to "to" is f(n+2) - f(m+1)
    // x = f(n+2)mod 60 will give the last digit at f(n+2) (from)
    // y = f(m+1)mod 60 will give the last digit at f(m+1) (to)
    int x = last_digit_fib(n + 2);
    int y = last_digit_fib(m + 1);
    
    return (x - y + 10) % 10;
}


int main() {
    long long from, to;
    std::cin >> from >> to;
    // std::cout << get_fibonacci_partial_sum_naive(from, to) << '\n';
    std::cout << get_fibonacci_partial_sum_fast(from, to) << '\n';
}
