
import yaml
from bot.trader import Trader
from utils.account import get_account_info
from utils.pnl import get_pnl
from binance.client import Client

def check_spot_balance(client):
    info = client.get_account()
    usdt = next((b for b in info['balances'] if b['asset'] == 'USDT'), None)
    print(f"Spot USDT Balance: {usdt['free'] if usdt else 0}")

def check_futures_balance(client):
    futures_balance = client.futures_account_balance()
    usdt_futures = next((b for b in futures_balance if b['asset'] == 'USDT'), None)
    print(f"Futures USDT Balance: {usdt_futures['balance'] if usdt_futures else 0}")

def main():
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    client = Client(config['binance']['api_key'], config['binance']['api_secret'])
    trader = Trader(config)


    while True:
        print("\n=== Binance Enterprise Bot ===")
        print("1. Check Spot Balance")
        print("2. Check Futures (USDⓈ-M) Balance")
        print("3. Trade (Simple Buy)")
        print("4. Show PnL (All)")
        print("5. Track Spot PnL by Date Range")
        print("6. Track Futures PnL by Date Range")
        print("7. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            check_spot_balance(client)
        elif choice == '2':
            check_futures_balance(client)
        elif choice == '3':
            trader.run()
        elif choice == '4':
            pnl = get_pnl()
            print(f"PnL: {pnl}")
        elif choice == '5':
            from_date = input("Enter start date (YYYY-MM-DD): ")
            to_date = input("Enter end date (YYYY-MM-DD): ")
            print("Tracking Spot PnL...")
            spot_pnl = track_spot_pnl(client, from_date, to_date)
            print(f"Spot PnL from {from_date} to {to_date}: {spot_pnl}")
        elif choice == '6':
            from_date = input("Enter start date (YYYY-MM-DD): ")
            to_date = input("Enter end date (YYYY-MM-DD): ")
            print("Tracking Futures PnL...")
            futures_pnl = track_futures_pnl(client, from_date, to_date)
            print(f"Futures PnL from {from_date} to {to_date}: {futures_pnl}")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

# Helper functions for tracking PnL by date range
def track_spot_pnl(client, from_date, to_date):
    # Example: fetch trades and calculate PnL (placeholder)
    # You can implement real logic using client.get_my_trades(symbol, startTime, endTime)
    print("(Spot PnL calculation not implemented)")
    return 0.0

def track_futures_pnl(client, from_date, to_date):
    # Example: fetch futures trades and calculate PnL (placeholder)
    # You can implement real logic using client.futures_account_trades(startTime, endTime)
    print("(Futures PnL calculation not implemented)")
    return 0.0

if __name__ == "__main__":
    main()
