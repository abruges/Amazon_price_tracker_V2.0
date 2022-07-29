from amz_tracker import track_amz_product
from target_api import target_products
from telegram_messenger import send_message

for item in target_products:
    amz_link = item['link']
    target_price = item['target_price']

    info = track_amz_product(amz_link)

    if len(info) > 1:
        if info[1] < target_price:
            product_name = info[0]
            good_price = str(info[1])

            short_product_name = product_name.split(',')[0]
            short_amz_link = amz_link.split('?')[0]

            send_message(f"Amazon price alert! 🚨\n{short_product_name}\nPrice: ${good_price}")
            send_message(f"Buy here: {short_amz_link}")

    else:
        send_message(f"🚨 The product: {info[0].split(',')[0]}, is no longer available")