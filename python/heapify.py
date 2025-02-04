# Heapify
# Time : O(n), Space : O(1)
# Parent = (index-2)// 2
# Child left = index * 2 + 1
# Child right = index * 2 + 2
import heapq

def heap_heapify(arr, n, i):
    largest = i # root node
    left = (i * 2) + 1
    right = (i * 2) + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap_heapify(arr, n, largest)


def build_heap(arr):
    n = len(arr)

    for i in range((n//2)-1, -1, -1):
        heap_heapify(arr, n, i)
        
def heap_sort(arr):
    n = len(arr)
    build_heap(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap_heapify(arr, i, 0)  

if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    heap_sort(arr)
    print(arr)