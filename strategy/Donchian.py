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


def ind_donchian(symbol, tf='4h', limit=500, lower_length=10, upper_length=15): # Donchian indicators for the selected pair
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_donchian = pd.concat([df, df.ta.donchian(lower_length, upper_length)], axis=1)
			df_donchian = df_donchian.tail(1)
			df_donchian = df_donchian.iloc[:, [6,7,8]]
			res_dcl, res_dcm, res_dcu = df_donchian.iloc[0,0], df_donchian.iloc[0,1], df_donchian.iloc[0,2] 
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_dcl, res_dcm, res_dcu


def main():
	pass

if __name__ == '__main__':
	main()