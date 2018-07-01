
# coding: utf-8

# In[24]:


import urllib
from bs4 import BeautifulSoup
import pandas as pd
import re
import math


# In[23]:


startnum = 1


# In[17]:


# アクセスURL
url = 'http://fishpix.kahaku.go.jp/fishimage/search?START=%d&JPN_FAMILY=&FAMILY=Chaetodontidae&JPN_NAME=&SPECIES=&LOCALITY=&FISH_Y=&FISH_M=&FISH_D=&PERSON=&PHOTO_ID=&JPN_FAMILY_OPT=1&FAMILY_OPT=0&JPN_NAME_OPT=1&SPECIES_OPT=1&LOCALITY_OPT=1&PERSON_OPT=1&PHOTO_ID_OPT=1'%startnum


# In[ ]:


# def url_generate(url):
#     if startnum == 1:
#         url = url
#         response = urllib.request.urlopen(url)
#         soup = BeautifulSoup(response, "html.parser")
#         text = soup.find('span', class_= 'captionTimes').text
#         num = text.split("件")[0].split()[0]
#         print(num)
#         print()


# In[18]:


df = pd.DataFrame(columns = ['name', 'nameEng', 'caption', 'URL'])


# In[19]:


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
        img_path.append(x['src'])
    img_path = img_path[1:]
    img_url = img_path[:-1]

    return names, namesHel, caps, img_url


# In[20]:


names, namesHel, caps, img_url = information_getter(url)
df_batch = pd.DataFrame([names, namesHel, caps, img_url], index=['name', 'nameEng', 'caption', 'URL']).transpose()


# In[21]:


df_batch


# In[22]:


df = pd.concat([df, df_batch])
df


# In[3]:


response = urllib.request.urlopen(url)


# In[4]:


soup = BeautifulSoup(response, "html.parser")


# In[5]:


result = soup.findAll('span', class_= 'result')
names = []
for x in result:
    names.append(x.text)
print(names)


# In[87]:


result_ = soup.findAll('span', class_= 'resultHelvetica')
namesHel = []
for x in result_:
    namesHel.append(x.text)
print(namesHel)


# In[10]:


soup.findAll('span', class_= 'captionTimes')


# In[70]:


caption = soup.findAll('span', class_= 'captionTimes')
display(caption)
caps = []
for x in caption:
    cap = x.find('a',href=re.compile('^detail'))
    if cap != None:
        caps.append(cap.text)
print(caps)


# In[98]:


text = soup.find('span', class_= 'captionTimes').text
num = text.split("件")[0].split()[0]
print(num)


# In[61]:


imgsoup = soup.findAll("img")
display(imgsoup)


# In[85]:


img_path = []

for x in imgsoup:
    img_path.append(x['src'])


# In[86]:


img_path = img_path[1:]
img_path = img_path[:-1]
print(len(img_path))
print(img_path)

