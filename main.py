import asyncio

from colorama import Fore, Back, Style
from colorama import init

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
init(autoreset=True)


print(Settings.LOGO)
print(Style.BRIGHT + Fore.YELLOW + Settings.DESC_TEXT)

def menu_render():
	for items, pt in Settings.MENU_ITEMS.items():
		print(items.ljust(36, '.') + (str(pt).rjust(8)))

def main():
	menu_render()
	try:
		while True:
			command = input('\nenter the command: ').upper().strip()	
			if command == 'B':
				asyncio.run(Screener.balances_acc())
			elif command == 'M':
				asyncio.run(Screener.scan_market(tokens))


			elif command == 'G':
				menu_render()
			else:
				print('enter the correct command.')
	except KeyboardInterrupt as e:
		print(Style.BRIGHT + Fore.RED + '\nthe program is stopped ...')


if __name__ == '__main__':
	main()