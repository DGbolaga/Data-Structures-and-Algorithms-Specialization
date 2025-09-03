
# You are given a set of valuable grains, 
# with each unique grain costing a certain amount and having specific weight.
# What is the maximum value you can get from a combination of grains, that
# will contain your knapsack.

# Input: n - Number of unique grains (int)
#       weights - list of integers representing the weight of each grain
#       values - list of int representing the value of each grain
#       capacity - Maximum weight the knapsack can hold.

# Output: k - max value of combined grains worth not more than the capacity of knapsack



def knapsack(w: list[int], v: list[int], c: int):
    #while knapsack is not full
    #choose item i with max worth in $/kg
    #if item with max worth fits knapsack, take all of it
    #Else take so much as to fill the knapsack
    #Return the total value and amounts taken
    sack = 0 
    value = 0
    while sack <= c:
        max_worth = [v[i] / w[i] for i in range(len(w))]
        max_val_itm = max(max_worth)
        max_val_idx = max_worth.index(max_val_itm)

        if w[max_val_idx] <= c:
            sack += w[max_val_idx]
            value += max_worth[max_val_idx]
        else:
            value += max_worth[max_val_idx] * (c - sack)
            sack += (c - sack)
    
    print(f"Weight: {w} \nAmount: {v}\n Max_worth: {max_worth}\nCapacity: {c} == Sack: {sack}\nValue: {value}")



w = [4, 6, 2, 7] # in kilogram
v = [25, 20, 25, 40] # in $
c = 15 # kg

knapsack(w, v, c)


