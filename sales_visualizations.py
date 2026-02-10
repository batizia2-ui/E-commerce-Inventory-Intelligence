import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
# Ensure this filename matches your CSV file exactly
df = pd.read_csv("orders_dataset.csv")
df["fecha"] = pd.to_datetime(df["fecha"])

# === Visualization 1: Total Sales by Category ===
# If you don't have 'total_sales' column, we calculate it first:
df['total_sales'] = df['precio'] * df['cantidad']

sales_by_category = df.groupby("categoria")["total_sales"].sum()

plt.figure(figsize=(8,5))
plt.bar(sales_by_category.index, sales_by_category.values, color='skyblue')

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales ($)")
plt.grid(axis='y', alpha=0.3)
plt.show()

# === Visualization 2: Total Sales by Product ===
sales_by_product = df.groupby("producto")["total_sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(9,5))
plt.bar(sales_by_product.index, sales_by_product.values, color='salmon')

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()

# === Visualization 3: Daily Sales Trend ===
daily_sales = df.groupby("fecha")["total_sales"].sum()

plt.figure(figsize=(9,5))
plt.plot(daily_sales.index, daily_sales.values, marker="o", color='green', linestyle='-')

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales ($)")
plt.grid(alpha=0.3)
plt.show()

# === Visualization 4: Cumulative Sales (KPI) ===
df_sorted = df.sort_values("fecha")
df_sorted["cumulative_sales"] = df_sorted["total_sales"].cumsum()

plt.figure(figsize=(9,5))
plt.plot(df_sorted["fecha"], df_sorted["cumulative_sales"], marker="o", color='purple')

plt.title("Cumulative Sales - Business Performance")
plt.xlabel("Date")
plt.ylabel("Cumulative Revenue ($)")
plt.grid(alpha=0.3)
plt.show()
