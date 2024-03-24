# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:14:43 2024

@author: craig
"""

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('P1_CTD_20081129.dat', delimiter= '\t') 

fig, ax = plt.subplots(1, 2)

ax[0].plot(data['Temp (C)'], data['Depth (m)'], color = 'b')
ax[1].plot(data['Salinity (PSU)'], data['Depth (m)'], color = 'r')

ax[0].set_xlabel('Temp (C)')
ax[1].set_xlabel('Salinity (PSU)')
ax[0].set_ylabel('Depth (m)')
fig.tight_layout()

fig.savefig('Temperature_+_Salinty_profiles.png')