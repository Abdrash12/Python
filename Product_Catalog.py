# Create the product catalog dictionary
product_catalog = {
    "SKU123": {
        "name": "FONE",
        "price": 19.99,
        "quantity": 50
    },
    "SKU456": {
        "name": "GANNE KA JUISE",
        "price": 34.95,
        "quantity": 25
    },
    "SKU789": {
        "name": "DAHI",
        "price": 9.99,
        "quantity": 100
    }
}

# Example SKU to search for
sku_to_find = "SKU123"

# Check if the SKU exists and retrieve price
if sku_to_find in product_catalog:
    price = product_catalog[sku_to_find]["price"]
    print(f"The price of {product_catalog[sku_to_find]['name']} is ${price}")
else:
    print("Sorry, that product SKU was not found.")
