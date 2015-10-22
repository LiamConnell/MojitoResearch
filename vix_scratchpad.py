# IPython log file
import pandas as pd
from yahoo_finance import Share

start, end = '2014-01-01','2015-10-21'

def price_data(symbol, start=start, end=end):
	x = pd.DataFrame(Share(symbol).get_historical(start, end))
	x.index = x.Date
	return x


def main():
	start, end = '2014-01-01','2015-10-21'
	vxx = price_data('VXX', start, end)
