from time import sleep
import asyncio

from colorama import Fore, Back, Style
from colorama import init
from prettytable import PrettyTable
from tqdm import tqdm
import pandas_ta as ta
import pandas as pd

from configuration import Settings, Settings_key

exchange = Settings_key.HUOBI_EXCHANGE
tokens = Settings.TRADING_PAIRS
tf_list = Settings.TIMEFRAMES

init(autoreset=True)


def ind_macd(symbol, tf='4h', limit=500, fast=12, slow=26): # macd indicators for the selected pair
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_macd = pd.concat([df, df.ta.macd(fast, slow)], axis=1)
			df_macd = df_macd.tail(1)
			df_macd = df_macd.iloc[:, [6,7,8]]
			res_macd, res_macdh, res_macds = df_macd.iloc[0,0], df_macd.iloc[0,1], df_macd.iloc[0,2] 
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_macd, res_macdh, res_macds


def main():
	pass

if __name__ == '__main__':
	main()