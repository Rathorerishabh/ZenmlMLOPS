import pandas as pd

# Define file paths
order_items_path = r'C:\Users\risha\Desktop\MLOps\data\archive\olist_order_items_dataset.csv'
order_reviews_path = r'C:\Users\risha\Desktop\MLOps\data\archive\olist_order_reviews_dataset.csv'
orders_path = r'C:\Users\risha\Desktop\MLOps\data\archive\olist_orders_dataset.csv'
customers_path = r'C:\Users\risha\Desktop\MLOps\data\archive\olist_customers_dataset.csv'

# Load the datasets
order_items_df = pd.read_csv(order_items_path)
order_reviews_df = pd.read_csv(order_reviews_path)
orders_df = pd.read_csv(orders_path)
customers_df = pd.read_csv(customers_path)

# Step 1: Join `order_items_df` and `order_reviews_df` on `order_id`
order_items_reviews = pd.merge(order_items_df, order_reviews_df, on='order_id', how='inner')

# Step 2: Join the result with `orders_df` on `order_id`
orders_combined = pd.merge(order_items_reviews, orders_df, on='order_id', how='inner')

# Step 3: Join the result with `customers_df` on `customer_id`
final_combined = pd.merge(orders_combined, customers_df, on='customer_id', how='inner')

# Save the final joined data to a new CSV file
output_path = r'C:\Users\risha\Desktop\MLOps\data\combined_orders_customers.csv'
final_combined.to_csv(output_path, index=False)

print("Successfully joined all datasets and saved the combined data!")
