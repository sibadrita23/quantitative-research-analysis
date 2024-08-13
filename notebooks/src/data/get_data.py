import requests
import pandas as pd
from datetime import datetime

def fetch_data(symbol):
    API_KEY = 'your_alpha_vantage_api_key'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&outputsize=full&datatype=csv'
    
    response = requests.get(url)
    file_name = f"data/raw/{symbol}_daily.csv"
    with open(file_name, 'wb') as f:
        f.write(response.content)
    
    print(f"Data for {symbol} saved to {file_name}")

if __name__ == '__main__':
    fetch_data('AAPL')  # Fetch data for Apple Inc.
