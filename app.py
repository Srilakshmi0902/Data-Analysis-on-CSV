# 📊 Sales Data Analysis using Pandas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Step 1: Create Sample CSV File
# -----------------------------
data = {
    "Date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
    "Product": ["Laptop", "Tablet", "Phone", "Headphones", "Monitor"] * 6,
    "Region": ["North", "South", "East", "West", "Central"] * 6,
    "Sales": [200, 150, 300, 100, 250, 400, 180, 220, 90, 310,
              130, 260, 180, 200, 150, 280, 120, 300, 210, 170,
              350, 400, 220, 160, 310, 200, 140, 260, 100, 330]
}

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)  # Save sample CSV
print("✅ Sample sales_data.csv created!\n")

# -----------------------------
# Step 2: Load CSV
# -----------------------------
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
print("📂 Data Loaded:")
print(df.head(), "\n")

# -----------------------------
# Step 3: Basic Exploration
# -----------------------------
print("🔎 Missing Values:\n", df.isnull().sum())
print("\n📊 Summary:\n", df.describe())
print("\n🛒 Products:", df["Product"].unique())
print("🌍 Regions:", df["Region"].unique(), "\n")

# -----------------------------
# Step 4: Sales by Product
# -----------------------------
sales_by_product = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("💰 Sales by Product:\n", sales_by_product, "\n")

plt.figure(figsize=(8,5))
sales_by_product.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Product")
plt.ylabel("Sales")
plt.xlabel("Product")
plt.show()

# -----------------------------
# Step 5: Sales by Region
# -----------------------------
sales_by_region = df.groupby("Region")["Sales"].sum()
print("🌍 Sales by Region:\n", sales_by_region, "\n")

plt.figure(figsize=(6,4))
sales_by_region.plot(kind="bar", color="coral")
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.xlabel("Region")
plt.show()

# -----------------------------
# Step 6: Monthly Sales Trend
# -----------------------------
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()
print("📈 Monthly Sales:\n", monthly_sales, "\n")

plt.figure(figsize=(10,5))
monthly_sales.plot(marker="o", color="green")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month")
plt.show()

# -----------------------------
# Step 7: Product vs Region Heatmap
# -----------------------------
pivot = df.pivot_table(values="Sales", index="Product", columns="Region", aggfunc="sum", fill_value=0)
print("🔥 Product vs Region Table:\n", pivot, "\n")

plt.figure(figsize=(8,6))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="Blues")
plt.title("Sales by Product and Region")
plt.show()

