import pandas as pd

# 1. Load Data
df = pd.read_csv("orders_dataset.csv")

# 2. Calculate Inventory Days
# Formula: (Average Inventory / Cost of Goods Sold) * Period Days
# Simplified for this analysis: Average stock units / Daily sales
avg_stock = df['cantidad'].mean()
daily_sales = df.groupby('producto')['cantidad'].sum().mean()

inventory_days = avg_stock / daily_sales

# 4. Output
print("=== Inventory Days Analysis ===")
print(f"Average days to turnover stock: {inventory_days:.2f} days")