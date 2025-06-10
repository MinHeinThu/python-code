import heapq

# Min Heap

if __name__ == "__main__":
    A = [-4, 3, -9, 0, 4, 1] # Normal arr
    heapq.heapify(A) # Time : O(n), Space : O(n)

    print(A)

    # Heap push, Time: O(log n) , Space: O(1)
    heapq.heappush(A,8)
    print(A)

    # Heap pop, Time: O(log n) , Space: O(1)
    heapq.heappop(A)
    print(A)

    # Heap puhspop, Time: O(log n) , Space: O(1)
    heapq.heappushpop(A, 2)
    print(A)

    # Heap peek , Time: O(1) , Space: O(1)
    print(A[0])

    # Max heap
    B = [-4, 3, -9, 0, 4, 1]
    n = len(B)

    for i in range(n):
        B[i] = -B[i]


    heapq.heapify(B)
    print(f"Max: {B}")

    # Build heap form scratch - Time : O(n log n)

    C = [1, 4, 0, -2]
    heap = []
    for i in C:
        heapq.heappush(heap, i)
    print(heap)

# Heap sort , Time: O(n log n) , Space: O(1)

def heap_sort(arr):
    heapq.heapify(arr)

    n = len (arr)

    sorted_arr = [0] * n
    for i in range(n):
        minn = heapq.heappop(arr)
        sorted_arr[i] = minn
    return sorted_arr

if __name__ == "__main__":
    A = [-4, 3, -9, 0, 4, 1]
    print(heap_sort(A))
