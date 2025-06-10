# Binary Search 
# Time complexity: O(log n)
# Space complexity: O(1)

def binary_search(arr, target):
    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        medium = left + ((right-left) // 2)
        if target == arr[medium]:
            return True
        elif target < arr[medium]:
            right = medium - 1
        else:
            left = medium + 1
        # if not found
    return False

if __name__ == "__main__":
    A = [1,2,3,4,5,6,7]
    print(binary_search(A,1))

def under_over(arr):
    n = len(arr)
    l, r = 0, n-1
    while l < r:
        m = l + ((r-l)//2)

        if arr[m]:
            r = m
        else:
            l = m + 1
    return l
if __name__ == "__main__":
    B = [False, True, True, True, True]
    print(under_over(B))

