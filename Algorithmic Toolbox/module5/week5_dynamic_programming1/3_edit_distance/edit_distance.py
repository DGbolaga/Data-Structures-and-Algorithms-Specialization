def edit_distance(first_string, second_string, i, j):
    # using recursion 
    if i < 0: return j + 1 # return remaining length of j 
    if j < 0: return i + 1 # return remaining length of i 
    if first_string[i] == second_string[j]: return edit_distance(first_string, second_string, i-1, j-1)
    
    # insert = move j only, delete = move i only, replace = move both.
    return 1 + min(edit_distance(first_string, second_string, i-1, j), edit_distance(first_string, second_string, i, j-1), edit_distance(first_string, second_string, i-1, j-1))
    
def edit_distance_memo(x, y, memo, i, j):
    # using memoization
    if i >-1 and j >-1 and memo[i][j] != None: return memo[i][j]

    if i < 0: return j + 1
    if j < 0: return i + 1
    if x[i] == y[j]: 
        memo[i][j] = edit_distance_memo(x, y, memo, i-1, j-1)
        return memo[i][j]

    memo[i][j] = 1 + min(edit_distance_memo(x, y, memo, i-1, j), edit_distance_memo(x, y, memo, i, j-1), edit_distance_memo(x, y, memo, i-1, j-1))
    #memo[i][j] = 1 + min(edit_distance_memo(x, y, memo, i-1, j), edit_distance_memo(x, y, memo, i, j-1))
    return memo[i][j]

if __name__ == "__main__":
    x, y = input(), input()
    memo = [[None for _ in range(len(y))] for _ in range(len(x))]
    print(edit_distance_memo(x, y, memo, i=len(x)-1, j=len(y)-1))
