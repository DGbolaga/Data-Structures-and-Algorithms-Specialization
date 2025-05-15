# Implement an algorithm for the fractional knapsack problem.

# Maximum Value of the Loot:
# A thief finds much more loot than his bag can fit. Helpt him to find the most valuable combination
# of items assuming that any fraction of a loot iteem can be put into his bag.


# Inputs and Constraints: 
#       W = capacity of Knapsack = 0 <= W <= 2*10^6
#       v = value of item = 0 <= v <= 2*10^6
#       w = weight of item = 0 <= w <= 2*10^6
#       n = number of items = 1 <= n <= 10*3


# Output:
#       Output the maximum value of fractions of items that fit into the
#       knapsack. The absolute value of the difference between the answer of 
#       your program and the optimal value should be at most 10^-3. To ensure
#       this, output your answer at least 4 digits after teh decimal points 
#       otherwise your answer, while being computed correctly, can turn out to be
#       wrong because of round issues).


def maxValueLoot(
