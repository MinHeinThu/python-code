import time

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

print(time.localtime())
print(time.time())

import calendar

print(calendar.prcal(2025))

import pandas as pd
import numpy as np

data = np.array([9, 3, 5, 5, 6])

s = pd.Series(data,index = ['A','B','C','D','E'])
print(s)

# Crating series using pandas

data_key = {"amid": 22, 'jali': 25, 'Fli': 33}
serie = pd.Series(data_key, index = ['jali', 'amid', 'Fli'])
print(serie)
print(serie.iloc[1])
print(serie[1:])

# Pandas dataframe

data_name = [['farli', 22],['jarki', 24], ['xaxi', 21]]
frame = pd.DataFrame(data_name, columns = ['name', 'age'])
print(frame)
print(frame[1:])

