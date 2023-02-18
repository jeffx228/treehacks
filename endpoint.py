import requests

# API endpoint
url = 'https://api.pro.coinbase.com/products/BTC-USD/ticker'

# Send GET request to the endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()
    
    # Extract the price from the data
    price = data['price']
    
    # Print the price
    print(f"Current BTC-USD price: {price}")
else:
    print(f"Request failed with status code {response.status_code}")
