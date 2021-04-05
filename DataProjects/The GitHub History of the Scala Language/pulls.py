# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:18:46 2020

@author: omar
"""

# Importing pandas
import pandas as pd
import matplotlib.pyplot as plt

# Loading in the data
pulls_one = pd.read_csv('pulls_2011-2013.csv')
pulls_two = pd.read_csv('pulls_2014-2018.csv')
pull_files = pd.read_csv('pull_files.csv') 

# Append pulls_one to pulls_two
pulls = pulls_one.append(pulls_two, ignore_index=True)

# Convert the date for the pulls object
pulls['date'] = pd.to_datetime(pulls['date'], utc=True)

# Merge the two DataFrames
data = pulls.merge(pull_files, on='pid')

# Create a column that will store the month
data['month'] = data['date'].dt.month

# Create a column that will store the year
data['year'] = data['date'].dt.year

# Group by the month and year and count the pull requests
counts = data.groupby(['year', 'month'])['pid'].count()

# Plot the results
counts.plot(kind='bar', figsize = (12,4))

# Group by the submitter
by_user = data.groupby('user').agg({'pid': 'count'})

# Plot the histogram
by_user.hist()

# Identify the last 10 pull requests
last_10 = pulls.sort_values(by = 'date').tail(10)

# Join the two data sets
joined_pr = pull_files.merge(last_10, on='pid')

# Identify the unique files
files = set(joined_pr['file'])

# Print the results
files

# This is the file we are interested in:
file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

# Identify the commits that changed the file
file_pr = data[data['file'] == file]

# Count the number of changes made by each developer
author_counts = file_pr.groupby('user').count()

# Print the top 3 developers
author_counts.nlargest(3, 'file')

file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

# Select the pull requests that changed the target file
file_pr = pull_files[pull_files['file'] == file]

# Merge the obtained results with the pulls DataFrame
joined_pr = pulls.merge(file_pr, on='pid')

# Find the users of the last 10 most recent pull requests
users_last_10 = set(joined_pr.nlargest(10, 'date')['user'])

# Printing the results
users_last_10

