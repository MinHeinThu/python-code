# Exercise 2.10 (extract numbers)

# Write a function extract_numbers that gets a string as a parameter. It should return a list of numbers that can be both ints and floats. Split the string to words at whitespace using the split() method. Then iterate through each word, and initially try to convert to an int. If unsuccesful, then try to convert to a float. If not a number then skip the word.

# Example run: print(extract_numbers("abd 123 1.2 test 13.2 -1")) will return [123, 1.2, 13.2, -1]


def extract_numbers(arr):
    new_arr = arr.split()
    n = len(new_arr)
    result = []
    def is_numeric_string(arr):
        try:
            float(arr)
            return True
        except ValueError:
            return False
    for i in range(n):
        if is_numeric_string(new_arr[i]):
            result.append(float(new_arr[i]))
    return result

arr = "abd 123 1.2 test 13.2 -1" 
print(extract_numbers(arr))
