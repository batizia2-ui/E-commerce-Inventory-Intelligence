import pandas as pd

# 1. Load Data
df = pd.read_csv("orders_dataset.csv")

# 2. Simulate Profitability
# Assuming a 30% profit margin for Electronics and 25% for Computing
def calculate_margin(row):
    if row['category'] == 'Electronics':
        return row['total_sales'] * 0.30
    else:
        return row['total_sales'] * 0.25

df['estimated_profit'] = df.apply(calculate_margin, axis=1)

# 3. Profit by Category
category_profit = df.groupby('category')['estimated_profit'].sum()

print("=== Estimated Profit by Category ===")
print(category_profit.apply(lambda x: f"${x:,.2f}"))

# 4. Total Profitability Margin
total_margin = (df['estimated_profit'].sum() / df['total_sales'].sum()) * 100
print(f"\nOverall Profit Margin: {total_margin:.2f}%")