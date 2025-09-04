#include <iostream>
using namespace std;

int fibonacci_sum_squares_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current * current;
    }    
    
    return sum % 10;
}    


int fibonacci_sum_squares_fast(long long val) {
    // sum of sqaures of n number = f(n) * f(n+1)
    val %= 60;
    if (val == 0) return 0;

    int prev = 0;
    int curr = 1;
    for (int i = 2; i <= val; i++) {
        int temp = prev;
        prev = curr;
        curr = (curr + temp) % 10;
    }
    
    return (curr * ((curr+prev)%10)) % 10;
}    


int main() {
    long long n = 0;
    std::cin >> n;
    // std::cout << fibonacci_sum_squares_naive(n) << endl;
    std::cout << fibonacci_sum_squares_fast(n) << endl;
}
