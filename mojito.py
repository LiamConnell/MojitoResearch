



import pandas as pd
from yahoo_finance import Share

start, end = '2011-01-01','2013-12-21'

def price_data(symbol, start=start, end=end):
	x = pd.DataFrame(Share(symbol).get_historical(start, end))
	x.index = x.Date
	return x

def make_IVTS():
	#start, end = '2014-01-01', '2015-10-20'
	vix = price_data('^VIX', start, end)
	vxv = price_data('^VXV', start, end)
	vix = vix.convert_objects(convert_numeric=True)
	vxv = vxv.convert_objects(convert_numeric=True)
	IVTS_1d = vix['Close']/vxv['Close']
	return IVTS_1d

def get_position():
	IVTS = make_IVTS()
	df = pd.DataFrame(IVTS)
	    
	def pos(val):
		if val > 1.02:
			return 1
		if val < 0.92:
			return -1
		else:
			return 0
		    
	df['pos'] = df['Close'].apply(pos)
	return df['pos']


def get_rets():
	position = get_position()
	#start, end = '2014-01-01', '2015-10-20'
	vxx = price_data('VXX', start, end)
	vxx = vxx.convert_objects(convert_numeric=True)
	vxx['diff'] = vxx['Close'].shift(1) - vxx['Close']
	rets = vxx['diff'] * position
	rets2 = (vxx['diff'] * position)/vxx['Close']
	return rets, rets2, vxx

def rets():
	dif, per, vxx = get_rets()
	per2 = per+1
	return per2.product()


if __name__ == '__main__':
	print(rets())





