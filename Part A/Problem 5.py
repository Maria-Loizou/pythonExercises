#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 21:01:43 2022

@author: MariaLoizou
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


#Part A: Read the CSV file and store as a panda dataframe 
url = 'http://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv'
data = pd.read_csv (url)

#Part B
"""Initiate dictionary"""
dict1 = {}
"""While loop: While the lenght of the dataframe > 0 then the mean rate
   for the first 12 months is calculated. 
   The year is derived from the first four vlaues of the date. 
   The year acts as the key and means as the values in dict1.
   Data is re-assigned to last len(data)-12 rows"""
   
while len(data)>0:
    year_mean = data.head(12)['VALUE'].mean()
    first_month = int(data.iloc[0]['DATE'][0:4])
    dict1[first_month]=year_mean
    data=data.tail(len(data)-12)

dict2 = {'Year':dict1.keys(),'Mean Rate':dict1.values()}

"""The dictionary is then converted to a dataframe """
yearly_data = pd.DataFrame.from_dict(dict2)

"""Plot the histogram"""
ax = yearly_data['Mean Rate'].plot(kind = 'hist')
ax.set_xlabel("Annual average rate")
ax.set_ylabel("Frequency")
plt.title("Frequency of the annual US civilian unmployment rate between the years 1948 and 2021")
plt.grid()         
plt.show()

#Part C
"""Define the arguments to be used for the regression"""
x = yearly_data['Year']
y = yearly_data['Mean Rate']

"""Perform linear regression"""
regression = stats.linregress(x,y)

"""Plot the graph"""
plt.plot(x, y, 'o', label='actual averages')
plt.plot (x, regression.intercept + regression.slope *x, 'r', label = 'regression line')
plt.grid()
plt.legend() 
plt.title('Average annual US civilian unmployment rate from 1948 to 201')
plt.xlabel("Year")
plt.ylabel("Annual average rate")
plt.show()
