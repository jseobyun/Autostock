import abc
from asset.etf import ETF

def check_asset_type(ticker):
    if '-' in ticker:
        return 'coin'
    else:
        return 'etf'

class Plan():
    __metaclass__ = abc.ABCMeta
    def __init__(self, tickers):
        assert isinstance(tickers, list)
        tickers = [ticker.upper() for ticker in tickers]
        self.tickers = tickers
        self.data = {}
        self.counts = {}
        self.investments = {}
        self.outcomes = {}

        start_dates = []
        for ticker in tickers:
            asset_type = check_asset_type(ticker)
            if asset_type == 'coin':
                #self.data[ticker] = Coin(ticker)
                return
            elif asset_type == 'etf':
                self.data[ticker] = ETF(ticker)
            elif asset_type == 'stock':
                #self.data[ticker] = Stock(ticker)
                return
            self.counts[ticker] = 0
            self.investments[ticker] = 0
            self.outcomes[ticker] = 0
            start_dates.append(self.data[ticker].start_date())

        self.start_date = max(start_dates)

        self.cash = 0
        self.total_investment = 0
        self.total_outcome = 0

    @abc.abstractmethod
    def initialize(self, **kwargs):
        return

    @abc.abstractmethod
    def run(self):
        return

    @abc.abstractmethod
    def print(self):
        print("################")
        for ticker in self.tickers:
            print(f"{ticker} : {self.counts[ticker]}  {self.investments[ticker]} -> {self.outcomes[ticker]}")
        print("Cash : ", self.cash)
        print("Total investment : ", self.total_investment)
        print("Total outcome : ", self.total_outcome)
        print("################")

    @abc.abstractmethod
    def deposit(self, cash):
        self.cash += cash

    @abc.abstractmethod
    def buy(self, ticker, year, month, day, count):
        return

    @abc.abstractmethod
    def sell(self, ticker, year, month, day, count):
        return

    @abc.abstractmethod
    def eval(self, year=None, month=None, day=None):
        return







