
# coding: utf-8

# In[69]:


import os
import glob
import pandas as pd
import urllib
import time


# In[9]:


df = pd.read_csv("butterfly.csv",index_col=0)


# In[12]:


df['name'].value_counts()


# In[66]:


url_base = "http://fishpix.kahaku.go.jp"

target = "ブラック・バタフライフィッシュ"
target_ind = list(df.query('name == @target')['URL'].values)
len(target_ind)

save_directory = "../data/originaldata/%s"%target
os.makedirs(save_directory, exist_ok=True)


# In[67]:


df.query('name == @target')


# In[70]:


for tar in target_ind:
    tar = tar[2:]
    url = urllib.parse.urljoin(url_base, tar)
    
    path = urllib.parse.urlsplit(url)[2]
    savename = os.path.basename(path)
    
    savepath = os.path.join(save_directory, savename)
    urllib.request.urlretrieve(url, savepath)
    time.sleep(2)

