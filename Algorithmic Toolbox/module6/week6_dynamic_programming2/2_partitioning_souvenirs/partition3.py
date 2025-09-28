from sys import stdin


def partition3(values):
    total_v = sum(values)
    n = len(values)
    if total_v % 3 != 0: 
        return 0 
    
    partition_sum = total_v // 3

    #using memoization
    memo = {}
    def rec(i, a, b):
        # i = index, a = 1st partition, b = 2nd partition

        if a > partition_sum or b > partition_sum:
            return False # don't continue if one partitionon exceeds the goal partition
        
        if i == n:
            return a == partition_sum and b == partition_sum
        
        k  = (i, a, b)
        if k in memo: return memo[k]
        
        curr = values[i] # current value at index i

        # trying adding curr to first partition or to second partition or to exclude it from both on the next turn
        ans = rec(i+1, a+curr, b) or rec(i+1, a, b+curr) or rec(i+1, a, b)
        memo[k] = ans 
        return memo[k]
        

    ans = rec(0, 0, 0)
    return int(ans) # 1 if true else 0
    


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
