import backtrader as bt

class MeanReversionStrategy(bt.Strategy):
    params = (('lookback_period', 50), ('entry_threshold', 2.5))  # Use the best combination

    def __init__(self):
        # Calculate the mean (SMA) and standard deviation over the lookback period
        self.mean = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.lookback_period)
        self.stddev = bt.indicators.StandardDeviation(self.data.close, period=self.params.lookback_period)

    def next(self):
        # Buy when the price is below mean - (entry_threshold * stddev)
        if self.data.close[0] < self.mean[0] - self.params.entry_threshold * self.stddev[0] and not self.position:
            self.buy()
        
        # Sell when the price is above mean + (entry_threshold * stddev)
        elif self.data.close[0] > self.mean[0] + self.params.entry_threshold * self.stddev[0] and self.position:
            self.sell()
