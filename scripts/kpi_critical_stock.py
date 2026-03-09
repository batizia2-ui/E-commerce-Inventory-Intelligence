import pandas as pd

# 1. Load Data
df = pd.read_csv("orders_dataset.csv")

# 2. Convert 'date' column to datetime objects
# Note: dayfirst=True ensures DD/MM/YYYY format is correctly parsed
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# 3. Calculate Daily Demand
# Formula: Total units sold / Total number of days in dataset
total_days = (df['date'].max() - df['date'].min()).days + 1
daily_demand = df.groupby('product')['quantity'].sum() / total_days

# 4. Define Lead Time (Supplier delivery time)
# Set to 7 days based on retail inventory standards
lead_time_days = 7

# 5. Calculate Critical Stock Level (Reorder Point)
# Formula: Daily Demand * Lead Time
critical_stock_level = daily_demand * lead_time_days

# 6. Output Results
print("=== Critical Stock Levels (Minimum units required) ===")
print(critical_stock_level.sort_values(ascending=False))

