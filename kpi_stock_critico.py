import pandas as pd

# Cargar dataset
df = pd.read_csv("ventas_dataset.csv")

# Convertir fecha a datetime
df["fecha"] = pd.to_datetime(df["fecha"])

# Calcular días en el dataset
dias_totales = (df["fecha"].max() - df["fecha"].min()).days + 1

# ============================
#  STOCK CRÍTICO POR PRODUCTO
# ============================

# Demanda diaria promedio por producto
demanda_producto = df.groupby("producto")["cantidad"].sum() / dias_totales

# Lead time fijo para todos los productos (suponemos 5 días)
lead_time_producto = 5

stock_critico_producto = demanda_producto * lead_time_producto

# ============================
#  STOCK CRÍTICO POR CATEGORÍA
# ============================

lead_time_categoria = {
    "Ropa": 5,
    "Calzado": 7,
    "Accesorios": 4
}

# Demanda diaria promedio por categoría
demanda_categoria = df.groupby("categoria")["cantidad"].sum() / dias_totales

# Calcular stock crítico usando lead time distinto por categoría
stock_critico_categoria = demanda_categoria * demanda_categoria.index.map(lead_time_categoria)

# ============================
# RESULTADOS
# ============================

print("\n=== Stock Crítico POR PRODUCTO ===")
print(stock_critico_producto)

print("\n=== Stock Crítico POR CATEGORÍA ===")
print(stock_critico_categoria)
