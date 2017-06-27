'''

Makes files called 'allExpressions-NL...' which collects ALL the expressions into large files. They are used to find the best models for RL!

'''
import numpy as np
import csv
import sys

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816]


lastsCount = 0
count = 0
#oFile = open('allExpressions-NL.txt','w')	
#fs='funcsNL = ['
for t in tasks:
	oFile = open('./topModels/allExpressions-NL-' + t + '.txt','w')	
	fs='funcsNL = ['




	for s in subjects:
		print t, s
		for i in range(100):
			try:		
				

				iFile = open("../" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z/"+ str(i) + '_line.txt','r')				#CHANGE HERE
				oFile.write('def funcNL_' + str(count) + '(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return ' + iFile.next() + '\n')		#CHANGE HERE (in function name)
				fs = fs + "funcNL_" + str(count) + ","
				count += 1

				iFile.close()

			except IOError:	
				print "OMGZ@!!1!, " + t + "_" + str(s) + " was not there!!!!"	
				print "\t../" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z/"+ str(i) + '_line.txt'		
				continue
	lastsCount += 1
	fs = fs + '\n'

	fs = fs + "]"
	oFile.write("\n" + fs)
	oFile.close()
	#print min(allBestVal)








