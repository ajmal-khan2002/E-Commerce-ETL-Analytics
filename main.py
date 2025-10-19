
# ============================================

# 🧱 Mini Project: Project : E-Commerce Analytics Dashboard (Orders, Customers, Products, Inventory, Reviews)

# ============================================

import pandas as pd


# ----------  Data Loading ----------

def load_data():

    try:

        customer = pd.read_csv('D:\DATA ENGINEER\PANDAS\E-Commerce Analytics Dashboard project/customers.csv')
        
        order = pd.read_csv('D:\DATA ENGINEER\PANDAS\E-Commerce Analytics Dashboard project/orders.csv')

        product = pd.read_csv('D:\DATA ENGINEER\PANDAS\E-Commerce Analytics Dashboard project/products.csv')

        review = pd.read_csv('D:\DATA ENGINEER\PANDAS\E-Commerce Analytics Dashboard project/reviews.csv')

        suppliers = pd.read_csv('D:\DATA ENGINEER\PANDAS\E-Commerce Analytics Dashboard project/suppliers.csv')

        print('Data loaded successfully')

        return customer,order,product,review,suppliers
    
    except FileNotFoundError:

        print('Error : File Not Found!')



#  ---------- Data Inspection  ----------

def inspection_data(df):

    print('Missing values per column')
    print(df.isna().sum())

    print('summary of the Data Frame')
    print(df.info())
    
    print('View the first 5 rows of the Data Frame')
    print(df.head())


#  ---------- 1. Data Cleaning   ----------

def data_cleaning(df):

    print('Started : Data cleaning!\n')

    print('Duplicate Value :',df.duplicated().sum())

    df.drop_duplicates(inplace=True)

    print('Duplicate Value remove successfully\n')

    # Standardize Column to Capitalize

    df.columns.str.strip().str.capitalize()

    # Checking missing Value

    print('Check Missing Value\n')

    print(df.isna().sum())
    
    print('checking Null Values :\n',df.isnull().sum())

    print('All Data Clean & standardize successfully!\n')
    
    return df

# Convert dates to datetime type

def convert_date_col(df,date_col):
    for col in date_col:
        df[col] = pd.to_datetime(df[col])
    return df


# 2. Data Transformation

# Calculate Revenue = Quantity * Price - Discount

def calculate_revenue(df):
    df['Total_Revenue'] = df['Quantity'] * df['Price'] - df['Discount']
    return df


# Calculate Customer Lifetime Value (CLV)

def customer_info(customer,order):
    customer_details = pd.merge(left=customer,right=order,on='CustomerID',how='inner')
    return customer_details


def calculate_clv(df):
    
    Total_Revenue_per_Customer = df.groupby('CustomerID')['Total_Revenue'].sum()

    return Total_Revenue_per_Customer


# Aggregate monthly sales by product, category, and supplier

def add_order_details(order,product,supplier):
    order_del = pd.merge(left=order,right=product,on='ProductID',how='inner')
    order_details = pd.merge(left=order_del,right=supplier,on='SupplierID',how='inner')
    return order_details

def calculate_monthly_sales(df):
    df['Month'] =df['OrderDate'].dt.to_period('M')
    monthly_sales = df.groupby(['Month','ProductName','Category','SupplierName'],as_index=False)['Total_Revenue'].sum().sort_values(by='Total_Revenue',ascending=False)
    return monthly_sales


# Calculate average product rating and number of reviews

def check_review(review,order,product):
    add_order = pd.merge(left=order,right=product,on='ProductID',how='inner')
    add_review =pd.merge(left=add_order,right=review,on='ProductID',how='inner')
    return add_review


def calculate_avg_rating(df):
    avg_rating = df['Rating'].mean()

    return avg_rating

def calculate_num_of_review(df):
    review_count = df.groupby('ProductID')['Comment'].count()
    return review_count
    

# Merge orders with customers → find top customers by revenue

def find_top_cust(df):
    top_customer = df.groupby('CustomerID', as_index=False)['Total_Revenue'].sum().sort_values(by='Total_Revenue',ascending=False)
    return top_customer


# Merge orders with products → category-level analysis

#     Which categories bring in the most revenue?


def add_order_product(order,product):
    order_dels = pd.merge(left=order,right=product,on='ProductID',how='inner')

    return order_dels

def categories_revenue(df):
    high_revenue = df.groupby('Category')['Total_Revenue'].sum()
    return high_revenue

# Which subcategories are most popular (highest units sold)?

def sub_categories_revenue(df):
    sub_high_revenue =df.groupby('SubCategory')['ProductID'].sum()
    return sub_high_revenue

# How does revenue trend over months/quarters per category?


#    Which category has the highest average order value?

def avg_categories_revenue(df):
    # Calculate average revenue per category
    avg_revenue = df.groupby('Category')['Total_Revenue'].mean()
    
    # Find the category with the highest average revenue
    highest_category = avg_revenue.idxmax()
    highest_value = avg_revenue.max()
    
    return highest_category, highest_value


#  How does revenue trend over months/quarters per category?

#       Track revenue over time (by month or quarter).

def extract_mon_quart(df):
    df['Month'] =df['OrderDate'].dt.to_period('M')
    df['Quarter'] =df['OrderDate'].dt.to_period('Q')
    df['Weekday'] =df['OrderDate'].dt.day_name()
    return df

def track_revenue(df):

    track_revenue_by_month = df.groupby(['Month','Category'],as_index=False)['Total_Revenue'].sum()

    track_revenue_by_quarter = df.groupby(['Quarter','Category'],as_index=False)['Total_Revenue'].sum()

    return track_revenue_by_month,track_revenue_by_quarter


# Merge products with suppliers → analyze supplier performance

def add_product_supplier(product,supplier,order):
    product_details = pd.merge(left=product,right=supplier,on='SupplierID',how='inner')
    product_details_order =pd.merge(left=product_details,right=order,on='ProductID',how='inner')
    return product_details_order


# Total revenue generated by their products

def total_revenue_by_product(df):
    total_revenue = df.groupby(['ProductID','ProductName'],as_index=False)['Total_Revenue'].sum().sort_values(by='Total_Revenue',ascending=False)
    return total_revenue

 # Number of products they supply

def check_product_they_supply(df):
    check_product =df.groupby('SupplierID')['ProductID'].nunique()
    # Use .nunique() if each product ID appears once per supplier,
    return check_product

# Average product price

def check_avg_product_price(df):
    avg_product = df.groupby('SupplierID')['UnitPrice'].mean()
    return avg_product


# Average product rating

def check_avg_product_rating(df):
    avg_rating =df.groupby(['ProductID','ProductName'],as_index=False)['Rating'].mean()
    return avg_rating

# Count of orders or units sold (if linked with orders too)

# Total Units Sold per Supplier

def check_total_unit_sold(df):
    supplier_stats = (df.groupby('SupplierID').agg(Total_Units=('Quantity','sum'),Unique_Orders=('OrderID','nunique')).reset_index().sort_values('Total_Units', ascending=False))
    return supplier_stats

    
# Merge orders with reviews → understand product performance

#       Find top-rated products by revenue
#       → high sales + high ratings

def check_top_rated_by_rev(df):
    high_sales = df.groupby('ProductID',as_index=False).agg({'Total_Revenue':'sum','Rating':'mean'}).sort_values(by='Rating',ascending=False)
    return high_sales



#  Identify low-rated but high-sales products
#       → products that sell well but customers dislike

def check_low_rated(df):
    low_rated =df.groupby('ProductID',as_index=False).agg({'Total_Revenue':'sum','Rating':'mean'}).sort_values(by=['Rating','Total_Revenue'],ascending=[True,False])
    return low_rated

# Average rating per category/product
#       helps in supplier or product quality evaluation


def check_avg_rating_category(df):
    avg_rate = (
        df.groupby(['Category', 'ProductName'], as_index=False)['Rating']
        .mean()
        .rename(columns={'Rating': 'Avg_Rating'})
        .round(2)
        .sort_values(by='Avg_Rating', ascending=False)
    )
    return avg_rate


# 4. Advanced Pandas Operations

# Pivot tables: monthly revenue per product category

def check_monthly_rev_per_product(df):
    check_monthly_revenue = df.groupby(['ProductID','Category','Month'],as_index=False)['Total_Revenue'].sum()
    pivot_table = check_monthly_revenue.pivot_table(index='ProductID',columns='Category',values='Total_Revenue',aggfunc='sum',fill_value=0)
    return pivot_table


# GroupBy + Aggregation: total revenue per customer, monthly revenue, top categories

def total_rev_per_cust(df):
     # total revenue per customer
    cust_rev = df.groupby('CustomerID')['Total_Revenue'].sum().reset_index()

# monthly revenue
    month_rev = df.groupby('Month')['Total_Revenue'].sum().reset_index()

# top categories
    top_cat = df.groupby('Category',as_index=False)['Total_Revenue'].sum().sort_values(by='Total_Revenue', ascending=False)

    return cust_rev,month_rev,top_cat

# MultiIndexing: hierarchical view of category → subcategory → product

def hirarchical_view_category(df):
    hierarchical_view = df.set_index(['Category', 'SubCategory', 'ProductID'])[['ProductName']]
    
    return hierarchical_view


# 6. Bonus Analytics

# Identify top 10 customers by revenue

def check_top_10_cust_by_revenue(df):
    top_cust = df.groupby('CustomerID',as_index=False)['Total_Revenue'].sum().sort_values(by='Total_Revenue',ascending=False)
    return top_cust.head(10)


# Identify top 10 products by review score

def check_top_10_prod_review(df):
    max_review = df.groupby(['ProductName','ProductID']).agg({'Rating':'mean',}).sort_values(by='Rating',ascending=False)

    return max_review.head(10)


# Find suppliers with consistently low stock or poor ratings


def check_low_stock_and_low_rating(df):
    low_rating = df.groupby('SupplierName',as_index=False).agg({'StockQuantity':'mean','Rating':'mean'})
    
    low_supplier = low_rating[(low_rating['StockQuantity']<50)&(low_rating['Rating']<3.5)]
    return low_supplier.sort_values(by='Rating',ascending=False)



# Filtering with conditions: high-value customers, products with low stock

def check_high_value_cust(df):
    high_value = df.groupby('CustomerID',as_index=False).agg({'Total_Revenue':'sum','StockQuantity':'mean'})
    high_value_with_low_stock = high_value[(high_value['StockQuantity']<50)&(high_value['Total_Revenue']>=15000)]
    return high_value_with_low_stock.sort_values(by='StockQuantity',ascending=False)
                  
    
# Datetime operations: find seasonality in orders, weekend vs weekday sales



def check_monthly_order(df):
    monthly_order = df.groupby('Month',as_index=False).agg({'Total_Revenue':'sum','OrderID':'count'}).sort_values(by='Month',ascending=True)

    return monthly_order


def check_quarter_order(df):
    
    quarter_order = df.groupby('Quarter',as_index=False).agg({'Total_Revenue':'sum','OrderID':'count'}).sort_values(by='Quarter',ascending=True)

    return quarter_order

def check_weekend_order(df):
     df["Is_Weekday"] = df['Weekday'].isin(['Monday','Tuesday','Wednesday','Thursday','Friday'])
     weekday_order = df.groupby('Is_Weekday',as_index=False).agg({'Total_Revenue':'sum','OrderID':'count'})  
     return weekday_order


# 5. Tricky / Real-World Scenarios

# Some customers have multiple emails; only use the most recent

def check_most_recent_email(df):
    sorted  = df.sort_values(by='JoinDate',ascending=False)

    most_recent_email = sorted.drop_duplicates(subset='CustomerID', keep='first')
    return most_recent_email


# Some orders are cancelled or returned—exclude or adjust revenue accordingly


def check_calculate_revenue_without_ret_cancel(df):

    df['Total_Revenue_No_Cancel_Return'] = df.apply(
        lambda x: 0 if x['OrderStatus'] in ['Cancelled', 'Returned'] else x['Total_Revenue'],
        axis=1
    )
    return df
            

# -----------------------------  Generates a dashboard summary. ----------------------------------------

def generate_dashboard(order):
    
    # KPIs 
    kpi = {
        'Total Order ' :len(order),
        'Total Customer' :order['CustomerID'].nunique(),
        'Total Revenue' :order['Total_Revenue'].sum(),
        'Net Revenue (No Cancel/Return)' :order['Total_Revenue_No_Cancel_Return'].sum(),
        'Cancelled/Returned Orders' : order[order['OrderStatus'].isin(['Cancelled','Returned'])].shape[0],
        'Avg Order Value':round(order['Total_Revenue_No_Cancel_Return'].mean(),2)

    }
    kpi_df = pd.DataFrame(list(kpi.items()), columns=['Metric', 'Value'])

    
    
    # Category-level summary

    category_summary = (
        order.groupby('Category', as_index=False)
                .agg({
                    'OrderID': 'count',
                    'Total_Revenue': 'sum',
                    'Total_Revenue_No_Cancel_Return': 'sum'
                })
                .rename(columns={'OrderID': 'Total_Orders'})
    )
    category_summary['% Revenue Lost'] = (
        (1 - category_summary['Total_Revenue_No_Cancel_Return'] / category_summary['Total_Revenue']) * 100
    ).round(2)


     # Monthly revenue trend 

    monthly_summary = (
        order.groupby('Month',as_index=False)
             .agg({
                 'Total_Revenue':'sum',
                 'Total_Revenue_No_Cancel_Return':'sum'
        
             })
    )
    
     # ---  Top 5 products by revenue ---

    top_products =(
         order.groupby(['ProductID','ProductName'],as_index=False)
              .agg({'Total_Revenue':'sum'})
              .sort_values(by='Total_Revenue',ascending=False)
              .head(5)
     )
    
     # --- Top 5 customers by revenue ---

    top_customer=(
        order.groupby('CustomerID',as_index=False)
             .agg({'Total_Revenue':'sum'})   
             .sort_values(by='Total_Revenue',ascending=False)
             .head(5)      
     )


    # --- Average rating per category ---


    avg_rating_category =(
        order.groupby('Category',as_index=False)['Rating']
             .mean()
             .round(2)
             .rename(columns={'Rating':'Avg_Rating'})
             .sort_values(by='Avg_Rating',ascending=False)
    )
    # ---  Print dashboard ---

    print("DASHBOARD SUMMARY\n")

    print(kpi_df, "\n")

    print("CATEGORY PERFORMANCE\n")
    print(category_summary, "\n")

    print("MONTHLY TREND\n")
    print(monthly_summary, "\n")

    print('TOP 5 PRODUCTS BY REVENUE \n')
    print(top_products[['ProductName','Total_Revenue']], "\n")

    print("👑 TOP 5 CUSTOMERS BY REVENUE\n")
    print(top_customer, "\n")

    print("⭐ AVERAGE RATING PER CATEGORY\n")
    print(avg_rating_category, "\n")

    
    # ---  Return all tables ---
    return {
        'kpi':kpi_df,
        'category': category_summary,
        'monthly':monthly_summary,
        'top_products':top_products,
        'top_customers': top_customer,
        'avg_rating_category': avg_rating_category
    }

    
    
# ---------- . Main Pipeline ----------

def main():
    customer,order,product,review,suppliers = load_data()

    # Only one safety check

    if any(df is None for df in [customer, order, product, review, suppliers]):

        print(" Pipeline stopped — missing data files.")
        return

    # Run pipeline in order

    inspection_data(customer)

    # ----------------- Data cleaning -----------------
   
    customer = data_cleaning(customer)
    order = data_cleaning(order)
    product = data_cleaning(product)
    review = data_cleaning(review)
    suppliers = data_cleaning(suppliers)
    
#   ------------- Convert dates to datetime type -----------------    

    customer = convert_date_col(customer,['JoinDate'])
    print(customer['JoinDate'].dtype)

    order = convert_date_col(order,['OrderDate'])
    print(order['OrderDate'].dtype)
 
    review = convert_date_col(review,['ReviewDate'])
    print(review['ReviewDate'].dtype)


    # -------------- Data Transformation ----------------------------------

    order = calculate_revenue(order)
    print(order)

    customer_details = customer_info(customer,order)

    print(f"Customer Details \n {customer_details}")

    Total_Revenue_per_Cust= calculate_clv(customer_details)

    print(Total_Revenue_per_Cust)


    order_details = add_order_details(order,product,suppliers)

    most_sales_product =calculate_monthly_sales(order_details)

    print(most_sales_product)

    avg_product_rating = check_review(order,product,review)

    avg_rating = calculate_avg_rating(avg_product_rating)
    
    print('Average product rating : ',avg_rating)

    count_num_review = calculate_num_of_review(avg_product_rating)

    print('Number of Reveiw on Product : ',count_num_review)


    top_cust_by_revenue = find_top_cust(customer_details)

    print(top_cust_by_revenue)


    #---------- Merge orders with products → category-level analysis ----------

    merge_order_product = add_order_product(order,product)

    #  add total Revenue colmun

    merge_order_product = calculate_revenue(merge_order_product)

    print(merge_order_product.info())

    # Which categories bring in the most revenue?


    categories_most_revenue = categories_revenue(merge_order_product)

    print(categories_most_revenue)

    # Which subcategories are most popular (highest units sold)?


    sub_categories_rev_most = sub_categories_revenue(merge_order_product)

    print(sub_categories_rev_most)

    # Which category has the highest average order value?

    highest_avg_order = avg_categories_revenue(merge_order_product)

    print(highest_avg_order)

    merge_order_product = extract_mon_quart(merge_order_product)

    track_revenue_by_categ = track_revenue(merge_order_product)

    print(track_revenue_by_categ)

    
    # Merge products with suppliers

    merge_product_with_supplier_order = add_product_supplier(product,suppliers,order)

    add_revenue_col =calculate_revenue(merge_product_with_supplier_order)
    print(merge_product_with_supplier_order.info())

    check_total_revenue_by_product = total_revenue_by_product(merge_product_with_supplier_order)
    print(check_total_revenue_by_product)


    # Number of products they supply

    check_num_product = check_product_they_supply(merge_product_with_supplier_order)
    print(check_num_product)

     # Average product price

    avg_product_price =check_avg_product_price(merge_product_with_supplier_order)
    print(avg_product_price)    

    # Average product rating

    avg_product_rating = check_avg_product_rating(merge_product_with_supplier_order)
    print(avg_product_rating)
    

    # Count of orders or units sold (if linked with orders too)

    count_order_per_unit_sold = check_total_unit_sold(merge_product_with_supplier_order)
    print(count_order_per_unit_sold)

    

    # Merge orders with reviews → understand product performance

    # Find top-rated products by revenue
    # → high sales + high ratings
    top_rated_product = check_top_rated_by_rev(merge_product_with_supplier_order)
    print(top_rated_product)

    low_rated_product = check_low_rated(merge_product_with_supplier_order)
    print(low_rated_product)

    # Average rating per category/product
    #   helps in supplier or product quality evaluation

    avg_rating_category_product = check_avg_rating_category(merge_product_with_supplier_order)

    print(avg_rating_category_product)

    
    #  Pivot tables: monthly revenue per product category

    monthly_rev_per_product = check_monthly_rev_per_product(merge_order_product)
    print(monthly_rev_per_product)
   
    # GroupBy + Aggregation: total revenue per customer, monthly revenue, top categories

    total_revene_cust = total_rev_per_cust(merge_order_product)
    print(total_revene_cust)

    # MultiIndexing: hierarchical view of category → subcategory → product

    hirarchical_category =hirarchical_view_category(merge_order_product)
    print(hirarchical_category)

    # Filtering with conditions: high-value customers, products with low stock

    
    # --------------------------- 6. Bonus Analytics ---------------------------

    # Identify top 10 customers by revenue

    top_10_cust_by_revenue = check_top_10_cust_by_revenue(merge_product_with_supplier_order)
    print(f' Top 10 Customer by Revunew\n {top_10_cust_by_revenue}')

    # Identify top 10 products by review score

    top_10_prod_review = check_top_10_prod_review(merge_product_with_supplier_order)
    print(f'Top 10 products by review score \n {top_10_prod_review}')

    # Find suppliers with consistently low stock or poor ratings

    low_stock_and_low_rating = check_low_stock_and_low_rating(merge_product_with_supplier_order)
    print(f' suppliers with consistently low stock or poor ratings \n {low_stock_and_low_rating}')

    

    # Filtering with conditions: high-value customers, products with low stock

    high_value_cust = check_high_value_cust(merge_product_with_supplier_order)
    print(f'High-value customers \n{high_value_cust}')


    # Datetime operations: find seasonality in orders, weekend vs weekday sales


    merge_product_with_supplier_order = extract_mon_quart(merge_product_with_supplier_order)
    

    monthly_order = check_monthly_order(merge_product_with_supplier_order)
    print(f'Monthly Order : \n {monthly_order}')

    quarterly_order = check_quarter_order(merge_product_with_supplier_order)
    print(f'Quarterly Order : \n {quarterly_order}')

    weekday_order = check_weekend_order(merge_product_with_supplier_order)
    print(f'Weekday Order :\n {weekday_order}')

    # --------------------   5. Tricky / Real-World Scenarios ------------------------

    # print(f"Customer Details \n {customer_details}")

    # Some customers have multiple emails; only use the most recent

    cust_email = check_most_recent_email(customer_details)

    print(f"Most Recent Email Used by Customer: \n{cust_email}")
    

    # Some orders are cancelled or returned—exclude or adjust revenue accordingly

    
    merge_product_with_supplier_order = check_calculate_revenue_without_ret_cancel(merge_product_with_supplier_order)
    print(f"Total Revenue calculate Without Cancelled or Returned Ordered \n :{merge_product_with_supplier_order}")

    
    

   # ------------------- Generate advanced dashboard ---------------------

    dashboard_tables = generate_dashboard(merge_product_with_supplier_order)


    # Export to Excel

    with pd.ExcelWriter('Ecommerce_Dashboard.xlsx') as writer:
        dashboard_tables['kpi'].to_excel(writer,sheet_name='KPIs',index=False)
        dashboard_tables['category'].to_excel(writer, sheet_name='Category_Summary', index=False)
        dashboard_tables['monthly'].to_excel(writer, sheet_name='Monthly_Trend', index=False)
        dashboard_tables['top_products'].to_excel(writer,sheet_name ='Top_Products',index=False)
        dashboard_tables['top_customers'].to_excel(writer, sheet_name='Top_Customers', index=False)
        dashboard_tables['avg_rating_category'].to_excel(writer, sheet_name='Avg_Rating_Category', index=False)



    # print(merge_product_with_supplier_order.info())


    





    # ---------- . Run ----------

if __name__ == "__main__":
    main()

