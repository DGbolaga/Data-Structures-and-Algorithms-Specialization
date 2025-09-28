def fib_with_dp(n):
    if memo[n] != None:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = fib_with_dp(n-1) + fib_with_dp(n-2)

    return memo[n]

n = int(input("Enter No of Fib Sequence: "))
memo = [None] * (n + 1)
print(fib_with_dp(n))
