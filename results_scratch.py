# IPython log file

import get_rets
import get_rets
dif, per, vxx = get_rets.main()
per.head()
per2 = per+1
per2.head()
per2.product()
get_ipython().magic('logstart results_scratch.py')
quit()
