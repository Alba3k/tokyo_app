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


def stat_stdev(symbol, tf='4h', limit=500):
	'''Показатели статистики Standard Deviation: stdev для выбранного таймфрейма и инструмента'''
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_stdev = pd.concat([df, df.ta.stdev()], axis=1)
			df_stdev = df_stdev.tail(1)
			df_stdev = df_stdev.iloc[:, [6]]
			res_stdev = round((df_stdev.iloc[0,0]),6)  
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_stdev


def stat_pdist(symbol, tf='4h', limit=500):
	'''Показатели статистики Price Distance: pdist для выбранного таймфрейма и инструмента'''
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_pdist = pd.concat([df, df.ta.pdist()], axis=1)
			df_pdist = df_pdist.tail(1)
			df_pdist = df_pdist.iloc[:, [6]]
			res_pdist = round((df_pdist.iloc[0,0]),6)  
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_pdist


def stat_entropy(symbol, tf='4h', limit=500):
	'''Показатели статистики entropy для выбранного таймфрейма и инструмента'''
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_entropy = pd.concat([df, df.ta.entropy()], axis=1)
			df_entropy = df_entropy.tail(1)
			df_entropy = df_entropy.iloc[:, [6]]
			res_entropy = round((df_entropy.iloc[0,0]),6)  
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_entropy


def stat_median(symbol, tf='4h', limit=500):
	'''Показатели статистики median для выбранного таймфрейма и инструмента'''
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_median = pd.concat([df, df.ta.median()], axis=1)
			df_median = df_median.tail(1)
			df_median = df_median.iloc[:, [6]]
			res_median = round((df_median.iloc[0,0]),6)  
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_median


def stat_quantile(symbol, tf='4h', limit=500):
	'''Показатели статистики quantile для выбранного таймфрейма и инструмента'''
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_quantile = pd.concat([df, df.ta.quantile()], axis=1)
			df_quantile = df_quantile.tail(1)
			df_quantile = df_quantile.iloc[:, [6]]
			res_quantile = round((df_quantile.iloc[0,0]),6)  
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_quantile


def stat_variance(symbol, tf='4h', limit=500):
	'''Показатели статистики variance для выбранного таймфрейма и инструмента'''
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_variance = pd.concat([df, df.ta.variance()], axis=1)
			df_variance = df_variance.tail(1)
			df_variance = df_variance.iloc[:, [6]]
			res_variance = round((df_variance.iloc[0,0]),6)  
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_variance


def stat_mad(symbol, tf='4h', limit=500):
	'''Показатели статистики mad для выбранного таймфрейма и инструмента'''
	try:
		ohlcv = exchange.fetch_ohlcv(symbol, tf)
		if len(ohlcv):
			df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
			df_mad = pd.concat([df, df.ta.mad()], axis=1)
			df_mad = df_mad.tail(1)
			df_mad = df_mad.iloc[:, [6]]
			res_mad = round((df_mad.iloc[0,0]),6)  
	except Exception as e:
		print(type(e).__name__, str(e))
	return res_mad


def main():
	pass

if __name__ == '__main__':
	main()
