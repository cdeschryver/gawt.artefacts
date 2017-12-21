import numpy as np
import matplotlib.pyplot as plt

mu = 0
sigma = 10
N = 10E4.as_integer_ratio()
numberOfBins = 100

count4, bins4, ignored = plt.hist(np.random.normal(-3, 0.6, N), numberOfBins, normed=True)
count3, bins3, ignored = plt.hist(np.random.normal(4, 1, N), numberOfBins, normed=True)
count2, bins2, ignored = plt.hist(np.random.normal(0, 3, N), numberOfBins, normed=True)
count1, bins1, ignored = plt.hist(np.random.normal(0, 1, N), numberOfBins, normed=True)

plt.show()
plt.clf()
plt.cla()
plt.close()
