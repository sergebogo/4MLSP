#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd

df_maths = pd.read_csv('C:\\Users\\juraykouka\\Documents\\DOSSIER COURS SUPINFO\\4MLSP\\Examen\\student-mat.csv', sep=';')


# In[3]:


df_maths


# In[7]:


import matplotlib.pyplot as plt

df_maths_pie_g3 = df_maths["G3"].value_counts()/len(df_maths)*100 


# In[24]:


plt.pie(df_maths_pie_g3, autopct='%1.1f%%' )
df_maths_pie_g3


# In[26]:


import pandas as pd

df_port = pd.read_csv('C:\\Users\\juraykouka\\Documents\\DOSSIER COURS SUPINFO\\4MLSP\\Examen\\student-por.csv', sep=';')
df_port


# In[27]:


import matplotlib.pyplot as plt

df_port_pie_g3 = df_port["G3"].value_counts()/len(df_port)*100 
plt.pie(df_port_pie_g3, autopct='%1.1f%%' )
df_port_pie_g3


# In[28]:


import seaborn as sns

corrMatrix = df_maths.corr()
_ = sns.heatmap(corrMatrix)


# In[29]:


import seaborn as sns

corrMatrix = df_port.corr()
_ = sns.heatmap(corrMatrix)


# In[ ]:




