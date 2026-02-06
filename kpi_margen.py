import pandas as pd

# Cargar dataset
df = pd.read_csv("ventas_dataset.csv")

# Supuesto profesional: costo = 60% del precio
df["costo_unitario"] = df["precio"] * 0.60

# Costo total por registro
df["costo_total"] = df["costo_unitario"] * df["cantidad"]

# Margen bruto por registro
df["margen_bruto"] = df["ventas_totales"] - df["costo_total"]

# Margen por categoría
margen_categoria = df.groupby("categoria").agg({
    "ventas_totales": "sum",
    "costo_total": "sum",
    "margen_bruto": "sum"
})

# Porcentaje de margen
margen_categoria["margen_%"] = (margen_categoria["margen_bruto"] / margen_categoria["ventas_totales"]) * 100

print("\n=== Margen Bruto por Categoría ===")
print(margen_categoria)
