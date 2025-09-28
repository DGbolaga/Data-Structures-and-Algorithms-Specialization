# solve the minimum num of coin problem using Tabulation DP 

def tabulationDP(n, coins):
    dp = [[0 for _ in range(n+1)] for _ in range(len(coins))]
    
    for i in range(len(coins)):
        for j in range(1, n+1):
            if i == 0:
                if j % coins[i] == 0:
                    dp[i][j] = j // coins[i]
                else:
                    dp[i][j] = float("inf")
            else:
                if j < coins[i]:
                    # copy the above values
                    dp[i][j] = dp[i-1][j]
                else:
                    # get the minimum between above and current 
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i]])
    
    return -1 if dp[-1][n] == float("inf") else dp[-1][n]



n = int(input("Enter amount of change: "))
x = int(input("Enter no of coin denomination: "))
coins = [int(input(f"Enter {i}: ")) for i in range(1, x+1)]

print(f"Answer: {tabulationDP(n, coins)}")
