# Time complexity: log n / space complexity constant 

def binary_search(arr, target):
    n = len(arr)
    # Like two pointer algorithm
    left, right = 0, n - 1

    while left <= right:

        middle = left + ((right-left)//2)

        if arr[middle] == target:
            return True
        elif target < arr[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return False

if __name__ == "__main__":
    A = [1,2,3,4,5,6,7]
    print(binary_search(A,2))

