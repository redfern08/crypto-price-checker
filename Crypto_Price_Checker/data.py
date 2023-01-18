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