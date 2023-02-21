# from time import sleep
# import asyncio

# from colorama import Fore, Back, Style
# from colorama import init
# from prettytable import PrettyTable
# import ccxt.async_support as ccxt
# from tqdm import tqdm

import pandas as pd

from configuration import Settings, Settings_key
from monitoring import Screener
from strategy import Macd, Ao, Psar, Sma, Donchian, Bbands, Rsi, Stat

exchange = Settings_key.HUOBI_EXCHANGE
tokens = Settings.TRADING_PAIRS
tf_list = Settings.TIMEFRAMES


# Screener.main()   # запуска монитора обзор рынка и баланс счета

print(Stat.stat_stdev('NEAR/USDT', '1d'))
print(Stat.stat_pdist('NEAR/USDT', '1d'))
print(Stat.stat_entropy('NEAR/USDT', '1d'))
print(Stat.stat_median('NEAR/USDT', '1d'))
print(Stat.stat_quantile('NEAR/USDT', '1d'))
print(Stat.stat_variance('NEAR/USDT', '1d'))
print(Stat.stat_mad('NEAR/USDT', '1d'))


# def main():  # точка входа в программу ****************************************
#     try:
#         while True:
#             asyncio.run(scan_market(tokens_list))  # сканирование торговых пар
#             asyncio.run(balances_acc())            # получение баланса счета

#             print(Style.BRIGHT + Fore.YELLOW + '\npause ...')
#             for i in tqdm(range(100), ncols=80, ascii=True):
#                 sleep(0.50)
#     except KeyboardInterrupt as e:
#             print(Style.BRIGHT + Fore.RED + '\nthe program is stopped ...')

