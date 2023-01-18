import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import requests as rq
import pprint as pp
import json

url = "http://api.coincap.io/v2/assets"

payload = {}
headers = {}


response = rq.get(url, headers=headers, data=payload)
data = response.json()
coin_data = data['data']


for info in coin_data[0:10]:
    coin = info['name']
    price_rd = float(info['priceUsd'])
    price = round(price_rd, 2)
    supply_rd = float(info['supply'])
    supply = round(supply_rd)
    symbol = info['symbol']
    print(f"Symbol: {symbol}, Name: {coin}, \nSupply: {supply}, Price: ${price}\n")

# plt.style.use('dark_background')
# fig, ax = plt.subplots(figsize=(10,8))


'''Iterate through the data and create a scatter
chart to display coin price and name.'''

# for-loop to iterate through data.
# for info in coin_data[0:8]:
#     coin = info['name']
#     price_rd = float(info['priceUsd'])  # convert to a float to shorten length of nums. round two decimal places
#     price = round(price_rd, 2)
#     supply_rd = float(info['supply'])   # float conversion. same conversion as price, round to zero decimal places
#     supply = round(supply_rd)
#     symbol = info['symbol']
#     print(info)
#     ax.bar(coin, price, color='red', label=coin)


# plt.bar_label(ax.bar, labels=[price])
# plt.xlabel('Coin Name', fontsize=12)
# plt.ylabel('Price', fontsize=12)
# plt.title('Crypto Coin Prices 2022')
# plt.tick_params(axis='x', rotation=0)
# plt.legend()
# plt.show()


