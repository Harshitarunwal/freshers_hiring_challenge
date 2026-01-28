import csv
import json

clean_data = []
seen = set()

with open("sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        order_id = int(row[0])
        product = row[1].replace('"', '').strip()
        price = row[2].replace('$', '').strip()
        country = row[3].strip()

        price_usd = float(price)
        price_inr = price_usd * 83

        key = (product, price_usd)
        if key in seen:
            continue
        seen.add(key)

        clean_data.append({
            "order_id": order_id,
            "product": product,
            "price_inr": price_inr,
            "country": country
        })

with open("clean_sales.json", "w") as outfile:
    json.dump(clean_data, outfile, indent=4)

print("clean_sales.json file created successfully")