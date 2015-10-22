# IPython log file
def main():
	import get_rets
	dif, per, vxx = get_rets.main()
	per2 = per+1
	return per2.product()
