# Implement an algorithm for the fractional knapsack problem.

# Maximum Value of the Loot:
# A thief finds much more loot than his bag can fit. Help him to find the most valuable combination
# of items assuming that any fraction of a loot item can be put into his bag.


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


def maxValueLoot(W: int, items: list[list[int]]) -> int:    
    """
    e.g W = 50
        n = 3
        items = [[60, 20], [100, 50], [120, 30]]
        items = [[v1, w1], [v2, w2], [v3, w3]]
        ValPerWeight = [v1/w1, v2/w2, ...]

    """
    def max_item_index(items: list[int]) -> list[int]:

        result = [0, -1]
        for idx, val in enumerate(items):
            if val > result[0]:
                result[0] =  val
                result[1] += idx

        return result


    










    
