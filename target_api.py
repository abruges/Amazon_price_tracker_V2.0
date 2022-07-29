import requests
from controls import sheets_link

response = requests.get(sheets_link)
data = response.json()

count = 1
target_products = []

for key, value in data.items():
    data_rows = value

for row in data_rows:
    if row.get("status") and row['status'] == 'ON':
        if len(row['productLink']) > 5 and isinstance(row['targetPrice'], int):
            x = {"link": row['productLink'], "target_price": row['targetPrice']}
            target_products.append(x)
