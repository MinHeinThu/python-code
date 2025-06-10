# Insertion sort
# Time complexity: O(n^2)
# Space complexity: O(1)

def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
    return arr
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    print(f"Bubble sort: {insertion_sort(arr)}")


    