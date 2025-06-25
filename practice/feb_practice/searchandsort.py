# Bubble sort T: n^2 S: constant

def bubble_sort(arr):
    n = len(arr)

    flag = True
    while flag:
        flag = False

        for i in range(1,n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True

if __name__ == "__main__":
    arr = [7,14,11,8,9]
    bubble_sort(arr)
    print(arr)


my_array = [64, 34, 25, 12, 22, 11, 1, 5]

n = len(my_array)
for i in range(n-1): # 0, 1, 2, 3, 4, 5, 6 = 7
    for j in range(n-i-1): # 7, 6, 5, 4, 3, 2, 1
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array:", my_array)

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
        
    return False

print(binary_search(my_array,2))


def insertion_sort(arr):

    n = len(arr) # length of arr

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr

if __name__ == "__main__":
    arr = [7,14,11,8,9]
    print(insertion_sort(arr)) 

def selection_sort(arr):

    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
if __name__ == "__main__":
    arr = [7,14,11,8,9]
    print(selection_sort(arr))


import heapq

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    m = n // 2

    left = arr[:m]

    right = arr[m:]

    left = merge_sort(left)

    right = merge_sort(right)

    l, r , i = 0, 0, 0

    sorted = [0] * n

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted[i] = left[l]
            l += 1
        else:
            sorted[i] = right[r]
            r += 1
        i += 1

    while l < len(left):
        sorted[i] = left[l]
        l += 1
        i += 1


    while r < len(right):
        sorted[i] = right[r]
        r += 1
        i += 1
    
    return sorted

if __name__ == "__main__":
    arr = [7,14,11,8,9]
    print(merge_sort(arr))


def quick_sort(arr): # T: O(n log n), S: O(log n)

    n = len(arr)

    if n <= 1:
        return arr
    
    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]

    right = [x for x in arr[:-1] if x > pivot]

    left = quick_sort(left)

    right = quick_sort(right)

    return left + [pivot] + right

if __name__ == "__main__":
    arr = [7,14,11,8,9]
    print(quick_sort(arr))


# counting sort
# Time: O(K + N), S: O(K)

def counting_sort(arr):
    n = len(arr)

    k = max(arr)

    count = [0] * (k + 1)

    for x in arr:
        count[x] += 1

    print(count)

    i = 0

    for c in range(k + 1):
        while count[c] > 0:
            arr[i] = c
            i += 1
            count[c] -= 1

if __name__ == "__main__":
    arr = [5, 3, 2, 1, 3, 3, 7, 1, 3]
    counting_sort(arr)
    print(arr)



def count_sort(arr):
    n = len(arr)

    k = max(arr)

    count = [0] * (k + 1)

    for x in arr:
        count[x] += 1

    i = 0

    for c in range(k+1):
        while count[c] > 0:
            arr[i] = c
            i += 1
            count[c] -= 1


