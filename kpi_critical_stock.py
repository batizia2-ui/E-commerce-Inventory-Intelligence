import pandas as pd

# 1. Load Data
df = pd.read_csv("orders_dataset.csv")

# 2. Convertir la columna 'date' a objetos de fecha reales
# Importante: dayfirst=True le dice a Python que tu fecha empieza con el día (DD/MM/YYYY)
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# 3. Calcular Demanda Diaria (Daily Demand)
# Fórmula: Total vendido / Número de días totales en el dataset
total_days = (df['date'].max() - df['date'].min()).days + 1
daily_demand = df.groupby('product')['quantity'].sum() / total_days

# 4. Definir Lead Time (Tiempo de espera del proveedor)
# Asumimos 7 días para que lleguen nuevos productos (esto tú lo defines como experta)
lead_time_days = 7

# 5. Calcular Nivel de Stock Crítico (Reorder Point)
critical_stock_level = daily_demand * lead_time_days

# 6. Output
print("=== Critical Stock Levels (Minimum units required) ===")
print(critical_stock_level.sort_values(ascending=False))

