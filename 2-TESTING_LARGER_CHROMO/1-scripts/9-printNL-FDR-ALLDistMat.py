'''
prints the matrix for generated for linear on LR on LR data.
'''

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816, 103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923, 106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123, 109325, 110411, 111312, 111413, 111514, 111716, 112819, 113215, 113619, 113821, 113922, 114419, 114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111, 120212, 120515, 121315, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422, 124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013, 130316, 130922, 131217, 131722, 131924, 132118, 133019, 133625, 133827, 133928, 134324, 135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231, 138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142424, 142626, 142828, 143325, 144226, 144832, 145531, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816]

pltz = []


iFile =  csv.reader(open('abEmat_NL_opt.csv', 'r'))

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

print abeMat


iFile =  csv.reader(open('msEmat_NL_opt.csv', 'r'))
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


avgMatTask = np.zeros((len(tasks),len(tasks)))

for i in range(len(tasks)):
	for j in range(len(tasks)):
		avgMatTask[i,j] = np.nanmean(abeMat[i * len(subjects):(i+1)* len(subjects),j * len(subjects):(j+1)* len(subjects)])

axes = plt.subplot2grid((1,3), (0,0))
pltz.append(axes)
img = pltz[0].matshow(avgMatTask)
#pltz[0].colorbar(label='Mean Absolute Error Averaged Over All Subjects')
pltz[0].set_title('Best Nonlinear Models')
pltz[0].set_xlabel('Models')
pltz[0].set_ylabel('Data')

#plt.xticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"])
#plt.yticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"], rotation =90)
pltz[0].set_xticks(range(0,len(tasks)))
pltz[0].set_xticklabels(["E", "G", "L", "M", "R", "S", "W"])
pltz[0].set_yticks(range(0,len(tasks)), ["E", "G", "L", "M", "R", "S", "W"])
pltz[0].set_yticklabels(["E", "G", "L", "M", "R", "S", "W"], rotation =90)
#pltz[0].legend()

for asd, cas in enumerate(avgMatTask):
	for sdf, c in enumerate(cas):
			pltz[0].text(sdf-.4, asd+.2, "%.2f" % c)


#plt.show()



# FDR


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



avgMatTask = np.zeros((len(tasks),len(tasks)))

for i in range(len(tasks)):
	for j in range(len(tasks)):
		avgMatTask[i,j] = np.nanmean(abeMat[i * len(subjects):(i+1)* len(subjects),j * len(subjects):(j+1)* len(subjects)])
	

axes = plt.subplot2grid((1,3), (0,1))
pltz.append(axes)
img = pltz[1].matshow(avgMatTask)
#pltz[0].colorbar(label='Mean Absolute Error Averaged Over All Subjects')
pltz[1].set_title('Best Linear Models - FDR')
pltz[1].set_xlabel('Models')
pltz[1].set_ylabel('Data')

#plt.xticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"])
#plt.yticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"], rotation =90)
pltz[1].set_xticks(range(0,len(tasks)))
pltz[1].set_xticklabels(["E", "G", "L", "M", "R", "S", "W"])
pltz[1].set_yticks(range(0,len(tasks)), ["E", "G", "L", "M", "R", "S", "W"])
pltz[1].set_yticklabels(["E", "G", "L", "M", "R", "S", "W"], rotation =90)
#pltz[0].legend()


for asd, cas in enumerate(avgMatTask):
	for sdf, c in enumerate(cas):
			pltz[1].text(sdf-.4, asd+.2, "%.2f" % c)






# All Lin


iFile =  csv.reader(open('abEmat_L_LR-TOP30.csv', 'r'))

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



iFile =  csv.reader(open('msEmat_L_LR-TOP30.csv', 'r'))
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


avgMatTask = np.zeros((len(tasks),len(tasks)))

for i in range(len(tasks)):
	for j in range(len(tasks)):
		avgMatTask[i,j] = np.nanmean(abeMat[i * len(subjects):(i+1)* len(subjects),j * len(subjects):(j+1)* len(subjects)])


axes = plt.subplot2grid((1,3), (0,2))
pltz.append(axes)
img = pltz[2].matshow(avgMatTask)
#pltz[0].colorbar(label='Mean Absolute Error Averaged Over All Subjects')
pltz[2].set_title('Best Linear Models - All ROI')
pltz[2].set_xlabel('Models')
pltz[2].set_ylabel('Data')

#plt.xticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"])
#plt.yticks(range(51,102*7, 102), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"], rotation =90)
pltz[2].set_xticks(range(0,len(tasks)))
pltz[2].set_xticklabels(["E", "G", "L", "M", "R", "S", "W"])
pltz[2].set_yticks(range(0,len(tasks)), ["E", "G", "L", "M", "R", "S", "W"])
pltz[2].set_yticklabels(["E", "G", "L", "M", "R", "S", "W"], rotation =90)
#pltz[0].legend()


for asd, cas in enumerate(avgMatTask):
	for sdf, c in enumerate(cas):
			pltz[2].text(sdf-.4, asd+.2, "%.2f" % c)

divider = make_axes_locatable(axes)
cax = divider.append_axes("right", size="5%", pad=0.50)

plt.colorbar(img, cax=cax, label='Mean Absolute Error Averaged Over All Subjects')
plt.show()


