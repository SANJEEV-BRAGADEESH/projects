import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
try:
    order_items = pd.read_csv(r"C:\Users\sanje\Downloads\archive\blinkit_order_items.csv")
    customers = pd.read_csv(r"C:\Users\sanje\Downloads\archive\blinkit_customers.csv")
    inventory = pd.read_csv(r"C:\Users\sanje\Downloads\archive\blinkit_inventoryNew.csv")
    orders = pd.read_csv(r"C:\Users\sanje\Downloads\archive\blinkit_orders.csv")
    delivery = pd.read_csv(r"C:\Users\sanje\Downloads\archive\blinkit_delivery_performance.csv")
    marketing = pd.read_csv(r"C:\Users\sanje\Downloads\archive\blinkit_marketing_performance.csv")
    feedback = pd.read_csv(r"C:\Users\sanje\Downloads\archive\blinkit_customer_feedback.csv")
    products = pd.read_csv(r"C:\Users\sanje\Downloads\archive\blinkit_products.csv")
except Exception as e:
    print("Error loading files:", e)

# Setup
sns.set(style="whitegrid")

# 1. Orders Over Time
if 'order_date' in orders.columns:
    orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
    monthly_orders = orders.groupby(orders['order_date'].dt.to_period('M')).size()
    monthly_orders.plot(kind='bar', figsize=(12, 6), title='Monthly Orders')
    plt.xlabel('Month')
    plt.ylabel('Number of Orders')
    plt.show()

# 2. Top Selling Products
if 'product_id' in order_items.columns:
    top = order_items['product_id'].value_counts().head(10)
    top_df = top.reset_index()
    top_df.columns = ['product_id', 'quantity']
    top_df = top_df.merge(products, on='product_id', how='left')
    plt.figure(figsize=(12,6))
    sns.barplot(x=top_df['product_name'], y=top_df['quantity'])
    plt.xticks(rotation=45)
    plt.title('Top 10 Best-Selling Products')
    plt.xlabel('Product Name')
    plt.ylabel('Units Sold')
    plt.show()

# 3. Delivery Time Distribution
if 'delivery_time_minutes' in delivery.columns:
    plt.figure(figsize=(10,6))
    sns.histplot(delivery['delivery_time_minutes'].dropna(), bins=30, kde=True)
    plt.title('Delivery Time Distribution')
    plt.xlabel('Minutes')
    plt.ylabel('Frequency')
    plt.show()

# 4. Customer Feedback Ratings
if 'rating' in feedback.columns:
    plt.figure(figsize=(8,5))
    sns.countplot(data=feedback, x='rating', hue='rating', palette='coolwarm', legend=False)
    plt.title('Customer Feedback Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.show()

