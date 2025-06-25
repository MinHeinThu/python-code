import pandas as pd

df = pd.read_csv('data.csv', na_values = ['?', ''])
# print(df.info())
# pd.options.display.max_rows = 30
# new_df = df.dropna()
# print(new_df)

# Inplace change
# df.dropna(inplace = True)
# print(df.to_string())

# To fill the empty cells
# df.fillna('Hello', inplace = True)
# print(df.to_string())

# To Fill the specific coloum 
# df['Date'].fillna('hello', inplace = True)
# print(df)

# x = df['Calories'].mean()
# print(x)
# df['Calories'].fillna(x, inplace=True)
# print(df)

# x = df['Calories'].median()
# print(x)
# df['Calories'].fillna(x, inplace=True)
# print(df.to_string())

# y = df['Date'].mode()[0]
# print(y)
# df['Date'].fillna(y, inplace=True)
# print(df.to_string())

df['Date'] = pd.to_datetime(df['Date'], errors ='coerce')
df['Date'].fillna(method='ffill', inplace=True)
print(df.to_string())