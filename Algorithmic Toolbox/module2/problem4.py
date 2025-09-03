# Least Common Multiple

def lcm(num1, num2):
    #Theory
    #The lcm of a and b is the product of ab divided by the gcf.
    #lcm(a, b) = (ab) / gcf(a, b)

    def gcf(a,b):
        if b == 0:
            return a

        a_prime = a % b
        return gcf(b, a_prime)

    return int((num1 * num2) / gcf(num1, num2))

print(f"The lcm of 6 and 8 is: {lcm(6, 8)}")
print (f"The lcm of 28851538 and 1183019 is: {lcm(28851538, 1183019)}")

