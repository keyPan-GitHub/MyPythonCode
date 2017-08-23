

import sys,time


for i in range(31):
	sys.stdout.write('\r')
	sys.stdout.write("%s%% |%s" % (int(i/30*100), int(i/30*100)*'*'))
	sys.stdout.flush()
	time.sleep(0.2)









