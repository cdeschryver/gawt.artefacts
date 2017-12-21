import numpy as np
from scipy.stats import expon
from matplotlib import pyplot as plt

#------------------------------------------------------------
# Define the distribution parameters to be plotted
lambda_values = [0, 0.1, 0.5, 1, 2]

fig, ax = plt.subplots(figsize=(5, 3.75))

for lambd in lambda_values:
    dist = expon(lambd)
    x = np.arange(-1, 200, 0.01)

    plt.plot(x, lambd * dist.pdf(x),
             label=r'$\lambda=%f$' % lambd, linestyle='steps-mid')

plt.xlim(-0.5, 30)
plt.ylim(0, 1.2)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\lambda)$')
plt.title('Exponential Distribution')

plt.legend()
plt.show()
