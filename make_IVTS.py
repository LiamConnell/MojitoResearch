# IPython log file
def main():
	import vix_scratchpad
	start, end = '2014-01-01', '2015-10-20'
	vix = vix_scratchpad.price_data('VIX', start, end)
	vxv = vix_scratchpad.price_data('^VXV', start, end)
	vix = vix.convert_objects(convert_numeric=True)
	vxv = vxv.convert_objects(convert_numeric=True)
	IVTS_1d = vix['Close']/vxv['Close']
	return IVTS_1d
