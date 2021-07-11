# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:01:42 2020

@author: omar
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

mpg = pd.read_csv("mpg.csv")

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",
            hue="cylinders")

# Show plot
plt.show()

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration",
            y="mpg",
            data=mpg,
            kind="scatter",
            hue="origin",
            style="origin")

# Show plot
plt.show()

# Create line plot
sns.relplot(x="model_year",
            y="mpg",
            data=mpg,
            kind="line")

# Show plot
plt.show()

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci="sd")

# Show plot
plt.show()

# Create line plot of model year vs. horsepower
# Change to create subgroups for country of origin
# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin",
            markers=True,
            dashes=False)

# Show plot
plt.show()

# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Identify plot type
type_of_g = type(g)

# Print type
print(type_of_g)

# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")

# Show plot
plt.show()

mpg['mean'] = mpg["mpg"].mean()
mpg_mean = mpg[["model_year", "origin", "mean"]]

# Create line plot
g = sns.lineplot(x="model_year", y="mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Show plot
plt.show()

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel="Car Model Year", ylabel="Average MPG")


# Show plot
plt.show()

# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation=90)

# Show plot
plt.show()