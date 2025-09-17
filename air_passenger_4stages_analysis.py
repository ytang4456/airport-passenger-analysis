import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# 1. Read CSV (GBK encoding)
df = pd.read_csv("air_passenger_201301_202507.csv", encoding="gbk")
df["Date"] = pd.to_datetime(df["month"], format="%Y%m")
df = df.sort_values("Date")
df["Total"] = df["Domestic"] + df["HK_MO"] + df["International"]

# -------------------------
# 2. Define 4 stages
stages = [
    ("2013-01-01", "2019-09-30", "Stage1_201301_201909"),
    ("2019-10-01", "2020-01-31", "Stage2_201910_202001"),
    ("2020-02-01", "2023-07-31", "Stage3_202002_202307"),
    ("2023-08-01", "2025-07-31", "Stage4_202308_202507"),
]

# -------------------------
# 3. Process each stage
for start, end, name in stages:
    stage_df = df[(df["Date"] >= start) & (df["Date"] <= end)]
    
    # 3a. Line chart
    plt.figure(figsize=(10,5))
    plt.plot(stage_df["Date"], stage_df["Domestic"], label="Domestic", marker='o')
    plt.plot(stage_df["Date"], stage_df["HK_MO"], label="Hong Kong & Macau", marker='o')
    plt.plot(stage_df["Date"], stage_df["International"], label="International", marker='o')
    plt.plot(stage_df["Date"], stage_df["Total"], label="Total", linestyle="--", marker='o')
    plt.title(f"Air Passenger Traffic {name}")
    plt.xlabel("Date")
    plt.ylabel("Passengers (10,000)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{name}_trend.png", dpi=300)
    plt.close()
    
    # 3b. Calculate YoY growth and save table
    stage_df["YoY_Growth(%)"] = stage_df["Total"].pct_change(12)
    stage_df[["Domestic","HK_MO","International","Total","YoY_Growth(%)"]].to_csv(
        f"{name}_analysis.csv", index=True, encoding="gbk"
    )

print("✅ All 4 stages charts and analysis tables have been generated.")
