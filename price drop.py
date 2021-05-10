from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import config

URL = 'https://www.tpstech.in/products/hp-oa04-notebook-original-battery-f3b94aa-black'
PRODUCT = 'TPS Laptop Battery'
TARGET_PRICE = 4000
account_sid = ${{ secrets.ACCOUNT_SID  }}
auth_token = ${{ secrets.AUTH_TOKEN  }}
FROM = ${{ secrets.FROM_NUM  }}
TO = ${{ secrets.TO_NUM  }}


response = requests.get(URL)
result = response.text

soup = BeautifulSoup(result, 'html.parser')
price_data = soup.find(name='span', class_='product-single__price')
price = float(price_data.get('content'))

if price <= TARGET_PRICE:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"\nPrice drop alert!! {PRODUCT} now costs {price}. Link: {URL}",
        from_=FROM,
        to=TO
    )
    print(message.status)
