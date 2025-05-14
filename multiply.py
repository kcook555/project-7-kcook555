# Author: Kevin Phillips
# GitHub username: kcook555
# Date: 5/13/2025
# Description: Function that takes two integers
#              and uses addition and recursion to
#              find the product

def multiply(a, b):
    """Find the product of two numbers using addition and recursion."""
    #Checking for a == 0 isn't strictly necessary, but will save b recursions
    #Checking for b == 0 is necessary to prevent infinite recursions
    if a == 0 or b == 0:
        return 0
    #If b == 1, the result is found and the recursion should be stopped
    if b == 1:
        return a
    b -= 1
    return a + multiply(a, b)
