/* PROJECT: Sales Analysis January 2025
   GOAL: Identify Top 5 Performing Products
*/

SELECT 
    product_name AS Product, 
    SUM(sales_amount) AS Total_Revenue,
    COUNT(order_id) AS Transactions
FROM sales_dataset_nuevo
WHERE sale_date BETWEEN '2025-01-01' AND '2025-01-15'
GROUP BY product_name
ORDER BY Total_Revenue DESC
LIMIT 5;
