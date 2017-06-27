'''
Does some very basic statistics between nonlinear and linear (with various thresholding) models

'''

import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts


tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]

NL_all = []
DF_all = []
BC_all = []
FDR_all = []
T30_all = []

for t in tasks:
	print t

	iFile = csv.reader(open('./topModels/bestExpressionsError-NL-' + t +'.txt','r'))
	NL = []
	for l in iFile:
		NL.append(float(l[0]))
	NL = np.array(NL)

	iFile = csv.reader(open('./topModels/bestExpressionsError-L-FDR-' + t +'.txt','r'))
	FDR = []
	count = 0
	for l in iFile:
		FDR.append(float(l[0]))
		count += 1
		if count == NL.shape[0]:
			break
	FDR = np.array(FDR)

	iFile = csv.reader(open('./topModels/bestExpressionsError-L-BC-' + t +'.txt','r'))
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

	iFile = csv.reader(open('./topModels/bestExpressionsError-L-DF-' + t +'.txt','r'))
	DF = []
	count = 0
	for l in iFile:
		DF.append(float(l[0]))
		count += 1
		if count == NL.shape[0]:
			break
	DF = np.array(DF)

	iFile = csv.reader(open('./topModels/bestExpressionsError-L-TOP30-' + t +'.txt','r'))
	T30 = []
	count = 0
	for l in iFile:
		T30.append(float(l[0]))
		count += 1
		if count == NL.shape[0]:
			break
	T30 = np.array(T30)

	'''
	print "NL MEAN, STD:", np.mean(NL), np.std(NL)
	print "L-FDR MEAN, STD, manWhitU:", np.mean(FDR), np.std(FDR), sts.mannwhitneyu(NL, FDR).pvalue
	print "L-BC MEAN, STD, manWhitU:", np.mean(BC), np.std(BC), sts.mannwhitneyu(NL, BC).pvalue
	print "L-DF MEAN, STD, manWhitU:", np.mean(DF), np.std(DF), sts.mannwhitneyu(NL, DF).pvalue
	print "L-30 MEAN, STD, manWhitU:", np.mean(T30), np.std(T30), sts.mannwhitneyu(NL, T30).pvalue
	print 
	print
	'''
	print np.mean(DF)
	print t + ' &\t' + '%.2f' % np.mean(NL) + ' &\t' + '%.2f' % np.std(NL) + ' &\t' + '%.2f' % np.mean(DF) + ' &\t' + '%.2f' % np.std(DF) + ' &\t' + '%.2f' % sts.mannwhitneyu(NL, DF).pvalue + ' &\t' + '%.2f' % np.mean(BC) + ' &\t' + '%.2f' % np.std(BC) + ' &\t' + '%.2f' % sts.mannwhitneyu(NL, BC).pvalue + ' &\t' + '%.2f' % np.mean(FDR) + ' &\t' + '%.2f' % np.std(FDR) + ' &\t' + '%.2f' % sts.mannwhitneyu(NL, FDR).pvalue + ' &\t' + '%.2f' % np.mean(T30) + ' &\t' + '%.2f' % np.std(T30) + ' &\t' + '%.2f' % sts.mannwhitneyu(NL, T30).pvalue


	NL_all.append(NL)
	DF_all.append(DF)
	BC_all.append(BC)
	FDR_all.append(FDR)
	T30_all.append(T30)


coloUrs = ['b', 'g', 'r', 'c', 'm','y','k']
pltz = []
for i in range(len(NL_all)):
	pltz.append(plt.scatter(NL_all[i], BC_all[i], color=coloUrs[i]))
plt.plot(np.arange(0.1,0.6,0.1),np.arange(0.1,0.6,0.1),'--')
plt.legend(pltz,tasks,loc='lower right',)
plt.show()


	#plt.hist(NL, alpha=0.5, bins=100)
	#plt.hist(FDR, alpha=0.5, bins=100)
	#plt.hist(TOPX, alpha=0.5, bins=100)
	#plt.show()

'''
b: blue.
g: green.
r: red.
c: cyan.
m: magenta.
y: yellow.
k: black.
'''
