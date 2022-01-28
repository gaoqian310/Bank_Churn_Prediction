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


# In[ ]:




