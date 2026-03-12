# 📖 Data Dictionary - E-commerce Inventory

This document describes the structure and columns of the dataset used in the **E-commerce Inventory & Profitability Intelligence** project.

| Column Name | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| **product_id** | Integer | Unique identifier for each hardware product. | `102` |
| **product_name** | String | Full name/model of the laptop or accessory. | `Gaming Laptop G5` |
| **category** | String | Product segment (Laptops, Accessories, etc.). | `Laptops` |
| **unit_price** | Float | Selling price per unit in USD. | `1250.00` |
| **unit_cost** | Float | Estimated manufacturing or acquisition cost. | `850.00` |
| **stock_level** | Integer | Current units available in the warehouse. | `15` |
| **sales_volume** | Integer | Total units sold during the analyzed period. | `45` |
| **margin_pct** | Percentage | Calculated gross profit margin ((Price-Cost)/Price). | `0.32` |

---
*Note: This dataset is optimized for business intelligence analysis and contains anonymized commercial data.*