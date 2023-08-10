#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


df = pd.read_excel(r"C:\Users\pavan\OneDrive\Documents\salesdata.xlsx")


# In[4]:


df.info()


# In[5]:


df.columns


# In[6]:


df.describe()
# descriptive statistcs


# In[7]:


df.head(10)


# In[8]:


df.tail(10)


# In[9]:


df.describe(include = 'all')


# In[10]:


a = df.groupby(by = 'Region')
a.sum('Sales').sort_values('Sales',ascending = False)


# In[11]:


df.groupby(['Region'])['Sales'].sum().sort_values(ascending = False)


# In[12]:


df.groupby(['Region'])[['Sales','COGS']].count()


# In[13]:


df.groupby(['Region'])[['Sales','COGS']].mean()


# In[14]:


df.groupby(['Region'])[['Sales','COGS']].mean().round(2)


# In[15]:


df.groupby(['Region','Sales Rep'])['Sales'].mean().round(2)


# In[16]:


df.groupby(['Region','Sales Rep'])['Sales'].mean().sort_values(ascending = False).round(2)


# In[17]:


df.groupby(['Region','Sales Rep'])['Sales'].mean().round(2).nlargest()


# In[18]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[19]:


sns.barplot(y = 'Sales', x = 'Sales Rep',hue = 'Region',data=df)


# In[20]:


figs, axs = plt.subplots(figsize = (15,10))
sns.barplot(x = 'Region',
           y = 'Sales',
           hue = 'Sales Rep',
           data = df.groupby(['Region','Sales Rep'],as_index = False)['Sales'].mean())


# In[21]:


figs, axs = plt.subplots(figsize = (15,10))
sns.barplot(x = 'Sales Rep',
           y = 'Sales',
           hue = 'Region',
           data = df.groupby(['Region','Sales Rep'],as_index = False)['Sales'].mean())


# In[22]:


sns.barplot(x = 'Sales Rep',y = 'Sales', data = df,estimator = sum)


# In[23]:


sns.barplot(x = 'Region',y = 'Sales', data = df,estimator = sum)


# In[24]:


df.groupby(['Sales Rep'])['Sales'].sum()


# In[25]:


df.groupby(['Sales Rep'])['Sales'].mean()


# In[26]:


df.groupby(['Sales Rep'])['Product'].count().sort_values(ascending = False)


# In[27]:


df.groupby(['Sales Rep','Region'])['Sales'].mean()


# In[28]:


df.groupby(['Sales Rep','Region'])['Sales'].sum()


# In[29]:


df['Sales_bin']= pd.cut(df['Sales'],bins = 4 , labels = (1,2,3,4))


# In[30]:


df.head()


# In[38]:


fig, ax = plt.subplots(figsize=(15, 10))
sns.barplot(x = 'Sales Rep',
        y = 'count',
        hue = 'Region',
        ci= None,
        data =df.groupby(['Sales Rep','Region','Sales_bin'], as_index = False)['Sales_bin'].value_counts())


# In[36]:


fig, ax = plt.subplots(figsize=(15, 10))
sns.barplot(x = 'Sales Rep',
        y = 'count',
        hue = 'Region',
        ci= None,
        data =df.groupby(['Sales Rep','Region','Sales_bin'], as_index = False)['Sales_bin'].value_counts())


# In[ ]:




