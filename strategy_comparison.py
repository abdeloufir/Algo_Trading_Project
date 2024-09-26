import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import backtrader as bt
import pandas as pd
import numpy as np
from strategies.backtrader_moving_average_crossover import MovingAverageCrossover
from strategies.backtrader_mean_reversion import MeanReversionStrategy
from strategies.backtrader_momentum import MomentumStrategy
from strategies.backtrader_trend_following import TrendFollowingStrategy

def run_strategy_and_collect_metrics(strategy_class, data, initial_cash=100000):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy_class)
    cerebro.adddata(data)
    cerebro.broker.set_cash(initial_cash)
    cerebro.broker.setcommission(commission=0.001)

    # Store starting value
    starting_value = cerebro.broker.getvalue()
    cerebro.run()
    ending_value = cerebro.broker.getvalue()

    # Calculate total return
    total_return = ending_value - starting_value

    # Calculate market return (buy-and-hold)
    initial_price = data.close[0]
    final_price = data.close[-1]
    market_return = (final_price - initial_price) / initial_price * 100  # Percentage return

    # Calculate Sharpe ratio
    portfolio_values = [starting_value] + [cerebro.broker.getvalue() for _ in range(len(data))]
    daily_returns = np.diff(portfolio_values) / portfolio_values[:-1]  # Daily percentage change in portfolio value
    sharpe_ratio = np.sqrt(252) * (daily_returns.mean() / daily_returns.std()) if daily_returns.std() > 0 else 0

    # Calculate maximum drawdown
    cumulative_returns = np.maximum.accumulate(portfolio_values)
    drawdowns = (cumulative_returns - portfolio_values) / cumulative_returns
    max_drawdown = np.max(drawdowns)

    return {
        'Total Return': total_return,
        'Sharpe Ratio': sharpe_ratio,
        'Maximum Drawdown': max_drawdown * 100,  # Convert to percentage
        'Market Return': market_return
    }

# Backtest data for each strategy
data = bt.feeds.YahooFinanceData(dataname='./data/AAPL_data.csv')  # Example: AAPL data

# Dictionary to store the performance of each strategy
performance_comparison = {}

# Run and collect metrics for each strategy
performance_comparison['Moving Average Crossover'] = run_strategy_and_collect_metrics(MovingAverageCrossover, data)
performance_comparison['Mean Reversion'] = run_strategy_and_collect_metrics(MeanReversionStrategy, data)
performance_comparison['Momentum'] = run_strategy_and_collect_metrics(MomentumStrategy, data)
performance_comparison['Trend Following'] = run_strategy_and_collect_metrics(TrendFollowingStrategy, data)

# Convert the results to a DataFrame for better readability
df_performance = pd.DataFrame(performance_comparison).T

# Display the performance comparison table
print(df_performance)

# Optionally: Visualize the results
import matplotlib.pyplot as plt

# Plot Total Returns for each strategy
df_performance['Total Return'].plot(kind='bar', title='Total Returns Comparison')
plt.ylabel('Total Return ($)')
plt.show()

# Plot Maximum Drawdown for each strategy
df_performance['Maximum Drawdown'].plot(kind='bar', title='Maximum Drawdown Comparison', color='red')
plt.ylabel('Max Drawdown (%)')
plt.show()

# Plot Sharpe Ratios for each strategy
df_performance['Sharpe Ratio'].plot(kind='bar', title='Sharpe Ratio Comparison', color='green')
plt.ylabel('Sharpe Ratio')
plt.show()
