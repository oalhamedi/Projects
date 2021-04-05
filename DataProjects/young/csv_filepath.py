# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:58:03 2020

@author: omar
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv("1.2.1_example_csv.csv")
survey_data = pd.read_csv("young-people-survey-responses.csv")

Spiders = survey_data["Spiders"]

# Print the head of df
print(df.head())

# Create a count plot with "Spiders" on the x-axis
sns.countplot(data=survey_data, x="Spiders")

# Display the plot
plt.show()

# Create count plot of internet usage
sns.catplot(x="Internet usage", data=survey_data, kind= "count")


# Show plot
plt.show()

# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()

# Create column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count",
            col="Age")

# Show plot
plt.show()

# Create a bar plot of interest in math, separated by gender
sns.catplot(x="Gender", y="Mathematics",
            data= survey_data, kind="bar" )


# Show plot
plt.show()


