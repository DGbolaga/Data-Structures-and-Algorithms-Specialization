#include <iostream>
#include <climits>
#include <random>
using namespace std;

int64_t maxPairwiseProductNaive(int arr[], int m);
int64_t maxPairwiseProductFast(int arr[], int m);
void stressTest(int arr_size, int num_max);

int main() {
    int m;
    cin >> m;
    int arr[m];

    int x = 0;
    while (x < m) {
        int n;
        cin >> n;
        
        arr[x++] = n;
        
    }
    cout << maxPairwiseProductFast(arr, m) << endl;
    // stressTest(100, 10);
    
    return 0;
}

int64_t maxPairwiseProductNaive(int arr[], int n) {
    int64_t ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j=i+1; j < n; j++) {
            if (arr[i] * arr[j] > ans && j != i) {
                ans = arr[i] * arr[j];
            }
        }
    }
    return ans;
}

int64_t maxPairwiseProductFast(int arr[], int n) {
    int64_t largest = LLONG_MIN;
    int64_t secondLargest = LLONG_MIN;

    int largest_idx = 0;
    int secondLargest_idx = 0;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] > largest) {
                secondLargest = largest;
                secondLargest_idx = largest_idx;

                largest = arr[i];
                largest_idx = i;
            }
        else if (arr[i] > secondLargest && i != largest_idx) {
            secondLargest = arr[i];
            secondLargest_idx = i;
        }
    }

    int64_t ans = largest * secondLargest;

    return ans;
}

void stressTest(int N, int M) {
    //random input in sequence
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dist(2, N);
    int n = dist(gen);
    int arr[n];

    //random value for array
    mt19937 gen1(rd());
    uniform_int_distribution<int> dist1(0, M);

    cout << "Array: ";
    for (int i=0; i<n; i++) {
        arr[i] = dist1(gen1);

        cout << arr[i] << " ";
    }
    cout << endl;
    

    int64_t ansN = maxPairwiseProductNaive(arr, n);
    int64_t ansF = maxPairwiseProductFast(arr, n);

    if (ansN == ansF) {
        cout << "OK: " << ansN << endl;
    }
    else {
        cout << "Wrong answer: ansN: " << ansN << " ansF: " << ansF << endl;
    }
}