import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mplfinance.original_flavor import candlestick_ohlc


def draw_multi_chart(tickers, dfs, tick='year'):
    fig = plt.figure(figsize=(8, 5))
    fig.set_facecolor('w')
    gs = gridspec.GridSpec(1, 1)
    axe = plt.subplot(gs[0])
    #axe.get_xaxis().set_visible(False)

    x = np.arange(len(dfs[tickers[0]].index))
    for ticker in tickers:
        axe.plot(x, dfs[ticker]['Close'], label=ticker, linewidth=0.7)


    _xticks = []
    _xlabels = []
    _prev = -1

    for _x, d in zip(x, dfs[tickers[0]].Close.axes[0]):
        # weekday :0~6 monday~sunday
        month = datetime.datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S').month
        weekday = datetime.datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S').weekday()
        if tick == 'year':
            if month < _prev:
                _xticks.append(_x)
                _xlabels.append(datetime.datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S').strftime('%Y/%m'))
            _prev = month
        elif tick == 'month':
            if month <= _prev:
                _xticks.append(_x)
                _xlabels.append(datetime.datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S').strftime('%Y/%m'))
            _prev = month
        elif tick == 'day':
            if weekday <= _prev:
                _xticks.append(_x)
                _xlabels.append(datetime.datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S').strftime('%Y/%m'))
            _prev = weekday

    axe.set_xticks(_xticks)
    axe.set_xticklabels(_xlabels, rotation=45, minor=False)
    axe.set_ylabel("Price($)")
    axe.legend()
    plt.tight_layout()
    plt.show()


def draw_single_chart(ticker, df, tick='year'):
    fig = plt.figure(figsize=(8, 5))
    fig.set_facecolor('w')
    gs = gridspec.GridSpec(2, 1, height_ratios=[4, 1])
    axes = []
    axes.append(plt.subplot(gs[0]))
    axes.append(plt.subplot(gs[1], sharex=axes[0]))
    axes[0].get_xaxis().set_visible(False)

    x = np.arange(len(df.index))
    ohlc = df[['Open', 'High', 'Low', 'Close']].astype(int).values
    dohlc = np.hstack((np.reshape(x, (-1, 1)), ohlc))
    candlestick_ohlc(axes[0], dohlc, width=0.5, colorup='r', colordown='b')
    axes[0].plot(x, df['Close'].rolling(window=30).mean(), label="Avg1m", linewidth=0.7)
    axes[0].plot(x, df['Close'].rolling(window=90).mean(), label="Avg3m", linewidth=0.7)
    axes[0].plot(x, df['Close'].rolling(window=180).mean(), label="Avg6m", linewidth=0.7)
    axes[0].plot(x, df['Close'].rolling(window=360).mean(), label="Avg12m", linewidth=0.7)
    axes[0].set_ylabel("Price($)")
    axes[0].legend()
    axes[0].set_title(ticker)

    axes[1].bar(x, df.Volume, color='k', width=0.6, align='center')


    _xticks = []
    _xlabels = []
    _prev = -1

    for _x, d in zip(x, df.Close.axes[0]):
        # weekday :0~6 monday~sunday
        month = datetime.datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S').month
        weekday = datetime.datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S').weekday()
        if tick=='year':
            if month < _prev:
                _xticks.append(_x)
                _xlabels.append(datetime.datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S').strftime('%Y/%m'))
            _prev = month
        elif tick=='month':
            if month <= _prev:
                _xticks.append(_x)
                _xlabels.append(datetime.datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S').strftime('%Y/%m'))
            _prev = month
        elif tick == 'day':
            if weekday <= _prev:
                _xticks.append(_x)
                _xlabels.append(datetime.datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S').strftime('%Y/%m'))
            _prev = weekday
    axes[1].set_xticks(_xticks)
    axes[1].set_xticklabels(_xlabels, rotation=45, minor=False)

    plt.tight_layout()
    plt.show()