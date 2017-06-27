'''

creates a large distance matrix for all non liear models. 

CHANGE THE iFile line to switch between LR/RL --- Also be sure to save the output file names too!


'''

import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def funcNL_EMOTION_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  (tan( -0.3952688725061826 )* ( ( ( v2 + ( -0.8039820609557644 * v6 ) ) - v7 ) - ( v9 /exp( (cos( ( 1.927824070814431 - ( 1.927824070814431 - v15 ) ) )+ ( v4 * v4 ) ) )) ) ) 
def funcNL_EMOTION_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v14 + v10 ) - ( ( ( v9 - v7 ) + ( v21 / 2.7227890588826433 ) ) - ( v6 + v1 ) ) ) - v17 ) / 2.7227890588826433 ) 
def funcNL_EMOTION_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v4 - ( ( v6 / 0.5368327131924353 ) - ( ( ( v21 + v11 ) - v7 ) - v23 ) ) ) / -2.6814387796674666 ) 
def funcNL_EMOTION_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( (cos( -6.576763109097076 )* v27 ) - ( ( ( v6 - v17 ) /cos( -6.576763109097076 )) *sin( ( (sin( ( ( v3 + v5 ) + v1 ) )-exp(tan( -6.576763109097076 ))) + ( ( v0 + v6 ) / -6.576763109097076 ) ) )) ) 
def funcNL_EMOTION_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v1 + ( ( v23 + v26 ) - v12 ) ) / 3.1594943890449017 ) + (abs( v15 )/ ( 3.1594943890449017 / v27 ) ) ) 
def funcNL_EMOTION_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( (sin(sin( v18 ))+ ( v17 - ( v24 - v14 ) ) ) / 2.877813676118258 ) - ( ( ( v23 - v9 ) -cos( ( v23 / ( v18 * v23 ) ) )) / -6.210029038791664 ) ) 
def funcNL_EMOTION_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v23 - ( ( ( ( v3 - v1 ) + ( v19 - v10 ) ) - v14 ) - v7 ) ) / 3.072840147941104 ) 
def funcNL_EMOTION_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( (cos( ( v4 - v1 ) )/ 2.7085386635340605 ) + ( ( ( (cos( (exp( v17 )- v2 ) )- v23 ) - v26 ) + ( ( ( v4 - v1 ) -sin( v6 )) +cos( ( v4 /cos( v1 )) )) ) / -3.1735138038937016 ) ) 
def funcNL_EMOTION_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( (cos( v25 )* ( v22 + v6 ) ) - v21 ) / 7.044057229979856 ) + ( v15 / 4.141935207057827 ) ) - (cos( -13.903655947333329 )* ( ( v15 - ( v26 + v7 ) ) + ( v15 - ( v1 + v18 ) ) ) ) ) 
def funcNL_EMOTION_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v3 - ( v26 + v8 ) ) / -4.916516014674039 ) - ( ( ( v27 + ( ( v1 - v11 ) - v26 ) ) + v14 ) / -3.0035596021921016 ) ) 

funcsNL_EMOTION = [funcNL_EMOTION_100307,funcNL_EMOTION_100408,funcNL_EMOTION_101006,funcNL_EMOTION_101107,funcNL_EMOTION_101309,funcNL_EMOTION_101410,funcNL_EMOTION_101915,funcNL_EMOTION_102008,funcNL_EMOTION_102311,funcNL_EMOTION_102816,]

def funcNL_GAMBLING_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v2 / ( v18 + 10.21579936413567 ) ) - ( ( v7 + v9 ) / -2.7481596481434245 ) ) - ( ( v8 - ( v6 + v15 ) ) / 3.79157187875758 ) ) 
def funcNL_GAMBLING_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v11 - ( v18 - v7 ) ) / 6.2003870526694485 ) - ( ( 7.26322062242993 * ( v6 / -18.686287135359464 ) ) + ( ( ( ( v26 + v24 ) + v15 ) + v9 ) / -5.855350281394752 ) ) ) 
def funcNL_GAMBLING_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v7 + ( ( ( ( v27 / 1.8274473905095974 ) + v28 ) - v25 ) + v6 ) ) + ( v19 + v11 ) ) / 4.059984924171985 ) + ( ( v16 *cos( ( v28 - ( v27 / 1.8274473905095974 ) ) )) / -6.817138057210199 ) ) 
def funcNL_GAMBLING_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( ( ( v7 / v6 ) * v27 ) /exp( ( ( v7 / v6 ) * v27 ) )) - ( v7 + v6 ) ) - ( v21 + v1 ) ) - ( ( ( v7 / v6 ) * v27 ) /exp( ( ( v7 / v6 ) * v27 ) )) ) / (sin( ( ( v27 - v1 ) *exp( v0 )) )+ -3.8704274501304745 ) ) 
def funcNL_GAMBLING_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v1 + ( ( v9 + ( v7 + v10 ) ) -sin( ( ( v10 - v0 ) - v6 ) )) ) - v25 ) / 3.509917873602415 ) 
def funcNL_GAMBLING_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v4 / ( ( v22 - 3.5626870083685773 ) - v4 ) ) + ( ( ( ( ( ( v11 / -2.1726548241654378 ) - v9 ) - v1 ) - v21 ) - v27 ) * -0.30024434564933244 ) ) 
def funcNL_GAMBLING_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v27 - ( v27 - v6 ) ) + ( ( v15 - v27 ) + v27 ) ) + (cos( v7 )* ( v15 - v27 ) ) ) + ( ( v7 + v9 ) + v21 ) ) / 4.547409370793343 ) 
def funcNL_GAMBLING_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v21 - ( ( v0 - v15 ) - ( v15 + ( ( ( v23 + v11 ) + v9 ) - v22 ) ) ) ) + v6 ) / (cos( ( v1 / v22 ) )+ 4.831994366371973 ) ) 
def funcNL_GAMBLING_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( (sin( v27 )+ v6 ) - ( (sin( (cos( -5.6323015775888585 )/ v3 ) )- ( ( v11 - -5.6323015775888585 ) + -5.6323015775888585 ) ) -sin( (sin( (cos( -5.6323015775888585 )/ v3 ) )- ( ( v11 - -5.6323015775888585 ) + -5.6323015775888585 ) ) )) ) /abs( 2.8802529623386555 )) + ( v20 / 2.2132434311587303 ) ) 
def funcNL_GAMBLING_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v23 + v9 ) / ( 4.166688619495961 - v2 ) ) + ( v7 / (exp( ( 4.166688619495961 / v7 ) )+ ( 4.166688619495961 - v2 ) ) ) ) - ( ( ( v19 - v20 ) - v27 ) / ( 3.5303598794701507 +sin( ( v7 + v2 ) )) ) ) 

funcsNL_GAMBLING = [funcNL_GAMBLING_100307,funcNL_GAMBLING_100408,funcNL_GAMBLING_101006,funcNL_GAMBLING_101107,funcNL_GAMBLING_101309,funcNL_GAMBLING_101410,funcNL_GAMBLING_101915,funcNL_GAMBLING_102008,funcNL_GAMBLING_102311,funcNL_GAMBLING_102816,]

def funcNL_LANGUAGE_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v28 - v26 ) - ( (sin( v19 )- v1 ) * 0.8896456144016973 ) ) / 2.8699559477244385 ) - (tan( 2.8699559477244385 )* ( v7 + ( v17 +sin( v9 )) ) ) ) 
def funcNL_LANGUAGE_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v17 + ( v18 + ( ( v27 - ( v24 - v18 ) ) - ( v26 - v13 ) ) ) ) / 3.817470808360902 ) - ( ( v1 - v3 ) / -4.702151436538472 ) ) 
def funcNL_LANGUAGE_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v4 - ( v18 + v17 ) ) + ( ( v26 *tan( -9.690447367358344 )) + ( ( v26 - v28 ) -sin( v17 )) ) ) / -3.4163223877697533 ) - ( ( v20 + v7 ) / ( -3.4163223877697533 + ( ( v17 / ( v21 + v4 ) ) + -3.4163223877697533 ) ) ) ) 
def funcNL_LANGUAGE_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( (abs( v15 )-abs(abs( v17 ))) + ( v7 - v11 ) ) / ( 1.9835335947009796 + ( ( v1 * v7 ) + v7 ) ) ) + ( v1 + v17 ) ) / 1.9835335947009796 ) 
def funcNL_LANGUAGE_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v25 - v15 ) - v21 ) / -3.689149054831539 ) - ( ( ( v7 +sin( v15 )) + ( v27 + ( ( ( v11 - v26 ) - v4 ) + v18 ) ) ) / -4.737991497480465 ) ) 
def funcNL_LANGUAGE_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v28 + v27 ) - ( v25 - v8 ) ) / 2.367505172614507 ) + ( ( (sin( v7 )+ ( v7 +sin( v0 )) ) - ( ( v12 - v6 ) + v13 ) ) / ( ( 5.237203779032733 + v7 ) + ( v12 - v6 ) ) ) ) 
def funcNL_LANGUAGE_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v18 + ( ( ( ( ( v17 - v6 ) + v1 ) - v26 ) - v24 ) + v15 ) ) + ( v27 - ( ( v19 - v4 ) / -2.546427047728269 ) ) ) / 3.4845030844269367 ) 
def funcNL_LANGUAGE_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v7 + v17 ) + ( ( ( v1 - v23 ) - v26 ) + v8 ) ) + ( ( ( v7 + v17 ) - v14 ) + v9 ) ) / 4.614667879985788 ) 
def funcNL_LANGUAGE_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( 0.5413873833135199 * ( ( (abs( ( v26 + v4 ) )/ ( (cos( ( v5 *exp( v4 )) )+abs(exp( v4 ))) + ( ( v26 *sin( v26 )) - v10 ) ) ) - ( v26 + ( ( ( v26 *sin( v26 )) - v10 ) /exp(exp( v4 ))) ) ) + ( v17 + v7 ) ) ) 
def funcNL_LANGUAGE_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v12 - v26 ) / ( 4.12679760641517 - v26 ) ) + ( ( ( v9 + ( ( ( ( v7 - v25 ) / 4.12679760641517 ) + v9 ) + v17 ) ) *exp(sin( 5.7536952258884675 ))) - v9 ) ) 

funcsNL_LANGUAGE = [funcNL_LANGUAGE_100307,funcNL_LANGUAGE_100408,funcNL_LANGUAGE_101006,funcNL_LANGUAGE_101107,funcNL_LANGUAGE_101309,funcNL_LANGUAGE_101410,funcNL_LANGUAGE_101915,funcNL_LANGUAGE_102008,funcNL_LANGUAGE_102311,funcNL_LANGUAGE_102816,]

def funcNL_MOTOR_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v16 + v9 ) +sin( v11 )) + v17 ) + ( ( v5 + v7 ) - ( ( v14 - v20 ) + ( v26 + v8 ) ) ) ) / 3.805249853314283 ) 
def funcNL_MOTOR_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v5 + v22 ) + ( ( ( ( v16 - ( ( v5 + v22 ) + v12 ) ) + ( ( v9 - ( v2 - v15 ) ) + (cos( v22 )* v7 ) ) ) - ( ( v5 + v22 ) + v12 ) ) *tan(cos( -13.838461599647731 ))) ) 
def funcNL_MOTOR_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( 0.3655808368714908 * ( ( v15 + v5 ) - ( ( v8 + ( ( v24 + ( ( v17 - v12 ) +sin( v5 )) ) / -1.994764314641717 ) ) - v19 ) ) ) 
def funcNL_MOTOR_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v1 - v2 ) + (sin( v4 )+ v5 ) ) * (cos(sin( v21 ))/ ( 4.297895256770474 + ( ( v26 - v20 ) +cos(exp( v21 ))) ) ) ) - ( ( ( v26 - v20 ) - ( v23 + v21 ) ) *tan( 12.888524592895934 )) ) 
def funcNL_MOTOR_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( (sin( v18 )* ( v20 - v14 ) ) - v22 ) - (sin( v21 )+ ( v20 + ( v5 + v21 ) ) ) ) *tan(tan( 12.341377585138972 ))) 
def funcNL_MOTOR_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v0 + ( ( ( ( ( v21 + ( v11 - v2 ) ) + v9 ) - v14 ) + v1 ) + v17 ) ) / ( 4.728901458938864 - ( v15 - v18 ) ) ) 
def funcNL_MOTOR_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v22 + ( v5 + v21 ) ) *tan( 6.644320356873983 )) + ( ( v1 - ( ( v26 + v12 ) -sin( v26 )) ) / ( v26 + ( 6.644320356873983 + ( v14 - ( v5 + v21 ) ) ) ) ) ) 
def funcNL_MOTOR_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( (sin( ( ( v20 - ( v0 - v22 ) ) + v2 ) )+ ( v20 + v2 ) ) + ( ( ( v20 + v21 ) - ( ( v0 - v22 ) - v1 ) ) - v26 ) ) / 4.549567952014677 ) 
def funcNL_MOTOR_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v26 - v9 ) - v8 ) - v21 ) / -2.62069231299148 ) + ( ( ( v24 + ( v17 -cos( (cos( v9 )- v5 ) )) ) / (exp(exp( v27 ))+tan( 1.0545091207199278 )) ) + ( v5 - v8 ) ) ) 
def funcNL_MOTOR_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v22 + v5 ) + ( v5 - v8 ) ) + v20 ) + ( v21 - ( ( v16 - ( v11 + v14 ) ) / ( ( v5 - v22 ) -abs( 3.5670462725088683 )) ) ) ) /abs( 3.5670462725088683 )) 

funcsNL_MOTOR = [funcNL_MOTOR_100307,funcNL_MOTOR_100408,funcNL_MOTOR_101006,funcNL_MOTOR_101107,funcNL_MOTOR_101309,funcNL_MOTOR_101410,funcNL_MOTOR_101915,funcNL_MOTOR_102008,funcNL_MOTOR_102311,funcNL_MOTOR_102816,]

def funcNL_RELATIONAL_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  (sin( ( ( ( v8 + v16 ) / ( ( 5.767393633548249 + v12 ) + ( 5.767393633548249 + v12 ) ) ) * (exp(cos( v24 ))+cos(sin( 5.767393633548249 ))) ) )+ ( ( v15 + v27 ) /abs( ( (cos( v24 )/ 5.767393633548249 ) - 2.7155662775103124 ) )) ) 
def funcNL_RELATIONAL_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( (cos( v19 )- ( ( v24 - ( v8 - v19 ) ) - ( v17 + v15 ) ) ) + v26 ) / 4.021514443667982 ) + ( v13 / ( v15 + 4.04758527381604 ) ) ) - (tan(cos(abs( ( v15 + 4.04758527381604 ) )))/ ( v24 - 4.04758527381604 ) ) ) 
def funcNL_RELATIONAL_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( (sin( v26 )+ ( ( v24 + ( ( ( v17 + v27 ) + v15 ) - v2 ) ) + ( v1 - ( v19 + ( v20 - v8 ) ) ) ) ) / 4.560655331774093 ) 
def funcNL_RELATIONAL_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v27 - ( ( ( v9 - v18 ) - v1 ) / ( ( 17.13888449489278 +sin( ( v18 -tan( v18 )) )) / ( 11.250705239128436 -exp( v28 )) ) ) ) + v13 ) / 2.52013222413515 ) 
def funcNL_RELATIONAL_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( -2.4232575407529744 + ( ( v24 + ( (sin( v19 )- v15 ) - v1 ) ) / ( ( v27 - ( v19 - v12 ) ) - ( v12 - v12 ) ) ) ) / ( -4.701124861720896 / ( v27 - ( v19 - v12 ) ) ) ) 
def funcNL_RELATIONAL_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v17 *tan( -5.746505802061197 )) - ( ( ( v15 - 0.17496174386386087 ) + ( v15 - 0.17496174386386087 ) ) / ( ( v24 + -5.746505802061197 ) + (sin( ( v24 + v24 ) )- v13 ) ) ) ) + ( ( v13 - v18 ) * 0.24359289830182007 ) ) 
def funcNL_RELATIONAL_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v17 + ( (abs(sin( v16 ))*sin( v6 )) + ( v15 + v13 ) ) ) /exp(exp( (sin( v16 )/ ( 13.562569493049075 + v13 ) ) ))) 
def funcNL_RELATIONAL_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( v13 + ( ( ( v13 + v19 ) - ( v7 - ( ( v4 *cos(cos( ( -15.019693693636565 - v17 ) ))) - ( ( v17 -cos( ( -15.019693693636565 - v17 ) )) -sin( ( ( 18.668637510589512 - v23 ) - ( -15.019693693636565 - v17 ) ) )) ) ) ) *sin( 16.01173403052153 )) ) 
def funcNL_RELATIONAL_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v26 - ( ( ( ( (exp(cos( v9 ))* 7.681276002684058 ) * ( v6 / ( v23 - 7.681276002684058 ) ) ) - ( v8 + v13 ) ) + (sin( v2 )*cos( v9 )) ) - v15 ) ) / 4.176493896004576 ) - ( ( ( v4 - v9 ) - v3 ) / (cos( v9 )+ ( v23 - 7.681276002684058 ) ) ) ) 
def funcNL_RELATIONAL_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( (cos( v27 )/ (tan( -8.062644874185011 )- v22 ) ) + ( ( ( v27 - v1 ) / ( (cos(exp(sin( v16 )))+ v27 ) + 3.5962868011776408 ) ) + ( (exp(sin( v16 ))/ -8.062644874185011 ) + v1 ) ) ) 

funcsNL_RELATIONAL = [funcNL_RELATIONAL_100307,funcNL_RELATIONAL_100408,funcNL_RELATIONAL_101006,funcNL_RELATIONAL_101107,funcNL_RELATIONAL_101309,funcNL_RELATIONAL_101410,funcNL_RELATIONAL_101915,funcNL_RELATIONAL_102008,funcNL_RELATIONAL_102311,funcNL_RELATIONAL_102816,]

def funcNL_SOCIAL_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v25 + v0 ) - v18 ) + ( v10 + v7 ) ) - ( (sin( ( v25 - v23 ) )- ( ( v25 + v0 ) - v18 ) ) + v17 ) ) / 3.746214099492903 ) 
def funcNL_SOCIAL_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( (exp( -1.2431676985557232 )* ( v0 - v22 ) ) + (tan(exp( -1.2431676985557232 ))* ( ( v26 + ( v0 - ( v25 / -1.2431676985557232 ) ) ) - ( ( ( -1.2431676985557232 * v7 ) + v21 ) + ( v18 - v24 ) ) ) ) ) 
def funcNL_SOCIAL_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v19 - ( ( v3 - v24 ) + ( v3 - v24 ) ) ) + v0 ) / 3.8215956523303944 ) - ( ( ( v25 + v8 ) - v18 ) *cos( 16.909273978108004 )) ) 
def funcNL_SOCIAL_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v23 + v25 ) / (abs( ( v28 * ( ( (cos(abs( ( v0 - v14 ) ))/ v7 ) / v15 ) * v5 ) ) )+tan( -2.2025583123571764 )) ) 
def funcNL_SOCIAL_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v20 - ( v3 + (cos( v27 )+ v4 ) ) ) - ( ( ( v27 + v3 ) - ( v16 +cos( v27 )) ) - ( v26 + v25 ) ) ) / 3.334312103085793 ) - ( ( v23 + v12 ) / ( -3.1508226292195083 - ( (cos( v27 )+ v4 ) * v4 ) ) ) ) 
def funcNL_SOCIAL_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( (cos( -1.0664492440860762 )* ( ( v0 + v25 ) - ( ( v15 - ( ( ( v27 -cos( -1.0664492440860762 )) * (sin( v26 )/ -3.7858170392541766 ) ) + ( ( v27 -cos( -1.0664492440860762 )) * (sin( v26 )/ -3.7858170392541766 ) ) ) ) + v22 ) ) ) - ( ( v16 + v7 ) / -3.7858170392541766 ) ) 
def funcNL_SOCIAL_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  (sin(exp( ( -4.007974073060758 / -4.007974073060758 ) ))* ( v8 - ( ( ( ( v26 / 1.2184264925287707 ) - ( v18 - v7 ) ) * ( (sin( v26 )- -4.007974073060758 ) / ( -4.007974073060758 + v24 ) ) ) - v0 ) ) ) 
def funcNL_SOCIAL_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v0 - v17 ) + ( v11 + v0 ) ) + ( v7 -sin( v18 )) ) + v25 ) / ( ( v13 - 16.831167604818482 ) /tan( 14.326212133570941 )) ) 
def funcNL_SOCIAL_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v23 + v25 ) / ( (abs( ( v5 / ( v24 - v16 ) ) )+ ( v23 - v5 ) ) - -2.8088361590647395 ) ) + ( v24 + ( ( ( v24 - v16 ) + v3 ) / -2.8088361590647395 ) ) ) 
def funcNL_SOCIAL_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v8 + ( v0 + ( ( ( v20 - v4 ) + v19 ) *cos(cos(cos( v4 )))) ) ) / 1.8120643410323183 ) + ( v18 / ( ( -4.313179256868839 - ( v20 -cos( v4 )) ) *sin( -17.82046915160054 )) ) ) 

funcsNL_SOCIAL = [funcNL_SOCIAL_100307,funcNL_SOCIAL_100408,funcNL_SOCIAL_101006,funcNL_SOCIAL_101107,funcNL_SOCIAL_101309,funcNL_SOCIAL_101410,funcNL_SOCIAL_101915,funcNL_SOCIAL_102008,funcNL_SOCIAL_102311,funcNL_SOCIAL_102816,]

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

funcsNL_WM = [funcNL_WM_100307,funcNL_WM_100408,funcNL_WM_101006,funcNL_WM_101107,funcNL_WM_101309,funcNL_WM_101410,funcNL_WM_101915,funcNL_WM_102008,funcNL_WM_102311,funcNL_WM_102816,]



#all_functions = [funcsNL_EMOTION, funcsNL_GAMBLING, funcsNL_LANGUAGE, funcsNL_MOTOR, funcsNL_RELATIONAL, funcsNL_SOCIAL, funcsNL_WM]
all_functions_line = funcsNL_EMOTION + funcsNL_GAMBLING + funcsNL_LANGUAGE + funcsNL_MOTOR + funcsNL_RELATIONAL + funcsNL_SOCIAL + funcsNL_WM
#all_functions_line = funcsNL

tasks = ["EMOTION", "GAMBLING", "LANGUAGE", "MOTOR", "RELATIONAL", "SOCIAL", "WM"]
lasts = ["7", "2", "16", "21", "28", "3", "21"]
#subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816, 103111, 103414, 103515, 103818, 104012, 104820, 105014, 105115, 105216, 105923, 106016, 106319, 106521, 107321, 107422, 108121, 108323, 108525, 108828, 109123, 109325, 110411, 111312, 111413, 111514, 111716, 112819, 113215, 113619, 113821, 113922, 114419, 114924, 115320, 116524, 117122, 117324, 118528, 118730, 118932, 119833, 120111, 120212, 120515, 121315, 121618, 122317, 122620, 123117, 123420, 123925, 124220, 124422, 124826, 125525, 126325, 126628, 127630, 127933, 128127, 128632, 129028, 130013, 130316, 130922, 131217, 131722, 131924, 132118, 133019, 133625, 133827, 133928, 134324, 135225, 135528, 135932, 136227, 136833, 137027, 137128, 137633, 137936, 138231, 138534, 139233, 139637, 140117, 140824, 140925, 141422, 141826, 142424, 142626, 142828, 143325, 144226, 144832, 145531, 145834]
subjects =[100307, 100408, 101006, 101107, 101309, 101410, 101915, 102008, 102311, 102816]

matrixMSE = []
matrixABE = []

matrixMIN = []


lastsCount = 0

for t in tasks:
	fs='funcsL_' + t + ' = ['
	count = 0
	for s in subjects:
		print t, s
		ALL = []
		#iFile = csv.reader(open("/home/james/Desktop/nData/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z.csv",'r'))
		iFile = csv.reader(open("/home/james/Desktop/nData/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_RL_Z.csv",'r'))
		for l in iFile:
			ALL.append(l)

		ALL = np.array(ALL)
		ALL = ALL.astype(float)
		allmsE = []
		allabE = []

		for f in all_functions_line:
			try:			
				msE = []
				abE = []			
				for l in ALL:
					err = l[-1] - f(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17],l[18],l[19],l[20],l[21],l[22],l[23],l[24],l[25],l[26],l[27],l[28],l[29])
					msE.append(err**2)
					abE.append(abs(err))
				
				allmsE.append((np.mean(msE)))
				allabE.append((np.mean(abE)))
				#allmsE.append(log(np.mean(msE)))
				#allabE.append(log(np.mean(abE)))
			except (ValueError, OverflowError):
				print '\t\t\tBBBBBUSTTTEDDDD: ', t, s
				allmsE.append(np.float('nan'))
				allabE.append(np.float('nan'))
				continue
		

		
		
		matrixMSE.append(allmsE)
		matrixABE.append(allabE)

		allmin = np.zeros(len(allabE))
		allmin[np.argsort(allabE)[0]] = 1
		matrixMIN.append(allmin)


	lastsCount +=1

np.savetxt('msEmat_NL_RLtop-RL.csv', matrixMSE, delimiter=",")
np.savetxt('abEmat_NL_RLtop-RL.csv', matrixABE, delimiter=",")
np.savetxt('minmat_NL_RLtop-RL.csv', matrixMIN, delimiter=",")


		








