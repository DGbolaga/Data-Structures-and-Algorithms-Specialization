#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

using std::vector;

int binary_search(const vector<int> &a, int x) {
  int left = 0;
  int right = (int)a.size() - 1; 
  //write your code here
  while (left <= right) {
    int mid = (int) (left + right)/2;
    if (a[mid] == x) return mid;
    else if (a[mid] < x) {
      left = mid + 1;
    } else {
      right = mid - 1;
    } 
  }
  return -1;
}


int linear_search(const vector<int> &a, int x) {
  for (size_t i = 0; i < a.size(); ++i) {
    if (a[i] == x) return i;
  }
  return -1;
}

int main() {
  //stress Testing.
//   while (true) {
//     // generate a random array
//     int n = rand() % 10 + 2;  // array size between 2 and 11
//     vector<int> a(n);
//     for (int i = 0; i < n; i++) {
//       a[i] = rand() % 10;     // numbers between 0 and 9
//     }
//     sort(a.begin(), a.end()); // binary search requires sorted input

//     // generate a random query
//     int x = rand() % 10;

//     // run both searches
//     int res1 = linear_search(a, x);
//     int res2 = binary_search(a, x);

//     // check if results match
//     if ((res1 == -1 && res2 == -1) || (res1 != -1 && a[res1] == x && a[res2] == x)) {
//       cout << "OK\n";
//     } else {
//       cout << "Wrong answer!\n";
//       cout << "Array: ";
//       for (int i = 0; i < n; i++) cout << a[i] << ' ';
//       cout << "\nQuery: " << x << endl;
//       cout << "Linear search returned: " << res1 << endl;
//       cout << "Binary search returned: " << res2 << endl;
//       break; // stop to inspect the bug
//     }
  
// }

  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  int m;
  std::cin >> m;
  vector<int> b(m);
  for (int i = 0; i < m; ++i) {
    std::cin >> b[i];
  }
  for (int i = 0; i < m; ++i) {
    //replace with the call to binary_search when implemented
    // std::cout << linear_search(a, b[i]) << ' ';
    std::cout << binary_search(a, b[i]) << ' ';
  }
  cout << endl;
}
