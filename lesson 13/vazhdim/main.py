import pandas as pd

df = pd.read_csv('../../lesson 14/data1.csv')


print(df.info())

# na shfaq 5 rreshtet e pare
print(df.head())


country_data=df['Country']

print(country_data)


subset = df[['Country','Avrage IQ']]

print(subset)


filtred_df = subset[subset['Avrage IQ']>100]
print(filtred_df)

null_mask = df.isnull()

null_count = null_mask.sum()

print(null_count)


df.dropna(inplace=True)


print(df.info())
print("--------------------")
duplicated_cound = df.dulicated().sum
print(duplicated_count)


average_iq_continent = df.groupby('Continent')['Average IQ'].mean()

print(vaerage_iq_continent)

sordetd_avg_by_continent = average_iq_continent.sort_values(ascending=False)

print(sordetd_avg_by_continent)


total_nobel_by_country= df.groupby('Country')['Nobel Prices'].sum()

print(total_nobel_by_country)


sorted_total_nobel_by_country

print(sorted_total_nobel_by_country)


sorted = sorted_total_nobel_by_country[sorted_tottal_nobel_by_country !=0]

print(sorted)