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


def ind_psar(symbol, tf='4h', limit=500):   # Parabolic Stop and Reverse indicators for the selected pair
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_psar = pd.concat([df, df.ta.psar()], axis=1)
			df_psar = df_psar.tail(1)
			df_psar = df_psar.iloc[:, [7,8,9]]
			res_psar_s, res_psar_af, res_psar_r = df_psar.iloc[0,0], df_psar.iloc[0,1], df_psar.iloc[0,2] 
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_psar_s, res_psar_af, res_psar_r


def main():
	pass

if __name__ == '__main__':
	main()