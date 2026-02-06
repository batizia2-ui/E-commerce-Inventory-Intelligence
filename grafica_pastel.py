import matplotlib.pyplot as plt

categorias = ["Ropa", "Zapatos", "Accesorios", "Otros"]
ventas = [300, 180, 120, 60]

plt.figure(figsize=(6,6))
plt.pie(
    ventas,
    labels=categorias,
    autopct="%1.1f%%",
    startangle=140
)

plt.title("Distribución de Ventas por Categoría")
plt.savefig("grafica_pastel.png", dpi=150)
plt.show()
