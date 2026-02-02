#!/usr/bin/env python
# coding: utf-8

# # Scraping Data from a Website + Pandas

# In[39]:


from bs4 import BeautifulSoup
import requests


# In[40]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

headers = {'User-Agent': 'MyPythonScript/123 (Spencer.roper101@gmail.com)'}

page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.text, 'html')

print(page)


# In[41]:


print(soup)


# In[42]:


table = soup.find_all('table')[0]


# In[43]:


print(table)


# In[44]:


soup.find_all('th')


# In[45]:


world_titles = table.find_all('th')


# In[46]:


world_titles


# In[47]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[48]:


import pandas as pd


# In[49]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[56]:


column_data = table.find_all('tr')


# In[85]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data


# In[86]:


df


# In[87]:


df.to_csv(r'C:\Users\spenc\OneDrive\Documents\Data Analysis\Python\Web Scraping Project Path\Companies.csv', index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




