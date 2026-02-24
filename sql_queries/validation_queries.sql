-- Validación de Revenue Total ($10,955)
SELECT 
    SUM(unit_price * quantity) AS total_revenue
FROM orders_dataset;

-- Validación de Margen Bruto (31%)
SELECT 
    product_name,
    AVG((unit_price - unit_cost) / unit_price) * 100 AS gross_margin_percentage
FROM orders_dataset
GROUP BY product_name;