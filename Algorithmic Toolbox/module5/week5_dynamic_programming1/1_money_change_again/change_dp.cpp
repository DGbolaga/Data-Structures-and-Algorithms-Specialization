#include <iostream>
#include <climits>
#include <vector>
#include <algorithm>
using namespace std;

int recursion(int n, vector<int>& coins, vector<int>& memo) {
    if (memo[n] != -1) return memo[n];
    if (n == 0) {
        memo[n] = 0;
        return memo[n];
    }
    if (n < 0) {
        memo[n] = INT_MAX;
        return memo[n];
    }

    vector<int> res;
    for (int c: coins) {
        int x = recursion(n-c, coins, memo);
        if (x != INT_MAX) {
            x++;
        }
        res.push_back(x);
    }
    memo[n] = *min_element(res.begin(), res.end());
    return memo[n];
}

int get_change(int m) {
  //write your code here
  vector<int> memo(m+1, -1);
  vector<int> coins = {1, 3, 4};
  return recursion(m, coins, memo);
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
