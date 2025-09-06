#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <iomanip>
using namespace std;

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  double value = 0.0;

  // write your code here
  // step 1: The greedy choice is to select objects based on values/weight.
  // step 2: Proof that it's a safe move: given values = [2, 3, 4, 5] and weights = [10, 33, 10, 5]
  //         a capacity of 40 is given. 
  // the v/w = [0.2, 0.091, 0.4, 1] -> sorted form [1, 0.4, 0.2, 0.091]
  // by selecting the highest v/w and deducting it weight from the capacity, we are guaranteed to pick the highest valued element that is within the capacity limit.
  // on selecting fraction_of_v/w_selected = [ 1, 1, 25/33, 0] 
  // 40 - 5 = 35 - 10 = 25 - 33(25/33) = 0;
  // thus the max value of fraction_of_v/w selected = (2*0) + (3*25/33) + (4*1) + (5*1) = 2.273 + 4 + 5
  // max weight = (10 * 0) + (33 * 25/33) + (10 * 1) + (5 * 1) = 25 + 10 + 5= 40.

  vector<pair<int, double>> value_per_weight;
  for (int i = 0; i < values.size(); i++) {
    value_per_weight.push_back({i, (double) values[i]/weights[i]});
  }
  //sort by value_per_weight
  sort(value_per_weight.begin(), value_per_weight.end(), [](auto &a, auto &b){return a.second > b.second; });

  int x = values.size();
  vector<float> fraction_of_v_per_w(x, 0.0f);
  int temp = capacity;
  for (int i = 0; i < x; i++) {
    int idx = value_per_weight[i].first;
    int item_weight = weights[idx];

    if (item_weight <= temp) {
      temp -= item_weight;
      fraction_of_v_per_w[idx] = 1.0f;
    } else if (temp > 0) {
      fraction_of_v_per_w[idx] = (double) temp / item_weight;
      temp = 0;
      break;
    }
  }

  double maxWeight = 0.0;
  for (int i = 0; i < x; i++) {
    value += (fraction_of_v_per_w[i] * values[i]);
    maxWeight += (fraction_of_v_per_w[i] * weights[i]);
  }

  // cout << "MaxWeight: " << maxWeight << endl;
  return value;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout << fixed << setprecision(3) << optimal_value << std::endl;
  return 0;
}
