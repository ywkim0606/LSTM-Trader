import pandas as pd
import util

# Momentum
def momentum(df, n):
	momentum = df.copy()
	momentum = momentum / momentum.shift(n) - 1
	momentum.ix[0:n] = 0
	return momentum

# Simple Moving Average
def SMA(df, n):
	SMA = df.rolling(n).mean()
	return SMA

# Exponential Moving Average
def EMA(df, n):
	alpha = 2.0 / (n + 1)
	EMA = df.copy()
	EMA.ix[0, :] = df.ix[0, :]
	for i in range(1, df.shape[0]):
		EMA.ix[i, :] = (1-alpha) * EMA.ix[i-1, :] + alpha * df.ix[i, :]
	return EMA

# Bollinger Band
def BB(df, n, func=SMA):
	sma = func(df, n)

	std = df.rolling(n).std()

	BB = [sma - std, sma + std]
	return BB

