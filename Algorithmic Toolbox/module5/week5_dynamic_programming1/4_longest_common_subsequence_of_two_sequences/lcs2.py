
def lcs2(a, i, b, j):
    if  memo[i][j] != None:
        return memo[i][j]

    if i >= len(a) or j >= len(b):
        memo[i][j] = 0
        return memo[i][j]

    if a[i] == b[j]:
        memo[i][j] = 1 + lcs2(a, i+1, b, j+1)
        return memo[i][j]

    #else 
    memo[i][j] = max(lcs2(a, i+1, b, j), lcs2(a, i, b, j+1))
    return memo[i][j]
    


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m
    
    memo = [[None for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    print(lcs2(a, 0, b, 0))
