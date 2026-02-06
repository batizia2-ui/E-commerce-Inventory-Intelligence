import pandas as pd

# Cargar dataset
df = pd.read_csv("ventas_dataset.csv")

# ================================
# 1. SUPOSICIÓN: Demanda estimada
# ================================
# Si un producto está en inventario < 20 → asumimos que faltó stock (demanda no surtida)
df["demanda_estimada"] = df["cantidad"] + df.apply(lambda x: 1 if x["inventario"] < 20 else 0, axis=1)

# ================================
# 2. FILL RATE POR PRODUCTO
# ================================
fill_rate_producto = df.groupby("producto").apply(
    lambda x: x["cantidad"].sum() / x["demanda_estimada"].sum()
)

# ================================
# 3. FILL RATE POR CATEGORÍA
# ================================
fill_rate_categoria = df.groupby("categoria").apply(
    lambda x: x["cantidad"].sum() / x["demanda_estimada"].sum()
)

print("\n=== FILL RATE POR PRODUCTO ===")
print(fill_rate_producto)

print("\n=== FILL RATE POR CATEGORÍA ===")
print(fill_rate_categoria)
