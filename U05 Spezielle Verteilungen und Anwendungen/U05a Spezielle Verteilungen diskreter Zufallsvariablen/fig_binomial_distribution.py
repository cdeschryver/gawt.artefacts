"""
Example of a Binomial distribution
----------------------------------
Figure 3.9.

This shows an example of a binomial distribution with various parameters.
We'll generate the distribution using::

    dist = scipy.stats.binom(...)

Where ... should be filled in with the desired distribution parameters
Once we have defined the distribution parameters in this way, these
distribution objects have many useful methods; for example:

* ``dist.pmf(x)`` computes the Probability Mass Function at values ``x``
  in the case of discrete distributions

* ``dist.pdf(x)`` computes the Probability Density Function at values ``x``
  in the case of continuous distributions

* ``dist.rvs(N)`` computes ``N`` random variables distributed according
  to the given distribution

Many further options exist; refer to the documentation of ``scipy.stats``
for more details.
"""
# Author: Jake VanderPlas
# License: BSD
#   The figure produced by this code is published in the textbook
#   "Statistics, Data Mining, and Machine Learning in Astronomy" (2013)
#   For more information, see http://astroML.github.com
#   To report a bug or issue, use the following forum:
#    https://groups.google.com/forum/#!forum/astroml-general
import numpy as np
from scipy.stats import binom
from matplotlib import pyplot as plt

#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
#from astroML.plotting import setup_text_plots
#setup_text_plots(fontsize=8, usetex=True)

#------------------------------------------------------------
# Define the distribution parameters to be plotted
#n_values = [100, 100, 100, 100, 100]
n_values = [1, 5, 10, 50, 100]
#p_values = [0.01, 0.2, 0.5, 0.8, 0.95]
p_values = [0.5, 0.5, 0.5, 0.5, 0.5]
x = np.arange(-1, 200)

#------------------------------------------------------------
# plot the distributions
fig, ax = plt.subplots(figsize=(5, 3.75))

for (n, p) in zip(n_values, p_values):
    # create a binomial distribution
    dist = binom(n, p)

    plt.plot(x, dist.pmf(x),
             label=r'$p=%.3f,\ n=%i$' % (p, n), linestyle='steps-mid')

plt.xlim(-0.5, 100)
plt.ylim(0, 0.8)

plt.xlabel('$x$')
plt.ylabel(r'$P(x|p, n)$')
plt.title('Binomial Distribution')

plt.legend()
plt.show()
