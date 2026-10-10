import pandas as pd

import matplotlib.pylot as plt

df = pd.read_csv("data1.csv")


nobel_prizes_by_continent = df.groupby("Continent")["Nobel Prices"].sum()

no_of_continents = nobels_prizes_by_continent.count()

print(no_of_continents)

color = ["gold","lightcoral","yellow","thistle","orange","lightskyblue","aquamarine","burlywood"]

plt.figures(figsize=(10,10))


nobel_prizes_by_continent.plot(kind="pie",colors=colors, autopct='%1.1f%%')

plt.title("Distribution of nobel prizes by continent")
plt.show

