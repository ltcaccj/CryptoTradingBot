from utils.binance_client import get_binance_client
from utils.logger import logger
from strategies.simple_moving_average import simple_moving_average
import pandas as pd

def fetch_ohlcv_data(client, symbol, interval='1h', limit=100):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    data = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 
        'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 
        'taker_buy_quote_asset_volume', 'ignore'])
    data['close'] = data['close'].astype(float)
    return data

def main():
    client = get_binance_client()
    data = fetch_ohlcv_data(client, 'BTCUSDT')
    sma = simple_moving_average(data, window=20)
    logger.info(f'Simple Moving Average: {sma.iloc[-1]}')

if __name__ == '__main__':
    main()
