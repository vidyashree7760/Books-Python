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

# In[2]:


import numpy as np


# In[3]:


sample_matrix=np.array([[50,20,1,23],[24,23,21,33],[55,76,24,7]])
sample_matrix


# In[4]:


sample_matrix[1,2]


# In[5]:


sample_matrix[2,:]


# In[6]:


sample_matrix[2]


# In[7]:


sample_matrix[:,(3,2)]


# ### selection techniques

# In[8]:


sample_array=np.arange(1,20)


# In[9]:


sample_array


# In[10]:


sample_array+sample_array


# In[11]:


np.exp(sample_array) # exponential


# In[12]:


np.sqrt(sample_array)


# In[14]:


np.log(sample_array)


# In[15]:


np.max(sample_array)


# In[16]:


np.min(sample_array)


# In[17]:


np.argmax(sample_array)


# In[18]:


np.argmin(sample_array)


# In[19]:


np.square(sample_array)


# In[20]:


np.std(sample_array)


# In[21]:


np.var(sample_array)


# In[24]:


np.mean(sample_array)


# In[25]:


array=np.random.rand(3,4)
array


# In[27]:


np.round(array,decimals=2)


# In[28]:


sports=np.array(['golf','cricket','fball','cricket'])
np.unique(sports)


# ### PANDAS

# In[29]:


import pandas as pd
import numpy as np


# #### Pandas dataframe and indexing

# In[30]:


sports1=pd.Series([1,2,3,4],index=['cricket','football','basketball','golf'])
sports1


# In[34]:


sports2=pd.Series([11,2,3,4],index=['cricket','football','baseball','golf'])
sports2


# In[35]:


sports1+sports2


# In[37]:


import pandas as pd
import numpy as np


# In[45]:


df1 = pd.DataFrame(np.random.rand(8, 5), index='A B C D E F G H'.split(), columns='Score1 Score2 Score3 Score4 Score5'.split())
df1


# In[48]:


df1["Score1"]


# In[49]:


df1[["Score1","Score2","Score3"]]


# In[52]:


df1['Score6']=df1['Score1']+df1['Score2']
df1


# In[57]:


df2={'ID':['101','102','103','107','176'],'Name':['John','Mercy','Akash','Kavin','Lally'],'Profit':[20,54,56,37,123]}
df=pd.DataFrame(df2)
df


# In[58]:


df["ID"]


# In[59]:


df[["ID","Name","Profit"]]


# In[60]:


df=df.drop("ID",axis=1)


# In[61]:


df


# In[62]:


df.drop(3)


# In[ ]:




