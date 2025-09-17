import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Read CSV file (use gbk encoding for Windows Excel CSV)
df = pd.read_csv("air_passenger_201301_202507.csv", encoding="gbk")

# 2. Convert month to datetime
df["Date"] = pd.to_datetime(df["month"], format="%Y%m")
df = df.sort_values("Date")
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# 3. Calculate total passengers
df["Total"] = df["Domestic"] + df["HK_MO"] + df["International"]

# -------------------------
# 4. Line chart
plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Domestic"], label="Domestic", marker='o')
plt.plot(df["Date"], df["HK_MO"], label="Hong Kong & Macau", marker='o')
plt.plot(df["Date"], df["International"], label="International", marker='o')
plt.plot(df["Date"], df["Total"], label="Total", linestyle="--", marker='o')
plt.legend()
plt.title("Air Passenger Traffic (2013–2025)")
plt.xlabel("Date")
plt.ylabel("Passengers (10,000 people)")
plt.grid(True)
plt.savefig("air_passenger_trend.png", dpi=300)
plt.close()
print("✅ Line chart saved: air_passenger_trend.png")

# -------------------------
# 5. Heatmaps for each category
categories = ["Domestic", "HK_MO", "International", "Total"]
for cat in categories:
    pivot = df.pivot(index="Year", columns="Month", values=cat)
    
    plt.figure(figsize=(12,6))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu", cbar_kws={'label':'Passengers (10,000)'})
    plt.title(f"{cat} Passenger Traffic Heatmap (2013–2025)")
    plt.xlabel("Month")
    plt.ylabel("Year")
    plt.savefig(f"{cat.lower()}_heatmap.png", dpi=300)
    plt.close()

print("✅ Heatmaps saved for Domestic, HK_MO, International, and Total passengers.")

# -------------------------
# 6. Calculate YoY growth for Total
df["YoY_Growth(%)"] = df["Total"].pct_change(12)

# 7. Save analysis table
df[["Domestic","HK_MO","International","Total","YoY_Growth(%)"]].to_csv(
    "air_passenger_analysis.csv", index=True, encoding="gbk"
)
print("✅ Analysis table saved: air_passenger_analysis.csv")
