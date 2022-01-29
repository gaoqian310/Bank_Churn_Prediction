#!/usr/bin/env python
# coding: utf-8

# In[2]:


## REQUIRED LIBRARIES
# For data wrangling 
import numpy as np
import pandas as pd

# For visualization
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
pd.options.display.max_rows = None
pd.options.display.max_columns = None


# In[3]:


# Read the data frame
df = pd.read_csv('Churn_Modelling.csv', delimiter=',')
df.shape


# In[4]:


# Check columns list and missing values
df.isnull().sum()


# In[5]:


# Get unique count for each variable
df.nunique()


# In[6]:


# drop the columns as explained above
df = df.drop(["RowNumber", "CustomerId","Surname"], axis = 1)


# In[7]:


# Review the top rows of what is left of the data frame
df.head()


# In[8]:


# Check variable data types
df.dtypes


# In[9]:


# Exploratory Data Analysis


# In[20]:


# using a pie chart , first create labels
labels = 'Exited', 'Retained'
# two parts of pie chart, Exited == 1 and Exited == 0
sizes = [df.Exited[df['Exited']==1].count(), df.Exited[df['Exited']==0].count()]
# explode created array-like pie chart, default:None will create a whole pie chart without explode
explode = (0, 0.15)

# plot
fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
# title
plt.title("Proportion of customer churned and retained", size = 20)
plt.show()


# #### So about 20% of the customers have churned. 
# 
# ###### So the baseline model could be to predict that 20% of the customers will churn. Given 20% is a small number, we need to ensure that the chosen model does predict with great accuracy this 20% as it is of interest to the bank to identify and keep this bunch as opposed to accurately predicting the customers that are retained.

# In[ ]:




