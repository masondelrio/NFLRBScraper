#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests, six #allows us to get html info
import lxml.html as lh #convert all html info into readable python text
import pandas as pd #storing data on dataframe
from itertools import cycle, islice
from matplotlib import colors #analysis and plotting
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
url = 'https://www.cbssports.com/fantasy/football/stats/RB/2020/tp/projections/ppr/'

page = requests.get(url)

doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//tr')

[len(T) for T in tr_elements[:12]]


# In[2]:


print(tr_elements[1:12])


# In[3]:


tr_elements = tr_elements[1:]


# In[4]:


[len(T) for T in tr_elements[:12]]


# In[5]:


col = []
i = 0

for t in tr_elements[0]:
    i+=1
    name = t.text_content()
    newname =" ".join(name.split())
    print('%d:"%s"'%(i,newname))
    col.append((newname,[]))


# In[6]:


for j in range(1,len(tr_elements)):
    T = tr_elements[j]
    
    if len(T)!=15:
        break
    
    i = 0
    for t in T.iterchildren():
        data = t.text_content()
        newdata =" ".join(data.split())
        if i>0:
            try:
                newdata=float(newdata)
                newdata =" ".join(data.split())
            except:
                pass
            
        col[i][1].append(newdata)
        i+=1

    


# In[7]:


[len(C) for (title,C) in col]


# In[8]:


Dict = {title:column for (title,column) in col}
import pandas as pd
df = pd.DataFrame(Dict)


# In[9]:


df.head()


# In[ ]:




