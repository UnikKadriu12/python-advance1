import pandas as pd

produktet = ["Molla","Banane","Protokajt","Rrushi"]

sales = [150,200,180,90]


sales_series = pd.Series(sales, index=produktet)

print(sales_series)


print(sales_series["Molla"])


shitjetTotale = sales_series.sum()

print(shitjetTotale)

shitjaMaEMadhe =  sales