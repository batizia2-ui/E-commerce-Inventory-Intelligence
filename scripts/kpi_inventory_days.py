import pandas as pd

# 1. Load Data
df = pd.read_csv("orders_dataset.csv")

# 2. Calculate Average Inventory and Cost of Goods Sold (COGS)
avg_inventory_value = df.groupby('product')['unit_price'].mean() * 50 
cogs = df.groupby('product')['unit_price'].sum()

# 3. Calculate Inventory Turnover Ratio
inventory_turnover = cogs / avg_inventory_value

# 4. Calculate Days Sales of Inventory (DSI)
# Formula: 365 / Inventory Turnover
inventory_days = 365 / inventory_turnover

# 5. Output Results
print("=== Days Sales of Inventory (DSI) ===")
print(inventory_days.sort_values(ascending=False))