import pandas as pd
df = pd.read_csv('datos_piloto_precios.csv')
analisis_por_producto = df.groupby('Producto')['Precio'].agg(['mean', 'median', 'count'])
print(analisis_por_producto)