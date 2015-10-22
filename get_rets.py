# IPython log file

def main():
	import get_position
	position = get_position.main()
	import vix_scratchpad
	start, end = '2014-01-01', '2015-10-20'
	vxx = vix_scratchpad.price_data('VXX', start, end)
	vxx = vxx.convert_objects(convert_numeric=True)
	vxx['diff'] = vxx['Close'].shift(1) - vxx['Close']
	rets = vxx['diff'] * position
	rets2 = (vxx['diff'] * position)/vxx['Close']
	return rets, rets2, vxx
