# Dynamic programming
# Memoization (Top - down method)
def fib(n):
    memo = {0:0, 1:1}

    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x-1) + f(x-2)
            return memo[x]
    return f(n)


print(fib(3))

# Tabulation (Bottom - up method)

def fib1(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    dp = [0] * (n+1)
    print(dp)

    dp[0] = 0
    dp[1] = 1
    print(dp)
    
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp)

    return dp[n]

print(fib1(4))

def fib2(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    pre, cur = 0, 1

    for i in range(2, n+1):
        pre, cur = cur , pre + cur
        print(pre,cur)
    return cur

print(fib2(5))