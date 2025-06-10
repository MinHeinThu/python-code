import csv
with open('example.txt', 'w') as file:
    file.write("hello \n")
    file.write("hello world")

with open('example.txt', 'r') as file1:
    # content = file1.read()
    # print(content)

    for line in file1:
        print(line.strip())

with open('example.txt', 'w') as file:
    file.write('append new line\n')

with open('data.csv', 'r') as file3:
    reader = csv.reader(file3)
    for row in reader:
        print(row)

import pandas as pd
df = pd.read_csv('data.csv')
print(df)