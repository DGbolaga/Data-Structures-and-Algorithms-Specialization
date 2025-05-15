# Last Digit of the Sum of Squares of Fibonacci Numbers.

# function -> get last digit of fib number
# last_digit_of_Fib_sum_sqares -> f(n) * f(n+1)

def last_digit_of_fib(n, m=10):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    mod = [0, 1]
    for i in range(2, n+1):
        a, b = b, (a + b) % m
        mod.append(b)

        if mod[-2] == 0 and mod[-1] == 1:
            mod.pop()
            mod.pop()
            break

    pisano_period = len(mod)
    result = mod[n % pisano_period]

    return result

def last_digit_fib_ss(n):
    result = (last_digit_of_fib(n) * last_digit_of_fib(n+1)) % 10
    print(f"The last digit of the {n}th fibonacci number is: {result}")

last_digit_fib_ss(5)
last_digit_fib_ss(6)
last_digit_fib_ss(7)
last_digit_fib_ss(8)


