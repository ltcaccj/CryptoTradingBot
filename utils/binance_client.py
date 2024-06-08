from binance.client import Client
from config import API_KEY, API_SECRET

def get_binance_client():
    client = Client(API_KEY, API_SECRET)
    return client
