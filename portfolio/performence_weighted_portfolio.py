import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import matplotlib.pyplot as plt
from strategy_comparison import df_performance  # Import the DataFrame from strategy_comparison.py

# Display the df_performance DataFrame (optional)
print("Strategy Performance Data:\n", df_performance)

### Performance-Based Weighting Portfolio
weights_performance = {
    'Moving Average Crossover': 0.10,  # Lower weight due to lower performance
    'Mean Reversion': 0.30,
    'Momentum': 0.40,  # Higher weight due to higher performance
    'Trend Following': 0.20
}

# Calculate the weighted metrics for the performance-weighted portfolio
performance_weighted_return = sum(df_performance['Total Return'][strategy] * weights_performance[strategy] for strategy in weights_performance)
performance_weighted_sharpe = sum(df_performance['Sharpe Ratio'][strategy] * weights_performance[strategy] for strategy in weights_performance)
performance_weighted_drawdown = sum(df_performance['Maximum Drawdown'][strategy] * weights_performance[strategy] for strategy in weights_performance)

print("\nPerformance Weighted Portfolio Results:")
print(f"Total Return: {performance_weighted_return:.2f}")
print(f"Sharpe Ratio: {performance_weighted_sharpe:.2f}")
print(f"Maximum Drawdown: {performance_weighted_drawdown:.2f}%")

# Bar chart for Total Returns
returns = [performance_weighted_return]
labels = ['Performance Weighted']
plt.bar(labels, returns)
plt.title('Total Returns - Performance Weighted Portfolio')
plt.ylabel('Total Return ($)')
plt.show()

# Bar chart for Sharpe Ratios
sharpes = [performance_weighted_sharpe]
plt.bar(labels, sharpes, color='green')
plt.title('Sharpe Ratios - Performance Weighted Portfolio')
plt.ylabel('Sharpe Ratio')
plt.show()

# Bar chart for Maximum Drawdown
drawdowns = [performance_weighted_drawdown]
plt.bar(labels, drawdowns, color='red')
plt.title('Maximum Drawdown - Performance Weighted Portfolio')
plt.ylabel('Max Drawdown (%)')
plt.show()
