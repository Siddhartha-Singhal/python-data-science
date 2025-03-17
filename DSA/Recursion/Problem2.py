# Print N to 1 using recursion

def count(n):
    if n == 0:
        return
    
    print(n)

    count(n-1)

n = int(input("Enter a no:"))
count(n)