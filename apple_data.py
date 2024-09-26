import yfinance as yf
import os

# Define the ticker symbol and data directory
ticker = 'AAPL'
data_dir = './data'

# Ensure the data directory exists
os.makedirs(data_dir, exist_ok=True)

# Download historical data for the ticker (daily data for the last 5 years)
stock_data = yf.download(ticker, period='5y', interval="1d")

# Save the data to a CSV file
csv_file = os.path.join(data_dir, f'{ticker}_data.csv')
stock_data.to_csv(csv_file)

print(f"Data for {ticker} saved to {csv_file}")