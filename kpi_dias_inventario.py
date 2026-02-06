import pandas as pd

# Cargar dataset
df = pd.read_csv("ventas_dataset.csv")

# Agrupar ventas diarias por producto
ventas_diarias = df.groupby("producto")["cantidad"].sum()

# Inventario actual por producto
inventario_actual = df.groupby("producto")["inventario"].sum()

# Cálculo del KPI: Días de inventario
dias_inventario = inventario_actual / ventas_diarias

print("\n=== DÍAS DE INVENTARIO (DOI) POR PRODUCTO ===")
print(dias_inventario)
