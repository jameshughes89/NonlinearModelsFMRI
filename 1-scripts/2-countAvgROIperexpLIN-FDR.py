'''
Counts the number of ROI in linear models after false discovery rate

'''

from pylab import *
import csv
import numpy as np
import matplotlib.pyplot as plt
import thresh_methods as tm

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816]



lastsCount = 0
for t in tasks:
	allCounts = []
	avgCount = []

	for s in subjects:
		try:
			fCount = np.zeros(30)
			#print s
			roiCount = 0
			#assumes it's on HDD
			inFile = csv.reader(open("/media/james/My Passport/HCP/HCP-Processed/" +t + "/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z.csv",'r'), delimiter=',')
			ALL = []
			fCount = np.zeros(30)
			for l in inFile:
				ALL.append(l)

			ALL = np.array(ALL)
			nTRs = len(ALL)
			ALL = ALL.astype(float)
			corrC = np.corrcoef(ALL.T)
			corrC = np.abs(corrC)					# DO ABS here because negative correlatoion is fine!
			thr = tm.FDR_thresh_corrmat(corrC, nTRs, alpha=0.05)
			#corrC[corrC < thr] = 0
			DATA = corrC[-1,:]
			
			for i in range(len(DATA)):
				if DATA[i] > thr:
					if i == (int(lasts[lastsCount]) - 1):
						fCount[29] += 1
					elif i == 29:
						fCount[int(lasts[lastsCount]) - 1] += 1
					else:
						fCount[i] += 1

			avgCount.append(sum(fCount))
		except IOError:
			continue			
			#print "OMGZ@!!1!, " + t + "_" + str(s) + " was not there!!!!"

	print t, np.mean(avgCount), np.std(avgCount)
	lastsCount += 1

	#plt.hist(avgCount, alpha=0.5, bins=30)
	#plt.show()

