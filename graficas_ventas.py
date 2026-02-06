import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset
df = pd.read_csv("ventas_dataset.csv")

# === Gráfica 1: Ventas por Categoría ===
ventas_categoria = df.groupby("categoria")["ventas_totales"].sum()

plt.figure(figsize=(8,5))
plt.bar(ventas_categoria.index, ventas_categoria.values)

plt.title("Ventas Totales por Categoría")
plt.xlabel("Categoría")
plt.ylabel("Ventas Totales")
plt.grid(axis='y', alpha=0.3)

plt.savefig("grafica_ventas_categoria.png", dpi=150)
plt.show()


# === Gráfica 2: Ventas Totales por Producto ===
ventas_producto = df.groupby("producto")["ventas_totales"].sum()

plt.figure(figsize=(9,5))
plt.bar(ventas_producto.index, ventas_producto.values)

plt.title("Ventas Totales por Producto")
plt.xlabel("Producto")
plt.ylabel("Ventas Totales")
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

plt.savefig("grafica_ventas_producto.png", dpi=150)
plt.show()


# === Gráfica 3: Ventas Totales por Día ===
df["fecha"] = pd.to_datetime(df["fecha"])
ventas_diarias = df.groupby("fecha")["ventas_totales"].sum()

plt.figure(figsize=(9,5))
plt.plot(ventas_diarias.index, ventas_diarias.values, marker="o")

plt.title("Ventas Totales por Día")
plt.xlabel("Fecha")
plt.ylabel("Ventas Totales")
plt.grid(alpha=0.3)

plt.savefig("grafica_ventas_diarias.png", dpi=150)
plt.show()


# === Gráfica 4: Ventas Acumuladas ===
df_sorted = df.sort_values("fecha")
df_sorted["ventas_acumuladas"] = df_sorted["ventas_totales"].cumsum()

plt.figure(figsize=(9,5))
plt.plot(df_sorted["fecha"], df_sorted["ventas_acumuladas"], marker="o")

plt.title("Ventas Acumuladas - KPI Profesional")
plt.xlabel("Fecha")
plt.ylabel("Ventas Acumuladas")
plt.grid(alpha=0.3)

plt.savefig("grafica_ventas_acumuladas.png", dpi=150)
plt.show()

