import abc

class Base():
    __metaclass__ = abc.ABCMeta
    def __init__(self, profile):
        self.profile = profile
        self.tickers = []
        self.items = {}
        self.cash = 0
        self.counts = {}
        self.investments = {}
        self.outcomes = {}

        self.total_investment = 0
        self.total_outcome = 0

    @abc.abstractmethod
    def print(self):
        print("################")
        for ticker in self.tickers:
            print(f"{ticker} : {self.counts[ticker]}")
        print("Cash : ", self.cash)
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







