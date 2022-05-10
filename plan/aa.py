from plan.base import Plan
from asset.etf import ETF

class StaticAssetAllocation(Plan):
    def __init__(self, tickers):
        super(StaticAssetAllocation, self).__init__(tickers)

    def initialize(self, ratios, **kwargs):
        ratio_sum = 0
        self.ratios = {}
        for ticker in list(ratios.keys()):
            assert ticker in self.tickers, "ticker is not matched."
            ratio = ratios[ticker]
            ratio_sum += ratio
            self.ratios[ticker] = ratio
        assert ratio_sum == 1, "Asset ratios are invalid. sum(ratios) > 1"

    def run(self):
        ###

        ###
        return


    def buy(self, ticker, year, month, day, count):
        ticker = ticker.upper()
        if ticker not in self.tickers:
            print("Wrong ticker : Portfolio does not support.")
            return
        item = self.data[ticker]
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
        item = self.data[ticker]
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
            item = self.data[ticker]
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



