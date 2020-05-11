# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:17:17 2020
Coronavirus analysis
@author: ak212
"""
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


# csv directories
state_totals= "latimes-state-totals.csv"

# import data
df = pd.read_csv(state_totals, header = 0)
df = df.dropna()
df['date'] = pd.to_datetime(df['date'])

def growth_funct(x,a,b,c):
    return (c/(1+np.exp(-(x-b)/a)))

x = list(df.index)
y = list(df.confirmed_cases)

fit = curve_fit(growth_funct,x,y)

a = 11.2
b = 87.9
c = 79216.8

sol = int(fsolve(lambda x: growth_funct(x,a,b,c) - int(c),b))

pred_x = list(range(max(x),sol))

plt.scatter(x,y,label="Real data",color="red")

plt.plot(x+pred_x, [growth_funct(i,fit[0][0],fit[0][1],fit[0][2]) for i in x+pred_x], label="Logistic model" )

plt.title("California COVID-19 Predictions")
plt.ylabel("Number of Infections")
plt.xlabel("Days Since Jan 1 2020")
plt.grid(True)
plt.legend(loc="upper left")
plt.show()

print(growth_funct(180,a,b,c))