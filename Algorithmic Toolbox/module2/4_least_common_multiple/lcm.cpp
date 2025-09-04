#include <iostream>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

long long lcm_fast(long long a, long long b, long long a1, long long b1) {
  if (b == 0) {
    return (a * (a1/a) * (b1/a));
  }
  return lcm_fast(b, a % b, a1, b1);
}

int main() {
  long long a, b;
  std::cin >> a >> b;
  // std::cout << lcm_naive(a, b) << std::endl;
  std::cout << lcm_fast(a, b, a, b) << std::endl;
  return 0;
}
