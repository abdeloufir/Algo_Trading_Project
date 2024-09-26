import backtrader as bt

class TrendFollowingStrategy(bt.Strategy):
    params = (('short_period', 5), ('long_period', 20))  # Default values for EMA

    def __init__(self):
        # Define short and long exponential moving averages (EMAs)
        self.short_ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.short_period)
        self.long_ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=self.params.long_period)

    def next(self):
        # Buy if short EMA crosses above long EMA (uptrend)
        if self.short_ema[0] > self.long_ema[0] and not self.position:
            self.buy()

        # Sell if short EMA crosses below long EMA (downtrend)
        elif self.short_ema[0] < self.long_ema[0] and self.position:
            self.sell()
