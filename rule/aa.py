from rule.base import Base
from asset.etf import ETF

class Portfolio(Base):
    def __init__(self, pf):
        super(Portfolio, self).__init__(pf)
        self.tickers = []
        self.items = {}
        self.cash = 0
        self.ratios = {}
        self.counts = {}
        ratio_sum = 0
        for ticker in list(pf.keys()):
            self.tickers.append(ticker.upper())
            self.ratios[ticker.upper()] = pf[ticker]
            self.counts[ticker.upper()] = 0
            ### classify asset : if etf or stock or coin
            self.items[ticker.upper()] = ETF(ticker)
            ratio_sum += pf[ticker]
        assert ratio_sum == 1, "The sum of ratios is not 100%"

        print(f"Portfolio is initialized with {self.tickers}")
        self.total_investment = 0
        self.total_outcome = 0

    def buy(self, ticker, year, month, day, count):
        ticker = ticker.upper()
        if ticker not in self.tickers:
            print("Wrong ticker : Portfolio does not support.")
            return
        item = self.items[ticker]
        price = item.close(year, month, day)
        total_price = count * price
        if self.cash < total_price:
            print("Need more money.")
            return
        self.cash -= total_price
        self.counts[ticker] += count

        print(f"buying {ticker} at price {price}")
        self.cal_total_outcome()
        self.print()


    def sell(self, ticker, year, month, day, count):
        ticker = ticker.upper()
        if ticker not in self.tickers:
            print("Wrong ticker : Portfolio does not support.")
            return
        item = self.items[ticker]
        if self.counts[ticker] < count:
            print(f"Current {self.counts[ticker]} {ticker} exists. : try lower than {count}")
            return
        price = item.close(year, month, day)
        total_price = count * price
        self.cash += total_price
        self.counts[ticker] -= count

        print(f"selling {ticker} at price {price}")
        self.cal_total_outcome()
        self.print()


    def cal_total_outcome(self, year=None, month=None, day=None):
        curr_outcome = 0
        for ticker in self.tickers:
            item = self.items[ticker]
            if year is None: # month is None and day is None:
                price = item.close()[-1]
            else:
                price = item.close(year, month, day)
            total_price = self.counts[ticker] * price
            curr_outcome += total_price
        curr_outcome += self.cash
        self.total_outcome = curr_outcome





    ### 종목 간 비율 계산
    ### 수익률 계산 ( 시작 날짜, 종료 날짜 ) FUTUREWORK: 수수료 반영
    ### 리밸런싱
    ### 적립식 투자
    ### 투입 자본금, 현 자본금
    ### 현 상태 출력



