import pandas as pd

# Cargar dataset
df = pd.read_csv("ventas_dataset.csv")

print("\n=== Primeras filas ===")
print(df.head())

# === KPI 1: Ventas Totales ===
ventas_totales = df["ventas_totales"].sum()
print(f"\n👉 Ventas totales del periodo: {ventas_totales}")

# === KPI 2: Ticket promedio ===
ticket_prom = df["ventas_totales"].mean()
print(f"👉 Ticket promedio: {ticket_prom:.2f}")

# === KPI 3: Producto más vendido (cantidad) ===
producto_top = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False).head(1)
print("\n👉 Producto con mayor cantidad vendida:")
print(producto_top)

# === KPI 4: Categoría más rentable ===
categoria_top = df.groupby("categoria")["ventas_totales"].sum().sort_values(ascending=False).idxmax()
print(f"\n👉 Categoría más rentable: {categoria_top}")

# === KPI 5: Inventario crítico (<20) ===
inventario_bajo = df[df["inventario"] < 20][["producto", "inventario"]]
print("\n👉 Productos con inventario BAJO (<20):")
print(inventario_bajo)

# === Resumen por producto ===
resumen_producto = df.groupby("producto").agg({
    "ventas_totales": "sum",
    "cantidad": "sum",
    "inventario": "sum"
})
print("\n=== Resumen por producto ===")
print(resumen_producto)
# === KPI: Ticket Promedio por Categoría ===

kpi_categoria = df.groupby("categoria").apply(
    lambda x: x["ventas_totales"].sum() / x["cantidad"].sum()
)

print("\n=== Ticket Promedio por Categoría ===")
print(kpi_categoria)

