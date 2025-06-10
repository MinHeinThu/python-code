# Time : O(n^2), Space: O(1)

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False  # Assume no swaps will be made
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True  # A swap was made, so another pass is needed

if __name__ == "__main__":
    A = [1, -4, -3, 0, 2, 3]
    bubble_sort(A)
    print(A)