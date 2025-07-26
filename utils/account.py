def get_account_info(client):
    info = client.get_account()
    balances = info['balances']
    usdt_balance = next((b for b in balances if b['asset'] == 'USDT'), None)
    return usdt_balance['free'] if usdt_balance else 0
