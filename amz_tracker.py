import requests
from bs4 import BeautifulSoup

def track_amz_product(url):
    headers = {
        "User-Agent": "Defined",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,km;q=0.5,zh-TW;q=0.4",
    }

    amz_url = url
    response = requests.get(amz_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # PROCESSING SCRAPPED INFORMATION
    info = soup.find("img", class_="a-dynamic-image")
    product_name = info["alt"]

    product_available = True
    try:
        price_raw = soup.find("span", id="tp-tool-tip-subtotal-price-value")
        price_raw1 = price_raw.text[1:]
        price_len = int(len(price_raw1) / 2)
        price = float(price_raw1[price_len:])

    except:
        product_available = False

    data = []

    if product_available:
        data.extend([product_name, price])
    else:
        data.append(product_name)

    return data