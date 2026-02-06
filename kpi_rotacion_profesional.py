import pandas as pd

# Cargar dataset
df = pd.read_csv("ventas_dataset.csv")

print("\n=== Rotación PROFESIONAL por categoría ===")

# Agrupar por categoría
rotacion_categoria = df.groupby("categoria").apply(
    lambda x: x["ventas_totales"].sum() / x["inventario"].sum()
)

print(rotacion_categoria)

# Interpretación automática
print("\n=== Interpretación ===")
for categoria, valor in rotacion_categoria.items():
    if valor > 1:
        print(f"✔ {categoria}: Buena rotación ({valor:.2f}) — Se vende rápido.")
    else:
        print(f"⚠ {categoria}: Rotación baja ({valor:.2f}) — Podría estar detenida en inventario.")
