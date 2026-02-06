import pandas as pd

# Cargar dataset
df = pd.read_csv("ventas_dataset.csv")

# KPI SIMPLE: Rotación por producto
df["rotacion_simple"] = df["ventas_totales"] / df["inventario"]

print("\n=== Rotación SIMPLE por producto ===")
print(df[["producto", "ventas_totales", "inventario", "rotacion_simple"]])

# Rotación por categoría
rotacion_categoria = df.groupby("categoria").apply(
    lambda x: x["ventas_totales"].sum() / x["inventario"].sum()
)

print("\n=== Rotación SIMPLE por categoría ===")
print(rotacion_categoria)
