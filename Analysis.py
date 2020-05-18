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
y_1 = list(df.deaths)

growth_fit = curve_fit(growth_funct,x,y)
death_fit = curve_fit(growth_funct,x,y_1)
print (growth_fit)

a = 8.925
b = 80.3
c = 56598.7

a_death = 12.3
b_death = 91.6
c_death = 91137.5

sol_growth = int(fsolve(lambda x: growth_funct(x,a,b,c) - int(c),b))
sol_death = int(fsolve(lambda x: growth_funct(x,a_death,b_death,c_death) - int(c_death),b_death))

growth_pred_x = list(range(max(x),sol_growth))
death_pred_x = list(range(max(x),sol_death))

plt.scatter(x,y,label="Observed Infections",color="red")
plt.scatter(x,y_1,label="Observed Deaths",color="black")
plt.plot(x+growth_pred_x, [growth_funct(i,growth_fit[0][0],growth_fit[0][1],growth_fit[0][2]) for i in x+growth_pred_x], label="Infections model" )
plt.plot(x+death_pred_x, [growth_funct(i,death_fit[0][0],death_fit[0][1],death_fit[0][2]) for i in x+death_pred_x], label="Deaths model" )
plt.title("California COVID-19 Predictions")
plt.ylabel("Number of Infections")
plt.xlabel("Days Since Jan 1 2020")
plt.grid(True)
plt.legend(loc="upper left")
plt.show()

print(growth_funct(250,a,b,c))