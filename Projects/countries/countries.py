# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:31:33 2020

@author: omar
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('countries-of-the-world.csv')

gdp = df["GDP ($ per capita)"]
phones = df["Phones (per 1000)"]
percent_literate = df["Population"]
region = df["Region"]

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()

