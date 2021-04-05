# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:05:53 2020

@author: omar
"""

import pandas as pd

licenses = pd.read_pickle('licenses.p')
biz_owners = pd.read_pickle('business_owners.p')

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values(by='account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())