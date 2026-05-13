import requests
import json

all_products_url = "https://fakeapi.net/products"


all_products = requests.get(all_products_url)
all_products_json = all_products.json()
all_products_formatted = json.dumps(all_products_json, indent=2)
print(all_products_formatted, "all_products_formatted")
for product in all_products_json["data"]:
    print(product["title"])


filter_params = {
    "page": 1,
    "limit": 10,
    "category": "electronics",
    "price": json.dumps({
        "min": 100,
        "max": 1000
    })
}

filtered_products = requests.get(all_products_url, params=filter_params)
filtered_products_json = filtered_products.json()
filtered_products_formatted = json.dumps(filtered_products_json, indent=2)
print(filtered_products_formatted, "filtered_products_formatted")


product_id = 1
get_detailed_product = requests.get(all_products_url + "/" + str(product_id))
get_detailed_product_json = get_detailed_product.json()
get_detailed_product_formatted = json.dumps(
    get_detailed_product_json, indent=2)
print(get_detailed_product_formatted, "get_detailed_product_formatted")
