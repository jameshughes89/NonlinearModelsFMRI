import csv
import matplotlib.pylab as plt
import numpy as np
import scipy.stats

oldD = np.array(list(csv.reader(open('../EMOTION_100307_2_L7_Z/stats.csv', 'r')))).astype(float)[:,1]
newD = np.array(list(csv.reader(open('EMOTION_100307_2_L7_Z/stats.csv', 'r')))).astype(float)[:,1]

print scipy.stats.mannwhitneyu(oldD, newD)
print np.min(oldD), np.mean(oldD)
print np.min(newD), np.mean(newD)
plt.hist(oldD, alpha=0.5)
plt.hist(newD, alpha=0.5)
plt.show()
