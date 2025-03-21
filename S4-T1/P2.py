#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


df = pd.read_csv("auto-mpg.csv")
df


# In[3]:


df.head(10)


# In[4]:


get_ipython().run_line_magic('pinfo2', 'df.head')


# In[5]:


df.tail(10)


# In[6]:


get_ipython().run_line_magic('pinfo2', 'df.tail')


# In[7]:


df.info()


# In[8]:


df.shape


# In[9]:


get_ipython().run_line_magic('pinfo2', 'df.shape')


# In[10]:


get_ipython().run_line_magic('pinfo2', 'df.describe')


# In[11]:


df.describe()


# In[12]:


df.describe(percentiles=[0.1,0.7,0.9])


# In[13]:


df.describe(include="all")


# In[14]:


df.describe(exclude=[np.number])


# In[15]:


df[['mpg','cylinders']]


# In[16]:


print(df.to_string())


# In[4]:


df.describe(include=[np.number])


# In[23]:


df[['mpg','cylinders']].describe()
df[df['horsepower']=='?']


# In[24]:


df = df[df['horsepower']!='?']
df[df['horsepower']=='?']


# In[15]:


import matplotlib.pyplot as plt


# In[8]:


pd.plotting.scatter_matrix(df,figsize=[15,15])


# In[16]:


pd.crosstab(df["cylinders"],df['model year'])


# In[25]:


pd.plotting.boxplot(df)


# In[26]:


pd.plotting.parallel_coordinates(df,'cylinders',cols=['acceleration','mpg'])


# In[27]:


df.corr()


# # wap to read the csv height and weight 
# # task 1 abstract the information of the csv 
# # task 2 write the statistical summary 
# # tast 3 create a corelation tabel
# # task 4 create a box-plot of height and weight 

# In[9]:


df = pd.read_csv("heights_weights.csv")
df


# In[11]:


df.info()


# In[12]:


df.describe()


# In[10]:


df.corr()


# In[13]:


pd.plotting.boxplot(df)


# In[16]:


df = pd.DataFrame([[1,2],[4,5],[7,8]],index=['cobra','viper','sidewind'],columns=['max_speed','shield'])
df


# In[17]:


df['shield']


# In[22]:


df.loc['viper','shield'] = 100
df


# In[23]:


df.loc['cobra':'viper','shield']


# In[ ]:




