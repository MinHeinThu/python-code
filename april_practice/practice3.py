# Searching algorithms 
# binary search
# Time complexity: O(log n), Space Complexity: (1)
# But If we use binary search we need to use sorted array

# def binary_search(arr, target):
#     l, r = 0, len(arr) - 1
#     while l <= r:
#         m = l + ((r - l) // 2)
#         if arr[m] == target:
#             return True
#         elif arr[m] < target:
#             l = m + 1
#         else:
#             r = m - 1
#     return False

# if __name__ == "__main__":
#     A = [1,2,3,4,5,6,7]
#     print(binary_search(A,0))

def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = l + ((r - l) // 2)
        if arr[m] == target:
            return True
        elif target < arr[m]:
            r = m - 1
        else:
            l = m + 1
    return False

if __name__ == "__main__":
    A = [1,2,3,4,5,6,7]
    print(binary_search(A,2))
    