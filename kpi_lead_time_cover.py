import pandas as pd

# Cargar dataset
df = pd.read_csv("ventas_dataset.csv")

# Convertir fecha
df["fecha"] = pd.to_datetime(df["fecha"])

# Días totales del dataset
dias_totales = (df["fecha"].max() - df["fecha"].min()).days + 1

# === KPI POR PRODUCTO ===
demanda_diaria_producto = df.groupby("producto")["cantidad"].sum() / dias_totales
inventario_producto = df.groupby("producto")["inventario"].sum()

lead_time_cover_producto = inventario_producto / demanda_diaria_producto

print("\n=== Lead Time Cover POR PRODUCTO (días de inventario) ===")
print(lead_time_cover_producto)

# === KPI POR CATEGORÍA ===
demanda_diaria_categoria = df.groupby("categoria")["cantidad"].sum() / dias_totales
inventario_categoria = df.groupby("categoria")["inventario"].sum()

lead_time_cover_categoria = inventario_categoria / demanda_diaria_categoria

print("\n=== Lead Time Cover POR CATEGORÍA (días de inventario) ===")
print(lead_time_cover_categoria)

