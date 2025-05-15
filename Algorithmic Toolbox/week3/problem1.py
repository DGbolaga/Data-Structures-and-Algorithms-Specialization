#Money Change

#Task: Find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5 and 10.
#Input: m (a single integer)
#Constraints: 1 <= m <= 10 ^ 3
#Output: Minimum number of coins with denominations 1, 5 and 10 that changes m.


def change(m):
    # Theory:
    # if the money >= 10:
    # find the reminder, keep track of num of 10s in money and check if:
    # the money >= 5:
    # find the remainder, keep track of num of 5s in money and check if:
    # the money >= 1:
    # find the remainder, keep track of num of 1s in money and return the count tracker.

    def rem(m, den):
        return [m//den, m % den]
    
    count = 0
    while m > 0:
        
        if m >= 10:
            den = 10
        elif m >= 5:
            den = 5
        else:
            den = 1

        mult, remainder = rem(m, den)
        count += mult
        m -= mult * den
    return count

print(f"Number of change of 2 naira: {change(2)}")
print(f"Number of change of 89 naira: {change(89)}")
print(f"Number of change of 6 naira: {change(6)}")
