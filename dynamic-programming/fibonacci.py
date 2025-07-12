
# recursive
def fibo(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibo(n-1) + fibo(n-2)

# Memoized, with dictionary

# AI Review
# Mutable Default Argument: Avoid mutable default arguments. Instead, initialize memo as None and create a new dictionary inside the function if needed
# No Input Validation: Add a check to handle negative inputs
# Use Iterative Approach for more effeciant space complexity

def fiboMemoD(n, memo = {}):

    if n == 0:
        return 0

    if n == 1:
        return 1
    
    if n in memo:
        return memo[n]
    
    memo[n] = fiboMemoD(n-1, memo) + fiboMemoD(n-2, memo)

    return memo[n]

# Next Time

# Memoize with list
# Try Iterative Approach
# Create fixed version