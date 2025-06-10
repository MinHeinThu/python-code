import pandas as pd

mydataset = {
    'car': ["Bmw", "Volvo", "Ford"],
    'passings': [3, 5, 5]
}

myVar = pd.DataFrame(mydataset)
print(myVar)
# this will only show with index
a = [2, 5, 5]
my_var = pd.Series(a)
# for index arguments , I can name my own labels
my_var = pd.Series(a, index = ['x', 'y', 'z'])

print(my_var)

# Series is like a column in a table , and one-dimensionla array
a = [1, 5, 6, 7]
print(pd.Series(a, index = ['z', 'y', 'b', 'z']))

# pd.options.display.max_rows = 9999
# print(pd.options.display.max_rows)
# print(pd.options.display.max_info_rows)

