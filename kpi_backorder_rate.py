import pandas as pd

# Cargar dataset simulado con backorders
df = pd.read_csv("backorders_dataset.csv")

# Calcular unidades en backorder
df["backorder_unidades"] = df["demanda"] - df["entregado"]

# KPI a nivel total
total_demanda = df["demanda"].sum()
total_backorder = df["backorder_unidades"].sum()

backorder_rate_total = (total_backorder / total_demanda) * 100

print("\n=== BACKORDER RATE TOTAL ===")
print(f"Demanda total: {total_demanda}")
print(f"Unidades en backorder: {total_backorder}")
print(f"Tasa de Backorder: {backorder_rate_total:.2f}%")

# KPI por producto
backorder_productos = df.groupby("producto")[["demanda", "backorder_unidades"]].sum()
backorder_productos["backorder_rate_%"] = (backorder_productos["backorder_unidades"] / backorder_productos["demanda"]) * 100

print("\n=== BACKORDER RATE POR PRODUCTO ===")
print(backorder_productos)
