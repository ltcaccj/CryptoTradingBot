import pandas as pd

def simple_moving_average(data, window):
    return data['close'].rolling(window=window).mean()
