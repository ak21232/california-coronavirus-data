# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:17:17 2020
Coronavirus analysis
@author: ak212
"""
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statistics import mean
import numpy as np
import datetime as dt
import math 


# csv directories
state_totals= "latimes-state-totals.csv"

# import data
df = pd.read_csv(state_totals, header = 0)
df = df.dropna()
df['date'] = pd.to_datetime(df['date'])
df['confirmed_cases'] = np.log(df['confirmed_cases'])
print(df.index)
x = df['date'].map(dt.datetime.toordinal)
y = df['confirmed_cases']


def logFit(x,y):
    # cache some frequently reused terms
    sumy = np.sum(y)
    sumlogx = np.sum(np.log(x))

    b = (x.size*np.sum(y*np.log(x)) - sumy*sumlogx)/(x.size*np.sum(np.log(x)**2) - sumlogx**2)
    a = (sumy - b*sumlogx)/x.size

    return a,b

def logFunc(x, a, b):
    return a + b*np.log(x)


plt.plot(df['date'], y, ls="none", marker='.')
xfit = np.linspace(737451,737580,num=200, endpoint = True)
plt.plot(xfit, logFunc(xfit, *logFit(x,y)))
plt.ylabel("Average Increase in Cases")
plt.xlabel("Time")
plt.title("Average Increase of COVID-19 Cases Over Time")
plt.show()