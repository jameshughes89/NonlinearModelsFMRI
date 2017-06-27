#finds the top models for each subject

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt

iFile =  csv.reader(open('abEmat_NL_RL_opt.csv', 'r'))

abeMat = []
for l in iFile:
	abeMat.append(l)
abeMat = np.array(abeMat)
abeMat = abeMat.astype(np.float)


for i in range(len(abeMat)):
	for j in range(len(abeMat[i])):
		abeMat[i][j] = log(abeMat[i][j])
		if abeMat[i][j] > 1 :
			#abeMat[i][j] = np.float('nan')
			abeMat[i][j] = np.float(1)



iFile =  csv.reader(open('msEmat_NL_RL_opt.csv', 'r'))
mseMat = []
for l in iFile:
	mseMat.append(l)
mseMat = np.array(mseMat)
mseMat = mseMat.astype(np.float)


for i in range(len(mseMat)):
	for j in range(len(mseMat[i])):
		if mseMat[i][j] > 2.5 :
			#mseMat[i][j] = np.float('nan')
			mseMat[i][j] = np.float(2.5)



font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 6}

matplotlib.rc('font', **font)


plt.matshow(abeMat)
#plt.colorbar(ticks=[0,0.25,0.5,0.75,1.0])
plt.colorbar()
plt.title('Error Matrix for All Models on Every Subject (Nonlinear)')
plt.xlabel('Models')
plt.ylabel('Data')

#plt.xticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"])
#plt.yticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"], rotation =90)
plt.xticks(range(5,10*7, 10), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"])
plt.yticks(range(5,10*7, 10), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"], rotation =90)

for i in range(10,10*7, 10):
#for i in range(102,102*7, 102):
	plt.axvline(float(i) - 0.5, color='k', linewidth=2)
	plt.axhline(float(i) - 0.5, color='k', linewidth=2)

'''
plt.axvline(101.5, color='k', linewidth=2)
plt.axvline(203.5, color='k', linewidth=2)
plt.axvline(305.5, color='k', linewidth=2)
plt.axvline(407.5, color='k', linewidth=2)
plt.axvline(509.5, color='k', linewidth=2)
plt.axvline(611.5, color='k', linewidth=2)

plt.axhline(101.5, color='k', linewidth=2)
plt.axhline(203.5, color='k', linewidth=2)
plt.axhline(305.5, color='k', linewidth=2)
plt.axhline(407.5, color='k', linewidth=2)
plt.axhline(509.5, color='k', linewidth=2)
plt.axhline(611.5, color='k', linewidth=2)
'''



plt.show()
#######
#######
iFile =  csv.reader(open('minmat_NL_RL_opt.csv', 'r'))

minMat = []
for l in iFile:
	minMat.append(l)
minMat = np.array(minMat)
minMat = minMat.astype(np.float)

plt.matshow(minMat)
plt.title('Best Model (Nonlinaer)')
plt.xlabel('Models')
plt.ylabel('Data')

#plt.xticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"])
#plt.yticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"], rotation =90)
plt.xticks(range(5,10*7, 10), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"])
plt.yticks(range(5,10*7, 10), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"], rotation =90)

for i in range(10,10*7, 10):
#for i in range(102,102*7, 102):
	plt.axvline(float(i) - 0.5, color='k', linewidth=2)
	plt.axhline(float(i) - 0.5, color='k', linewidth=2)

'''
plt.xticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"])
plt.yticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"], rotation =90)
plt.axvline(101.5, color='k', linewidth=2)
plt.axvline(203.5, color='k', linewidth=2)
plt.axvline(305.5, color='k', linewidth=2)
plt.axvline(407.5, color='k', linewidth=2)
plt.axvline(509.5, color='k', linewidth=2)
plt.axvline(611.5, color='k', linewidth=2)

plt.axhline(101.5, color='k', linewidth=2)
plt.axhline(203.5, color='k', linewidth=2)
plt.axhline(305.5, color='k', linewidth=2)
plt.axhline(407.5, color='k', linewidth=2)
plt.axhline(509.5, color='k', linewidth=2)
plt.axhline(611.5, color='k', linewidth=2)
'''
plt.show()

