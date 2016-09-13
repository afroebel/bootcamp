import numpy as np
import scipy.stats


import matplotlib.pyplot as plt

import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 15,
        'axes.titlesize' : 18}
sns.set(rc=rc)


def ecdf(data):
    """
    Compute x, y values for empirical distribution function.
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

# Load the food data.
xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low = np.loadtxt('data/xa_low_food.csv')

x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)


#Smoothing stuff?
x = np.linspace(1600, 2500, 400)
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale=np.std(xa_high))
cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))


# alpha sets transparency, good idea to add it in general, looks cooler and
# easier to see data.
plt.plot(x_high, y_high, marker='.', linestyle='none', markersize=20, alpha = 0.5)
plt.plot(x_low, y_low, marker='.', linestyle='none', markersize=20, alpha = 0.5)
plt.plot(x, cdf_high, color='gray')
plt.plot(x, cdf_low, color='gray')
plt.xlabel('Cross-sectional area (um)')
plt.ylabel('eCDF')
plt.legend(('high food', 'low food'), loc = 'lower right')
plt.show()
