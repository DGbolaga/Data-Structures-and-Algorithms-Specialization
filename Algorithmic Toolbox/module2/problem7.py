# Last digit of a partial sum of fibonacci numbers


#Last Digit of the Sum of Fibonacci Numbers

# for n, the last digit of the sum of all fibonacci numbers up to the nth is:
# the sum of the last digit of the individual fibonacci numbers


def fib_mod_last_digit(num, m=10):
    # a new sequence always begins with 0 1
    if num == 0:
        return 0
    if num == 1:
        return 1

    a, b = 0, 1
    mod = [0, 1]
    for i in range(2, num+1):
        a, b = b, (a+b) % m
        mod.append(b)

        if mod[-2] == 0 and mod[-1] == 1:
            mod.pop()
            mod.pop() 
                    
    period = len(mod)
    last_digit = mod[num % period]
    
    return last_digit


#compute sum of nth fibonacci numbers
def sum_fib(n1, n2):
    result = 0
    for i in range(n1, n2+1):
        result += fib_mod_last_digit(i)
    print(f"The partial sum of the {n1}th to {n2} Fibonacci number is: {result % 10}")

sum_fib(3, 7)
sum_fib(10, 10)
sum_fib(10, 200)

