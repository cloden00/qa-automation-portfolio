import requests

def get_live_bitcoin_price():
    
    # 1. The exact URL where Binance keeps its live ticker data
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    
    # 2. We 'GET' the data from that URL
    response = requests.get(url)
    
    # 3. If the server says "200 OK", we read the data
    if response.status_code == 200:
        data = response.json()                  # Convert the response into a Python dictionary
        price = float(data["price"])            # Extract the 'price' string and turn it into a math number
        
        print(f"Connection Successful!")
        print(f"The live price of 1 BTC is: {price} USDT")
        return price
    else:
        print(f"Error: {response.status_code}")

# Run the function
while True:
    get_live_bitcoin_price()