# Exercise 4: finches
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)


# Part A: load data files
finches_1973 = pd.read_csv('data/grant_1973.csv', comment = '#')
finches_1975 = pd.read_csv('data/grant_1975.csv', comment = '#')
finches_1987 = pd.read_csv('data/grant_1987.csv', comment = '#')
finches_1991 = pd.read_csv('data/grant_1991.csv', comment = '#')
finches_2012 = pd.read_csv('data/grant_2012.csv', comment = '#')


# Part B: Munging
finches_1973 = finches_1973.drop('yearband', axis=1)

# Create year Series:
year_1973 = pd.Series(len(finches_1973)*[1973], name = 'year')
year_1975 = pd.Series(len(finches_1975)*[1975], name = 'year')
year_1987 = pd.Series(len(finches_1987)*[1987], name = 'year')
year_1991 = pd.Series(len(finches_1991)*[1991], name = 'year')
year_2012 = pd.Series(len(finches_2012)*[2012], name = 'year')

# Concat:
finches_1973 = pd.concat((year_1973, finches_1973), axis=1)
finches_1975 = pd.concat((year_1975, finches_1975), axis=1)
finches_1987 = pd.concat((year_1987, finches_1987), axis=1)
finches_1991 = pd.concat((year_1991, finches_1991), axis=1)
finches_2012 = pd.concat((year_2012, finches_2012), axis=1)

# Standardize column names:
finches_1973 = finches_1973.rename(columns = {'beak length': 'beak length (mm)'})
finches_1973 = finches_1973.rename(columns = {'beak depth': 'beak depth (mm)'})
finches_1975 = finches_1975.rename(columns = {'Beak length, mm': 'beak length (mm)'})
finches_1975 = finches_1975.rename(columns = {'Beak depth, mm': 'beak depth (mm)'})
finches_1987 = finches_1987.rename(columns = {'Beak length, mm': 'beak length (mm)'})
finches_1987 = finches_1987.rename(columns = {'Beak depth, mm': 'beak depth (mm)'})
finches_1991 = finches_1991.rename(columns = {'blength': 'beak length (mm)'})
finches_1991 = finches_1991.rename(columns = {'bdepth': 'beak depth (mm)'})
finches_2012 = finches_2012.rename(columns = {'blength': 'beak length (mm)'})
finches_2012 = finches_2012.rename(columns = {'bdepth': 'beak depth (mm)'})

# Drop duplicates:
finches_1973 = finches_1973.drop_duplicates(subset='band')
finches_1975 = finches_1975.drop_duplicates(subset='band')
finches_1987 = finches_1987.drop_duplicates(subset='band')
finches_1991 = finches_1991.drop_duplicates(subset='band')
finches_2012 = finches_2012.drop_duplicates(subset='band')

# Concat total:
finches_all = pd.concat((finches_1973, finches_1975, finches_1987, finches_1991, finches_2012),
            ignore_index=True)


# Part D: ECDFs
# 1987 beak depths and lengths, fortis and scandens
fortis_bd = finches_all.loc[finches_all['year'] == 1987].loc[finches_all['species']
            == 'fortis', ['beak depth (mm)']]
scandens_bd = finches_all.loc[finches_all['year'] == 1987].loc[finches_all['species']
            == 'scandens', ['beak depth (mm)']]
fortis_bl = finches_all.loc[finches_all['year'] == 1987].loc[finches_all['species']
            == 'fortis', ['beak length (mm)']]
scandens_bl = finches_all.loc[finches_all['year'] == 1987].loc[finches_all['species']
            == 'scandens', ['beak length (mm)']]

x_fortis_bd, y_fortis_bd = ecdf(fortis_bd)
x_scandens_bd, y_scandens_bd = ecdf(scandens_bd)
x_fortis_bl, y_fortis_bl = ecdf(fortis_bl)
x_scandens_bl, y_scandens_bl = ecdf(scandens_bl)


plt.plot(x_fortis_bd, y_fortis_bd, marker = '.', linestyle = 'none')
plt.plot(x_scandens_bd, y_scandens_bd, marker = '.', linestyle = 'none')
plt.legend(('fortis', 'scandens'))
plt.show()
