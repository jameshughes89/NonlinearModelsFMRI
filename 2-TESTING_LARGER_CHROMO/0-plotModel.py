#finds the top models for each subject

import numpy as np
import csv
import sys
from math import *
import matplotlib.pylab as plt

# _ALL_lb_200-300 Subject_1_D 1st_session 1st_trial 43200

# (216, 318)
def func_OLD(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v6 + v7 ) - v2 ) /exp(cos(sin( ( -13.949668382490996 * v4 ) )))) + ( ( ( v19 + ( v24 / ( v4 + ( -13.949668382490996 * v4 ) ) ) ) - v23 ) / -4.935206529128816 ) ) 
# (31, 314)
def func_NEW(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return ( 0.1609350965335281 * ( ( ( v7 - v21 ) - ( ( -2.3085201226188623 * ( ( v6 + ( v1 - v2 ) ) - (sin( ( v2 - v23 ) )+sin( ( v3 *tan( (tan( v2 )/ ( v2 * ( v2 - v23 ) ) ) )) )) ) ) +sin(exp( (tan( v2 )/ ( v2 * ( v2 - v23 ) ) ) ))) ) -cos( v26 )) ) 



model = func_OLD
data = np.array(list(csv.reader(open('EMOTION_100307_2_L7_Z.csv','r')))).astype(float)


real = []
pred = []
absErr = []

for l in data:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17], l[18], l[19], l[20], l[21], l[22], l[23], l[24], l[25], l[26], l[27], l[28], l[29]))
	absErr.append(abs(real[-1] - pred[-1]))

print np.mean(absErr)
plt.plot(real)
plt.plot(pred)


model = func_NEW
data = np.array(list(csv.reader(open('EMOTION_100307_2_L7_Z.csv','r')))).astype(float)


real = []
pred = []
absErr = []

for l in data:
	real.append(l[-1])
	pred.append(model(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15], l[16], l[17], l[18], l[19], l[20], l[21], l[22], l[23], l[24], l[25], l[26], l[27], l[28], l[29]))
	absErr.append(abs(real[-1] - pred[-1]))

print np.mean(absErr)
plt.plot(pred)



plt.show()
