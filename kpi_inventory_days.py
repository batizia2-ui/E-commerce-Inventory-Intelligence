import pandas as pd

# 1. Load Data
df = pd.read_csv("orders_dataset.csv")

# 2. Calculate Inventory Days
# CORRECCIÓN: Usamos 'inventory' y 'quantity' (como en tu CSV)
avg_stock = df['inventory'].mean()
daily_sales = df.groupby('product')['quantity'].sum().mean()

inventory_days = avg_stock / daily_sales

# 4. Output
print("=== Inventory Days Analysis ===")
print(f"Average days to turnover stock: {inventory_days:.2f} days")