def linear_search_product(product_list, target_product):
    indices = []

    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)

    return indices

# Example usage:
products = ["apple", "banana", "apple", "orange", "grape", "apple"]
target = "apple"
result = linear_search_product(products, target)
if result:
    print(f"{target} found at indices: {result}")
else:
    print(f"{target} not found in the list.")
