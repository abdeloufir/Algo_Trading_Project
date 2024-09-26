import backtrader as bt

class MovingAverageCrossover(bt.Strategy):
    params = (('short_period', 5), ('long_period', 30))  # Default values, but will be overridden by grid search

    def __init__(self):
        # Define short and long moving averages
        self.short_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.short_period)
        self.long_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.long_period)

    def next(self):
        # Buy when short MA crosses above long MA
        if self.short_ma[0] > self.long_ma[0] and not self.position:
            self.buy()

        # Sell when short MA crosses below long MA
        elif self.short_ma[0] < self.long_ma[0] and self.position:
            self.sell()
