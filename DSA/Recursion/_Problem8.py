# You are given N stairs, and you can climb either 1 step or 2 steps at a time. Your task is to find the total number of distinct ways to reach the top of the staircase.

def noOfSteps(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
       return noOfSteps(n-1) + noOfSteps(n-2) 
    
n = int(input("Enter the number of stairs:"))
ways = noOfSteps(n)
print(f"Total number of distinct ways to reach the top of the staircase is {ways}")


# if there is 0 step so no of ways to climb is 1 as there is no way
# if there is 1 step so no of ways to climb is 1
# if there is 2 step so no of ways to climb is 2 (1+1, 2)
# if there is 3 step so no of ways to climb is 3 (1+1+1, 1+2, 2+1)
# if there is 4 step so no of ways to climb is 5 (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
# this is forming a fibonacci like sequnence: 1, 1, 2, 3, 5, ....

#  it is a sum of fibonacci series based ques