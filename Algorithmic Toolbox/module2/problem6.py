#Last Digit of the Sum of Fibonacci Numbers

# for n, the last digit of the sum of all fibonacci numbers up to the nth is:
# the sum of the last digit of the individual fibonacci numbers

# function to get the last digit of fibonacci numbers
# call the function from 0 till the highest number
# sum all the last digit.
# return the last digit of the sum (mod 10)

# compute the Fibonacci number (num) in mod 10. 
def fib_mod_last_digt(num, m=10):
    # a new sequence always begins with 0 1
    if num == 0:
        return 0
    if num == 1:
        return 1

    a, b = 0, 1
    mod = [0, 1]
    for i in range(2, num+1):
        a, b = b, (a+b)%m
        mod.append(b)

        if mod[-2] == 0 and mod[-1] == 1:
            mod.pop()
            mod.pop() 
            break
                
    period = len(mod)
    last_digit = mod[num % period] # fib_num is the last digit.

    return last_digit    


#compute sum of nth fibonacci numbers
def sum_fib(n):
    result = 0
    for i in range(n+1):
        result += fib_mod_last_digt(i, m=10)

    print(f"The n is: {n}")
    print(f"The last digit of nth fibonacci number: {result % 10}")


sum_fib(3)
sum_fib(200)
sum_fib(100)
