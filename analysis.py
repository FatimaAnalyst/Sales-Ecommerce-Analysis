# =====================================================
# Sales & E-commerce Analysis
# Tools: Python, Pandas, Matplotlib
# Put this file in the SAME folder as sales_ecommerce_dataset.csv
# Run with: python analysis_full.py
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------
# STEP 1: Load the data
# -----------------------------------------------------
df = pd.read_csv("sales_ecommerce_dataset.csv")

# -----------------------------------------------------
# STEP 2: Look at the data
# -----------------------------------------------------
print(df.head())       # first 5 rows
print(df.shape)        # (rows, columns) -> (2000, 17)
print(df.columns)      # all column names

# -----------------------------------------------------
# STEP 3: Check data quality
# -----------------------------------------------------
print(df.info())                # data types
print(df.isnull().sum())        # missing values per column
print(df.duplicated().sum())    # number of duplicate rows

# -----------------------------------------------------
# STEP 4: Fix the date + calculate main numbers
# -----------------------------------------------------
df["order_date"] = pd.to_datetime(df["order_date"])   # text -> real date

total_revenue = df["net_amount"].sum()
total_profit = df["profit"].sum()
total_orders = df["order_id"].count()
avg_order_value = df["net_amount"].mean()
profit_margin = total_profit / total_revenue * 100

print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Order Value:", avg_order_value)
print("Profit Margin %:", profit_margin)

# -----------------------------------------------------
# STEP 5: Group the data (like GROUP BY in SQL)
# -----------------------------------------------------
revenue_by_region = df.groupby("region")["net_amount"].sum().sort_values(ascending=False)
profit_by_category = df.groupby("category")["profit"].sum().sort_values(ascending=False)
top_products = df.groupby("product")["net_amount"].sum().sort_values(ascending=False)

print(revenue_by_region)
print(profit_by_category)
print(top_products)

# -----------------------------------------------------
# STEP 6: Return rate
# -----------------------------------------------------
return_rate = df["is_returned"].mean() * 100
print("Return Rate %:", return_rate)

# -----------------------------------------------------
# STEP 7: Monthly revenue trend
# -----------------------------------------------------
df["month"] = df["order_date"].dt.strftime("%Y-%m")
monthly_revenue = df.groupby("month")["net_amount"].sum()
print(monthly_revenue)

# -----------------------------------------------------
# STEP 8: Segments, category returns, payment methods
# -----------------------------------------------------
segment_revenue = df.groupby("customer_segment")["net_amount"].sum().sort_values(ascending=False)
return_by_category = (df.groupby("category")["is_returned"].mean() * 100).sort_values(ascending=False)
payment_orders = df["payment_method"].value_counts()

print(segment_revenue)
print(return_by_category)
print(payment_orders)

# -----------------------------------------------------
# STEP 9: Charts (all saved first, then shown together)
# -----------------------------------------------------

# Chart 1: Revenue by region
plt.figure()
revenue_by_region.plot(kind="bar", color="teal")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("revenue_by_region.png")

# Chart 2: Profit by category
plt.figure()
profit_by_category.plot(kind="bar", color="orange")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit (INR)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("profit_by_category.png")

# Chart 3: Monthly revenue trend
plt.figure()
monthly_revenue.plot(kind="line", marker="o", color="green")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_revenue.png")

# Show all 3 charts at once (each opens in its own window)
plt.show()