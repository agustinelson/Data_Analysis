#!/usr/bin/env python
# coding: utf-8

# ### Excercise 1, 2
# 

# In[1]:


import numpy as np


# In[2]:


array = np.arange(1,65).reshape((8,8))
print(array)


# In[3]:


arraytranspose = array.transpose()
print(arraytranspose)


# In[4]:


arraytranspose[( (arraytranspose-3)%10 == 0 ) + (arraytranspose < 40) * (arraytranspose > 29)] = -99
print(arraytranspose)


# ### Exercise 3

# In[5]:


array3 = np.arange(0.4, 0.80, 0.01).reshape((8,5))
print(array3)


# In[9]:


arraytot = np.append(arraytranspose, array3, axis = 1)
print(arraytot)


# In[48]:


arrayaverage = []
for i in arraytot.transpose():
    arrayaverage.append(i.sum()/len(i))
print(arrayaverage)


# In[46]:


data = np.concatenate([arraytot, [arrayaverage]],axis = 0)
print(data)


# In[49]:


arraymax = []
for i in data:
    arraymax.append(i.max())
print(arraymax)


# In[50]:


data2 = np.append(data, np.array([arraymax]).transpose(), axis = 1)
print(data2)


# In[51]:


np.savetxt('exercise3.tsv', data2, delimiter='\t', fmt='%.3f')

