#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

// using std::vector;
// using std::swap;

int partition2(vector<int> &a, int l, int r) {
  int x = a[l];
  int j = l;
  for (int i = l + 1; i <= r; i++) {
    if (a[i] <= x) {
      j++;
      swap(a[i], a[j]);
    }
  }
  swap(a[l], a[j]);
  return j;
}

void randomized_quick_sort(vector<int> &a, int l, int r) {
  if (l >= r) {
    return;
  }

  int k = l + rand() % (r - l + 1);
  swap(a[l], a[k]);
  int m = partition2(a, l, r);

  randomized_quick_sort(a, l, m - 1);
  randomized_quick_sort(a, m + 1, r);
}

void randomized_3way_quick_sort(vector<int> &a, int l, int r) {
  if (l >= r) return;
  //choose randome value between l and r, and swap with a[l]
  int k = l + rand() % (r - l + 1);
  swap(a[l], a[k]);

  int lt = l;
  int gt = r;
  int i = l + 1;
  int pivot = a[l];

  while (i <= gt) {
    if (a[i] < pivot) {
      //swap with lt
      swap(a[lt], a[i]);
      lt++;
      i++;
    } else if (a[i] > pivot) {
      //swap with gt
      swap(a[gt], a[i]);
      gt--;
    } else {
      i++;
    }
  }

  randomized_3way_quick_sort(a, l, lt-1);
  randomized_3way_quick_sort(a, gt+1, r);
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }

  randomized_3way_quick_sort(a, 0, a.size() - 1);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cout << a[i] << ' ';
  }
  cout << endl;
}
