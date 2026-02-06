import pandas as pd

# 1. Loading the data (Como abrir tu reporte de ventas)
df = pd.read_csv("pilot_pricing_dataset.csv")

# 2. Calculating Unit Profit (Precio de venta - Costo)
# Creamos una columna nueva llamada 'unit_profit'
df['unit_profit'] = df['precio'] - df['costo']

# 3. Calculating Margin Percentage (Margen de utilidad %)
# La fórmula: (Ganancia / Precio) * 100
df['margin_percentage'] = (df['unit_profit'] / df['precio']) * 100

# 4. Grouping by Category (Nuestra "Tabla Dinámica")
# Queremos saber qué categoría es más rentable (Laptops vs Accesorios)
category_profitability = df.groupby('categoria')['margin_percentage'].mean()

# 5. Business Insight Results
print("Average Profit Margin per Category:")
print(category_profitability)