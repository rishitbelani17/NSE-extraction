#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
url = 'https://archives.nseindia.com/content/equities/EQUITY_L.csv'
data = pd.read_csv(url, sep = ",")


# In[2]:


data.head()


# In[4]:


import requests
print('Downloading started')
url = 'https://archives.nseindia.com/content/historical/EQUITIES/2022/OCT/cm11OCT2022bhav.csv.zip'
req = requests.get(url)
 
filename = url.split('/')[-1]
 
with open(filename,'wb') as output_file:
    output_file.write(req.content)
print('Downloading Completed')


# In[9]:


bhav = pd.read_csv(filename)


# In[11]:


bhav.head()


# In[12]:


bhav = bhav.drop('Unnamed: 13', axis = 1)


# In[13]:


bhav.head()


# In[18]:


bhav.isnull().sum()


# In[19]:


bhav['gains'] = (bhav['CLOSE'] - bhav['OPEN'])/bhav['OPEN']


# In[20]:


bhav.head()


# In[22]:


bhav.sort_values("gains", ascending=False)


# In[23]:


data.to_csv('1st.csv')


# In[24]:


bhav.to_csv('bhavcopy.csv')


# In[ ]:




