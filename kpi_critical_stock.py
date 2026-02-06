import pandas as pd

# 1. Load Data
df = pd.read_csv("orders_dataset.csv")

# 2. Daily demand calculation
# Calculate total days in the dataset to get daily average
total_days = (pd.to_datetime(df["fecha"]).max() - pd.to_datetime(df["fecha"]).min()).days + 1
product_demand = df.groupby("producto")["cantidad"].sum() / total_days

# 3. Critical Stock Logic (Lead time = 5 days)
# Critical stock is the buffer needed to avoid stockouts during lead time
lead_time = 5
critical_stock = product_demand * lead_time

# 4. Output
print("=== Critical Stock Levels per Product ===")
print(critical_stock)
