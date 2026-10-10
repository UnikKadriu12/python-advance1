import pandas as pd
import matplotlib.pylot as plt

df = pd.read_csv('data1.csv')

filtred_df = df[df["Avrage IQ"]>=100]

filtred_df = filtred_df.sort_values(by="Avrage IQ",ascending=False)

print(filtred_df)

plt.figure(figsize=(14,8))



bars = plt.bar(filtred_df["Country"],filtred_df["Average IQ"],color="skyblue")

plt.title("Avrage IQ by Country")

plt.show