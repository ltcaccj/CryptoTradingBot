# Crypto Trading Bot

这是一个使用 Python 编写的加密货币交易机器人，能够自动在 Binance 交易所进行交易。

## 特性

- 支持简单移动平均线策略
- 自动化交易
- 日志记录

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

## 贡献

欢迎贡献代码！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与贡献。

## 许可证

本项目采用 MIT 许可证，详情请参见 [LICENSE](LICENSE) 文件。
