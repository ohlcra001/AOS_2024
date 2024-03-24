# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:32:12 2024

@author: craig
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

Posdata = pd.read_csv('SAA2_WC_2017_metocean_10min_avg.csv', parse_dates = ['TIME_SERVER'], index_col = ['TIME_SERVER'], na_values= 'NaN') 

trip = Posdata['2017-06-28 17:10:00' : '2017-07-04 23:50:00']
plt.style.use('grayscale')
fig, ax = plt.subplots()

plt.style.use('grayscale')
ax.plot(trip.index, trip['TSG_TEMP'])
ax.xaxis.set_major_locator(ticker.LinearLocator(3))
ax.set_ylabel('Temp(C)')
ax.set_xlabel('Time')

fig.savefig('Timeseries_gray_p2.png')



        
fig1, ax1 = plt.subplots()
sal = trip[trip['TSG_SALINITY'] > 30]

ax1.hist(sal['TSG_SALINITY'], bins=(10))
ax1.set_xlabel('Salinity (PSU)')
ax1.set_ylabel('Number of observations')

fig1.savefig('Histogram_p2.png')


plt.style.use('default')
fig2, ax2 = plt.subplots()

ax2.scatter(trip['WIND_SPEED_TRUE'], trip['AIR_TEMPERATURE'], c= trip['LATITUDE'])
ax2.set_ylabel('Air temp (C)')
ax2.set_xlabel('Wind Speed (m/s)')

fig2.savefig('Scatterplot_p2.png', dpi=200)
