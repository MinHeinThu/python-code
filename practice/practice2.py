# Binary_search Time : O(log n), space : O(1)
from practice1 import heap_sort
import heapq
def binary_search(arr, target):
    n = len(arr)
    L , R = 0, n - 1

    while L <= R:
        M = L + ((R - L)//2)
        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1
    # not found
    return "Not found"

if __name__ == "__main__":
    A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    # heap sort T:O(n log n), space: O(1)
    def heap_sort(arr):
        n = len(arr)
        heapq.heapify(arr)
        sorted_arr = [0] * n
        for i in range(n):
            minn = heapq.heappop(arr)
            sorted_arr[i] = minn
        return sorted_arr
    print(heap_sort(A))
    print(binary_search(A, 9))


def bubble_sort(arr): # T: O(n ^ 2), S: O(1)
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]

if __name__ == "__main__":
    A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    bubble_sort(A)
    print(A)

def selection_sort(arr): # T: O(n ^ 2), S: O(1)
    n = len(arr)
    for i in range(1, n):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

if __name__ == "__main__":
    A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    selection_sort(A)
    print(A)

def selection_sort(arr): # T: O(n^2), S: O(1)
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if arr[j] < arr[min_index]:
                arr[j], arr[min_index] = arr[min_index], arr[j]

if __name__ == "__main__":
    A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
    selection_sort(A)
    print(A)