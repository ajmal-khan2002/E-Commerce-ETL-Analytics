# E-Commerce-Analytics-Dashboar

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
```bash
git clone https://github.com/<your-username>/E-Commerce-Analytics-Dashboard.git
