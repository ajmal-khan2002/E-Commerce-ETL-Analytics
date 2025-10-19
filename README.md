# E-Commerce-ETL-Analytics

## Project Overview
This project implements an **ETL pipeline** for an e-commerce business using **Python** and **Pandas**. It extracts, transforms, and loads data from multiple sources, performs analytics, and generates actionable insights. The focus is on **data engineering skills**, including data cleaning, aggregation, and dashboard generation.

---
---

## Features

1. **ETL Pipeline**
   - Extract: Load CSV datasets for customers, orders, products, suppliers, and reviews.
   - Transform: Clean data, handle duplicates/missing values, convert data types, calculate revenue, merge datasets.
   - Load: Generate insights and export results into an **Excel dashboard**.

2. **Data Cleaning & Transformation**
   - Remove duplicates and standardize columns.
   - Handle missing/null values.
   - Calculate **Total Revenue**, Customer Lifetime Value (CLV), and other metrics.

3. **Analytics & Insights**
   - Aggregate monthly sales by product, category, and supplier.
   - Identify top customers and top-performing products.
   - Analyze category/subcategory performance.
   - Track revenue trends over months and quarters.
   - Evaluate product and supplier performance using ratings and reviews.

4. **Advanced Data Engineering Operations**
   - Pivot tables, hierarchical indexing (Category → Subcategory → Product).
   - Filtering high-value customers and low-stock/high-sales products.
   - Handle real-world scenarios: cancelled/returned orders, multiple emails.

5. **Dashboard Generation**
   - KPIs: Total revenue, net revenue, average order value, order counts.
   - Category-level and monthly summaries.
   - Export all insights to an Excel dashboard (`Ecommerce_Dashboard.xlsx`).

---

## Dataset
The project uses five CSV files:

- `customers.csv` – Customer information
- `orders.csv` – Order transactions
- `products.csv` – Product details
- `suppliers.csv` – Supplier information
- `reviews.csv` – Product reviews

> **Note:** Update file paths in the `load_data()` function to match your system or repository structure.

#Output
<img width="477" height="181" alt="Screenshot 2025-10-19 222618" src="https://github.com/user-attachments/assets/4565ec2a-c321-495c-b16e-08446b8d0b3f" />
<img width="782" height="165" alt="Screenshot 2025-10-19 222630" src="https://github.com/user-attachments/assets/75361fcc-efe5-4400-9875-8afdfd36e5b7" />
<img width="531" height="524" alt="Screenshot 2025-10-19 222643" src="https://github.com/user-attachments/assets/d032c2fc-0333-48bf-bd38-20bba92a0d82" />
<img width="473" height="491" alt="Screenshot 2025-10-19 222704" src="https://github.com/user-attachments/assets/2b208d70-0be5-4593-aca0-ab8ff382a3ce" />
