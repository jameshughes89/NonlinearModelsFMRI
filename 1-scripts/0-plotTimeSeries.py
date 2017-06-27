import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr  

# Same DF
def funcL_8_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return 1.48348347495e-13 * 1 + 0.396687665768 * v1 + -0.0194383377603 * v6 + 0.140722339042 * v7 + 0.167177622803 * v8 + 0.179742151737 * v11 + 0.211062209408 * v26 + -0.0628737862403 * v27

# BC (29 ROI)
def funcL_BC_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return 9.09029795881e-14 * 1 + -0.091834955903 * v0 + 0.0767018384152 * v1 + -0.0391396024738 * v2 + -0.131007298787 * v3 + -0.189724894232 * v4 + 0.0597163424436 * v5 + 0.170109640274 * v6 + 0.2300125151 * v7 + 0.0697209628336 * v8 + 0.0125549697452 * v9 + -0.0745144692433 * v10 + 0.154606162674 * v11 + -0.0262131835549 * v12 + 0.0738998635814 * v13 + 0.0858478657616 * v14 + -0.253955718198 * v15 + 0.0305066469603 * v16 + 0.112155730725 * v17 + 0.281068244426 * v18 + -0.0430616684985 * v19 + 0.00144408877425 * v20 + -0.153316111093 * v21 + 0.0489700358252 * v22 + 0.0752802348644 * v23 + 0.019223655424 * v24 + -0.0602575121679 * v25 + 0.0912064760928 * v26 + -0.070620572626 * v27 + 0.0426191459126 * v28

# FDR (28 ROI)
def funcL_FDR_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return 1.52333007319e-13 * 1 + -0.112492601823 * v0 + 0.118611009087 * v1 + -0.119218784321 * v2 + -0.132736139211 * v3 + -0.217109434622 * v4 + 0.0864339914263 * v5 + 0.155477224979 * v6 + 0.1943815077 * v7 + 0.374652354191 * v8 + -0.0183829240419 * v9 + -0.161550330495 * v10 + 0.215393229535 * v11 + -0.113689452448 * v12 + 0.208856841054 * v13 + 0.0201090020164 * v14 + 0.122179327838 * v16 + 0.0277299065752 * v17 + 0.206016576767 * v18 + -0.0155437984111 * v19 + 0.0989064521977 * v20 + -0.261634438181 * v21 + 0.121036941544 * v22 + 0.130969795823 * v23 + 0.0209290885559 * v24 + -0.0986817501111 * v25 + 0.159304152997 * v26 + -0.213865412459 * v27 + -0.00904716986248 * v28

# All ROI (30)
def funcL_30_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return 9.09029795881e-14 * 1 + -0.091834955903 * v0 + 0.0767018384152 * v1 + -0.0391396024738 * v2 + -0.131007298787 * v3 + -0.189724894232 * v4 + 0.0597163424436 * v5 + 0.170109640274 * v6 + 0.2300125151 * v7 + 0.0697209628336 * v8 + 0.0125549697452 * v9 + -0.0745144692433 * v10 + 0.154606162674 * v11 + -0.0262131835549 * v12 + 0.0738998635814 * v13 + 0.0858478657616 * v14 + -0.253955718198 * v15 + 0.0305066469603 * v16 + 0.112155730725 * v17 + 0.281068244426 * v18 + -0.0430616684985 * v19 + 0.00144408877425 * v20 + -0.153316111093 * v21 + 0.0489700358252 * v22 + 0.0752802348644 * v23 + 0.019223655424 * v24 + -0.0602575121679 * v25 + 0.0912064760928 * v26 + -0.070620572626 * v27 + 0.0426191459126 * v28

# NL!
# 7 ROI
def funcNL_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( (exp( ( -4.1889991937283355 / ( (abs( -4.1889991937283355 )- ( v28 *cos( v7 )) ) + ( v0 * v15 ) ) ) )* v18 ) + ( ( v15 - ( v7 + v6 ) ) / (sin( v20 )+ ( -3.9622526574550356 +cos( v7 )) ) ) ) 


tasks = ["EMOTION"]
subjects = [102311]
lasts = ["7"]

#tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
#lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816,103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923,106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123,109325, 110411, 111312, 111413, 111514, 111716, 113215, 113619, 113922, 114419,114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111,120212, 120515, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422,124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013,130316, 130922, 131217, 131722, 131924, 133019, 133625, 133827, 133928, 134324,135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231,138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142828, 143325, 144832, 145834]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816]


outData = []

for t in tasks:
	allError = 0
	allErrorList = []
	count = 0
	for index, s in enumerate(subjects):
		inFile = csv.reader(open("/media/james/My Passport/HCP/HCP-Processed/" +t + "/" + t + "_"+str(s)+"_2_L" + str(lasts[0]) + "_Z.csv",'r'))
		#inFile = csv.reader(open("../roiData/" + str(s) + "_2.csv",'r'))		# use for gaussian brain
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
		YsL_BC = []
		YsL_FDR = []
		YsL_30 = []

		yNLabs = 0
		yLabs = 0
		diffabs = 0

		yNLmse = []
		yLmse = []
		yLmse_BC = []
		yLmse_FDR = []
		yLmse_30 = []

		diffmse = 0


		for i in range(len(v29)):	
			# L		
			yL = funcL_8_102311(v0[i],v1[i],v2[i],v3[i],v4[i],v5[i],v6[i],v7[i],v8[i],v9[i],v10[i],v11[i],v12[i],v13[i],v14[i],v15[i],v16[i],v17[i],v18[i],v19[i],v20[i],v21[i],v22[i],v23[i],v24[i],v25[i],v26[i],v27[i],v28[i],v29[i])
			yL_BC = funcL_BC_102311(v0[i],v1[i],v2[i],v3[i],v4[i],v5[i],v6[i],v7[i],v8[i],v9[i],v10[i],v11[i],v12[i],v13[i],v14[i],v15[i],v16[i],v17[i],v18[i],v19[i],v20[i],v21[i],v22[i],v23[i],v24[i],v25[i],v26[i],v27[i],v28[i],v29[i])
			yL_FDR = funcL_FDR_102311(v0[i],v1[i],v2[i],v3[i],v4[i],v5[i],v6[i],v7[i],v8[i],v9[i],v10[i],v11[i],v12[i],v13[i],v14[i],v15[i],v16[i],v17[i],v18[i],v19[i],v20[i],v21[i],v22[i],v23[i],v24[i],v25[i],v26[i],v27[i],v28[i],v29[i])
			yL_30 = funcL_30_102311(v0[i],v1[i],v2[i],v3[i],v4[i],v5[i],v6[i],v7[i],v8[i],v9[i],v10[i],v11[i],v12[i],v13[i],v14[i],v15[i],v16[i],v17[i],v18[i],v19[i],v20[i],v21[i],v22[i],v23[i],v24[i],v25[i],v26[i],v27[i],v28[i],v29[i])

			# NL
			yNL = funcNL_102311(v0[i],v1[i],v2[i],v3[i],v4[i],v5[i],v6[i],v7[i],v8[i],v9[i],v10[i],v11[i],v12[i],v13[i],v14[i],v15[i],v16[i],v17[i],v18[i],v19[i],v20[i],v21[i],v22[i],v23[i],v24[i],v25[i],v26[i],v27[i],v28[i],v29[i])

	
			yNLmse.append(abs(v29[i] - yNL))
			yLmse.append(abs(v29[i] - yL))
			yLmse_BC.append(abs(v29[i] - yL_BC))
			yLmse_FDR.append(abs(v29[i] - yL_FDR))
			yLmse_30.append(abs(v29[i] - yL_30))

			YsNL.append(yNL)
			YsL.append(yL)
			YsL_BC.append(yL_BC)
			YsL_FDR.append(yL_FDR)
			YsL_30.append(yL_30)


		print 'NL:\t', np.mean(yNLmse)
		print 'L:\t', np.mean(yLmse)
		print 'L_bc:\t', np.mean(yLmse_BC)
		print 'L_fdr:\t', np.mean(yLmse_FDR)
		print 'L_30:\t', np.mean(yLmse_30)

		plt.plot(Xs, v29, 'b', label='Measured')
		plt.plot(Xs, YsNL, 'r', label='Symbolic Regression (Nonlinear) - Mean Abs Error %.4f' % np.mean(yNLmse))
		plt.plot(Xs, YsL, 'g', label='GLM with same # ROI - Mean Abs Error %.4f' % np.mean(yLmse))
		#plt.plot(Xs, YsL_BC, 'c', label='GLM with BC - Mean Abs Error %.4f' % np.mean(yLmse_BC))
		#plt.plot(Xs, YsL_FDR, 'm', label='GLM with FDR - Mean Abs Error %.4f' % np.mean(yLmse_FDR))
		plt.plot(Xs, YsL_30, 'y', label='GLM with all ROI - Mean Abs Error %.4f' % np.mean(yLmse_30))
		plt.legend()
		plt.ylim([-4,4])
		plt.title('Time Series Plot of ROI 7 for Subject 102311 on EMOTION')
 		plt.ylabel('Intensity')
		plt.xlabel('Time Point')
		plt.show()


'''
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white
'''

