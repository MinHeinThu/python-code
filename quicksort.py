#  Quick sort
#Time : O(n log n) (average case, for worst case is O (n ^ 2))
# Space : O(n)

def quick_sort(arr):

    if len(arr) <= 1:
        return arr# for base case
    

    p = arr[-1]

    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + [p] + R

if __name__ == "__main__":
    A = [-5, 3, 1, -4 , -1, 0, 5, 4]
    print(quick_sort(A))

