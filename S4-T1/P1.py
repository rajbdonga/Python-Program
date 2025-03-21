#!/usr/bin/env python
# coding: utf-8

# ## Pandas Series

# In[53]:


import pandas as pd


# In[54]:


a = 'hello'
ser1 = pd.Series(a)
print(ser1)
print(type(ser1))


# In[55]:


import numpy as np
b = [1,2,3]
c = {'a':1 , 'b':2}
d = np.arange(3)
ser2 = pd.Series(b)
ser3 = pd.Series(c)
ser4 = pd.Series(d)
print(ser2)
print(ser3)
print(ser4)


# In[56]:


get_ipython().run_line_magic('pinfo2', 'ser1.shape')


# In[57]:


ser1.shape


# In[58]:


print(ser1)


# In[59]:


myseries = pd.Series(data = b,index = ['x','y','z'], name = 'python')
print(myseries)


# ## INDEXING

# In[60]:


myseries[0]


# In[61]:


ob1 = pd.Series([1,2,3,None])
print(ob1)
ob2 = pd.Series([1,2,3,""])
print(ob2)


# ## ATTRIBUTES

# In[62]:


series = pd.Series(data = [1,2,None],index = ['x','y','z'], name = 'python')
print(series)


# In[63]:


print(series.index)
print(series.values)
print(series.dtype)
print(series.shape)
print(series.dtype.itemsize)
print(series.size)
print(series.hasnans)
print(series.empty)
print(series.ndim)
print(series.name)
print(series.count())


# In[64]:


type(np.nan)


# In[65]:


get_ipython().run_line_magic('pinfo2', 'series.dtype.itemsize')


# In[66]:


ser = pd.Series(data = [1,2,None],index = [8,1,2], name = 'python')
print(ser)


# In[67]:


ser.sort_index()


# In[68]:


ser.sort_values()


# In[69]:


ser


# In[70]:


ser.reindex([100,1,300])


# In[71]:


l = [1,2,3,4,5,6]
ser = pd.Series(l)
print(ser)


# In[72]:


ser[2:4] = 100


# In[73]:


ser


# In[74]:


print(ser>5)


# In[75]:


print(ser[ser>5])


# ## DATAFRAME

# In[76]:


pwd


# In[77]:


get_ipython().run_cell_magic('writefile', 'jupytercsv.csv', 'id,name,school\n1,a,x\n2,b,y\n3,c,z')


# ## Loading CSV

# In[ ]:


df = pd.read_csv("mydata.csv");
df


# ## Read CSV From URL

# In[78]:


df = pd.read_csv("https://raw.githubusercontent.com/patelmanishv/Sem4Data/refs/heads/master/auto-mpg.csv")


# In[79]:


df


# In[80]:


print(type(df))


# In[81]:


print(df.to_string())


# ## Creating Interface

# In[82]:


data = { 'name' : ['AA', 'IBM', 'GOOG'],
'date' : ['2001-12-01', '2012-02-10', '2010-04-09'],
'shares' : [100, 30, 90],
'price' : [12.3, 10.3, 32.2]
}


# In[83]:


df = pd.DataFrame(data)
df


# In[84]:


df['owner'] = 'python'
df


# In[85]:


df['name']


# In[86]:


type(df['name'])


# In[87]:


df['shares']


# In[88]:


df.loc[2]


# In[89]:


df = df.set_index(['date'])
df


# In[90]:


df.loc['2001-12-01']

