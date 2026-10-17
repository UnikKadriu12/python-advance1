
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("data.csv", skipinitialspace=True)

# Clean column names
df.columns = df.columns.str.strip()

# Convert numeric columns
df["temperature"] = pd.to_numeric(
    df["temperature"].astype(str).str.strip(),
    errors="coerce"
)

# Create a date column
df["date"] = pd.to_datetime(
    df["year"].astype(str) + "/" + df["day"].astype(str).str.strip(),
    format="%Y/%m/%d",
    errors="coerce"
)

# Remove invalid rows and sort by date
df = df.dropna(subset=["date", "temperature"])
df = df.sort_values("date")

# 1. Temperature Overview
average_temperature = df["temperature"].mean()

print("1. TEMPERATURE OVERVIEW")
print(f"Average temperature: {average_temperature:.2f} °C")

# 2. Monthly Temperature
df["month"] = df["date"].dt.month

monthly_average = df.groupby("month")["temperature"].mean()

monthly_average.index = pd.to_datetime(
    monthly_average.index, format="%m"
).strftime("%B")

print("\n2. MONTHLY AVERAGE TEMPERATURE")
print(monthly_average.round(2))

plt.figure(figsize=(10, 5))
plt.bar(monthly_average.index, monthly_average.values,
        color="skyblue", edgecolor="black")

plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Highs and Lows
hottest_day = df.loc[df["temperature"].idxmax()]
coldest_day = df.loc[df["temperature"].idxmin()]

print("\n3. HOTTEST DAY")
print(hottest_day)

print("\nCOLDEST DAY")
print(coldest_day)

# 4. Temperature Trends
plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["temperature"],
         color="red", marker="o")

plt.title("Temperature Changes Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Seasonal Average Temperature
def get_season(month):
    if month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Winter"

df["season"] = df["date"].dt.month.apply(get_season)

seasonal_average = df.groupby("season")["temperature"].mean()

seasonal_average = seasonal_average.reindex(
    ["Spring", "Summer", "Autumn", "Winter"]
).dropna()

print("\n5. SEASONAL AVERAGE TEMPERATURE")
print(seasonal_average.round(2))

plt.figure(figsize=(8, 5))
plt.bar(seasonal_average.index, seasonal_average.values,
        color=["lightgreen", "orange", "brown", "lightblue"],
        edgecolor="black")

plt.title("Average Temperature by Season")
plt.xlabel("Season")
plt.ylabel("Average Temperature (°C)")
plt.tight_layout()
plt.show()
