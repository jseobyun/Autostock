import numpy as np

def CAGR(df):
    x = df['Close']
    price_curr = np.array(x)
    tdiff = np.arange(1, len(price_curr))
    cagr = (price_curr[1:] / price_curr[0])**(365/tdiff) - 1
    cagr = cagr*100
    return cagr

def MDD(df):
    """
    MDD(Maximum Draw-Down)
    :return: (peak_upper, peak_lower, mdd rate)
    """
    x = df['Close']
    arr_v = np.array(x)
    peak_lower = np.argmax(np.maximum.accumulate(arr_v) - arr_v)
    peak_upper = np.argmax(arr_v[:peak_lower])
    return (arr_v[peak_lower] - arr_v[peak_upper]) / arr_v[peak_upper]