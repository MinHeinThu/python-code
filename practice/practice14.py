import heapq

# Heap Sort
# Time Complexity : O( n log n )
# Space : O (1)

def heap_sort(arr):
    n = len(arr)
    heapq.heapify(arr) # Time complexity O(n), Space complexity O(1)
    sorted = [0] * n
    for i in range(n):
        minn = heapq.heappop(arr) # Time : O(log n), Space(1)
        sorted[i] = minn
    return sorted

if __name__ == "__main__":
    A = [-4, 3, -9, 0, 4, 1]
    print(heap_sort(A))

