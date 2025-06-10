# Fixed length window

def fixed_length_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return float(max_sum/k)

nums = [1,12,-5,-6,50,3]
k = 4

print(fixed_length_window(nums, k))