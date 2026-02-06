import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr"]
ventas = [120, 150, 170, 160]

plt.figure(figsize=(8, 4))
plt.bar(meses, ventas)
plt.title("Ventas por Mes - Gráfica de Barras")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.grid(axis='y', alpha=0.3)

plt.savefig("grafica_barras.png", dpi=150)
plt.show()

