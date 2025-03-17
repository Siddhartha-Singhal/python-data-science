# Print name N times

def showName(name, n):
    # base case
    if n == 0:
        return
    
    print(name)

    showName(name, n-1)

name = 'Siddhartha'
n = 5
showName(name, n)