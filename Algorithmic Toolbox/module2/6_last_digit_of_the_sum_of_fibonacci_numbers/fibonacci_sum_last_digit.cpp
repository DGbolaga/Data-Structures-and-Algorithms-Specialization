#include <iostream>
#include <random>
using namespace std;

int fibonacci_sum_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 2; i <= n; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current) % 10;
        sum = (sum + current) % 10;
    }

    return sum;
}


int fibonacci_sum_fast(long long n) {
    if (n <= 1)
        return n;
    
    int pisano_period = 60; 
    n = (n + 2) % pisano_period;    

    if (n == 0) return 9;  // special case

    long long previous = 0;
    long long current  = 1;

    for (long long i = 2; i <= n; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current) % 10;
    }

    // (n + 10) % 10 removes negative
    return (current - 1 + 10) % 10; 
}


void stressTest() {
    //random input in sequence
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dist(2, 1000000);
    int n = dist(gen);

    int arr[n];
    for (int i=0; i<n; i++) {
        arr[i] = dist(gen);
    }

    for (int x: arr) {
        int fast = fibonacci_sum_fast(x);
        int naive = fibonacci_sum_naive(x);
    
        if (naive == fast) {
            cout << "OK: " << naive << "Value: " << x << endl;
        } else {
            cout << "Nooo: naive: " << naive << " fast: " << fast << " Value: " << x << endl;
            break;
        }
    }
}



int main() {
    long long n = 0;
    std::cin >> n;
    // std::cout << fibonacci_sum_naive(n) << endl;
    std::cout << fibonacci_sum_fast(n) << endl;
    // stressTest();
}
