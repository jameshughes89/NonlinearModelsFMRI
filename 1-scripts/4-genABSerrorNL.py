'''
Takes the expressions (have to copy and paste, sorry, should make better...) and generate their absolute error (as opposed to MSE)
'''

import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr  

def funcNL_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v1 + ( v24 + ( v13 + v22 ) ) ) - (sin( ( v17 - v8 ) )- v21 ) ) +sin( ( ( v18 -sin( v24 )) * ( ( v13 + v22 ) / ( v24 + ( v13 + v22 ) ) ) ) )) /abs( 4.284504153887912 )) +sin( ( v17 - v8 ) )) 
def funcNL_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v20 + ( v28 + v22 ) ) + v7 ) / 2.8239522815100315 ) - ( ( ( v21 - v28 ) + ( v16 - v20 ) ) / ( -5.042795142369636 - (sin( ( v20 + ( v28 + v22 ) ) )- v17 ) ) ) ) 
def funcNL_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( 0.25325792136424496 * ( ( v10 + ( ( v26 - ( ( ( v0 - v15 ) - v19 ) - v16 ) ) +sin( ( v16 - v10 ) )) ) - ( v6 - v21 ) ) ) 
def funcNL_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( (tan( 3.264725190388276 )* ( ( v22 - v2 ) + ( v21 + v18 ) ) ) - ( ( (cos( ( -19.28695663346057 + ( v25 + ( (cos( ( v17 - v0 ) )- v12 ) - v12 ) ) ) )+abs(sin( v12 ))) - ( v25 + ( (cos( ( v17 - v0 ) )- v12 ) - v12 ) ) ) *tan( 3.264725190388276 )) ) + ( ( v17 + v22 ) / 3.264725190388276 ) ) 
def funcNL_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v21 / ( 7.69595785634305 + ( -2.9295933861195422 + v22 ) ) ) + ( ( ( v23 - v5 ) - v28 ) / ( ( v5 * v11 ) - ( -6.72862413641532 - ( -2.9295933861195422 + v22 ) ) ) ) ) - ( ( ( v27 + v25 ) - ( ( v23 - v5 ) - v28 ) ) / -2.9295933861195422 ) ) 
def funcNL_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( ( v23 + v17 ) - v4 ) + ( v15 + v28 ) ) / (abs( v27 )+ 4.925500747513102 ) ) - ( v5 / ( ( v1 - 4.020345948024019 ) - v15 ) ) ) - ( ( ( v3 - v20 ) - v22 ) / 4.925500747513102 ) ) 
def funcNL_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v22 / ( (exp( v20 )+ ( v20 - v2 ) ) - -5.080464426686429 ) ) + ( ( ( v27 - ( v20 + ( v1 - ( v8 - ( v5 + v21 ) ) ) ) ) - ( ( v15 + v15 ) + v21 ) ) / -5.080464426686429 ) ) 
def funcNL_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v21 + v20 ) + ( ( v2 - ( v21 + v20 ) ) / 1.9304692407320942 ) ) - ( ( ( v21 - v28 ) + v4 ) / ( 6.313092868252461 + ( v6 -abs( ( v4 -sin( v22 )) )) ) ) ) - ( ( ( v22 - ( v12 + v26 ) ) - ( ( v21 + v20 ) + ( ( v2 - ( v21 + v20 ) ) / 1.9304692407320942 ) ) ) / -6.408433466219385 ) ) 
def funcNL_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v5 + ( ( v1 -abs( v13 )) + v21 ) ) - ( v0 /sin( 4.847876927981055 )) ) + ( ( v5 + v15 ) + ( (exp( ( v1 - v6 ) )- v18 ) *cos( v25 )) ) ) / 5.725594796987103 ) 
def funcNL_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v14 - ( v13 * v12 ) ) +exp( ( v25 +sin( ( ( v4 - v22 ) + 8.484295138407688 ) )) )) + ( v20 * ( v14 + 4.429707619894675 ) ) ) - ( ( ( v13 * v12 ) + ( 4.429707619894675 * ( v13 - ( v4 + ( v22 + v4 ) ) ) ) ) - ( v21 * ( ( ( v4 - v22 ) + 8.484295138407688 ) - v21 ) ) ) ) * 0.041829541248723956 ) 

funcsNL = [funcNL_100307,funcNL_100408,funcNL_101006,funcNL_101107,funcNL_101309,funcNL_101410,funcNL_101915,funcNL_102008,funcNL_102311,funcNL_102816,]


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
	oFile = open('./topModels/bestExpressionsError-NL-' + t + '.txt','w')
	for index, s in enumerate(subjects):
		try:
			inFile = csv.reader(open("/media/james/My Passport/HCP/HCP-Processed/" +t + "/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z.csv",'r'))
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



