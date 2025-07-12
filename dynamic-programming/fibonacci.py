
# recursive
def fibo(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibo(n-1) + fibo(n-2)

# Memoized, with dictionary
def fiboMemoD(n, memo = {}):

    if n == 0:
        return 0

    if n == 1:
        return 1
    
    if n in memo:
        return memo[n]
    
    memo[n] = fiboMemoD(n-1, memo) + fiboMemoD(n-2, memo)

    return memo[n]

# Memoize with list next time