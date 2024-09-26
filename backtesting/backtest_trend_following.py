import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import backtrader as bt
import pandas as pd
import numpy as np
from strategies.backtrader_trend_following import TrendFollowingStrategy

# Load historical data (e.g., AAPL or any other asset)
data = pd.read_csv('./data/AAPL_data.csv', index_col='Date', parse_dates=True)

# Prepare the data for Backtrader
data_feed = bt.feeds.PandasData(dataname=data)

# Create a Cerebro engine instance
cerebro = bt.Cerebro()

# Add the Trend Following strategy with risk management
cerebro.addstrategy(TrendFollowingStrategy)

# Add the data feed to the Cerebro engine
cerebro.adddata(data_feed)

# Set the initial capital
cerebro.broker.set_cash(100000.0)

# Add a fixed commission
cerebro.broker.setcommission(commission=0.001)

# Store the starting portfolio value
starting_value = cerebro.broker.getvalue()

# Run the backtest
print(f'Starting Portfolio Value: {starting_value:.2f}')
cerebro.run()
ending_value = cerebro.broker.getvalue()
print(f'Ending Portfolio Value: {ending_value:.2f}')

# 1. Calculate total return (strategy return)
total_return = ending_value - starting_value
print(f"Total Return: ${total_return:.2f}")

# 2. Calculate market return (buy and hold)
initial_price = data['Close'].iloc[0]  # First available close price
final_price = data['Close'].iloc[-1]  # Last available close price
market_return = (final_price - initial_price) / initial_price * 100  # Market return as a percentage
print(f"Market Return: {market_return:.2f}%")

# 3. Calculate daily returns and Sharpe ratio
portfolio_values = [starting_value] + [cerebro.broker.getvalue() for i in range(len(data))]
daily_returns = np.diff(portfolio_values) / portfolio_values[:-1]  # Daily percentage change in portfolio value

# Avoid divide by zero by checking std
if daily_returns.std() > 0:
    sharpe_ratio = np.sqrt(252) * (daily_returns.mean() / daily_returns.std())  # Annualized Sharpe ratio
else:
    sharpe_ratio = 0  # If there's no variation, the Sharpe ratio is 0

print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# 4. Calculate maximum drawdown
cum_returns = np.maximum.accumulate(portfolio_values)
drawdowns = (cum_returns - portfolio_values) / cum_returns
max_drawdown = np.max(drawdowns)

print(f"Maximum Drawdown: {max_drawdown * 100:.2f}%")

# Plot the results
cerebro.plot()
