import backtrader as bt

class MomentumStrategy(bt.Strategy):
    params = (('lookback_period', 15),)  # Using the best lookback period (15 days)

    def __init__(self):
        # Rate of Change (ROC) indicator for momentum
        self.roc = bt.indicators.RateOfChange(self.data.close, period=self.params.lookback_period)

    def next(self):
        # Buy if the ROC is greater than 0 (positive momentum)
        if self.roc[0] > 0 and not self.position:
            self.buy()

        # Sell if the ROC is less than or equal to 0 (negative momentum or loss of momentum)
        elif self.roc[0] <= 0 and self.position:
            self.sell()
