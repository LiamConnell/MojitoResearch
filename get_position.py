# IPython log file
def main():
	import make_IVTS
	IVTS = make_IVTS.main()
	import pandas as pd
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
