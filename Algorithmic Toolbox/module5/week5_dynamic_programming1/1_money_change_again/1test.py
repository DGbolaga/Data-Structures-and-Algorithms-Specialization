# Solve the minimum coin problem using memoization

def recursion(n, coins):
    # recursive helper function
    if memo[n] != None:
        return memo[n]
    if n == 0:
        memo[n] = 0
        return memo[n]
    if n < 0:
        memo[n] = float("inf") # indicating not a valid path
        return memo[n]

    minimumCoin = min((recursion(n-x, coins) + 1) for x in coins)
    memo[n] = minimumCoin
    return memo[n]

def minCoin(n, coins):
    # main function
    result = recursion(n, coins)
    if result == float("inf"):
        print("Not feasible")
        return -1
    else:
        return result

n = int(input("Enter amount of change: "))
x = int(input("Enter no of coin denominations: "))
coins = [int(input(f"Enter {i}: ")) for i in range(1, x+1)]
memo = [None] * (n + 1)
print(minCoin(n, coins))
