# Bubble Sort
# the biggest one stay in the end of the array
def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
    #    [6, 2, 5, 3, 9] 
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"Pass{j+1}, {arr}")
    return arr

n = bubble_sort([6, 2, 5, 3, 9])
print(n)

# Time complexity is O(n^2) and Space complexity : O(1)