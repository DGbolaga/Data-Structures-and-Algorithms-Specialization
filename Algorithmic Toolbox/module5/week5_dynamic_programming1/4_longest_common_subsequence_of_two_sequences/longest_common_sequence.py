def lcs_using_dp(a, b):
    pass

def lcs_using_memo(a, a_len, i, b, b_len, j):
    # a and b represent the array, while i and j represent the index 
    if memo[i][j] != None:
        return memo[i][j]

    if i >= a_len or j >= b_len:
        memo[i][j] = 0
        return memo[i][j]

    if a[i] == b[j]:
        memo[i][j] = 1 + lcs_using_memo(a, a_len, i+1, b, b_len, j+1)
        return memo[i][j]

    memo[i][j] = max(lcs_using_memo(a, a_len, i+1, b, b_len, j), lcs_using_memo(a, a_len, i, b, b_len, j+1))
    return memo[i][j]


a = [int(input(f"Enter {i} value: ")) for i in range(int(input("Enter length of first string: ")))]
b = [int(input(f"Enter {i} value: ")) for i in range(int(input("Enter length of second string: ")))]
memo = [[None for _ in range(len(b)+1)] for _ in range(len(a)+1)]
print(f"Answer: {lcs_using_memo(a, len(a), 0, b, len(b), 0)}")
