# Print fibonacci series

def fib(n, a, b, i):
    # Base cases
    if n <= 0:
        return
    if i > n:
        return
    print(a+b, end=" ")
    fib(n, b, a+b, i+1)

n = int(input("Enter the number of terms in fibonacci series:"))
# Edge cases
if n == 1:
    print(0, end=" ")
elif n == 2:
    print(0, 1, end=" ")
else:
    print(0, 1, end=" ")
    fib(n, 0, 1, 3)