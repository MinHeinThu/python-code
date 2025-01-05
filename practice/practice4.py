import heapq

# Binary Search 
# T: O(log n), S: O(1)

def binarySearch(arr, target):
    n = len(arr)
    l,r = 0, n-1

    while l <= r:
        m = l + ((r-l)//2)

        if target == arr[m]:
            return True
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    # if not found
    return False

if __name__ == "__main__":
    arr = [-5, -4, -1, 0, 1, 3, 4, 5]
    print(binarySearch(arr,5))


def underOver(arr):
    n = len(arr)

    l,r = 0, n-1

    while l < r:
        m = l + ((r-l)//2)

        # if arr[m] for true under over
        if arr[m] is False: # for false under over
            r = m
        else:
            l = m + 1
    return l
    
if __name__ == "__main__":
    # B = [False, True, True, True, True]
    # print(underOver(B))
    B = [True,True, False, False, False]
    print(underOver(B))
            
    a = [-4, 3, 3, 4, 5, 6, 2, 1, 0]  # normal list

    # heapify T: O(n), S: O(1)
    # min heap
    heapq.heapify(a)
    print(a)
    print(heapq.heappop(a)) # O(log n)
    heapq.heappush(a,-2) # O(log n)
    print(a)
    # Heap peek is O(1)
    print(a[0])

    #heappushpop(O (log n))
    heapq.heappushpop(a, 2)
    print("pp",a)

    # mix heap

    b = [-4, 3, 3, 4, 5, 6, 2, 1, 0]
    n = len(b)

    for i in range(n):
        b[i] = -b[i]
    heapq.heapify(b)
    print(b)

# T: O (n log n), S: O(1)
def heapSort(arr):
    n = len(arr)
    heapq.heapify(arr)
    sorted = [0] * n
    for i in range(n):
        minn = heapq.heappop(arr)
        sorted[i] = minn
    return sorted

if __name__ == "__main__":
    a = [-4, 3, 3, 4, 5, 6, 2, 1, 0]
    print(f"heapsorr:{heapSort(a)}")


def bubbleSort(arr): # T: O(n ^ 2), S: O(1)
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1] > arr [i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True

if __name__ == "__main__":
    a = [-4, 3, 3, 4, 5, 6, 2, 1, 0]
    bubbleSort(a)
    print(f"Bubble sort: {a}")

# Insertion sort, T: O(n^2), S:O(1)
def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

if __name__ == "__main__":
    a = [-4, 3, 3, 4, 5, 6, 2, 1, 0]
    insertionSort(a)
    print(f"Insertion sort:{a} n^2")

# Selection sort T: O(n^2), S:O(1)
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    a = [-4, 3, 3, 4, 5, 6, 2, 1, 0]
    selectionSort(a)  
    print(f"Selection sort: {a} n^2")

# merge sort T: (n log n), space(n)
def mergeSort(arr):
    n = len(arr)
    if n == 1:
        return arr # for the base case
    
    m = n // 2
    left = arr[:m]
    right = arr[m:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    l , r = 0, 0

    sorted_arr = [0] * n
    i = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_arr[i] = left[l]
            l += 1
        else:
            sorted_arr[i] = right[r]
            r +=1
        i += 1

    while l < len(left):
        sorted_arr[i] = left[l]
        l += 1
        i += 1
    
    while r < len(right):
        sorted_arr[i] = right[r]
        r += 1
        i += 1
    
    return sorted_arr
if __name__ == "__main__":
    A = [1, -4, -3, 0, 2, 3]
    print(f"Merge sort: {mergeSort(A)}")     


