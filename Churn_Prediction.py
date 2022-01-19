#!/usr/bin/env python
# coding: utf-8

# In[1]:

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


# In[2]:


# Read the data frame
df = pd.read_csv('Churn_Modelling.csv', delimiter=',')
df.shape


# In[3]:


# Check columns list and missing values
df.isnull().sum()


# In[4]:


# Get unique count for each variable
df.nunique()


# In[ ]:




