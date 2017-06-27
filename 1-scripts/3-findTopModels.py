'''
Generates files with some details on each of the top models for each task/subject combo.

The files with the actual expressions in them are used for other scripts for analysis

'''

#finds the top models for each subject
import numpy as np
import csv
import sys

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816]


lastsCount = 0
for t in tasks:
	allBestVal = []
	allBestInd = []
	bestExpressions = []


	oFile = open('./topModels/bestExpressions-NL-' + t + '.txt','w')	
	o2File = open('./topModels/bestExpressionsMSE-NL-' + t + '.txt','w')	
	fs='funcsNL = ['
	count = 0
	
	print t

	for s in subjects:
		try:		
			bestInd = -1;
			bestVal = sys.float_info.max
			iFile = csv.reader(open("../" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z/" + 'stats.csv','r'))
			
			for l in iFile:
				if float(l[1]) < bestVal:
					bestVal = float(l[1])
					bestInd = int(l[0])
			print s, bestInd, bestVal
			allBestVal.append(bestVal)
			allBestInd.append(bestInd)
			
			o2File.write(str(allBestVal[-1]) + '\n')			

			iFile = open("../" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z/"+ str(allBestInd[-1]) + '_line.txt','r')				#CHANGE HERE
			oFile.write('def funcNL_' + str(subjects[count]) + '(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return ' + iFile.next() + '\n')		#CHANGE HERE (in function name)
			fs = fs + "funcNL_" + str(subjects[count]) + ","
			count += 1

			iFile.close()

		except IOError:	
			print "OMGZ@!!1!, " + t + "_" + str(s) + " was not there!!!!"			
			continue


	fs = fs + "]"
	oFile.write("\n" + fs)
	oFile.close()
	o2File.close()
	#print min(allBestVal)

	lastsCount += 1






