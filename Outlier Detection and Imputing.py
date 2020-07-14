#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Required Python Machine learning Packages
import pandas as pd
import numpy as np


# In[2]:

adult_df=pd.read_csv(r'C:\Users\hp\Desktop\imarticus\python\datasets\adult_data.csv',header=None,delimiter=' *, *',engine='python')

adult_df.head()


# In[3]:


adult_df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
                    'marital_status', 'occupation', 'relationship',
                    'race', 'sex', 'capital_gain', 'capital_loss',
                    'hours_per_week', 'native_country', 'income']

adult_df.head()


# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
adult_df.boxplot() #for plotting boxplots for all the numerical columns in the df
plt.show()


# In[5]:
#when you see cluster of points as a outlier do not impute them
#do not use outlier on categorical data
#logically relevent values should never be consideredx as outliers
#monintory value variablees should never be imputed
#%%
adult_df.boxplot(column='fnlwgt')
plt.show()


# In[6]:


adult_df.boxplot(column='capital_gain')
plt.show()


# In[7]:


adult_df.boxplot(column='capital_loss')
plt.show()


# In[8]:


adult_df.boxplot(column='hours_per_week')
plt.show()


# In[9]:


adult_df.boxplot(column='age') 
plt.show()


# In[10]:

#detecting coutlie
#for value in colname:
q1 = adult_df['age'].quantile(0.25) #first quartile value
q3 = adult_df['age'].quantile(0.75) # third quartile value
iqr = q3-q1 #Interquartile range
low  = q1-1.5*iqr #acceptable range
high = q3+1.5*iqr #acceptable range


# In[11]:


adult_df_include = adult_df.loc[(adult_df['age'] >= low) & \
                                (adult_df['age'] <= high)] # meeting the acceptable range
adult_df_exclude = adult_df.loc[(adult_df['age'] < low) |                                
                                (adult_df['age'] > high)] #not meeting the acceptable range


# In[12]:


print(adult_df_include.shape)


# In[13]:


print(adult_df_exclude.shape)

#%% treating outlier
#1]capping approch
#measure id central tendency=
# In[14]:


print(low)


# In[15]:


age_mean=int(adult_df_include.age.mean()) #finding the mean of the acceptable range
print(age_mean)


# In[16]:


#imputing outlier values with mean value
adult_df_exclude.age=age_mean


# In[17]:


#getting back the original shape of df
adult_df_rev=pd.concat([adult_df_include,adult_df_exclude]) #concatenating both dfs to get the original shape
adult_df_rev.shape


# In[ ]:


#capping approach

adult_df_exclude.loc[adult_df_exclude["age"] <low, "age"] = low
adult_df_exclude.loc[adult_df_exclude["age"] >high, "age"] = high


# In[ ]: generic codde  to check outliers
import matplotlib.pyplot as plt
colname=[]
for x in adult_df.columns[:-1]:
    if adult_df[x].dtype=="int64" or adult_df[x].dtype=="float64":
        colname.append(x)

for x in colname:
    adult_df.boxplot(column=x)
    plt.show()




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




