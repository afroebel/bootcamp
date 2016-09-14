import numpy as np
import matplotlib.pyplot as plt

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

x_1975, y_1975 = ecdf(bd_1975)

plt.plot(x_1975, y_1975)
