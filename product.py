def get_product_info(product_id, name, quantity, price):
    """
    Return a formatted string containing product details.
    """
    return (
        f"Product ID:{product_id}\n"
        f"Product Name:{name}\n"
        f"Quantity:{quantity}\n"
        f"Price:{price}"
    )


# Example usage (optional)
if __name__ == "__main__":
    print(get_product_info("P001", "Laptop", 5, 1200))