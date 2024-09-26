import pandas as pd
import os

# Load the historical data (make sure the data file is in the right path)
data_path = './data/AAPL_data.csv'

# Load the data into a DataFrame
df = pd.read_csv(data_path, index_col='Date', parse_dates=True)

# Define moving average windows
short_window = 50
long_window = 200

# Calculate the short-term and long-term moving averages
df['Short_MA'] = df['Close'].rolling(window=short_window, min_periods=1).mean()
df['Long_MA'] = df['Close'].rolling(window=long_window, min_periods=1).mean()

# Generate buy and sell signals (without using loc[] but fixing the warning)
df['Signal'] = 0  # Default value for no signal
df['Signal'][short_window:] = (df['Short_MA'][short_window:] > df['Long_MA'][short_window:])  # Buy when Short_MA crosses above Long_MA
df['Position'] = df['Signal'].diff()  # 1 = Buy, -1 = Sell

# Count the buy (1) and sell (-1) signals
buy_signals = len(df[df['Position'] == 1])
sell_signals = len(df[df['Position'] == -1])

# Print the number of buy and sell signals
print(f"Number of Buy signals: {buy_signals}")
print(f"Number of Sell signals: {sell_signals}")

# Save the signals to a CSV for visualization later
output_file = './data/moving_average_signals.csv'
df.to_csv(output_file)

print(f"Moving Average Crossover signals saved to {output_file}")
