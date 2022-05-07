import datetime
import numpy as np
import yfinance as yf

def ymd_tuple2str(ymd_tuple):
    y, m ,d = ymd_tuple[0], ymd_tuple[1], ymd_tuple[2]
    ymd_str = str(y) + '-' + format(m, '02d') + '-' + format(d, '02d')
    return ymd_str

def ymd_str2int(ymd_str):
    y, m, d = ymd_str[:4], ymd_str[5:7], ymd_str[8:10]
    ymd_int = int(y+m+d)
    return ymd_int

def ymd_tuple2int(ymd_tuple):
    ymd_str = ymd_tuple2str(ymd_tuple)
    ymd_int = ymd_str2int(ymd_str)
    return ymd_int

def ymd_int2str(ymd_int):
    ymd = str(ymd_int)
    ymd_str = ymd[:4] + '-' + ymd[4:6] + '-' + ymd[6:8]
    return ymd_str


def get_data(tickers, ymd):
    if not isinstance(tickers, list):
        tickers = [tickers]
    for i in range(len(tickers)):
        tickers[i] = tickers[i].upper()
    if not isinstance(ymd, str):
        start = str(ymd[0])+'-'+format(ymd[1], '02d')+'-'+format(ymd[2], '02d')
    elif isinstance(ymd, str) and '-' not in ymd:
        start = ymd[:4]+'-'+ymd[4:6]+'-'+ymd[6:8]
    else:
        start = ymd
    data = {}
    ymd_min_list = []

    for ticker in tickers:
        data[ticker] = yf.download(ticker, start)#.to_dict()
        ymd_list = data[ticker].Close.axes[0]
        ymd_min = ymd_list[0]
        y, m, d = str(ymd_min)[:4], str(ymd_min)[5:7], str(ymd_min)[8:10]
        ymd_min_list.append(int(y+m+d)+1)

    ymd_ref = np.max(ymd_min_list)
    for i, ticker in enumerate(tickers):
        if ymd_min_list[i] < ymd_ref:
            data[ticker] = get_data(ticker, str(ymd_ref))[ticker]

    print(f"All start is revised as {ymd_ref-1}")

    return data