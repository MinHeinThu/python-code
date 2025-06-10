# l = [input() for _ in range(int(input()))]
# print(l)

def outer_fun(x):
    def inner_fun(y):
        return x + y
    return inner_fun

hello = outer_fun(2)
# print(hello)
print(hello(3))

def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
@my_decorator
def greet():
    print("Hello!")

greet()
