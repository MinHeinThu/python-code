# Selection Sort
# Time complexity : O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    print(f"Selection sort: {selection_sort(arr)}")