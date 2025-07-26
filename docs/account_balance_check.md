# Binance Account Balance Check

This document explains how to check your Binance account balance for both Spot and Futures (USDⓈ-M) using the bot.

## Spot Account Balance

The following code checks your Spot account USDT balance:

```python
from binance.client import Client
import yaml

# Load config
with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

client = Client(config['binance']['api_key'], config['binance']['api_secret'])
info = client.get_account()
usdt = next((b for b in info['balances'] if b['asset'] == 'USDT'), None)
print(f'Spot USDT Balance: {usdt["free"] if usdt else 0}')
```

## Futures (USDⓈ-M) Account Balance

The following code checks your Futures USDT balance:

```python
from binance.client import Client
import yaml

# Load config
with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

client = Client(config['binance']['api_key'], config['binance']['api_secret'])
futures_balance = client.futures_account_balance()
usdt_futures = next((b for b in futures_balance if b['asset'] == 'USDT'), None)
print(f'Futures USDT Balance: {usdt_futures["balance"] if usdt_futures else 0}')
```

## Notes
- Ensure your API key has permissions for both Spot and Futures endpoints.
- For Futures, use the `futures_account_balance()` method.
- Always keep your API keys secure and never share them publicly.
