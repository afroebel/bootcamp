import numpy as np
import matplotlib.pyplot as plt
from e3_2 import *

# Part A: load data
wt_lac = np.loadtxt('data/wt_lac.csv', delimiter = ',', skiprows=3)
q18m_lac = np.loadtxt('data/q18m_lac.csv', delimiter = ',', skiprows=3)
q18a_lac = np.loadtxt('data/q18a_lac.csv', delimiter = ',', skiprows=3)

#wt
iptg0 = wt_lac[:,0]
fold0 = wt_lac[:,1]

#q18m
iptgm = q18m_lac[:,0]
foldm = q18m_lac[:,1]

#q18a
iptga = q18a_lac[:,0]
folda = q18a_lac[:,1]

# theoreticals
th0 = fold_change(np.logspace(-5,2,20), 141.5, KdA=0.017, KdI=0.002, Kswitch=5.8)
tha = fold_change(np.logspace(-5,2,20), 16.56, KdA=0.017, KdI=0.002, Kswitch=5.8)
thm = fold_change(np.logspace(-5,2,20), 1328, KdA=0.017, KdI=0.002, Kswitch=5.8)

#Part B: plot data
plt.plot(iptg0, fold0, marker='.', linestyle='none', markersize=20)
plt.plot(iptgm, foldm, marker='.', linestyle='none', markersize=20)
plt.plot(iptga, folda, marker='.', linestyle='none', markersize=20)
plt.plot(np.logspace(-5,2,20), th0)
plt.plot(np.logspace(-5,2,20), tha)
plt.plot(np.logspace(-5,2,20), thm)
plt.xscale('log')
plt.xlabel('IPTG (mM)')
plt.ylabel('fold change')
plt.legend(('wild type', 'q18m', 'q18a'), loc = 'upper left')
plt.title('lac operon fold change by mutant')
plt.show()
