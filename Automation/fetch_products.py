import requests
import json

# List of product IDs to retrieve
product_ids = [
    'recZkNf2kwmdBcqd0',
    'recEHmzvupvT8ZONH',
    'rec5NBwZ5zCD9nfF0',
    'recd1jIVIEChmiwhe',
    'recotY5Nh00DQFdkm',
    'rec1Ntk7siEEW9ha1',
    'recNZ0koOqEmilmoz',
    'recrfxv3EwpvJwvjq',
    'recoW8ecgjtKx2Sj2',
    'recEOA6qtDag1hRbU',
    'recoAJYUCuEKxcPSr',
    'recQ0fMd8T0Vk211E',
    'rec7CjDWKRgNQtrKe',
    'recF0KpwlkF7e8kXO',
    'recs5BSVU3qQrOj4E',
    'recroK1VD8qVdMP5H',
    'rec7JInsuCEHgmaGe',
    'rec3jeKnhInKHJuz2',
    'recv2ohxljlK2FZO7',
    'recJIjREF3dlFi3sR',
    'recm7wC8TBVdU9oEL',
    'rectfNsySwAJeWDN2'
]

# Function to fetch product details from the API and return as a list
def fetch_product_details(product_id):
    url = f"https://course-api.com/react-store-single-product?id={product_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch product with ID {product_id}")
        return None

# List to store all product details
all_products = []

# Fetch details for each product ID and append to the list
for product_id in product_ids:
    product_details = fetch_product_details(product_id)
    if product_details:
        all_products.append(product_details)

# Save all products to a JSON file
with open('products_info.json', 'w') as json_file:
    json.dump(all_products, json_file, indent=4)

print("Products fetched and saved to products.json file.")
