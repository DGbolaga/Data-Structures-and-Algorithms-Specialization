#include <iostream>
using namespace std;

long long get_fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % m;
}

long long get_fibonacci_huge_fast(long long n, long long m) {
    if (n <= 1)
        return n;
    
    //get period
    int pisano_period = 0;
    int prev = 0; 
    int curr = 1; 
    for (int i = 0; i < 1000; i++) {
        int temp = prev;
        prev = curr;
        curr = (temp + curr) % m;

        pisano_period+=1;
        if (prev == 0 && curr == 1) {
            break;
        }
    }

    int newN = n % pisano_period;

    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < newN - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current) % m;
    }

    return current;
}

int main() {
    long long n, m;
    std::cin >> n >> m;
    std::cout << get_fibonacci_huge_fast(n, m) << '\n';
}
