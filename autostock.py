from asset.etf import ETF
from portfolio import Portfolio

if __name__=='__main__':
    # spy = ETF('SPY')
    # ief = ETF('IEF')
    # a = spy.close(2017, 3, 3)
    # b = ief.close(2017, 3, 3)
    # draw_single_chart('VOO', VOO)
    # draw_multi_chart(tickers, data)
    ratio = {
        'VOO' : 0.3, # ticker ratio
        'QQQ' : 0.3,
        'DBC' : 0.2,
        'GLD' : 0.2,
    }
    pf = Portfolio(ratio)
    pf.deposit(100000)
    pf.buy('voo', 2017, 3, 4, count=3)
    pf.sell('voo', 2017, 3, 4, count=3)
    pf.buy('qqq', 2020, 4, 8, count=3)



    print("")
