/* ========================================================
   PROJECT: E-commerce Inventory Intelligence
   FILE: validation_queries.sql
   PURPOSE: Cross-validation of key business metrics
   AUTHOR: Basilia del Pozo
   ======================================================== */

-- 1. Total Revenue Validation ($10,955)
-- Goal: Confirm that the sum of all sales matches the dashboard total.
SELECT 
    SUM(unit_price * quantity) AS total_revenue
FROM orders_dataset;

-- 2. Gross Margin Validation (31%)
-- Goal: Verify the profitability margin across all product lines.
SELECT 
    product_name,
    AVG((unit_price - unit_cost) / unit_price) * 100 AS gross_margin_percentage
FROM orders_dataset
GROUP BY product_name;