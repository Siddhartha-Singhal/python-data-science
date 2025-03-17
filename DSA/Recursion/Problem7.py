# Power function using recursion

def power(n, p):
    if p == 1:
        return n
    return n * power(n, p-1)

n = int(input("Enter the number whose power is to be calculated: "))
p = int(input("Enter the power for the number: "))
print(f"Value of {n} raised to the power {p} is {power(n, p)}")