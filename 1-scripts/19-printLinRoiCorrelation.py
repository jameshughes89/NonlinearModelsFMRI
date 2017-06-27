#finds the top models for each subject
import numpy as np
import csv
import sys
import matplotlib.pylab as plt
import matplotlib

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816]

#tasks = ["MOTOR"]
#lasts = ["21"]
#subjects =[100307]

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 10}

matplotlib.rc('font', **font)

'''
iFile =  csv.reader(open('roiCount_L.csv', 'r'))

roiMat = []
for l in iFile:
	roiMat.append(l)
roiMat = np.array(roiMat)
roiMat = roiMat.astype(np.float)
'''


allVarCounts = []


count = 0
lastsCount = 0
for t in tasks:
	for s in subjects:
			print t, s
		#try:	
			fcount = np.zeros(30)	
			ALL = []
			iFile = csv.reader(open("/media/james/My Passport/HCP/HCP-Processed/" +t + "/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z.csv",'r'))
			for l in iFile:
				ALL.append(l)

			ALL = np.array(ALL)
			ALL = ALL.astype(float)

			corrC = np.corrcoef(ALL.T)
			#topX = np.argsort(corrC[-1,:])[-1*int(np.sum(roiMat[count])):]
			topX = corrC[-1,:]
			topX = np.abs(topX)

			topX[-1] = topX[int(lasts[lastsCount]) - 1]
			topX[int(lasts[lastsCount]) - 1] = 1			
			allVarCounts.append(topX)


			count+=1

	lastsCount+=1

#np.savetxt('roiCount_L.csv', allVarCounts, delimiter=",")

plt.matshow(allVarCounts, aspect='auto')
plt.colorbar()
plt.title('ROI Correlation Coefficient for Each Model (Linear)')
plt.xlabel('ROI')
plt.ylabel('Model')

plt.xticks(range(0,30), ["ROI 1", "ROI 2", "ROI 3", "ROI 4", "ROI 5", "ROI 6", "ROI 7", "ROI 8", "ROI 9", "ROI 10", "ROI 11", "ROI 12", "ROI 13", "ROI 14", "ROI 15", "ROI 16", "ROI 17", "ROI 18", "ROI 19", "ROI 20", "ROI 21", "ROI 22", "ROI 23", "ROI 24", "ROI 25", "ROI 26", "ROI 27", "ROI 28", "ROI 29", "ROI 30"])
plt.yticks(range(len(subjects)/2,len(subjects)*7, len(subjects)), ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"], rotation =90)

for i in range(1,7):
	plt.axhline((len(subjects)*i)-0.5, color='k', linewidth=2)
'''
plt.axhline((len(subjects)*1.0)-0.5, color='k', linewidth=2)
plt.axhline((len(subjects)*2.0)-0.5, color='k', linewidth=2)
plt.axhline((len(subjects)*3.0)-0.5, color='k', linewidth=2)
plt.axhline((len(subjects)*4.0)-0.5, color='k', linewidth=2)
plt.axhline((len(subjects)*5.0)-0.5, color='k', linewidth=2)
plt.axhline((len(subjects)*6.0)-0.5, color='k', linewidth=2)
'''


#_#_#_#_#_#
compMat = []
compMat.append(np.mean(allVarCounts[len(subjects)*0:len(subjects)*1], axis=0))
compMat.append(np.mean(allVarCounts[len(subjects)*1:len(subjects)*2], axis=0))
compMat.append(np.mean(allVarCounts[len(subjects)*2:len(subjects)*3], axis=0))
compMat.append(np.mean(allVarCounts[len(subjects)*3:len(subjects)*4], axis=0))
compMat.append(np.mean(allVarCounts[len(subjects)*4:len(subjects)*5], axis=0))
compMat.append(np.mean(allVarCounts[len(subjects)*5:len(subjects)*6], axis=0))
compMat.append(np.mean(allVarCounts[len(subjects)*6:len(subjects)*7], axis=0))



plt.matshow(compMat, aspect='auto')
plt.colorbar(label='Correlation Coeffieient')
plt.title('Average ROI Correlation Coefficient and Rank')
plt.xlabel('ROI')
plt.ylabel('Model')

plt.xticks(range(0,30), ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"])
plt.yticks(range(0,7), ["E", "G", "L", "M", "R", "S", "W"], rotation =90)

compMat = np.array(compMat)
ranks = []
for row in compMat:
	ranks.append(np.argsort(row))
ranks = np.array(ranks)

place = np.zeros(compMat.shape)
for i in range(compMat.shape[0]):
	for j in range(compMat.shape[1]):
		place[i,ranks[i,j]] = 30 - j

place = place.astype('int')

for asd, cas in enumerate(compMat):
	for sdf, c in enumerate(cas):
		if c>0:
			plt.text(sdf-.4, asd+.2, str("%.2F"%c) + "\n  " + str(place[asd][sdf]), fontsize=8)

plt.show()


