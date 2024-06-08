# Crypto Trading Bot

这是一个使用 Python 编写的加密货币交易机器人，能够自动在 Binance 交易所进行交易。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置

在 `config.py` 文件中添加你的 Binance API 密钥和其他配置：

```python
API_KEY = 'your_binance_api_key'
API_SECRET = 'your_binance_api_secret'
SYMBOL = 'BTCUSDT'
TRADE_AMOUNT = 0.001
```

## 运行

```bash
python main.py
```
