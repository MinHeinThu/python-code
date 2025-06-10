# Bubble sort
# Time complexity: O(n^2)
# Space complexity: O(1)

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True            
    return arr

if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    print(f"Bubble sort: {bubble_sort(arr)}")



