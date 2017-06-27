'''
Takes the expressions (have to copy and paste, sorry, should make better...) and generate their absolute error (as opposed to MSE)
'''

import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr  

def funcNL_WM_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v15 + ( v17 - v8 ) ) + v22 ) + ( ( ( v17 - v8 ) + v1 ) + v24 ) ) / ( v18 + ( 9.02977470006839 - v8 ) ) ) - ( ( v13 / ( -4.456626583244901 - ( v13 * v13 ) ) ) - ( ( ( ( v15 + ( v17 - v8 ) ) + v22 ) + ( ( ( v17 - v8 ) + v1 ) + v24 ) ) / ( v18 + ( 9.02977470006839 - v8 ) ) ) ) ) 
def funcNL_WM_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v15 + ( v22 + v7 ) ) + ( v19 + v16 ) ) + ( v4 +sin( v5 )) ) / ( (cos( ( v4 +sin( v5 )) )- -5.1566955593857955 ) -cos( v12 )) ) 
def funcNL_WM_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v19 + ( ( v16 - ( ( v27 - v12 ) - v15 ) ) - ( v0 - v21 ) ) ) / 3.5889879111626826 ) 
def funcNL_WM_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v17 - v2 ) + v22 ) /tan( 16.974411051088403 )) + ( ( v7 / ( 3.784393766999795 -cos( ( v25 + ( v26 - ( ( v17 - v2 ) + v22 ) ) ) )) ) + ( ( ( v25 + v24 ) /tan( 16.974411051088403 )) / (exp( ( ( ( v17 - v2 ) + v22 ) - ( (sin( v17 )+ v22 ) +sin( v17 )) ) )+tan( 16.974411051088403 )) ) ) ) 
def funcNL_WM_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  (tan( 19.085481284967507 )* ( ( ( ( ( v28 +cos( v23 )) -cos( v16 )) *cos(cos( v0 ))) + ( ( ( -0.5589172932348632 * v23 ) + v25 ) + v20 ) ) + ( v21 + v6 ) ) ) 
def funcNL_WM_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v17 * 2.0386042895790304 ) - ( ( v23 + v28 ) - ( ( v3 / 2.0386042895790304 ) - ( v25 / 2.0386042895790304 ) ) ) ) / (sin( ( ( v3 / 2.0386042895790304 ) / ( ( v17 * 2.0386042895790304 ) - ( ( v23 + v28 ) - ( ( v3 / 2.0386042895790304 ) - ( v25 / 2.0386042895790304 ) ) ) ) ) )- (cos( v15 )- -2.9728012310320366 ) ) ) - ( ( ( v19 - v13 ) / -7.707381734472204 ) - v17 ) ) 
def funcNL_WM_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( v21 - ( ( ( ( ( ( v21 - v15 ) - v20 ) + v21 ) - ( v22 - v8 ) ) -sin( v25 )) *tan( 9.651050279986023 )) ) 
def funcNL_WM_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( ( ( v26 + v2 ) / -6.420486471276794 ) - v4 ) + v22 ) + v21 ) * 0.7008306330487386 ) + ( ( ( ( v20 + v2 ) - ( ( ( v22 * ( ( ( ( v26 + v2 ) / -6.420486471276794 ) - v4 ) + v22 ) ) / -6.420486471276794 ) * ( ( v22 * ( ( ( ( v26 + v2 ) / -6.420486471276794 ) - v4 ) + v22 ) ) / -6.420486471276794 ) ) ) - ( v22 + ( v21 - v4 ) ) ) /exp(cos(sin( v4 )))) ) 
def funcNL_WM_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( (sin( v5 )* ( (cos( v26 )- v27 ) / ( -10.108020027571879 / v2 ) ) ) - ( ( v11 / -5.153613730886985 ) + ( ( ( ( v27 - ( v5 + v21 ) ) - v20 ) - v15 ) / 3.905091444534264 ) ) ) 
def funcNL_WM_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v21 - ( (abs( ( -3.695201159204366 +sin( v8 )) )/ -16.76367106413575 ) * ( v22 - (sin( v13 )+ ( v21 -sin( ( -3.695201159204366 - v21 ) )) ) ) ) ) + ( ( ( (abs( ( -3.695201159204366 +sin( v8 )) )/ -16.76367106413575 ) * ( v4 - v21 ) ) * ( -3.695201159204366 +sin( v8 )) ) * ( ( -3.695201159204366 - v21 ) / -6.820122196040085 ) ) ) 

funcsNL = [funcNL_WM_100307,funcNL_WM_100408,funcNL_WM_101006,funcNL_WM_101107,funcNL_WM_101309,funcNL_WM_101410,funcNL_WM_101915,funcNL_WM_102008,funcNL_WM_102311,funcNL_WM_102816,]

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


tasks = ["WM"]
lasts = ["21"]
#tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
#lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816]


outData = []
lastsCount = 0
for t in tasks:
	allError = 0
	allErrorList = []
	count = 0
	oFile = open('./topModels/bestExpressionsError-NL-' + t + '-RL.txt','w')
	for index, s in enumerate(subjects):
		try:
			inFile = csv.reader(open("/media/james/My Passport/HCP/HCP-Processed/" +t + "/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_RL_Z.csv",'r'))
			singleError = 0
			numLines = 0
			v0 = []
			v1 = []
			v2 = []
			v3 = []
			v4 = []
			v5 = []
			v6 = []
			v7 = []
			v8 = []
			v9 = []
			v10 = []
			v11 = []
			v12 = []
			v13 = []
			v14 = []
			v15 = []
			v16 = []
			v17 = []
			v18 = []
			v19 = []
			v20 = []
			v21 = []
			v22 = []
			v23 = []
			v24 = []
			v25 = []
			v26 = []
			v27 = []
			v28 = []
			v29 = []
			for l in inFile:
				v0.append(float(l[0]))
				v1.append(float(l[1]))
				v2.append(float(l[2]))
				v3.append(float(l[3]))
				v4.append(float(l[4]))
				v5.append(float(l[5]))
				v6.append(float(l[6]))
				v7.append(float(l[7]))
				v8.append(float(l[8]))
				v9.append(float(l[9]))
				v10.append(float(l[10]))
				v11.append(float(l[11]))
				v12.append(float(l[12]))
				v13.append(float(l[13]))
				v14.append(float(l[14]))
				v15.append(float(l[15]))
				v16.append(float(l[16]))
				v17.append(float(l[17]))
				v18.append(float(l[18]))
				v19.append(float(l[19]))
				v20.append(float(l[20]))
				v21.append(float(l[21]))
				v22.append(float(l[22]))
				v23.append(float(l[23]))
				v24.append(float(l[24]))
				v25.append(float(l[25]))
				v26.append(float(l[26]))
				v27.append(float(l[27]))
				v28.append(float(l[28]))
				v29 .append(float(l[29]))
			
			Xs = range(len(v29))

			YsNL = []
			YsL = []
			yNLabs = 0
			yLabs = 0
			diffabs = 0

			yNLmse = 0
			yLmse = 0
			diffmse = 0


			for i in range(len(v29)):
				#use count, it works when skilling subjects. 
				try:
					yNL = funcsNL[count](v0[i],v1[i],v2[i],v3[i],v4[i],v5[i],v6[i],v7[i],v8[i],v9[i],v10[i],v11[i],v12[i],v13[i],v14[i],v15[i],v16[i],v17[i],v18[i],v19[i],v20[i],v21[i],v22[i],v23[i],v24[i],v25[i],v26[i],v27[i],v28[i],v29[i])
				#yL = funcsL[index](v0[i],v1[i],v2[i],v3[i],v4[i],v5[i],v6[i],v7[i],v8[i],v9[i],v10[i],v11[i],v12[i],v13[i],v14[i],v15[i],v16[i],v17[i],v18[i],v19[i],v20[i],v21[i],v22[i],v23[i],v24[i],v25[i],v26[i],v27[i],v28[i],v29[i])
				except OverflowError:
					print "\tOverrrrflow!"
					yNL = np.mean(yNLabs)

				yNLabs = yNLabs + abs(yNL - v29[i])			
				#yLabs = yLabs + abs(yL - v29[i])
				#diffabs = diffabs + abs(yNL - yL)

				#yNLmse = yNLmse + (yNL - v29[i])**2
				#yLmse = yLmse + (yL - v29[i])**2
				#diffmse = diffmse + (yNL - yL)**2

				#Ys.append(y)
				#YsL.append(yL)

			yNLabs = yNLabs/len(v29)
			#yLabs = yLabs/len(v29)
			#diffabs = diffabs/len(v29)		
			#yNLmse = yNLmse/len(v29)
			#yLmse = yLmse/len(v29)
			#diffmse = diffmse/len(v29)	

			#print s, yNLabs, yLabs, diffabs, yNLmse, yLmse, diffmse
			#outData.append([yNLabs])

			print t, s, yNLabs			
			
			oFile.write(str(yNLabs) + '\n')			
			'''	
			print yabs/len(v29)
			print yLabs/len(v29)
			print diffabs/len(v29)
			print "------"
			print ymse/len(v29)
			print yLmse/len(v29)
			print diffmse/len(v29)
		

			#plt.plot(Xs, v29 'go')
			plt.plot(Xs, v29 'b', label='measured')
			plt.plot(Xs, Ys, 'r', label='SR-butLin')
			plt.plot(Xs, YsL, 'g', label='GLM-Top 3')
			plt.legend()
			plt.show()
			'''

			count += 1		#ONLY INCREASE COUNT WHEN WE SUCESSFULLY DID EVAL
	
		except IOError:	
			print "OMGZ@!!1!, " + t + "_" + str(s) + " was not there!!!!"			
			continue
			
		

	lastsCount += 1
	oFile.close()



