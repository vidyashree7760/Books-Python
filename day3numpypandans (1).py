#!/usr/bin/env python
# coding: utf-8

# numpy:package for multidimentional array

# In[1]:


import numpy as np


# In[3]:


simple_list=[1,2,3]
np.array(simple_list)


# In[7]:


list_of_lists=[[1,2,3],[4,5,6],[7,8,9]]
np.array(list_of_lists)


# In[8]:


np.arange(5,10)


# In[10]:


np.arange(1,100)


# In[11]:


np.arange(1,31,5) #shift+tab->help box


# In[12]:


np.arange(5)


# In[13]:


np.zeros(10)


# In[14]:


np.zeros(10,int)


# In[15]:


np.ones((2,3))


# In[16]:


np.ones(100)


# In[17]:


np.ones(10,int)


# In[18]:


np.zeros((2,5),int)


# In[19]:


np.linspace(0,2,5)


# In[20]:


np.linspace(0,20,8)


# In[21]:


np.eye((10))


# In[23]:


np.random.rand(10,5)


# In[26]:


arr=np.random.randint(2,100)
arr


# In[27]:


np.random.randint(20,56,100)


# In[28]:


sample_array=np.arange(30)
sample_array


# In[29]:


rand_array=np.random.randint(0,100,20)
rand_array


# In[30]:


sample_array.reshape(5,6)


# In[36]:


sample_array.reshape(3,6)


# In[37]:


rand_array.max()


# In[38]:


rand_array.argmax()


# In[40]:


a=np.eye(5)


# In[41]:


a.T


# In[42]:


a=np.random.rand(2,3)
a


# In[45]:


sample_array=np.arange(10,21)
sample_array


# In[46]:


sample_array[0]


# In[47]:


sample_array[2:5]


# In[49]:


sample_array[1:4]=100
sample_array


# In[51]:


sample_array=np.arange(10,21)
sample_array


# In[52]:


sample_array[0:7]


# In[53]:


subset_sample_array=sample_array[0:7]
subset_sample_array


# In[54]:


subset_sample_array[:]=1001
subset_sample_array


# two-dimentional array

# In[3]:


import numpy as np


# In[4]:


sample_matrix=np.array([[50,20,1,23],[24,23,21,33],[55,76,24,7]])
sample_matrix


# In[5]:


sample_matrix[1,2]


# In[6]:


sample_matrix[2,:]


# In[7]:


sample_matrix[2]


# In[8]:


sample_matrix[:,(3,2)]


# In[ ]:




