name: str = "hello"
age: int = 22
isWorking: bool = False

print(f"{name} is {age} years and {isWorking}")

def my_name(name: str) -> str:
    print(f"hello, {name}")

name = "Enter your name: "
my_name(name)
print(type(name), type(my_name))

def binarySearch(arr: str, target: str):
    n = len(arr)

    l, r = 0, n-1

    while l <= r:
        m = l + ((r-l)// 2)

        if arr[m] == target:
            return True
        elif target > arr[m]:
            l = m + 1
        else: 
            r = m - 1
    else: 
        return "Not found"

if __name__ == "__main__":
    array = [1, 3, 3, 4, 6, 7, 8]
    print(binarySearch(array, 30))