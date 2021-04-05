# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:52:12 2020

@author: omar
"""

import pandas as pd

gdp = pd.read_csv('WorldBank_GDP.csv')
sp500 = pd.read_csv('S&P500.csv')
pop = pd.read_csv('WorldBank_POP.csv')

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='Year', right_on='Date', 
                             how='left')
# Print gdp_sp500
print (gdp_sp500)

# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='Year', right_on='Date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['GDP','Returns']]

# Print gdp_returns correlation
print(gdp_returns.corr())

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp, pop, on=['Year','Country Name'], 
                             fill_method='ffill')

# Print ctry_date
print(ctry_date)

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=['Country Name','Year'], 
                             fill_method='ffill')

# Print date_ctry
print(date_ctry)