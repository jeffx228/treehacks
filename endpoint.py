import requests
import time
import os
import slack
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# Makes API call for given URL
def hitAPI(url, coin):
    # Send GET request to the endpoint
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()
        
        # Extract the price from the data
        price = data['price']
        
        # Print the price
        # print(f"Current {coin} price: {price}")

        return price
    
    else:
        print(f"Request failed with status code {response.status_code}")

urls = ['https://api.pro.coinbase.com/products/BTC-USD/ticker',\
        'https://api.pro.coinbase.com/products/ETH-USD/ticker',\
        'https://api.pro.coinbase.com/products/BCH-USD/ticker',\
        'https://api.pro.coinbase.com/products/LTC-USD/ticker',\
        'https://api.pro.coinbase.com/products/LINK-USD/ticker',\
        'https://api.pro.coinbase.com/products/XLM-USD/ticker'\
        ]

coins = ['Bitcoin', 'Ethereum', 'Bitcoin Cash', 'Litecoin', 'Chainlink', 'Stellar Lumens']
# Bitcoin (BTC-USD): 'https://api.pro.coinbase.com/products/BTC-USD/ticker'
# Ethereum (ETH-USD): https://api.pro.coinbase.com/products/ETH-USD/ticker
# Bitcoin Cash (BCH-USD): https://api.pro.coinbase.com/products/BCH-USD/ticker
# Litecoin (LTC-USD): https://api.pro.coinbase.com/products/LTC-USD/ticker
# Chainlink (LINK-USD): https://api.pro.coinbase.com/products/LINK-USD/ticker
# Stellar Lumens (XLM-USD): https://api.pro.coinbase.com/products/XLM-USD/ticker

dict_list = {}

for coin in coins:
    dict_list[coin] = []

start_time = time.time()

while True: 
    for url in urls:
        coin = coins[urls.index(url)]
        price = hitAPI(url, coin)
        dict_list[coin].append(price)
        if len(dict_list[coin]) >= 2 and dict_list[coin][-1] > 1.01 * dict_list[coin][-2]:
            client.chat_postMessage(channel='#a', text=f"ALERT: Greater than 1% upmove detected for {coin}")

        if len(dict_list[coin]) >= 2 and dict_list[coin][-1] < 0.99 * dict_list[coin][-2]:
            client.chat_postMessage(channel='#a', text=f"ALERT: Greater than 1% downmove detected for {coin}")
        time_elapsed = time.time() - start_time
        min_price = min(dict_list[coin])
        max_price = max(dict_list[coin])
        print(f"Price interval: [${min_price} , ${max_price}] for {coin}, lookback: {time_elapsed} seconds.")
        client.chat_postMessage(channel='#a', text=f"Price interval: [${min_price} , ${max_price}] for {coin}, lookback: {time_elapsed} seconds.")
    print("Waiting to alert for large movies")
    client.chat_postMessage(channel='#a', text="Waiting to alert for large moves")
    time.sleep(30)

