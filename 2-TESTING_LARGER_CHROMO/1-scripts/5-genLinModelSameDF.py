#generates a model with OLS in a weird way

import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import thresh_methods as tm



tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
DF = [-8, -8, -9, -10, -8, -9, -10]			# This number should include the left hand side of the equation in the count (we remove the left hand side below)
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816]

lastsCount = 0

for t in tasks:
	bestExpressions = []
	oFile = open('./topModels/bestExpressions-L-DF-' + t + '.txt','w')	
	o2File = open('./topModels/bestExpressionsError-L-DF-' + t + '.txt','w')	
	fs='funcsL = ['
	count = 0
	for s in subjects:
		try:		
			X = []
			y = []
			ALL = []

			iFile = csv.reader(open("/media/james/My Passport/HCP/HCP-Processed/" +t + "/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z.csv",'r'))
			for l in iFile:
				X.append(l[:-1])
				y.append(l[-1])
				ALL.append(l)

			ALL = np.array(ALL)
			ALL = ALL.astype(float)
	
			X = np.array(X)
			y = np.array(y)
			X = X.astype(float)
			y = y.astype(float)
	
			nTRs = len(y)

			corrC = np.corrcoef(ALL.T)
			corrC = np.abs(corrC)					# DO ABS here because negative correlatoion is fine!
			topX = np.argsort(corrC[-1,:])[DF[lastsCount]:]		# Take all the top X, INCLUDING left hand side
			topX = np.sort(topX)
			print topX
			signif = topX[:-1]						# remove left hand side here.  (so the math checks out here)	
			print signif
			X = X.T[signif]	
			X = X.T

			#OLS STUFF
			X = sm.add_constant(X)
			rez = sm.OLS(y, X).fit()
			B = rez.params
			print t, s
			eqn = str(B[0]) + " * 1 + "
	
			for i in range(1, len(B)):
				eqn = eqn + str(B[i]) + " * v" + str(signif[i-1])
				if i != len(B)-1:
					eqn = eqn + " + "
				#eqn = eqn + str(B[i]) + " * v[i] + "
	
			oFile.write('def funcL_' + str(subjects[count]) + '(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return ' + eqn + '\n')		#CHANGE HERE (in function name)
			fs = fs + "funcL_" + str(subjects[count]) + ","

			count += 1
			
			resids = rez.resid
			resids = [abs(x) for x in resids]
			error = np.mean(resids)		
			o2File.write(str(error) + '\n')
		except IOError:
			print "OMGZ@!!1!, " + t + "_" + str(s) + " was not there!!!!"			
			continue
		
	fs = fs + "]"
	oFile.write("\n" + fs)
	oFile.close()
	o2File.close()

	lastsCount += 1

	









