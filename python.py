import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("ssbmedier.csv", index_col = 0, skiprows=[0, 1], sep=";", na_values=[".", ".."], encoding="Latin-1")

print(data)
print(data.head())
data.plot()
plt.show()