import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# Generate and array of x-values
x = np.linspace(-15, 15, 400)

#Compute the normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x)**2

# Plot our computation
# $$ makes stuff in between be rendered more mathishy
plt.plot(x, norm_I, marker='.', linestyle='none')
plt.xlabel('$x$')
plt.ylabel('$I(x) / I_0$')
