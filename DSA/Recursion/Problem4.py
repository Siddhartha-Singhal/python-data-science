# Sum of first N numbers

def add(n):
    if n == 1:
        return 1
    
    return n + add(n-1)

n = int(input("Enter a no:"))
sum = add(n)
print(f"Sum of {n} numbers is: {sum}")