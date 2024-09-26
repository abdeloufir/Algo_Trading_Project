# Algorithmic Trading Project

## Overview

This project implements several algorithmic trading strategies using Python and Backtrader. The strategies include:

- **Moving Average Crossover**
- **Mean Reversion**
- **Momentum**
- **Trend Following**

Each strategy is backtested using historical data, optimized, and combined into portfolios for comparison. The goal of the project is to identify trading strategies and portfolio combinations that offer the best risk-adjusted returns while managing risk effectively through drawdown minimization and position sizing.

## Folder Structure

algo_trading_project/
├── data/                                 # Data files (CSV files)
├── strategies/                           # Strategy implementations
│   ├── moving_average_crossover.py       # Moving Average Crossover strategy
│   ├── mean_reversion.py                 # Mean Reversion strategy
│   ├── momentum.py                       # Momentum strategy
│   ├── trend_following.py                # Trend Following strategy
├── backtesting/                          # Backtest scripts
│   ├── backtest_moving_average.py        # Backtest for Moving Average Crossover
│   ├── backtest_mean_reversion.py        # Backtest for Mean Reversion
│   ├── backtest_momentum.py              # Backtest for Momentum
│   ├── backtest_trend_following.py       # Backtest for Trend Following
├── portfolio/                            # Portfolio scripts
│   ├── equal_weighted_portfolio.py       # Equal-weighted portfolio
│   ├── performance_weighted_portfolio.py # Performance-weighted portfolio
├── report.md                             # Final report in Markdown
├── README.md                             # Project documentation
└── requirements.txt                      # Python dependencies


## How to Run

### 1. Setup the Environment

First, ensure you have Python 3.x installed. Then, you can install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

### 2. Running Backtests
Each strategy can be backtested individually by running the respective Python script located in the backtesting/ folder.

Example:
To run the Moving Average Crossover backtest, execute:

```bash 
python backtesting/backtest_moving_average.py
```

Other strategies follow a similar format:

Mean Reversion: python backtesting/backtest_mean_reversion.py
Momentum: python backtesting/backtest_momentum.py
Trend Following: python backtesting/backtest_trend_following.py

### 3. Portfolio Construction
After running individual strategies, you can run the portfolio scripts to see the performance of combined strategies.

Equal-Weighted Portfolio:
```bash
python portfolio/equal_weighted_portfolio.py
```

Performance-Weighted Portfolio:
```bash 
python portfolio/performance_weighted_portfolio.py
```

### 4. View the Final Report
You can find a comprehensive summary of the project, including the methodology, results, and conclusions, in the report.md file.

Technologies Used
This project was developed using the following technologies and libraries:

Python 3.x
Backtrader: An open-source Python library for backtesting trading strategies.
Pandas: For data manipulation and analysis.
Matplotlib: For data visualization and plotting graphs.
YahooFinanceData (Backtrader Data Feeds): Used to load historical price data from Yahoo Finance.
Future Improvements
The following improvements can be made to further enhance the project:

Walk-Forward Optimization: Implement walk-forward optimization to avoid overfitting the strategy to historical data.
Live Trading: Integrate the project with a broker API such as Alpaca or Interactive Brokers for live trading or paper trading.
Dynamic Portfolio Rebalancing: Implement dynamic portfolio rebalancing to adjust strategy allocations over time based on changing market conditions.