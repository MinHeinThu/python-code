def greet(func):
    def wrapper(name):
        print(f"hello: {name}")
        func(name)
    return wrapper

@greet
def greeting(name):
    print(f"hello: {name}, back")

greeting("alice")

