# Recursion

def f(num):
    # Base case
    if num == 0:
        return num
    else:
        return num + f(num -1)

print(f(4))
print(f(9))

def factorail(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorail(n-1)

print(factorail(5))