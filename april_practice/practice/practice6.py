# Heap sort T: O(n log n), S: O(n)
import heapq
def heap_sort(arr):

    n = len(arr)
    heapq.heapify(arr) #T: O(n), S:O(1)
    #print(arr)
    sorted_arr = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        sorted_arr[i] = minn 
    return sorted_arr

if __name__ == "__main__":
    A = [-4, 3, -9, 0, 4, 1]
    print(f"Heap sort: {heap_sort(A)}")

# Bubble sort: T: (n^2), S:O(1)
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
    A = [-4, -3, 0, 9, 3, 5, 4]
    bubble_sort(A)
    print(f"Bubble sort: {A}")

# Insertion sort T: O(n^2), S: O(1)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
if __name__ == "__main__":
    A = [-4, -3, 0, 9, 3, 5, 4]
    insertion_sort(A)
    print(f"Insertion sorting: {A}")

# Selection sort T: O(n^2), S: O(1)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
if __name__ == "__main__":
    A = [-4, -3, 0, 9, 3, 5, 4]
    selection_sort(A)
    print(f"Selection sort: {A}")

# Quick sort T: O(n log n), S: O(n)
def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr # base case
    pv = arr[-1]
    left = [x for x in arr[:-1] if x <= pv]
    right = [x for x in arr[:-1] if x > pv]
    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pv] + right
if __name__ == "__main__":
    A = [-5, 3, 1, -4 , -1, 0, 5, 4]
    print(f"Quick sort: {quick_sort(A)}")

def heapp(arr):
    def heapify(arr, n, i):
        # Set largest as root
        largest = i
        
        # Left child index: 2 * i + 1
        l = (2 * i) + 1  
        
        # Right child index: 2 * i + 2
        r = (2 * i) + 2  
        
        # If left child is larger than root
        if (l < n) and (arr[i] < arr[l]):
            largest = l
        
        # If right child is larger than the largest so far
        if (r < n) and (arr[largest] < arr[r]):
            largest = r
        
        # If largest is not root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)  # Get the length of the array

    # Build a max-heap from the bottom up
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Swap the root (maximum value) with the last element
        arr[i], arr[0] = arr[0], arr[i]

        # Call heapify on the reduced heap to maintain the heap property
        heapify(arr, i, 0)

if __name__ == "__main__":
    A = [-5, 3, 1, -4]
    heapp(A)
    print(f"Heap sort: {A}")