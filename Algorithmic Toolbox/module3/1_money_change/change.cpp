#include <iostream>

int get_change(int n) {
  //write your code here
  int ans = 0;
  while (n) {
    if (n >= 10) {
      n -= 10;
    } else if (n >= 5) {
      n -= 5;
    } else {
      n -= 1;
    }
    ans++;
  }
  return ans;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
