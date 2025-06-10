import pandas as pd

myData = {
    'name': ['hello', 'world'],
    'id' : [1, 4]
}

myVar = pd.DataFrame(myData, index=['row1', 'row2'])
print(myVar)

data = ['hello', 'world', 'is nothing']
var_data = pd.Series(data)
print(var_data)

