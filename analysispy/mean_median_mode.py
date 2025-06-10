import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# example of moving record by my iphone one week counting by calories

data = [145, 122, 182, 182, 141, 85, 136]

mean = np.mean(data)
median = np.median(data)
# mode = np.mode(data)

variance = np.var(data)
std_deviation = np.std(data)

df = pd.DataFrame(data, columns= ["Calories buried"])
print(df)

print(f"Mean: {mean}")
print(f"median: {median}")
# print(f"Mode: {mode}")

print(f"Variance: {variance}")

print(f"Standard deviation: {std_deviation}")

plt.scatter(range(len(data)), data, color = "blue", label = "data points")

plt.axhline(mean, color = "red", linestyle = "--", label = f"Mean: {mean}")

plt.axhline(mean, color = "green", linestyle = "--", label = f"Medain: {median}")

plt.xlabel("Index")
plt.ylabel("Caloried buried")
plt.title("Scatter plot of exercies")

plt.legend()
plt.show()