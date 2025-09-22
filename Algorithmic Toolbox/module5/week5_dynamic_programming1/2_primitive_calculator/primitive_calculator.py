def compute_operations(n):
    # tabultationDP
    dp = [0, 0]
    prev = [0, 0]
    for i in range(2, n+1):
        # store the value in dp and its location.
        allMoves = [(dp[i-1], i-1)]
        if i % 2 == 0:
            allMoves.append((dp[i//2], i//2))
        if i % 3 == 0:
            allMoves.append((dp[i//3], i//3))
        
        minMove, fromMove = min(allMoves, key=lambda x: x[0])
        dp.append(1 + minMove)
        prev.append(fromMove)
    
    # rebuild path from prev arr
    res = [] # path
    temp = n 
    while temp > 0:
        res.append(temp)
        if temp == 1:
            break 

        temp = prev[temp]
    
    res.reverse() 

    return res


def recursive(n, x=1):
    # memoization
    if x > n:
        return float("inf")  #indicating not a valid path

    if memo[x] != float("inf"):
        return memo[x]

    if x == n:
        memo[x] = 0
        return memo[x]


    times3 = recursive(n, x*3)
    times2 = recursive(n, x*2)
    add1 = recursive(n, x+1)


    return 1 + min(add1, times2, times3)

def bfs(n):
    stack = [1] 
    ans = 0
    while stack:
        new_stack = []
        for x in stack:
            if x == n:
                return ans
            if x + 1 <= n:
                new_stack.append(x + 1)
            if x * 2 <= n:
                new_stack.append(x * 2)
            if x * 3 <= n:
                new_stack.append(x * 3)
        stack = new_stack
        ans += 1
        

    return ans


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)











