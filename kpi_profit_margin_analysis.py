import pandas as pd

# 1. Load Data
df = pd.read_csv("orders_dataset.csv")

# 2. Calculate Margins
# Gross Profit = Price - Cost
df['unit_profit'] = df['precio'] - df['costo']

# Margin % = (Profit / Price) * 100
df['margin_percentage'] = (df['unit_profit'] / df['precio']) * 100

# 3. Analyze by Category
# Identify which product categories yield the highest return
category_profitability = df.groupby('categoria')['margin_percentage'].mean().sort_values(ascending=False)

# 4. Output
print("=== Average Profit Margin by Category ===")
print(category_profitability)