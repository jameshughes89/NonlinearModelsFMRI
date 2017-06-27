'''
prints the matrix for generated for linear on LR on LR data.
'''

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816, 103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923, 106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123, 109325, 110411, 111312, 111413, 111514, 111716, 112819, 113215, 113619, 113821, 113922, 114419, 114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111, 120212, 120515, 121315, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422, 124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013, 130316, 130922, 131217, 131722, 131924, 132118, 133019, 133625, 133827, 133928, 134324, 135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231, 138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142424, 142626, 142828, 143325, 144226, 144832, 145531, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816]


iFile =  csv.reader(open('abEmat_L_LR-FDR.csv', 'r'))

abeMat = []
for l in iFile:
	abeMat.append(l)
abeMat = np.array(abeMat)
abeMat = abeMat.astype(np.float)


for i in range(len(abeMat)):
	for j in range(len(abeMat[i])):
		#abeMat[i][j] = log(abeMat[i][j])
		if abeMat[i][j] > 1 :
			abeMat[i][j] = np.float('nan')
			#abeMat[i][j] = np.float(1)



iFile =  csv.reader(open('msEmat_L_LR-FDR.csv', 'r'))
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


plt.matshow(abeMat)
#plt.colorbar(ticks=[0,0.25,0.5,0.75,1.0])
plt.colorbar()
plt.title('Error Matrix for All Models on Every Subject (Linear)')
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


avgMatTask = np.zeros((len(tasks),len(tasks)))

for i in range(len(tasks)):
	for j in range(len(tasks)):
		avgMatTask[i,j] = np.nanmean(abeMat[i * len(subjects):(i+1)* len(subjects),j * len(subjects):(j+1)* len(subjects)])
	
plt.matshow(avgMatTask)
plt.colorbar(label='Mean Absolute Error Averaged Over All Subjects')
plt.title('Best Linear Models - FDR')
plt.xlabel('Models')
plt.ylabel('Data')

#plt.xticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"])
#plt.yticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"], rotation =90)
plt.xticks(range(0,len(tasks)), ["E", "G", "L", "M", "R", "S", "W"])
plt.yticks(range(0,len(tasks)), ["E", "G", "L", "M", "R", "S", "W"], rotation =90)
plt.legend()

for asd, cas in enumerate(avgMatTask):
	for sdf, c in enumerate(cas):
			plt.text(sdf-.4, asd+.2, "%.2f" % c)


plt.show()

#######
#######

iFile =  csv.reader(open('minmat_L_LR.csv', 'r'))

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

