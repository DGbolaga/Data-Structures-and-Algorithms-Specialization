#include <iostream>
#include <vector>
#include <string>

int fib(int num);
int main(int argc, char* argv[]) {
    
    std::cout << fib(std::stoi(argv[1])) << std::endl;
    return 0;
}

int fib(int num) {
    if (num == 0) {
        return 0;    
    } 
    if (num == 1) {
        return 1;
    }
    
    std::vector<int> vec = {0, 1};
    
    for (int i = 2; i <= num; i++) {
        int next = vec.back() + vec[vec.size() - 2];
        vec.push_back(next);   
    }

    return vec.back();
}
