# Heapify
# Time: O(log n)
# Space: O(1)
# Min heap
def heap_heapify(arr, n, i):
    smallest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child
    
    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i] # swap 
        heap_heapify(arr, n, i)

def build_heap(arr):
    n = len(arr)
    for i in range((n - 2)//2, -1, -1):
        heap_heapify(arr, n, i)





    
        
       
