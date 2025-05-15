# Solve the Greedy Party Grouping problem:

# Many Childeren came to a party. Organize them into the minimum possible number of groups such  that the age group of any two children in the same group differ by at most 2 years.


# input: n = number of children
#        N = list of n integers, representing the ages of the children
#        k = max age difference i.e 2

# Output: z = minimum number of goups needed.


# Solution:
# Sort the arr in ascending order
# initialize a sub array.
# add elements into the sub array that differ no more than 2
# remove the sub array from initial array, when an age more than 2 is reached.
# keep track of number of times sub array is removed.
# return the number of times sub array is removed.

def min_group(n: int, N: list[int], k=2) -> int:
    sort_n = sorted(N) # ascending order
    group_track = 0
    while sort_n:
        sub_arr = [sort_n[0]]
        sort_n_length = len(sort_n)
        for i in range(1, sort_n_length):
            if abs(sub_arr[0] - sort_n[i]) <= 2:
                sub_arr.append(sort_n[i])
            else:
                group_track += 1
                sort_n = sort_n[len(sub_arr):]
                break

    return group_track
n = 7
N = [3, 4, 5, 10, 11, 12, 13]
print(f"Minimum group for {n} children, with {N} is: {min_group(n,N)}")











