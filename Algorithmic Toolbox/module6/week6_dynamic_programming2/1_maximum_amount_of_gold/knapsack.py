from sys import stdin


def maximum_gold_dp(capacity, weights, i):
    # using dp 
    pass

def maximum_gold_memo(capacity, weights):
    # using memo 
    n = len(weights)
    memo = [[None for _ in range(capacity + 1)] for _ in range(n+1)]
    def rec(i, c):
        if memo[i][c] != None: return memo[i][c]

        if i == n or c == 0:
            memo[i][c] = 0
            return memo[i][c]

        if weights[i] <= c:
            memo[i][c] = max(rec(i+1, c), weights[i] + rec(i+1, c - weights[i]))
            return memo[i][c]
        else:
            memo[i][c] = rec(i+1, c)
            return memo[i][c]

    return rec(0, capacity)


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold_memo(input_capacity, input_weights))
