# Time: O(n^2) , Space: O(1)

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    A = [1, -3, 0, 2, 3, -4]
    selection_sort(A)
    print(A)