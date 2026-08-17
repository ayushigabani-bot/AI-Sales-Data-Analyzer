import pandas as pd
import numpy as np 

def clean_sales_data(file_path):
    print("START DATA CLEANING")

# read .csv data
df=pd.read_csv("data/sales_data.csv")
initial_rows=df.shape[0]
initial_columns=df.shape[1]
print(f"The Dataset Contain {initial_rows} Rows and {initial_columns} Columns.")

# remove the duplicate 
df.drop_duplicates(inplace=True)
duplicate_count=initial_rows - df.shape[0]
print(f" Removed {duplicate_count} duplicat ROWS ")

# STANDARDIZE COLUMN NAMES (Lowercase & Strip Spaces)
df.columns=df.columns.str.strip().str.lower().str.replace(' ','_')
print(df.columns)

# identify critical columns
id_col='product_id' if 'product_id' in df.columns else df.columns[0]
date_col='sale_date' if 'sale_date' in df.columns else 'date'
sales_col='sales_amount' if 'sales_amount' in df.columns else 'sales'
qty_col='quantity_sold' if 'quantity_sold' in df.columns else 'quantity'
region_col='region' if 'region' in df.columns else 'sales_channel'
rep_col='sales_rep' if 'sales_rep' in df.columns else 'region_and_sales_rep'

# remove the rows of missing id
before_id_drop=df.shape[0]
df.dropna(subset=[id_col],inplace=True)
print(f"Removed {before_id_drop-df.shape[0]} rows with missing id ")

# using numpy and pandas convert sales and quantity into numric and replace the missing values with any specific number.
if sales_col in df.columns:
    df[sales_col]=pd.to_numeric(df[sales_col],errors='coerce')

    df[sales_col]=np.where(df[sales_col].isna(),0,df[sales_col])
  

if qty_col in df.columns:
    df[qty_col]=pd.to_numeric(df[qty_col],errors='coerce')

    df[qty_col]=np.where(df[qty_col].isna(),1,df[qty_col])

print("Missing is handle using numpy")

if date_col in df.columns:
    df[date_col]=pd.to_datetime(df[date_col],errors='coerce')
    # drop rows with corrupt dates
    df.dropna(subset=[date_col],inplace=True)

    # Create a Year-Month column for easier aggregation later
    df['year_month']=df[date_col].dt.to_period('M')
    print("Date column standarized ")

#Remove negative values in Sales and Quantity that don't make sense.
if sales_col in df.columns and qty_col in df.columns:
    before_filter=df.shape[0]
    df=df[(df[sales_col]>=0) & (df[qty_col]>=0)]
    print(f"after_filter {before_filter-df.shape[0]} " )

final_rows=df.shape[0]
print(f"Total row remain after Data Cleaning compelete {final_rows} Valid Record {(final_rows/initial_rows)*100:.1f}%") 
print(df.head())
print("\n")



print("****Analyzing Regional Revenue Performance...*****")

region_sales=df.groupby(region_col, as_index=False)[sales_col].sum()
region_sales=region_sales.sort_values(by=sales_col,ascending=False)
total_sales=region_sales[sales_col].sum()
region_sales['contribution%']=(region_sales[sales_col]/total_sales)*100
print(region_sales)
print("\n")


print("*****Analyzing Sales Representative Performance...*****")

sales_rep=df.groupby(rep_col , as_index=False ).agg(Total_Sales=(sales_col,'sum'),Deal_closed=(sales_col,'count'),Avg_deal=(sales_col,'mean'))

sales_rep=sales_rep.sort_values(by='Total_Sales', ascending=False).head(3) #Top 3 sales_rep
print(sales_rep)
print("\n")

print("*****Analyzing Product Category Performance...*****")

product_col=df.groupby('product_category',as_index=False).agg(Total_Sales=(sales_col,'sum'),Total_Quantity=('quantity_sold','sum'),Avg_Sale=(sales_col,'mean'))
product_col=product_col.sort_values(by='Total_Sales',ascending=False)
print(product_col)

print("------------------ PRODUCT CATEGORY INSIGHTS-----------------------------")

print(f"1. Best Performing Category   :           {product_col.iloc[0]['product_category']}") #iloc return index location 
print(f"2. Highest Revenue            :           {product_col.iloc[0]['Total_Sales']}")
print(f"3. Lowest Performing Category :           {product_col.iloc[-1]['product_category']}")
print(f"4. Lowest Revenue             :           {product_col.iloc[-1]['Total_Sales']}")
print(f"5. Revenue Difference         :           {(product_col.iloc[0]['Total_Sales']-product_col.iloc[-1]['Total_Sales']):.2f}") 
print(f"6. Highest Quantity sold      :           {product_col.loc[product_col['Total_Quantity'].idxmax(),'product_category']}({product_col['Total_Quantity'].max()})")
print(f"7.Lowest Quantity Sold        :           {product_col.loc[product_col['Total_Quantity'].idxmin(),'product_category']}({product_col['Total_Quantity'].min()})")
print(f"8.Higest Average Sale         :           {product_col.loc[product_col['Avg_Sale'].idxmax(),'product_category']}({product_col['Avg_Sale'].max():.2f})")
print("\n")

print("*****Customer Type Analysis...*****")
customer_type=df.groupby('customer_type',as_index=False).agg(total_sales=(sales_col,'sum'),Total_Quantity=('quantity_sold','sum'),Avg_Sale=(sales_col,'mean'))
customer_type=customer_type.sort_values(by='total_sales',ascending=False)
print(customer_type)
total_sales=customer_type['total_sales'].sum()
customer_type['contribution%']=(customer_type['total_sales']/total_sales)*100
print(customer_type)

# Which customer type generates the highest total sales revenue? 
print(f"1.Customer Highest Total Sales : {customer_type.iloc[0]['customer_type']}")
# Which customer type purchases the highest total quantity?
print(f"2.Highest Quantity Customer : {customer_type.loc[customer_type['Total_Quantity'].idxmax(),'customer_type']}({customer_type['Total_Quantity'].max()} units)")
#  Highest Average Sale remains.
print(f"3. Highest Average Sale : {customer_type.loc[customer_type['Avg_Sale'].idxmax(), 'customer_type']} ({customer_type['Avg_Sale'].max():,.2f})")
print("\n")

print("***** Sales Channel Analysis... *****")

sales_channel = df.groupby('sales_channel', as_index=False).agg(
    Total_Sales=(sales_col, 'sum'),
    Total_Quantity=('quantity_sold', 'sum'),
    Avg_Sale=(sales_col, 'mean')
)

sales_channel = sales_channel.sort_values(by='Total_Sales', ascending=False)
print(sales_channel)

total_sales = sales_channel['Total_Sales'].sum()

sales_channel['contribution%'] = (
    sales_channel['Total_Sales'] / total_sales
) * 100

print(sales_channel)

print("------------------ SALES CHANNEL INSIGHTS-----------------------------")

# Q1: Highest Total Sales 
print(f"1. Best Performing Channel : {sales_channel.iloc[0]['sales_channel']}")
print(f"2. Highest Revenue         : ₹{sales_channel.iloc[0]['Total_Sales']:,.2f}")

# Q2: Highest Quantity Sold 
print(f"3. Highest Quantity Channel: {sales_channel.loc[sales_channel['Total_Quantity'].idxmax(), 'sales_channel']}")
print(f"   Quantity Sold           : {sales_channel['Total_Quantity'].max()}")

# Q3: Highest Average Sale 
print(f"4. Highest Average Sale   : {sales_channel.loc[sales_channel['Avg_Sale'].idxmax(), 'sales_channel']}")
print(f"   Average Sale            : ₹{sales_channel['Avg_Sale'].max():,.2f}")
print("\n")

print("***** Payment Method Analysis... *****")

payment_method = df.groupby('payment_method', as_index=False).agg(
    Total_Sales=(sales_col, 'sum'),
    Total_Quantity=('quantity_sold', 'sum'),
    Avg_Sale=(sales_col, 'mean')
)

payment_method = payment_method.sort_values(by='Total_Sales', ascending=False)
print(payment_method)

total_sales = payment_method['Total_Sales'].sum()

payment_method['contribution%'] = (
    payment_method['Total_Sales'] / total_sales
) * 100

print(payment_method)

print("------------------ PAYMENT METHOD INSIGHTS-----------------------------")

# Q1: Highest Total Sales 
print(f"1. Best Payment Method : {payment_method.iloc[0]['payment_method']}")
print(f"2. Highest Revenue     : ₹{payment_method.iloc[0]['Total_Sales']:,.2f}")

# Q2: Highest Quantity Sold 
print(f"3. Highest Quantity Payment Method : {payment_method.loc[payment_method['Total_Quantity'].idxmax(), 'payment_method']}")
print(f"   Quantity Sold                    : {payment_method['Total_Quantity'].max()}")

# Q3: Highest Average Sale 
print(f"4. Highest Average Sale Payment Method : {payment_method.loc[payment_method['Avg_Sale'].idxmax(), 'payment_method']}")
print(f"   Average Sale                        : ₹{payment_method['Avg_Sale'].max():,.2f}")

print("\n")

print("*****  Discount Strategy Analysis... *****")

if 'discount' in df.columns:

    df['has_discount'] = np.where(  df['discount'] > 0, 'Discounted Order','Full Price Order')

    discount_analysis = df.groupby('has_discount', as_index=False).agg(
        Total_Revenue=(sales_col, 'sum'),
        Average_Order_Value=(sales_col, 'mean'),
        Total_Units_Sold=('quantity_sold', 'sum')
    )

    discount_analysis = discount_analysis.sort_values( by='Total_Revenue',ascending=False
    )

    total_revenue = discount_analysis['Total_Revenue'].sum()

    discount_analysis['contribution%'] = ( discount_analysis['Total_Revenue'] / total_revenue ) * 100

    print(discount_analysis)

else:
    print("Discount column not found in dataset schema.")
print("\n")    

print("*****  Overall Sales Summary... *****")
total_sales = df[sales_col].sum()
total_quantity = df['quantity_sold'].sum()
avg_transaction = df[sales_col].mean()

print(f"1. Total Accumulated Revenue : ₹{total_sales:,.2f}")
print(f"2. Total Physical Units Sold : {total_quantity:,} units")
print(f"3. Average Transaction Value : ₹{avg_transaction:,.2f}")

# AUTOMATED EXCEL DASHBOARD GENERATION
output_excel_file="Sales_Data_Pipeline_Dashboard.xlsx"
print(f"Generating Structured multi-tab workbook: {output_excel_file}")

with pd.ExcelWriter(output_excel_file,engine='openpyxl') as writer:

    region_sales.to_excel(writer,sheet_name='Regional Performance',index=False)
    sales_rep.to_excel(writer,sheet_name='sales Rep Standings', index=False)
    product_col.to_excel(writer,sheet_name='Product Category Metrics',index=False)
    customer_type.to_excel(writer,sheet_name='Customer Profiles',index=False)
    sales_channel.to_excel(writer,sheet_name='Channel Efficiency',index=False)
    payment_method.to_excel(writer,sheet_name='Payment Mode',index=False)
    if 'discount_analysis' in locals() and not discount_analysis.empty:
        discount_analysis.to_excel(writer,sheet_name='Discount Impact Analysis',index=False)

    df.head(1000).to_excel(writer,sheet_name='Cleaned Raw Sample',index=False)

print("PIPLINE COMPLETE!")

























