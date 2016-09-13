import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlibs rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 10}
sns.set(rc=rc)

# Load the food data.
xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low = np.loadtxt('data/xa_low_food.csv')

# Make the bin boundaries.
bins = np.arange(1700, 2500, 50)

#Plot the data as a histogram.
# _ is garbage collector to get rid of unnecessary output
_ = plt.hist(xa_low, bins=bins)
plt.xlabel('Cross-sectional area (um$^2$)')
plt.ylabel('count')
plt.show()

#Save the figure
plt.savefig('egg_area_histograms.svg', bbox_inches='tight')
