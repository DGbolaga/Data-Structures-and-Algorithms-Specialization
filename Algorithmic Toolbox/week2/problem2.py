# Last digit of a large Fibonacci Number
num = 331
def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    a, b = 0, 1
    for i in range(2, num+1):
        a, b = b, (a + b)
        #arr.append(arr[-2] + arr[-1])

    return b

print(f"The last digit of the '{num}'th number is: {fib(num) % 10}")
