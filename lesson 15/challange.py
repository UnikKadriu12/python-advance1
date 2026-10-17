
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("data.csv", skipinitialspace=True)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Clean numeric columns
numeric_columns = [
    "temperature",
    "humidity",
    "atmospheric pressure"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column].astype(str).str.strip(),
        errors="coerce"
    )

# Create a date column from year and day (month/day)
df["date"] = pd.to_datetime(
    df["year"].astype(str) + "/" + df["day"].astype(str).str.strip(),
    format="%Y/%m/%d",
    errors="coerce"
)

# Remove rows with missing temperature or invalid dates
df = df.dropna(subset=["temperature", "date"]).copy()

# Sort data by date
df = df.sort_values("date")

# 2. Temperature Overview
average_temperature = df["temperature"].mean()

print("1. TEMPERATURE OVERVIEW")
print(f"Average temperature: {average_temperature:.2f}")

# 3. Monthly Temperature
df["month"] = df["date"].dt.month
df["month_name"] = df["date"].dt.strftime("%B")

monthly_average = df.groupby("month")["temperature"].mean()

# Display monthly averages in calendar order
monthly_average.index = pd.to_datetime(
    monthly_average.index, format="%m"
).strftime("%B")

print("\n2. MONTHLY AVERAGE TEMPERATURE")
print(monthly_average.round(2))

# Bar plot of monthly average temperatures
plt.figure(figsize=(10, 5))
plt.bar(monthly_average.index, monthly_average.values,
        color="skyblue", edgecolor="black")

plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Highs and Lows
hottest_day = df.loc[df["temperature"].idxmax()]
coldest_day = df.loc[df["temperature"].idxmin()]

print("\n3. HOTTEST DAY")
print(hottest_day.to_string())

print("\nCOLDEST DAY")
print(coldest_day.to_string())

# 5. Temperature Trends
plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["temperature"],
         color="red", marker="o", markersize=4,
         linestyle="-")

plt.title("Temperature Changes Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Seasonal Average Temperature
# Northern Hemisphere seasons
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["season"] = df["date"].dt.month.apply(get_season)

seasonal_average = (
    df.groupby("season")["temperature"]
    .mean()
    .reindex(["Spring", "Summer", "Autumn", "Winter"])
    .dropna()
)

print("\n4. SEASONAL AVERAGE TEMPERATURE")
print(seasonal_average.round(2))

# Optional: plot seasonal averages
plt.figure(figsize=(8, 5))
plt.bar(seasonal_average.index, seasonal_average.values,
        color=["lightgreen", "orange", "brown", "lightblue"],
        edgecolor="black")

plt.title("Seasonal Average Temperature")
plt.xlabel("Season")
plt.ylabel("Average Temperature (°C)")
plt.tight_layout()
plt.show()
