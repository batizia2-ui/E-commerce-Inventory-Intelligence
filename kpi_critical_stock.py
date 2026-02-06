import pandas as pd

# 1. Load Data
df = pd.read_csv("orders_dataset.csv")

# 2. Daily demand calculation
# Calculamos cuántos días abarca el reporte para sacar el promedio diario
total_days = (pd.to_datetime(df["fecha"]).max() - pd.to_datetime(df["fecha"]).min()).days + 1
product_demand = df.groupby("producto")["cantidad"].sum() / total_days

# 3. Critical Stock Logic (Lead time = 5 days)
# El stock crítico es lo que necesitas tener para no quedarte sin nada mientras llega el pedido
lead_time = 5
critical_stock = product_demand * lead_time

# 4. Output
print("=== Critical Stock Levels per Product ===")
print(critical_stock)
