import random, time

def stress_test_lcs3(n=100, m=100, q=100, value_range=(1, 20)):
    """
    Generate three random integer sequences of lengths n, m, q
    and measure how long lcs3 takes.
    """
    # random sequences in the given value range
    a = [random.randint(*value_range) for _ in range(n)]
    b = [random.randint(*value_range) for _ in range(m)]
    c = [random.randint(*value_range) for _ in range(q)]

    # memo table sized to len+1 in each dimension
    memo = [[[None]*(q+1) for _ in range(m+1)] for _ in range(n+1)]

    start = time.perf_counter()
    result = lcs3(a, b, c, memo, 0, 0, 0)
    elapsed = time.perf_counter() - start
    
    print(f"arr 1: {a} \n arr 2: {b} \n arr 3: {c}")
    print(f"Lengths: {n}, {m}, {q}")
    print(f"LCS length: {result}")
    print(f"Time: {elapsed:.3f} seconds")
    return result, elapsed


def lcs3(first_sequence, second_sequence, third_sequence, memo, i, j, k):
    if memo[i][j][k] != None: return memo[i][j][k]

    if i >= len(first_sequence) or j >= len(second_sequence) or k >= len(third_sequence): 
        memo[i][j][k] = 0
        return memo[i][j][k]

    if first_sequence[i] == second_sequence[j] == third_sequence[k]: 
        memo[i][j][k] = 1 + lcs3(first_sequence, second_sequence, third_sequence, memo, i+1, j+1, k+1)
        return memo[i][j][k]
    
    memo[i][j][k] = max(lcs3(first_sequence, second_sequence, third_sequence, memo, i+1, j, k), lcs3(first_sequence, second_sequence, third_sequence, memo, i, j+1, k), lcs3(first_sequence, second_sequence, third_sequence, memo, i, j, k+1))

    return memo[i][j][k]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    memo = [[[None for _ in range(len(c)+1)] for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    print(lcs3(a, b, c, memo, 0, 0, 0))
