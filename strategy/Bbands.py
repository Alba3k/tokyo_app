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


def ind_bbands(symbol, tf='4h', limit=500, length=20):  # Bollinger bands indicators for the selected pair
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df['time'] = pd.to_datetime(df['time'], unit='ms')
			df_bbands = pd.concat([df, df.ta.bbands(length)], axis=1)
			df_bbands = df_bbands.tail(1)
			df_bbands = df_bbands.iloc[:, [6,7,8,9,10]]
			res_bbl, res_bbm, res_bbu = df_bbands.iloc[0,0], df_bbands.iloc[0,1], df_bbands.iloc[0,2] 
			res_bbb, res_bbp = df_bbands.iloc[0,3], df_bbands.iloc[0,4]     
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_bbl, res_bbm, res_bbu, res_bbb, res_bbp


def main():
	pass

if __name__ == '__main__':
	main()