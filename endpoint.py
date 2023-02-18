import requests
import time

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
        time_elapsed = time.time() - start_time
        min_price = min(dict_list[coin])
        max_price = max(dict_list[coin])
        print(f"Price interval: [${min_price} , ${max_price}] for {coin}, lookback: {time_elapsed} seconds.")
    print("Waiting for 30 seconds")
    time.sleep(30)

