#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    // write your code here
    stops.push_back(dist);
    int i =0;
    int c =0;
    int start = 0;
    while (true) {
      int temp = 0;
      while (i < stops.size() && stops[i]-start <= tank) {
        temp = stops[i++];
      }
      
      if (i < stops.size() && stops[i] - temp > tank) {
        return -1;
      } else if (start == dist) {
        return c - 1;
      }
      
      start = temp;
      c++;
    }
    

    return -1;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}
