#!/usr/bin/env python
# coding: utf-8

# # Answer 1

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# # Import Requests Libraies
# 

# In[2]:


from bs4 import BeautifulSoup
import requests

import pandas as pd


# In[3]:


page = requests.get("https://en.wikipedia.org/wiki/Main_Page")


# In[4]:


page


# In[5]:


soup = BeautifulSoup(page.content)
soup


# In[6]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[7]:


scraped_header = soup.find_all('div', class_="vector-header-container")
scraped_header


# In[8]:


header = []
for head in scraped_header:
    head = head.get_text().replace('\n', "")
    head = head.strip(" ")
    header.append(head)
header


# # Answer 2

# In[9]:


from bs4 import BeautifulSoup
import requests

import pandas as pd
 


# In[10]:


page = requests.get("https://www.imdb.com/list/ls565461384/")


# In[11]:


page


# In[12]:


soup = BeautifulSoup(page.content)
soup


# In[13]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[14]:


# Scrape movie names
scraped_movies = soup.find_all('div', class_="lister-item mode-detail")
scraped_movies


# In[15]:


# parse movie name
movies = []
for movie in scraped_movies:
    movie = movie.get_text().replace('\n', "")
    movie = movie.strip(" ")
    movies.append(movie)
movies


# In[16]:


# scrap rating for movies
scarped_ratings = soup.find_all('div',class_="ipl-rating-widget")


scarped_ratings


# In[17]:


# parse ratings
ratings = []
for rating in scarped_ratings:
    rating = rating.get_text().replace('\n', "")
    ratings.append(rating)
ratings


# In[18]:


# scrap rating for movies
scarped_years_of_release = soup.find_all('span',class_="lister-item-year text-muted unbold")


scarped_years_of_release


# In[19]:


years = []
for year in scarped_years_of_release:
    year = year.get_text().replace('(','')
    years.append(year)
years


# # Store the Scraped data

# In[20]:


data = pd.DataFrame()
data["Movies Names"] = movies
data["Ratings"] = ratings
data["Year_of_Release"] = years


# In[21]:


data.head()


# # Answer 3

# In[22]:


# importing the requests libraies 
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[23]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[24]:


page


# In[25]:


soup = BeautifulSoup(page.content)
soup


# # Scrape restaurant name

# In[26]:


restaurant_name = soup.find_all('div', class_="restnt-info cursor")
restaurant_name


# In[27]:


names = []
for name in restaurant_name:
    name = name.get_text().replace('\n', "")
    name = name.strip(" ")
    names.append(name)
names


# # Scrape restaurant cuisine

# In[28]:


restaurant_cuisine = soup.find_all('span',class_='double-line-ellipsis')
restaurant_cuisine


# In[29]:


cuisine = []

for i in soup.find_all('span',class_='double-line-ellipsis'):
    cuisine.append(i.text.replace('₹ ',''))
    
    
cuisine


# # scrape restaurant location

# In[30]:


restaurant_location = soup.find_all('div',class_='restnt-loc')
restaurant_location 


# In[31]:


location = []

for i in soup.find_all('div',class_='restnt-loc ellipsis'):
    location.append(i.text)
    
    
    
location  
    



# # scrape ratings

# In[32]:


ratings

for i in soup.find_all('div',class_='restnt-rating'):
    ratings.append(i.text)
    
    
    
ratings 
   


# # scrape images

# In[33]:


images = []

for i in soup.find_all("img",class_='no-img'):
    images.append(i['data-src'])
images


# # Answer 4

# In[34]:


# importing the requests libraies 
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[43]:


page = requests.get("https://presidentofindia.nic.in/former-presidents")


# In[44]:


page


# In[45]:


soup = BeautifulSoup(page.content)
soup


# In[46]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[48]:


scraped_name = soup.find_all('body',class_="layout-no-sidebars path-former-presidents")
scraped_name


# In[50]:


names = []
for name in scraped_name:
    name = name.get_text().replace('\n', "")
    name = name.strip(" ")
    names.append(name)
names


# In[51]:


data = pd.DataFrame()
data["President Names"] = names


# In[52]:


data.head()


# In[ ]:




