# Input: n = number of children (int)
#         N = list of integer
# Output: k = number of segements to be formed, where
#             the maximum difference in age group is 2.


def group(n, N):
    #Theory:
    # Implement algorithm using greedy strategy.
    # Use sliding window to group efficiently
    
    N.sort() # sort list of age
    
    segment = 0
    l_ptr = 0

    while l_ptr < n:
        r_ptr = l_ptr
        
        while r_ptr < n and N[r_ptr] - N[l_ptr] <= 2:
            r_ptr += 1

        segment += 1
        l_ptr = r_ptr

    return segment

a = [2, 5, 3, 7, 39, 9, 3]
print(f"The best grouping strategy of {a} where the maximum age difference is not more than 2 is: {group(len(a), a)}")
    

