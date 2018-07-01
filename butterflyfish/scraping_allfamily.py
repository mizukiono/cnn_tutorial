
# coding: utf-8

# In[1]:


import urllib
from bs4 import BeautifulSoup
import pandas as pd
import re
import math
import numpy as np
import time


# In[2]:


startnum = 1


# In[3]:


# アクセスURL
url = 'http://fishpix.kahaku.go.jp/fishimage/search?START=%d&JPN_FAMILY=&FAMILY=&JPN_NAME=&SPECIES=&LOCALITY=&FISH_Y=&FISH_M=&FISH_D=&PERSON=&PHOTO_ID=&JPN_FAMILY_OPT=0&FAMILY_OPT=0&JPN_NAME_OPT=0&SPECIES_OPT=0&LOCALITY_OPT=1&PERSON_OPT=1&PHOTO_ID_OPT=1'%startnum


# In[4]:


def url_generate(url):
#     if startnum == 1:
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")
    text = soup.find('span', class_= 'captionTimes').text
    num = text.split("件")[0].split()[0]
    print('%s images were found'%num)
    page = math.ceil(int(num)/20.)
    page_nums = list(np.arange(1, page*20, 20))
    return page_nums


# In[5]:


page_nums = url_generate(url)
print(page_nums)


# In[6]:


def information_getter(url):
    '''
    urlを渡すと情報を返す
    '''
    
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")
    
    result = soup.findAll('span', class_= 'result')
    names = []
    for x in result:
        names.append(x.text)
    result_ = soup.findAll('span', class_= 'resultHelvetica')
    namesHel = []
    for x in result_:
        namesHel.append(x.text)
    
    caption = soup.findAll('span', class_= 'captionTimes')
    caps = []
    for x in caption:
        cap = x.find('a',href=re.compile('^detail'))
        if cap != None:
            caps.append(cap.text)
    
    imgsoup = soup.findAll("img")
    img_path = []
    for x in imgsoup:
        if x['height'] == "130":
            img_path.append(x['src'])

    return names, namesHel, caps, img_path


# In[7]:


def dataframe_maker(page_nums):
    df = pd.DataFrame(columns = ['name', 'nameEng', 'caption', 'URL'])
    
    for n in page_nums:
        url = 'http://fishpix.kahaku.go.jp/fishimage/search?START=%d&JPN_FAMILY=&FAMILY=&JPN_NAME=&SPECIES=&LOCALITY=&FISH_Y=&FISH_M=&FISH_D=&PERSON=&PHOTO_ID=&JPN_FAMILY_OPT=0&FAMILY_OPT=0&JPN_NAME_OPT=0&SPECIES_OPT=0&LOCALITY_OPT=1&PERSON_OPT=1&PHOTO_ID_OPT=1'%n
        names, namesHel, caps, img_url = information_getter(url)
        df_batch = pd.DataFrame([names, namesHel, caps, img_url],                                index=['name', 'nameEng', 'caption', 'URL']).transpose()
#         display(df_batch.head())
        df = pd.concat([df, df_batch])
#         display(df.tail())
        print(n)
#         display(names)
#         display(caps)
        time.sleep(2.01)
    return df


# In[8]:


df = dataframe_maker(page_nums)


# In[9]:


df.count()


# In[ ]:


df['name'].value_counts()


# In[ ]:


df.to_csv("butterfly.csv")

