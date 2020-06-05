from numpy import random
import numpy as np
import matplotlib.pyplot as plt

# we sample 500k samples of size 30 from chisquare distribution
s30 = np.random.chisquare(2, (30, 1500000))
# we sample 500k samples of size 10 from chisquare distribution
s10 = np.random.chisquare(2, (10, 1500000))
# for every sample we calculate the mean, obtaining "sampling distribution of the mean"
s_mean_30 = np.mean(s30, 0)
s_mean_10 = np.mean(s10, 0)
# create bins
bins = np.linspace(0, 10, 1000)
# plot histogram of one of the samples and distribuition of the mean
plt.hist(s30[0, :], bins, alpha=0.4, label='chi-square, k = 2')
plt.hist(s_mean_10, bins, alpha=0.4, label='distribution of sample means, s = 10')
plt.hist(s_mean_30, bins, alpha=0.4, label='distribution of sample means, s = 30')
plt.legend(loc='upper right')
plt.show()

