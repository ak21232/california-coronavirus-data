# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:05:20 2020

@author: ak212
"""

import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Import Data

county_totals= "latimes-county-totals.csv"

df = pd.read_csv(county_totals, header=0)
df = df.dropna()
df = df[['date','county','confirmed_cases']]
df['date'] = pd.to_datetime(df['date'])
df['cumilative_cases'] = 0

#Separate data by county
df_dict = {name: df.loc[df['county'] == name] for name in df['county']}

for name in df_dict:
    i = 0
    while i < len(df_dict[name]):
        if i == 0:
            (df_dict[name])['cumilative_cases'].iloc[0] = (df_dict[name])['confirmed_cases'].iloc[0]
        else:
            (df_dict[name])['cumilative_cases'].iloc[i] += (df_dict[name])['confirmed_cases'].iloc[i-1]
        i+=1
    fig, ax = plt.subplots()
    ax.plot((df_dict[name])['date'], (df_dict[name])['cumilative_cases'] )
    fig.autofmt_xdate()
    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.set_title('COVID-19 Cases in '+ name + ' County')
    plt.show()
    plt.savefig(name + "_county_figure.png")
            

        
        


    



