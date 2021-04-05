# -*- coding: utf-8 -*-

#1-# Import pandas using the alias pd
import pandas as pd

#2-Importing Data with Pandas
homelessnessdf = pd.read_csv('homelessness.csv')

#3-Inspecting a DataFrame

# Print the head of the homelessness data
print(homelessnessdf.head())

# Print information about homelessness
print(homelessnessdf.info())

# Print the shape of homelessness
print(homelessnessdf.shape)

# Print a description of homelessness
print(homelessnessdf.describe())

#4-Parts of a DataFrame

# Print the values of homelessness
print(homelessnessdf.values)

# Print the column index of homelessness
print(homelessnessdf.columns)

# Print the row index of homelessness
print(homelessnessdf.index)

#5-Sorting rows
# Sort homelessness by individuals
homelessness_ind = homelessnessdf.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())

#6-Subsetting columns
# Select the individuals column
individuals = homelessnessdf['individuals']

# Print the head of the result
print(individuals.head())

#7-Subsetting rows
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessnessdf[homelessnessdf['individuals'] > 10000]

# See the result
print(ind_gt_10k)

#8-Subsetting rows by categorical variables
# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessnessdf[(homelessnessdf['region'] == "South Atlantic") | (homelessnessdf['region'] == "Mid-Atlantic")]

# See the result
print(south_mid_atlantic)

#9-Adding new columns
# Add total col as sum of individuals and family_members
homelessnessdf['total'] = homelessnessdf['individuals'] + homelessnessdf['family_members']

# Add p_individuals col as proportion of individuals
homelessnessdf['p_individuals'] = homelessnessdf['individuals'] / homelessnessdf['total']

# See the result
print(homelessnessdf)

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessnessdf["indiv_per_10k"] = 10000 * homelessnessdf['individuals'] / homelessnessdf['state_pop'] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessnessdf[homelessnessdf["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k',ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state', 'indiv_per_10k']]

# See the result
print(result)





