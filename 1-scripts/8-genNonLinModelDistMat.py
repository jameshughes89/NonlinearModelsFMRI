'''

creates a large distance matrix for all non liear models. 

CHANGE THE iFile line to switch between LR/RL --- Also be sure to save the output file names too!


'''

import csv
from math import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def funcNL_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v6 + v7 ) - v2 ) /exp(cos(sin( ( -13.949668382490996 * v4 ) )))) + ( ( ( v19 + ( v24 / ( v4 + ( -13.949668382490996 * v4 ) ) ) ) - v23 ) / -4.935206529128816 ) ) 
def funcNL_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  (sin( -9.766019915829176 )* ( ( ( v7 + v1 ) - ( v9 + ( v21 -sin( v28 )) ) ) + ( ( v10 + v6 ) - ( v3 * ( v7 - v2 ) ) ) ) ) 
def funcNL_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v4 - v19 ) / ( -2.3441929772893744 + v5 ) ) - ( ( ( ( v2 - v3 ) -sin( v9 )) + v6 ) / -2.3441929772893744 ) ) 
def funcNL_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v12 - (cos( -10.814286428584875 )+ v20 ) ) * ( (cos( -10.814286428584875 )+ ( v3 - v24 ) ) * ( v24 + ( ( v3 - v12 ) * v3 ) ) ) ) + v27 ) 
def funcNL_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  (abs( 0.4470765362276765 )* ( ( ( v4 - v17 ) - (cos( (sin( ( v14 * v11 ) )+sin( ( v14 * v11 ) )) )* v12 ) ) + ( v1 + v26 ) ) ) 
def funcNL_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( (sin(sin( v15 ))- ( ( v14 / -3.87544672313906 ) + ( v9 + ( v0 *abs(sin( v15 ))) ) ) ) - ( ( (abs(sin( v15 ))- v6 ) - v14 ) - ( v23 +cos( v10 )) ) ) / 2.8951061811373364 ) 
def funcNL_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v3 - ( v10 -sin( ( v22 -sin( v7 )) )) ) - v14 ) - ( v7 + v15 ) ) / -2.945912777589214 ) 
def funcNL_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( ( 1.5499947482169851 -abs( v13 )) -sin(tan( v13 ))) *cos( ( v23 - 8.168676049124045 ) )) - ( v13 - v27 ) ) + ( v6 + v26 ) ) /abs( (sin( v13 )- 2.562091015531756 ) )) 
def funcNL_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( (exp( ( -4.1889991937283355 / ( (abs( -4.1889991937283355 )- ( v28 *cos( v7 )) ) + ( v0 * v15 ) ) ) )* v18 ) + ( ( v15 - ( v7 + v6 ) ) / (sin( v20 )+ ( -3.9622526574550356 +cos( v7 )) ) ) ) 
def funcNL_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v25 + v14 ) - ( ( v11 + v19 ) -sin( (exp( 2.7883421980953855 )-sin( v1 )) )) ) / ( 4.597995655453076 - v1 ) ) - ( ( v27 + v7 ) / ( (sin(exp( ( v7 * v7 ) ))/ ( (tan( 2.7883421980953855 )/ ( v11 + v19 ) ) +exp( ( v7 * v7 ) )) ) - 4.597995655453076 ) ) ) 

funcsNL_EMOTION = [funcNL_100307,funcNL_100408,funcNL_101006,funcNL_101107,funcNL_101309,funcNL_101410,funcNL_101915,funcNL_102008,funcNL_102311,funcNL_102816,]

def funcNL_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v9 +sin( ( ( (sin( v7 )- -3.160660269250066 ) - v8 ) - -3.3127551426067825 ) )) / ( (sin( v7 )- -3.160660269250066 ) - v8 ) ) + ( ( ( v6 + v2 ) + v27 ) * ( -15.491786746426776 *tan( -3.160660269250066 )) ) ) 
def funcNL_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v24 / ( ( ( v6 - v7 ) - -6.367841026498473 ) / ( ( ( v7 + v11 ) / v24 ) - -1.7688464571941722 ) ) ) + ( ( v26 + v6 ) /abs( 3.1130252005431167 )) ) - ( ( v18 - v15 ) / 3.1130252005431167 ) ) 
def funcNL_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v27 / 6.5375004569625546 ) + ( ( ( v16 +abs( v1 )) * ( v16 +abs( v1 )) ) / 3.9088854533735464 ) ) - ( ( ( ( v16 + ( ( ( v16 +abs( v1 )) * ( v16 +abs( v1 )) ) - v18 ) ) - v9 ) - ( ( v6 + v19 ) + v22 ) ) / ( 3.9088854533735464 +cos( ( v16 +abs( v1 )) )) ) ) 
def funcNL_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v6 - ( ( ( v3 - v27 ) - v21 ) - v1 ) ) / ( ( ( v3 - v27 ) - v21 ) - -5.085897221157278 ) ) + ( ( v7 / 3.4572182673396554 ) - ( ( v11 - (sin( ( v7 / 3.4572182673396554 ) )* ( v1 * (exp( v0 )/cos( -5.085897221157278 )) ) ) ) / ( -5.085897221157278 -exp( v1 )) ) ) ) 
def funcNL_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  (sin( -12.319949424599965 )* ( ( v1 + ( v9 + v6 ) ) - ( ( ( v25 - v7 ) - v0 ) +cos( (exp(cos( ( ( v25 - v7 ) - v0 ) ))+ v15 ) )) ) ) 
def funcNL_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( (sin( v5 )- v27 ) + (cos( ( v5 * ( ( 17.52798208287882 - v25 ) -exp( v5 )) ) )- v11 ) ) / -4.787231345807591 ) + ( ( ( v9 + v21 ) + v1 ) / 3.8524041526597976 ) ) 
def funcNL_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v16 + ( v9 + v6 ) ) + ( v21 + v15 ) ) -cos( (tan( ( v15 + ( v9 + v6 ) ) )-exp( v16 )) )) / 3.6046141525069295 ) - ( v0 / 3.6046141525069295 ) ) 
def funcNL_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v0 - v11 ) / -7.146505429190473 ) * (exp(sin(cos( v0 )))- v19 ) ) + ( ( v15 /abs( 1.6891850945357163 )) - ( ( v22 - ( v21 + v6 ) ) / ( ( 1.6891850945357163 + 1.6891850945357163 ) -sin( (cos( v15 )/ v0 ) )) ) ) ) 
def funcNL_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  (cos( v1 )* ( ( (sin( v22 )- v3 ) + ( ( v19 - v27 ) - ( ( ( ( v6 + v7 ) + ( ( v20 + v9 ) + v11 ) ) + v27 ) /cos( v1 )) ) ) / -5.617064989598264 ) ) 
def funcNL_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v27 - ( ( v19 - ( ( v9 + v23 ) + v7 ) ) - (sin( v20 )- v18 ) ) ) * ( -3.539227518252112 / ( v11 + ( -11.101890442709852 - v9 ) ) ) ) 

funcsNL_GAMBLING = [funcNL_100307,funcNL_100408,funcNL_101006,funcNL_101107,funcNL_101309,funcNL_101410,funcNL_101915,funcNL_102008,funcNL_102311,funcNL_102816,]

def funcNL_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( (sin( v21 )+ ( v17 + ( ( v21 - ( v20 - v19 ) ) - v1 ) ) ) / ( ( v20 - v19 ) - -6.42676083402732 ) ) + ( (sin( (cos(cos( v26 ))* v26 ) )- ( ( v28 + v7 ) - ( ( v21 - ( v20 - v19 ) ) - v1 ) ) ) * -0.4235785034009325 ) ) 
def funcNL_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v27 / 2.065031953454202 ) + v18 ) - ( ( ( ( v11 - ( v18 - v20 ) ) + (cos( ( ( -13.053900477895727 + v3 ) + ( v17 + v17 ) ) )- v3 ) ) - ( v24 + v26 ) ) *cos( 1.890350921713658 )) ) 
def funcNL_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v4 / -3.590933882766425 ) - ( ( ( ( v18 +sin( v1 )) + ( ( ( v18 + ( v3 * -0.7082451112490382 ) ) + v20 ) - v26 ) ) / -5.509557117922178 ) - ( ( v17 + v28 ) / 2.6191747980764966 ) ) ) 
def funcNL_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v17 + (sin( v5 )+ (cos( v17 )- v11 ) ) ) - ( 0.5503883887221939 * ( (sin( v5 )+ (cos( v17 )- v11 ) ) +cos( v26 )) ) ) + v1 ) *cos(cos( ( (cos( v26 )* 0.5503883887221939 ) *cos( v17 )) ))) 
def funcNL_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v7 - ( ( v4 - v18 ) - ( ( v9 - v5 ) - ( ( v26 - v15 ) - v21 ) ) ) ) + ( ( v27 - v25 ) + v11 ) ) / 4.287030860914456 ) 
def funcNL_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( 4.577534171105533 / ( ( ( ( v16 - v26 ) - -14.738440743870939 ) + v9 ) +cos( v8 )) ) * ( ( ( ( v6 - ( v26 - v17 ) ) + ( v17 -sin( (cos( v9 )* v25 ) )) ) + v28 ) + ( (sin( ( v6 - ( v26 - v17 ) ) )+ ( v3 + v8 ) ) - ( v12 + v12 ) ) ) ) 
def funcNL_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v18 - v24 ) - ( ( ( v26 - v21 ) - v1 ) - v17 ) ) - v6 ) / 3.6116437940504618 ) + ( ( (abs( v5 )+ ( v5 + v24 ) ) / ( v25 - ( v18 + 4.029037858830577 ) ) ) + ( ( v15 + (abs( v5 )+ ( v5 + v24 ) ) ) / 4.029037858830577 ) ) ) 
def funcNL_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v9 - v26 ) + v12 ) / ( v23 + ( 5.633238501396466 - v26 ) ) ) + ( v1 / ( 5.633238501396466 - v26 ) ) ) + ( ( v7 + ( v17 -sin( v14 )) ) / 2.6314296264027135 ) ) 
def funcNL_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  (sin( ( v7 - ( v9 +sin( (abs( ( v5 - v13 ) )+ ( v5 - v13 ) ) )) ) )+ ( ( v9 +sin( (abs( ( v5 - v13 ) )+ ( v5 - v13 ) ) )) - ( ( v17 / -2.3526664200639544 ) - ( ( v27 / ( ( v27 + ( v27 / v27 ) ) - ( -2.3526664200639544 + v0 ) ) ) - v26 ) ) ) ) 
def funcNL_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v17 - (abs( ( ( v26 * v26 ) - v26 ) )/exp( ( 3.430534876431139 + ( v25 - v17 ) ) )) ) + ( ( ( v27 - v25 ) / 3.430534876431139 ) - ( ( (sin( ( v27 - v18 ) )/ 3.430534876431139 ) + ( ( v26 + v17 ) - v12 ) ) / (cos( ( (tan(cos( v26 ))- -3.0600712841360505 ) + v27 ) )+ 3.430534876431139 ) ) ) ) 

funcsNL_LANGUAGE = [funcNL_100307,funcNL_100408,funcNL_101006,funcNL_101107,funcNL_101309,funcNL_101410,funcNL_101915,funcNL_102008,funcNL_102311,funcNL_102816,]

def funcNL_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( -0.850567680987556 / ( ( 3.2337184086176443 + ( v2 * v2 ) ) / ( v14 + ( v18 - v11 ) ) ) ) + ( ( v20 - ( ( v26 - v5 ) + ( v2 - ( v24 + ( v17 + v7 ) ) ) ) ) / 3.2337184086176443 ) ) 
def funcNL_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v7 + ( ( v20 + v5 ) + v21 ) ) + ( ( (sin( v5 )- ( v26 - v22 ) ) - v8 ) + ( (sin( v5 )- ( v26 - v22 ) ) - v8 ) ) ) / ( 5.9678731297462235 -cos( ( v9 - v22 ) )) ) + ( v16 / ( 5.9678731297462235 - v23 ) ) ) 
def funcNL_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v28 + ( ( v16 + ( v17 + v15 ) ) + ( (sin( v1 )+ ( v24 + ( v5 + v5 ) ) ) - ( v12 - ( -1.6473271987158853 * v8 ) ) ) ) ) / 4.903575721475715 ) 
def funcNL_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v3 - ( ( v26 - v20 ) - v23 ) ) / ( ( v5 - ( ( v19 - -18.602852208790527 ) + ( v2 - v5 ) ) ) / -5.261246396382017 ) ) + ( ( v7 / ( ( v5 - ( ( v19 - -18.602852208790527 ) + ( v2 - v5 ) ) ) / -5.261246396382017 ) ) + ( ( ( ( v19 - -18.602852208790527 ) + ( v2 - v5 ) ) + ( -18.602852208790527 - v17 ) ) / -7.503539097440154 ) ) ) 
def funcNL_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( ( v18 + v26 ) / 3.7062883289155053 ) +exp(sin(sin( v11 )))) - v26 ) / ( v8 + ( ( 3.7062883289155053 - v18 ) - v4 ) ) ) + ( ( ( ( (sin(sin( v11 ))-cos( (cos( v11 )* v26 ) )) + v5 ) + v21 ) + v20 ) / ( 3.7062883289155053 +sin( v23 )) ) ) 
def funcNL_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v3 - v9 ) - ( v21 + ( v16 - v14 ) ) ) / -4.247987173080885 ) + ( ( ( ( v19 + ( v17 + v17 ) ) + v1 ) - v2 ) / ( ( 4.985419868559433 - v23 ) + v18 ) ) ) 
def funcNL_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v1 - v12 ) / ( (exp(abs( ( v5 - v6 ) ))*abs( ( v5 - v6 ) )) - ( -2.9241350692829435 - ( v5 - v6 ) ) ) ) + ( ( ( ( v5 *exp( (abs( v21 )* -0.4876232350569438 ) )) + v22 ) + v21 ) / 2.418275227941468 ) ) 
def funcNL_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v20 + (cos( ( ( v5 - 1.178763455921846 ) + ( v13 - v12 ) ) )+ ( ( ( v21 + 1.178763455921846 ) -exp( ( v0 - v2 ) )) + v28 ) ) ) / 3.525657124558343 ) 
def funcNL_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v17 - ( ( v26 - v7 ) - ( v20 + ( v28 + ( v7 + v0 ) ) ) ) ) / ( v6 + 5.65581067890848 ) ) - ( ( v21 / ( ( ( v21 - v17 ) - 5.65581067890848 ) + v22 ) ) + ( v8 - v5 ) ) ) 
def funcNL_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v5 - v22 ) + v21 ) - ( ( v17 - ( ( ( v5 - v2 ) *abs( v22 )) + v20 ) ) / ( 6.242520495208673 - v25 ) ) ) - ( ( ( ( ( ( v5 - v2 ) *abs( v22 )) + (abs( ( v17 + v20 ) )- 12.913012726145958 ) ) /abs( 6.242520495208673 )) / 3.0678821399099654 ) * ( v22 - ( ( v5 - v22 ) + v21 ) ) ) ) 

funcsNL_MOTOR = [funcNL_100307,funcNL_100408,funcNL_101006,funcNL_101107,funcNL_101309,funcNL_101410,funcNL_101915,funcNL_102008,funcNL_102311,funcNL_102816,]

def funcNL_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v8 / (abs( ( ( -2.4121231733878865 * v13 ) - ( v15 * -7.242104711877859 ) ) )+abs( ( v1 /sin(tan( 5.654148334767264 ))) )) ) - ( -0.3344930585441439 * ( ( v15 + v17 ) - (sin(tan( 5.654148334767264 ))* v1 ) ) ) ) 
def funcNL_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v15 - ( ( ( ( v4 * -0.37500537892456975 ) + v17 ) + ( v13 - v24 ) ) * -0.37500537892456975 ) ) - ( ( v26 - v15 ) * ( v3 / 10.690361895491694 ) ) ) + ( ( ( v15 - ( v26 - v15 ) ) - ( v0 - v19 ) ) / ( v19 + -4.168571435381892 ) ) ) 
def funcNL_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v17 + ( ( ( v8 - v19 ) + v26 ) + v18 ) ) + ( ( ( ( v27 - v2 ) + v1 ) - v14 ) + (cos( 2.258891785205165 )+cos( v26 )) ) ) / 4.518492263652565 ) 
def funcNL_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v23 - ( v15 + v0 ) ) / ( ( v28 - v17 ) - 4.114682222194208 ) ) - ( ( 4.114682222194208 - 4.114682222194208 ) - v13 ) ) - ( ( ( (sin( ( v28 - v17 ) )+ ( ( v28 - v17 ) / 4.114682222194208 ) ) - ( v1 - v13 ) ) - ( ( 4.114682222194208 - 4.114682222194208 ) - v13 ) ) / 4.114682222194208 ) ) 
def funcNL_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v21 + v1 ) / 3.6814931929363546 ) + ( v17 / 3.6814931929363546 ) ) - (sin( ( v26 / -3.216624666220799 ) )+ ( ( v22 / ( (cos( v22 )- v24 ) + (exp( v25 )- -3.216624666220799 ) ) ) + ( 0.3747493227215699 * ( v19 - v12 ) ) ) ) ) 
def funcNL_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v16 + v28 ) - v17 ) /sin(cos(sin( ( ( v26 *cos( 1.7847466126376368 )) + ( ( ( v26 *cos( 1.7847466126376368 )) * 1.7847466126376368 ) - v12 ) ) )))) *sin(cos( 1.7847466126376368 ))) - (exp(cos( 9.919551981287782 ))* ( ( ( ( v26 *cos( 1.7847466126376368 )) * 1.7847466126376368 ) - v12 ) - ( v4 + v15 ) ) ) ) 
def funcNL_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  (sin( ( ( (cos( v13 )/abs( ( v13 - ( -1.0312940737255083 + v17 ) ) )) / ( 10.710746163347224 -abs(abs( ( v13 - ( -1.0312940737255083 + v17 ) ) ))) ) * ( v6 - v16 ) ) )+ ( (sin( (cos( -1.0312940737255083 )* -2.596548041481892 ) )/ ( -2.596548041481892 / ( v13 + v17 ) ) ) - ( v15 / -2.596548041481892 ) ) ) 
def funcNL_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v7 - v4 ) + ( v13 - v19 ) ) + v17 ) + ( ( ( v6 *cos( ( v13 - v19 ) )) +sin( ( v17 - v23 ) )) + v13 ) ) / 3.421025596103494 ) 
def funcNL_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( (cos( -11.289552122019568 )* ( v27 - ( ( ( ( v2 - ( v26 + v22 ) ) / ( 3.4425023033748374 + ( v26 - v2 ) ) ) - v13 ) + ( v15 / -2.5937260159828845 ) ) ) ) + ( ( v8 - v19 ) / ( (cos( v22 )* v22 ) + 3.4425023033748374 ) ) ) 
def funcNL_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v1 + ( ( v4 - ( (cos( ( ( v26 * v18 ) * v18 ) )+ ( v26 * v18 ) ) / (exp( v18 )- -1.1293839530711658 ) ) ) + ( v6 +cos( ( ( v13 - v26 ) / -1.1293839530711658 ) )) ) ) / 3.517797864895819 ) 

funcsNL_RELATIONAL = [funcNL_100307,funcNL_100408,funcNL_101006,funcNL_101107,funcNL_101309,funcNL_101410,funcNL_101915,funcNL_102008,funcNL_102311,funcNL_102816,]

def funcNL_100307(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( ( ( v17 - v0 ) + ( v18 - v24 ) ) + ( v3 - v25 ) ) - ( v26 + v0 ) ) - v10 ) / -3.7155763290827757 ) + ( v19 / (abs( v28 )- -2.4137821141389466 ) ) ) 
def funcNL_100408(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v14 - v18 ) + v26 ) / (abs( ( 4.400619552043246 + v17 ) )- v0 ) ) + ( ( v7 /exp(exp( v8 ))) - ( ( v0 /tan( -0.9784889011236118 )) + ( v21 /exp(exp( v7 ))) ) ) ) 
def funcNL_101006(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( v0 - v3 ) + ( v25 *sin(cos(cos(sin( v3 ))))) ) - ( ( v18 - v24 ) - ( v8 + (abs( v3 )*sin( ( v19 -sin( v3 )) )) ) ) ) /exp(cos(cos(sin( v3 ))))) 
def funcNL_101107(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( v16 + ( ( ( v7 - v7 ) + ( ( v18 *sin( 3.5781459797817092 )) *cos( ( v7 - v18 ) )) ) + ( ( v12 / 3.5781459797817092 ) + ( ( v7 - v16 ) *cos( ( ( v18 *sin( 3.5781459797817092 )) + ( v10 -sin( 3.5781459797817092 )) ) )) ) ) ) 
def funcNL_101309(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( v19 / 2.913973130871529 ) - ( (tan( -9.704825302151843 )* ( ( ( v3 + v16 ) + v22 ) + v0 ) ) + ( ( ( v8 + v25 ) / ( -2.982682257790721 - ( v27 * ( v27 -cos( ( v3 + v16 ) )) ) ) ) + ( v3 - ( v27 / -2.345840961307619 ) ) ) ) ) 
def funcNL_101410(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v22 - ( v25 + v0 ) ) / -2.120677121033218 ) - ( ( ( ( v17 - v22 ) - 1.6595744966717234 ) / ( ( v4 + v4 ) - -7.839776397677483 ) ) * ( v20 + ( ( ( v26 - v15 ) - v18 ) +sin( v0 )) ) ) ) 
def funcNL_101915(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( 0.38140576325928066 * ( ( v26 + v0 ) + v19 ) ) + ( v3 * (cos( v24 )/ (cos( v24 )- (cos( ( v15 + v26 ) )+exp( 1.0033097763388632 )) ) ) ) ) + ( ( v25 - v14 ) / (cos( ( v15 + v26 ) )+exp( 1.0033097763388632 )) ) ) 
def funcNL_102008(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( ( ( v0 + v0 ) - v5 ) + v25 ) + ( ( v21 + v8 ) + ( ( v7 - v17 ) - v18 ) ) ) * ( (sin( v13 )- -4.719554397583426 ) /abs( -14.747702167286745 )) ) 
def funcNL_102311(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( ( ( v5 *cos( ( v24 - v25 ) )) - ( ( ( v16 + v24 ) - ( v28 - v0 ) ) + (sin( v25 )+ v9 ) ) ) / -3.022511894881461 ) 
def funcNL_102816(v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29): return  ( v8 + ( ( ( ( v19 - ( ( ( v18 - v19 ) + ( v28 - v0 ) ) + ( ( v18 - v19 ) + ( v28 - v0 ) ) ) ) -cos( (abs(sin( v18 ))- ( ( ( v18 - v19 ) + ( v28 - v0 ) ) + ( ( v18 - v19 ) + ( v28 - v0 ) ) ) ) )) / 3.69531981155788 ) - ( ( v14 - (tan(sin( v18 ))+ v28 ) ) / ( v26 + 6.493684916832013 ) ) ) ) 

funcsNL_SOCIAL = [funcNL_100307,funcNL_100408,funcNL_101006,funcNL_101107,funcNL_101309,funcNL_101410,funcNL_101915,funcNL_102008,funcNL_102311,funcNL_102816,]

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

funcsNL_WM = [funcNL_100307,funcNL_100408,funcNL_101006,funcNL_101107,funcNL_101309,funcNL_101410,funcNL_101915,funcNL_102008,funcNL_102311,funcNL_102816,]



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
		iFile = csv.reader(open("/home/james/Desktop/nData/" + t + "_"+str(s)+"_2_L" + lasts[lastsCount] + "_Z.csv",'r'))
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

np.savetxt('msEmat_NL_opt.csv', matrixMSE, delimiter=",")
np.savetxt('abEmat_NL_opt.csv', matrixABE, delimiter=",")
np.savetxt('minmat_NL_opt.csv', matrixMIN, delimiter=",")


		








