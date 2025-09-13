# def f(n):
#     if n <= 1:
#         return n
#     else:    
#         return f(n-1) + f(n-2)

# print(f(2))


count = 2

def f(prev1, prev2):
    global count
    if count <= 19:
        new_f = prev1 + prev2
        print(new_f)
        prev2 = prev1
        prev1 = new_f
        count += 1
        f(prev1, prev2)
    else:
        return -1
    
print(f(1,0))
