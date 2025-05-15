# Greatest Comomon Divisor

def gcd(a, b):
    # theory:
    # if a = a(prime) + bq
    # d, divides a and b if and only if it divides a(prime) and b
    # a(prime) is the remainder of a / b

    if b == 0:
        return a
    
    a_prime = a % b
    return gcd(b, a_prime)

print(f"The gcd of 6 and 8 is {gcd(6, 8)}")
print(f"The gcd of 18 and 35 is {gcd(18, 35)}")
print(f"The gcd of 28851538 and 1183019 is {gcd(28851538, 1183019)}")



