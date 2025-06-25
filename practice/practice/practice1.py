import heapq
if __name__ == "__main__":

    # Min heap
    a = [1, 3, -2, 4, 2, -2, 0]

    heapq.heapify(a) # O(n
    print(a)

    heapq.heappush(a, 3) # T : log(n)
    print(a)

    heapq.heappop(a) # log n
    print(a)

    # peak the min Time : O(1)
    print(a[0])


# Time : O(n log n), Space : O(n)
def heap_sort(arr):
    n = len(arr)
    heapq.heapify(arr)
    sorted_arr = [0] * n
    for i in range(n):
        minn = heapq.heappop(arr)
        sorted_arr[i] = minn
    return sorted_arr
if __name__ == "__main__":
    a = [1, 3, -2, 4, 2, -2, 0]
    print(heap_sort(a))
# Max heap
    b = [-3, 9, 5, 0, 2, 1]

    n = len(b)
    for i in range(n):
        b[i] = -b[i]
    
    heapq.heapify(b)
    print(b)
    largest = -heapq.heappop(b)
    print(largest)

    c = [1, 3, 5, 6, 7, -4, 2]

    heap = []
    for i in c:
        heapq.heappush(heap, i)
    print(heap)
    
    # Heap puhspop, Time: O(log n) , Space: O(1)
    heapq.heappushpop(c, 2)
    print(c)