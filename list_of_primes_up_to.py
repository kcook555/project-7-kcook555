# Author: Kevin Phillips
# GitHub username: kcook555
# Date: 4/23/2025
# Description: Function that takes an integer
#              and returns all prime numbers up
#              to that integer

def list_of_primes_up_to(limit=100):
    """Takes an upper limit and returns all prime numbers up to that limit."""
    if limit == 0:
        return []
    # Create a list of limit+1 elements
    indexed_bools = [True] * (limit+1)
    indexed_bools[0] = False
    indexed_bools[1] = False
    # Start next_divisor as 2
    next_divisor = 2
    # Repeat the following until next divisor is <= the square root of the limit
    while next_divisor <= limit**0.5:
        #Check everything after this for divisibility
        for i in range(next_divisor,limit+1):
            if i != next_divisor and i % next_divisor == 0:
                indexed_bools[i] = False
        # Find the smallest index, starting with 2, with a value of True and set it as next_divisor
        next_divisor = find_next_divisor(next_divisor, limit, indexed_bools)
    # Use list comprehension to create a new list containing the indices of the True elements
    primes = [index for index in range(len(indexed_bools)) if indexed_bools[index] == True]
    # Return the new list
    return primes

def find_next_divisor(next_divisor,limit,indexed_bools):
    """Takes a range and a list of bools and returns the index of the first True"""
    for i in range(next_divisor+1,limit+1):
        if indexed_bools[i]:
            return i
