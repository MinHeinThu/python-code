A = [1,2,3,4,5,6,7]

# Time complexity : O(log n) space complexity: O(1)
# Traditional ways
def binary_search(arr, target):

    L , R = 0, len(arr) -1

    while L <= R:
        M = L + ((R - L) // 2)

        if target == arr[M]:
            return True
        elif target > arr[M]:
            L = M + 1
        else:
            R = M -1
    return False
print(binary_search(A,7))


# Over Under Search
# Time complexity : O(log n)

B = [False, True, True, True, True]

def over_under(arr):
    L , R = 0, len(arr) - 1

    while L < R:
        M = L + ((R - L) // 2)

        if arr[M]:
            R = M
        else:
            L = M + 1
    return L

print(over_under(B))
            