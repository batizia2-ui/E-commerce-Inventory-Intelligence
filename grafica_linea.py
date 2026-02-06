import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [120, 150, 170, 160, 180, 210]

plt.figure(figsize=(8,4))
plt.plot(meses, ventas, marker="o", linewidth=2)

plt.title("Ventas por Mes - Gráfica de Línea")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.grid(True, alpha=0.3)

plt.savefig("grafica_linea.png", dpi=150)
plt.show()


