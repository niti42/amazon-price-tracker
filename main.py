import requests
from bs4 import BeautifulSoup
from pprint import pprint
from notifications import send_email
import os
from dotenv import load_dotenv
import re
load_dotenv()
my_email = os.getenv("my_email")
password = os.getenv("password")

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,kn;q=0.8,mr;q=0.7",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

# url = "https://appbrewery.github.io/instant_pot/"
url = "https://www.amazon.com/SAMSUNG-Dust-Resistant-Powerful-Processor-Lightweight/dp/B0CCX11JT6?ref=dlx_deals_dg_dcl_B0CCX11JT6_dt_sl14_f8&th=1"

resp = requests.get(url, headers=header)
amazon_prod_page = resp.content
print(resp.status_code)

soup = BeautifulSoup(amazon_prod_page, "html.parser")


price_whole = soup.find("span", class_="a-price-whole").getText().strip()
price_whole = re.sub(r"\,", '', price_whole)

price_frac_tag = soup.find("span", class_="a-price-fraction")
price_frac = price_frac_tag.getText().strip() if price_frac_tag else "00"
price = float(price_whole + price_frac)
print(price)

target_price = 300  # to compare current price with. if lower, send alert

prod_title = soup.find(
    "span", id="productTitle").getText().strip()

prod_title = re.sub(r'\s+', ' ', prod_title)

currency = soup.find("span", class_="a-price-symbol").getText().strip()
print(currency)

message = f"{prod_title} is now {currency}{price}\n{url}"

print(message)
if price < target_price:
    try:
        send_email(
            subject="Low Price Alert!",
            message=message,
            to_email="radkin17@gmail.com",
            user_email=my_email,
            user_password=password
        )
    except Exception as e:
        print(f"An error occurred: {e}")
