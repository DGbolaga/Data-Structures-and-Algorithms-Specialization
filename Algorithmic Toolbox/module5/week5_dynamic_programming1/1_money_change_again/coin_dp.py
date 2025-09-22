# Recursive solution to the change coin problem. 
# given the coins are [4, 5, 6, 9]
# w = 10

def recursion(n, coins):
    # the goal is to get the smallest value on every iteration + 1
    if n == 0: return 0
    if n < 0: return float("inf")

    minimumNumCoin = min(recursion(n-x, coins)+1 for x in coins)
    return minimumNumCoin

def minCoin(n, coins):
    result = recursion(n, coins)
    if result == float("inf"):
        return -1
    else:
        return result 


n = int(input("Enter amount: "))
x = int(input("How many coins: "))
coins = [int(input(f"Enter {x}: ")) for x in range(1, x+1)]


print(minCoin(n, coins))



