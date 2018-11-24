import util
import indicators
import pandas as pd
import portfolio
import math
class naive_agent:
	def __init__(self, df, symbols, window_size):
		self.df = df
		self.window_size = window_size
		self.my_portfolio = portfolio.Portfolio(budget, symbols)
	def train(self):
		pass
	def invest(self, symbol, start_date, end_date, budget):
		BB = indicators.BB(self.df, self.window_size, 
			func=indicators.EMA)
		bb_0, bb_1 = BB
		date_range = pd.date_range(start_date, end_date)

		for today in date_range:
			today_price = df[today:today]
			if today_price.shape[0] == 0:
				continue
			else:
				today_price = today_price.iloc[0,0]
				today_bb_0 = bb_0[today:today].iloc[0,0]
				today_bb_1 = bb_1[today:today].iloc[0,0]
				if today_bb_0 > today_price:
					# BUY
					shares = math.floor(self.my_portfolio.budget / today_price)
					self.my_portfolio.buy_stock(symbol, today_price, shares)
				elif today_bb_1 < today_price:
					# SELL
					shares = self.my_portfolio.symbols_index[symbol]
					self.my_portfolio.sell_stock(symbol, today_price, shares)
				else:
					# WAIT
					continue
if __name__ == "__main__":
	start_date = '2015-01-01'
	end_date = '2018-11-23'
	budget = 1000000
	df = util.read_data(['GOOG'], start_date, end_date)
	agent = naive_agent(df, ['GOOG'], 20)
	agent.invest('GOOG', start_date, end_date, budget)
	stock_prices_today = [df['2018-11-23':'2018-11-23'].iloc[0,0]]
	print (agent.my_portfolio.evaluate_portfolio(stock_prices_today))