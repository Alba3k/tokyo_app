from time import sleep
import asyncio

from colorama import Fore, Back, Style
from colorama import init
from prettytable import PrettyTable
import ccxt.async_support as ccxt
from tqdm import tqdm

from configuration import Settings, Settings_key

exchange = Settings_key.HUOBI_EXCHANGE
tokens_list = Settings.TRADING_PAIRS
init(autoreset=True)


async def scan_market(tokens_list): # market scanning for trading pairs ******* 
    mytable = PrettyTable()
    mytable.field_names = ['symbol', 'open', 'high', 'low', 'close', 'average', 'percent, %']
    mytable.align['symbol'] = 'l'
    mytable.align['open'] = 'r'
    mytable.align['high'] = 'r'
    mytable.align['low'] = 'r'
    mytable.align['close'] = 'r'
    mytable.align['average'] = 'r'
    mytable.align['percent, %'] = 'r'
    mytable.sortby = 'percent, %'

    print(Style.BRIGHT + Fore.YELLOW + '\nmarket analysis in progress ...')

    for ticker in tokens_list:

        symbol = exchange.fetch_ticker(ticker + '/USDT')['symbol']
        open_price = exchange.fetch_ticker(ticker + '/USDT')['open']
        high_price = exchange.fetch_ticker(ticker + '/USDT')['high']
        low_price = exchange.fetch_ticker(ticker + '/USDT')['low']
        close_price = exchange.fetch_ticker(ticker + '/USDT')['close']
        avg_price = exchange.fetch_ticker(ticker + '/USDT')['average']
        percentage = round((exchange.fetch_ticker(ticker + '/USDT')['percentage']),4) 
        mytable.add_row([symbol, open_price, high_price, low_price, close_price, avg_price, percentage])

    print(mytable)


async def balances_acc():  # account balance **********************************
    mytable = PrettyTable()
    mytable.field_names = ['symbol', 'free', 'used', 'total', 'total, usdt']
    mytable.align['symbol'] = 'l'
    mytable.align['free'] = 'r'
    mytable.align['used'] = 'r'
    mytable.align['total'] = 'r'
    mytable.align['total, usdt'] = 'r'
    mytable.sortby = 'total, usdt'

    balance = exchange.fetch_balance()
    total_list = []
    keys_lst = ['free', 'used', 'total', 'info']
    balance_dict_new = {}
    
    for i, j in balance.items():

        if i not in keys_lst:
            free_money = round((j.get('free')),4)
            used_money = round((j.get('used')),4)
            total_money = round((j.get('total')),4)

            if free_money > 0 or used_money > 0 or total_money > 0:
                new_lst = [free_money, used_money, total_money]
                new_lst.insert(0, i)
                total_list.append(new_lst)

    for token in total_list:
        symbol = token[0]
        if symbol != 'USDT':
            price_usdt = exchange.fetch_ticker(symbol + '/USDT')['last']
            total_usdt = round((token[3] * price_usdt),4)
            token.append(total_usdt)
            mytable.add_row(token)
        elif symbol == 'USDT':
            total_usdt = round((token[3] * 1),4)
            token.append(total_usdt)
            mytable.add_row(token)
            
    print(Style.BRIGHT + Fore.YELLOW + '\ntrading account balance ...')
    print(mytable)


def main():  # точка входа в программу ****************************************
    asyncio.run(scan_market(tokens_list))  # сканирование торговых пар
    asyncio.run(balances_acc())            # получение баланса счета


if __name__ == '__main__':
    main()