# Print 1 to N using recursion

def count(n, i=1):
    if i>n:
        return
    
    print(i)

    count(n, i+1)

n = int(input("Enter a no."))
count(n)