# Modulo of Fibonacci Numbers and pisano period
# 2015 mod 3 = 251(8) + 7, where 8 is the pisano period and 7 is the 
#remainder. F(2015) mod 3 = F(7) mod 3 = 1

def fib_mod(n, m):
    #Theory:
    a, b = 0, 1
    mod_arr = [0, 1]

    for i in range(2, m * 6):
        a, b = b, (a + b) % m
        mod_arr.append(b)

        if mod_arr[-2] == 0 and mod_arr[-1] == 1:
            mod_arr.pop()
            mod_arr.pop() 
            break
        
    period = len(mod_arr)
    fib_num = mod_arr[n % period]

    print(f"The fibonacci number of {n} in mod {m} is: {fib_num}\nIt has a period of {period}")
    print(f"-------------------------------")

            


fib_mod(15, 2)
fib_mod(15, 3)
fib_mod(2015, 3)
fib_mod(239, 1000)
#fib_mod(9999, 3)
#fib_mod(2816213588, 239)



