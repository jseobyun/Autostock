import datetime
import yfinance as yf
import numpy as np
from utils.data_utils import closest_date_index
'''
20220504
Only USA ETF, Korea ETF not implemented yet
'''
### USA ETF

class Stock():
    def __init__(self, ticker):
        assert isinstance(ticker, str), "Ticker must be string."
        self.ticker = ticker.upper()
        data = yf.download(self.ticker)
        assert len(data) != 0, "Wrong ticker!"

        self.__price_open = data.Open # 시가
        self.__price_close = data.Close # 종가
        self.__price_high = data.High # 고가
        self.__price_low = data.Low # 저가
        self.__volume = data.Volume # 거래량
        self.__date = data.axes[0].date # 일시, datetime.time

        # 이동평균선
        self.__mvavg = {}
        for wsize in [5, 20, 30, 60, 120, 200, 300]:
            self.__mvavg[wsize] = data.Close.rolling(window=wsize).mean()

    def __len__(self):
        return len(self.__price_open)

    ### get function
    def open(self, year=None, month=None, day=None):
        if year is None and month is None and day is None:
            return self.__price_open
        else:
            target_date = datetime.date(year=year, month=month, day=day)
            at = closest_date_index(self.__price_open, target_date)
            return self.__price_open[at]

    def close(self, year=None, month=None, day=None):
        if year is None and month is None and day is None:
            return self.__price_close
        else:
            target_date = datetime.date(year=year, month=month, day=day)
            at = closest_date_index(self.__price_close, target_date)
            return self.__price_close[at]

    def high(self, year=None, month=None, day=None):
        if year is None and month is None and day is None:
            return self.__price_high
        else:
            target_date = datetime.date(year=year, month=month, day=day)
            at = closest_date_index(self.__price_high, target_date)
            return self.__price_high[at]

    def low(self, year=None, month=None, day=None):
        if year is None and month is None and day is None:
            return self.__price_low
        else:
            target_date = datetime.date(year=year, month=month, day=day)
            at = closest_date_index(self.__price_low, target_date)
            return self.__price_low[at]

    def mvavg(self, wsize, year=None, month=None, day=None):
        mvavgs = self.__mvavg[wsize]
        if year is None and month is None and day is None:
            return mvavgs
        else:
            target_date = datetime.date(year=year, month=month, day=day)
            at = closest_date_index(mvavgs, target_date)
            return mvavgs[at]









