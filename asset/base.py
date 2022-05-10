import abc

class Asset():
    __metaclass__ = abc.ABCMeta
    def __init__(self, ticker):
        self.ticker = ticker.upper()
        self._price_open = None
        self._price_close = None
        self._price_high = None
        self._price_low = None
        self._volume = None
        self._data = None

        self._mvavg = {}
        for wsize in [5, 20, 30, 60, 120, 200, 300]:
            self._mvavg[wsize] = None

    @abc.abstractmethod
    def __len__(self):
        return

    @abc.abstractmethod
    def start_date(self):
        return

    @abc.abstractmethod
    def open(self, year=None, month=None, day=None):
        return

    @abc.abstractmethod
    def close(self, year=None, month=None, day=None):
        return

    @abc.abstractmethod
    def high(self, year=None, month=None, day=None):
        return

    @abc.abstractmethod
    def low(self, year=None, month=None, day=None):
        return

    @abc.abstractmethod
    def mvavg(self, year=None, month=None, day=None):
        return





