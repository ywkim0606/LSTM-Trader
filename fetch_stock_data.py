from pandas_datareader import data
import pandas as pd
import datetime
import os

def download_csv(symbols, start_date=None, end_date=None, path='data'):
	if start_date == None:
		start_date = '2010-01-01'
	if end_date == None:
		end_date = datetime.datetime.today().strftime('%Y-%m-%d')
	for symbol in symbols:
		df = data.DataReader(symbol, 'yahoo', start_date, end_date)
		df.to_csv(os.path.join(path, symbol + '.csv'))

if __name__ == "__main__":
	# Testing purpose
	#symbols = ['AAPL', 'GOOG', 'FB', 'AMZN']
	symbols = ['SPY']
	download_csv(symbols)