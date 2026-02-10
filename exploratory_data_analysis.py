import pandas as pd

# 1. Load dataset
# Use "orders_dataset.csv" to keep consistency with your other scripts
df = pd.read_csv("orders_dataset.csv")

print("\n=== Dataset Overview: First Rows ===")
print(df.head())

# === KPI 1: Total Revenue ===
total_revenue = df["total_sales"].sum()
print(f"\nTotal Revenue for the period: ${total_revenue:,.2f}")

# === KPI 2: Average Ticket (AOV) ===
avg_ticket = df["total_sales"].mean()
print(f"Average Order Value (AOV): ${avg_ticket:.2f}")

# === KPI 3: Best Selling Product (Quantity) ===
top_product = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False).head(1)
print("\nTop Selling Product by Quantity:")
print(top_product)

# === KPI 4: Most Profitable Category ===
top_category = df.groupby("categoria")["total_sales"].sum().sort_values(ascending=False).idxmax()
print(f"\nMost Profitable Category: {top_category}")

# === KPI 5: Critical Stock Alert (< 20 units) ===
critical_inventory = df[df["inventario"] < 20][["producto", "inventario"]]
print("\nProducts with CRITICAL STOCK (< 20):")
print(critical_inventory)

# === Product Performance Summary ===
product_summary = df.groupby("producto").agg({
    "total_sales": "sum",
    "cantidad": "sum",
    "inventario": "sum"
})
print("\n=== Product Performance Summary ===")
print(product_summary)

# === KPI: Average Ticket by Category ===
avg_ticket_category = df.groupby("categoria").apply(
    lambda x: x["total_sales"].sum() / x["cantidad"].sum(),
    include_groups=False
)

print("\n=== Average Ticket by Category ===")
print(avg_ticket_category)