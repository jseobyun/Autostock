import datetime
import yfinance as yf
import numpy as np
from utils.data_utils import closest_date_index
from asset.base import Asset
'''
20220504
Only USA ETF, Korea ETF not implemented yet
'''
### USA ETF

class ETF(Asset):
    def __init__(self, ticker):
        super(ETF, self).__init__(ticker)
        assert isinstance(ticker, str), "Ticker must be string."
        self.ticker = ticker.upper()
        data = yf.download(self.ticker)
        assert len(data) != 0, "Wrong ticker!"

        self._price_open = data.Open # 시가
        self._price_close = data.Close # 종가
        self._price_high = data.High # 고가
        self._price_low = data.Low # 저가
        self._volume = data.Volume # 거래량
        self._date = data.axes[0].date # 일시, datetime.time

        # 이동평균선
        self._mvavg = {}
        for wsize in [5, 20, 30, 60, 120, 200, 300]:
            self._mvavg[wsize] = data.Close.rolling(window=wsize).mean()

    def __len__(self):
        return len(self._price_open)

    ### get function
    def start_date(self):
        return self._date[0]

    def open(self, year=None, month=None, day=None):
        if year is None and month is None and day is None:
            return self._price_open
        else:
            target_date = datetime.date(year=year, month=month, day=day)
            at = closest_date_index(self._price_open, target_date)
            return self._price_open[at]

    def close(self, year=None, month=None, day=None):
        if year is None and month is None and day is None:
            return self._price_close
        else:
            target_date = datetime.date(year=year, month=month, day=day)
            at = closest_date_index(self._price_close, target_date)
            return self._price_close[at]

    def high(self, year=None, month=None, day=None):
        if year is None and month is None and day is None:
            return self._price_high
        else:
            target_date = datetime.date(year=year, month=month, day=day)
            at = closest_date_index(self._price_high, target_date)
            return self._price_high[at]

    def low(self, year=None, month=None, day=None):
        if year is None and month is None and day is None:
            return self._price_low.values
        else:
            target_date = datetime.date(year=year, month=month, day=day)
            at = closest_date_index(self._price_low, target_date)
            return self._price_low[at]

    def mvavg(self, wsize, year=None, month=None, day=None):
        mvavgs = self._mvavg[wsize]
        if year is None and month is None and day is None:
            return mvavgs
        else:
            target_date = datetime.date(year=year, month=month, day=day)
            at = closest_date_index(mvavgs, target_date)
            return mvavgs[at]









