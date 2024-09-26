import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import matplotlib.pyplot as plt
from strategy_comparison import df_performance  # Import the DataFrame from strategy_comparison.py

# Display the df_performance DataFrame (optional)
print("Strategy Performance Data:\n", df_performance)

### Equal Weighting Portfolio
weights_equal = {
    'Moving Average Crossover': 0.25,
    'Mean Reversion': 0.25,
    'Momentum': 0.25,
    'Trend Following': 0.25
}

# Calculate the weighted metrics for the equal-weighted portfolio
equal_weighted_return = sum(df_performance['Total Return'][strategy] * weights_equal[strategy] for strategy in weights_equal)
equal_weighted_sharpe = sum(df_performance['Sharpe Ratio'][strategy] * weights_equal[strategy] for strategy in weights_equal)
equal_weighted_drawdown = sum(df_performance['Maximum Drawdown'][strategy] * weights_equal[strategy] for strategy in weights_equal)

print("\nEqual Weighted Portfolio Results:")
print(f"Total Return: {equal_weighted_return:.2f}")
print(f"Sharpe Ratio: {equal_weighted_sharpe:.2f}")
print(f"Maximum Drawdown: {equal_weighted_drawdown:.2f}%")

# Bar chart for Total Returns
returns = [equal_weighted_return]
labels = ['Equal Weighted']
plt.bar(labels, returns)
plt.title('Total Returns - Equal Weighted Portfolio')
plt.ylabel('Total Return ($)')
plt.show()

# Bar chart for Sharpe Ratios
sharpes = [equal_weighted_sharpe]
plt.bar(labels, sharpes, color='green')
plt.title('Sharpe Ratios - Equal Weighted Portfolio')
plt.ylabel('Sharpe Ratio')
plt.show()

# Bar chart for Maximum Drawdown
drawdowns = [equal_weighted_drawdown]
plt.bar(labels, drawdowns, color='red')
plt.title('Maximum Drawdown - Equal Weighted Portfolio')
plt.ylabel('Max Drawdown (%)')
plt.show()
