'''
Does some very basic statistics between nonlinear and linear (with various thresholding) models

'''

import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts


tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]

for t in tasks:
	print t

	iFile = csv.reader(open('./topModels/bestExpressionsError-NL-' + t +'-RL.txt','r'))
	NL = []
	for l in iFile:
		NL.append(float(l[0]))
	NL = np.array(NL)

	iFile = csv.reader(open('./topModels/bestExpressionsError-L-FDR-' + t +'-RL.txt','r'))
	FDR = []
	count = 0
	for l in iFile:
		FDR.append(float(l[0]))
		count += 1
		if count == NL.shape[0]:
			break
	FDR = np.array(FDR)

	iFile = csv.reader(open('./topModels/bestExpressionsError-L-BC-' + t +'-RL.txt','r'))
	BC = []
	count = 0
	for l in iFile:
		BC.append(float(l[0]))
		count += 1
		if count == NL.shape[0]:
			break
	BC = np.array(BC)
	
	'''
	iFile = csv.reader(open('bestExpressionsError-L-TOPX-' + t +'.txt','r'))
	TOPX = []
	for l in iFile:
		TOPX.append(float(l[0]))
	TOPX = np.array(TOPX)
	'''

	iFile = csv.reader(open('./topModels/bestExpressionsError-L-DF-' + t +'-RL.txt','r'))
	DF = []
	count = 0
	for l in iFile:
		DF.append(float(l[0]))
		count += 1
		if count == NL.shape[0]:
			break
	DF = np.array(DF)


	print "NL MEAN, STD:", np.mean(NL), np.std(NL)
	print "L-FDR MEAN, STD, manWhitU:", np.mean(FDR), np.std(FDR), sts.mannwhitneyu(NL, FDR).pvalue
	print "L-BC MEAN, STD, manWhitU:", np.mean(BC), np.std(BC), sts.mannwhitneyu(NL, BC).pvalue
	print "L-DF MEAN, STD, manWhitU:", np.mean(DF), np.std(DF), sts.mannwhitneyu(NL, DF).pvalue
	print 
	print
	#plt.scatter(NL, FDR)
	#plt.show()


	#plt.hist(NL, alpha=0.5, bins=100)
	#plt.hist(FDR, alpha=0.5, bins=100)
	#plt.hist(TOPX, alpha=0.5, bins=100)
	#plt.show()
