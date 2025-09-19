#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

using std::vector;

int binary_search(const vector<int> &a, int x) {
  int left = 0, right = (int)a.size()-1; 
  //write your code here

  while (left <= right) {
    int m = (int) (left + right) /2;
    if (x == a[m]) {
      if (m - 1 >= 0 && a[m-1]==x) {
        right = m - 1;
      } else {
        return m;
      }
    }
    else if (a[m] > x) right = m - 1;
    else left = m + 1;
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




// Stress Test
// int main() {
//   while (true) {
//     // Generate random array size
//     int n = rand() % 15 + 2; // between 2 and 16
//     vector<int> a(n);
//     for (int i = 0; i < n; i++) {
//       a[i] = rand() % 5; // small range to force duplicates (0–4)
//     }
//     sort(a.begin(), a.end()); // binary search assumes sorted input

//     // Generate a random query
//     int x = rand() % 5;

//     // Run both searches
//     int res1 = linear_search(a, x);
//     int res2 = binary_search(a, x);

//     // Check consistency
//     if ((res1 == -1 && res2 == -1) || (res1 != -1 && a[res1] == x && a[res2] == x && res1 == res2)) {
//       cout << "OK\n";
//     } else {
//       cout << "Wrong answer!\n";
//       cout << "Array: ";
//       for (int i = 0; i < n; i++) cout << a[i] << ' ';
//       cout << "\nQuery: " << x << endl;
//       cout << "Linear search returned: " << res1 << endl;
//       cout << "Binary search returned: " << res2 << endl;
//       break; // stop when a mismatch is found
//     }
//   }
// }
