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


def ind_sma(symbol, timeframe='4h', limit=500, sma_length=30):  # SMA indicators for the selected pair
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_sma = pd.concat([df, df.ta.sma(sma_length)], axis=1)
			df_sma = df_sma.tail(1)
			df_sma = df_sma.iloc[:, [6]]
			res_sma = round((df_sma.iloc[0,0]),6)  
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_sma


def main():
	pass

if __name__ == '__main__':
	main()
