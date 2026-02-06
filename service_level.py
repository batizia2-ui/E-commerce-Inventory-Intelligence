import pandas as pd

# Dataset simulado de pedidos (para practicar)
data = {
    "pedido_id": [1,2,3,4,5,6,7,8,9,10],
    "producto": [
        "Camiseta Básica","Pantalón Mezclilla","Bolsa Casual","Reloj Digital","Tenis Deportivos",
        "Camiseta Básica","Bolsa Casual","Tenis Deportivos","Pantalón Mezclilla","Reloj Digital"
    ],
    "entregado_a_tiempo": [1,1,0,1,1,1,0,1,1,1]  
    # 1 = entregado a tiempo, 0 = retraso
}

df = pd.DataFrame(data)

# Calcular service level
service_level = df["entregado_a_tiempo"].mean() * 100

print("=== SERVICE LEVEL GENERAL ===")
print(f"{service_level:.2f}%")

# Service Level por producto
service_level_prod = df.groupby("producto")["entregado_a_tiempo"].mean() * 100

print("\n=== SERVICE LEVEL POR PRODUCTO ===")
print(service_level_prod)
