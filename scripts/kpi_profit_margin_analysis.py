import pandas as pd

# 1. Load Data
df = pd.read_csv("orders_dataset.csv")

# 2. Calculate Gross Profit per Product
# Cost is estimated at 70% of unit_price (resulting in ~30% margin)
df['cost'] = df['unit_price'] * 0.7
df['profit'] = (df['unit_price'] - df['cost']) * df['quantity']

# 3. Calculate Profit Margin Percentage
revenue_per_product = df.groupby('product')['unit_price'].sum()
profit_per_product = df.groupby('product')['profit'].sum()
margin_percentage = (profit_per_product / revenue_per_product) * 100

# 4. Output Results
print("=== Profit Margin Analysis by Product (%) ===")
print(margin_percentage.sort_values(ascending=False))