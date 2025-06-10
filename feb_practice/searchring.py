# Bubble sort T: O(n^2), S: O(1)

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True
    return arr

if __name__ == "__main__":
    arr = [1,5,3,2,1,0]
    print(bubble_sort(arr))

# Insertion sort T: O(n^2), S: O(1)

def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr
if __name__ == "__main__":
    arr = [1,5,3,2,1,0]
    print(insertion_sort(arr))

# Selection sort T: O(n^2), S: O(1)

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
if __name__ == "__main__":
    arr = [1,5,3,2,1,0]
    print(selection_sort(arr))

# Merge sort T: O(n log n), space(n)

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    m = n // 2

    left = arr[:m]
    right = arr[m:]

    left = merge_sort(left)
    right = merge_sort(right)

    l = r = 0

    sorted = [0] * n
    i = 0

    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            sorted[i] = right[r]
            r += 1
        else:
            sorted[i] = left[l]
            l += 1
        i += 1
    
    # for remaining part

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
    arr = [1,5,3,2,1,0]
    print(merge_sort(arr))

# Quick sort T: O(n log n), S: O(log n)

def quick_sort(arr):
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
    arr = [1,5,3,2,1,0]
    print(quick_sort(arr))

# Counting sort T: O(K + N), O(K)

def counting_sort(arr):
    n = len(arr)
    maxx = max(arr)
    counts = [0] * (maxx + 1)

    for i in arr:
        counts[i] += 1
    
    j = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            arr[j] = c
            j += 1
            counts[c] -= 1


if __name__ == "__main__":
    arr = [5, 3, 2, 1, 3, 3, 7, 1, 3]
    counting_sort(arr)
    print(arr)


        
