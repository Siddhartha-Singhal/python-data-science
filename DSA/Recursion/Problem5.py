# Print factorial of N number

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

n = int(input("Enter a no:"))
fact = factorial(n)
print(f"Factorial of {n} is {fact}")