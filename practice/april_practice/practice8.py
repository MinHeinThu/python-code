#// Bubble sort is like the biggest one is go to the end

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True
if __name__ == "__main__":
    A = [1, -4, -3, 0, 2, 3]
    bubble_sort(A)
    print(A)
