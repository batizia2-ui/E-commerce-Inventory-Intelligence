import pandas as pd

# Cargar dataset
df = pd.read_csv("orders_dataset.csv")

# === Perfect Order Rate ===
df["perfect_order"] = (
    (df["entregado_a_tiempo"] == 1) &
    (df["completo"] == 1) &
    (df["sin_danos"] == 1)
).astype(int)

# KPI general
porcentaje_general = df["perfect_order"].mean() * 100

print("\n=== PERFECT ORDER RATE (GENERAL) ===")
print(f"{porcentaje_general:.2f}%")

# KPI por tipo de error
print("\n=== Breakdown de problemas ===")
print("Retrasos:", (df["entregado_a_tiempo"] == 0).mean() * 100, "%")
print("Incompletos:", (df["completo"] == 0).mean() * 100, "%")
print("Con daños:", (df["sin_danos"] == 0).mean() * 100, "%")
