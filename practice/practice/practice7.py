# Max heap, heapify T: O(n)
def heapify(arr):
    n = len(arr)
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n - 1)
if __name__ == "__main__":
    A = [1, -4, -3, 0, 2, 3]
    heapify(A)
    print(A)
