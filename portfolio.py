class Portfolio:
	def __init__(self, budget, symbols):
		self.budget = budget
		self.symbols = symbols
		self.symbols_index = {symbols[i]: i for i in range(len(symbols))}
		self.portfolio = [0 for i in range(len(symbols))]
	def buy_stock(self, symbol, stock_price, shares):
		if stock_price * shares > self.budget:
			print ('The price of the stock exceeds the budget')
			return 0
		else:
			self.budget -= stock_price * shares
			self.portfolio[self.symbols_index[symbol]] += shares
			return shares

	def sell_stock(self, symbol, stock_price, shares):
		if self.portfolio[self.symbols_index[symbol]] < shares:
			print ('We cannot sell more stocks than we have')
			return 0
		else:
			self.budget += stock_price * shares
			self.portfolio[self.symbols_index[symbol]] -= shares
			return shares
	def evaluate_portfolio(self, stock_prices_today):
		portval = self.budget
		for i in range(len(stock_prices_today)):
			portval += stock_prices_today[i] * self.portfolio[i]
		return portval
