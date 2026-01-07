"""
Script to create sample product price data CSV file.
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define products
products = [
    {'product_id': 'P001', 'product_name': 'Laptop Pro 15'},
    {'product_id': 'P002', 'product_name': 'Wireless Mouse'},
    {'product_id': 'P003', 'product_name': 'Mechanical Keyboard'},
    {'product_id': 'P004', 'product_name': 'USB-C Hub'},
    {'product_id': 'P005', 'product_name': 'Laptop Stand'},
]

# Define shops
shops = ['TechMart', 'ElectroWorld', 'BestBuy Electronics', 'GadgetHub', 'DigitalStore']

# Base prices for each product
base_prices = {
    'P001': 1200,  # Laptop
    'P002': 25,    # Mouse
    'P003': 80,    # Keyboard
    'P004': 35,    # USB-C Hub
    'P005': 45,    # Stand
}

# Generate data
data = []
for product in products:
    # Each product available in 3-5 random shops with varying prices
    num_shops = np.random.randint(3, 6)
    selected_shops = np.random.choice(shops, size=num_shops, replace=False)
    
    base_price = base_prices[product['product_id']]
    
    for shop in selected_shops:
        # Add price variation (±20%)
        price_variation = np.random.uniform(-0.2, 0.2)
        price = base_price * (1 + price_variation)
        price = round(price, 2)
        
        data.append({
            'product_id': product['product_id'],
            'product_name': product['product_name'],
            'shop_name': shop,
            'price': price
        })

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('product_prices.csv', index=False)
print(f"Sample CSV created successfully with {len(df)} records")
print(f"Products: {df['product_id'].nunique()}")
print(f"Shops: {df['shop_name'].nunique()}")


