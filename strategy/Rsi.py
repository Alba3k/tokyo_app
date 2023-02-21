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


def ind_rsi(symbol, tf='4h', limit=500, rsi_length=14):  # rsi indicators for the selected pair
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_rsi = pd.concat([df, df.ta.rsi(length=rsi_length)], axis=1)
			df_rsi = df_rsi.tail(1)
			res_rsi = round((df_rsi.iat[0,6]),6)
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_rsi


def main():
	pass

if __name__ == '__main__':
	main()