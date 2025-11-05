from flask.testing import FlaskClient


def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True 
    return arr

if __name__ == "__main__":
    arr = [4, 2, 6, 7, 5, 3]
    bubble_sort(arr)
    print(arr)


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    arr = [4, 2, 6, 7, 5, 3]
    selection_sort(arr)
    print(arr)


def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1] , arr[j] = arr[j], arr[j-1]
    return arr

if __name__ == "__main__":
    arr = [4, 2, 6, 7, 5, 3]
    insertion_sort(arr)
    print(arr)


