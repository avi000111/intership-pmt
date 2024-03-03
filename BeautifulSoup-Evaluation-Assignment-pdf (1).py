#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# # Answer 1

# In[2]:


from bs4 import BeautifulSoup
import requests

import pandas as pd
import numpy as np


# In[3]:


url = "https://www.imdb.com/list/ls056092300/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


# In[4]:


Movie_name = []
year = []
ratings = []


# In[5]:


movie_data = soup.find_all("div", class_="lister-item mode-detail")


# In[6]:


movie_data


# In[7]:


for store in movie_data:
    name = store.h3.a.text
    Movie_name.append(name)
    
    year_of_release = store.h3.find('span', class_="lister-item-year text-muted unbold").text.replace('(', '').replace(')', '')
    year.append(year_of_release)
    
    rate = store.find("span", class_="ipl-rating-star__rating").text.replace('\n','')
    ratings.append(rate)

    
        


    
        


# In[8]:


moive_df = pd.DataFrame({"Movie Name":Movie_name, "Year_of_release":year, "Movie Ratings":ratings})


# In[9]:


moive_df


# # Answer 2

# In[37]:


# importing the requests libraies 
from bs4 import BeautifulSoup
import requests


# In[38]:


url = "https://peachmode.com/search?q=bags&f_Product%20Type=Handbags"


# In[39]:


req = requests.get(url)


# In[40]:


content = BeautifulSoup(req.content, "html.parser")


# In[41]:


content


# In[54]:


name=soup.find('div',class_='product-title')
discount=soup.find('span', class_='discounted_price st-money money done')
price=soup.find('span', class_='price st-money money done')



# In[55]:


Name = []
Price = []
Discount = []


# In[56]:


Name = []

for i in soup.find_all('div',class_='product-title'):
    Name.append(i.text)
    
    
    
Name  
    

        



# In[57]:


Price = []

for i in soup.find_all('span',class_='price st-money money done'):
    Price.append(i.text)
    
    
    
Price  
    



# In[58]:


Discount = []

for i in soup.find_all('span',class_='discounted_price st-money money done'):
    Discount.append(i.text)
    
    
    
Discount  


# # Answer 3 (a)

# In[15]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[16]:


url = requests.get("https://www.icc-cricket.com/rankings/team-rankings/mens/odi")


# In[17]:


url


# In[18]:


soup = BeautifulSoup(url.content)
soup


# In[24]:


top_10_odi_team = soup.find('h3', class_="si-table-data si-team")
top_10_odi_team


# In[20]:


Matches = soup.find('span',class_="si-text" )
print(Matches)


# In[21]:


points = soup.find('div', class_="si-table-data si-pts")
points


# In[25]:


Ratings = soup.find('div', class_="si-table-data si-rating")
Ratings


# In[30]:


team = []

for i in soup.find_all('h3', class_="si-table-data si-team"):
    team.append(i.text)
    
    
    
team


# In[28]:


matches = []

for i in  soup.find_all('span',class_="si-text" ):

    matches.append(i.text)
    
    
    
matches


# In[29]:


ratings = []

for i in soup.find_all('div', class_="si-table-data si-rating"):

    ratings.append(i.text)
    
    
    
ratings


# In[26]:


points = []

for i in  soup.find_all('div', class_="si-table-data si-pts"):


    points.append(i.text)
    
    
    
points


# # Answer 3 (b)

# In[32]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[33]:


url = requests.get("https://www.icc-cricket.com/rankings/batting/mens/odi")


# In[34]:


url


# In[35]:


soup = BeautifulSoup(url.content)
soup


# In[38]:


top_10_batsman_team = soup.find('div', class_="si-table-data si-team")
top_10_batsman_team


# In[39]:


ratings = soup.find('div', class_="si-table-data si-rating")
ratings


# In[40]:


team = []

for i in  soup.find_all('div', class_="si-table-data si-team"):


    team.append(i.text)
    
    
    
team


# In[41]:


rating = []

for i in  soup.find_all('div', class_="si-table-data si-rating"):


    rating.append(i.text)
    
    
    
rating


# # Answer 3 (c)

# In[43]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[42]:


url = requests.get("https://www.icc-cricket.com/rankings/bowling/mens/odi")


# In[44]:


url


# In[45]:


soup = BeautifulSoup(url.content)
soup


# In[46]:


top_10_bowler_team = soup.find('div', class_="si-table-data si-team")
top_10_bowler_team


# In[47]:


ratings = soup.find('div', class_="si-table-data si-rating")
ratings


# In[48]:


team = []

for i in  soup.find_all('div', class_="si-table-data si-team"):


    team.append(i.text)
    
    
team


# In[49]:


rating = []

for i in  soup.find_all('div', class_="si-table-data si-rating"):


    rating.append(i.text)
    
    
rating


# # Answer 4

# In[50]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[51]:


page = requests.get("https://www.patreon.com/coreyms")


# In[52]:


page


# In[53]:


soup = BeautifulSoup(page.content)
soup


# In[61]:


heading = soup.find('span',{"data-tag":"post-title"})
heading


# In[12]:


content = soup.find('div', {"id":"cid-7"})
content


# In[10]:


date = soup.find('a',class_="sc-hGPBjI jHegYr") 
date


# In[11]:


video_like = soup.find('div', class_="sc-bdvvtL eHmEtx")
video_like


# In[13]:


heading = []

for i in  soup.find_all('span',{"data-tag":"post-title"}):


    heading.append(i.text)
    
    
heading


# In[15]:


content = []

for i in  soup.find_all('div', {"id":"cid-7"}):


    content.append(i.text)
    
    
content


# In[16]:


date = []

for i in  soup.find_all('a',class_="sc-hGPBjI jHegYr"):


    date.append(i.text)
    
    
date


# In[17]:


videolike = []

for i in  soup.find_all('div', class_="sc-bdvvtL eHmEtx"):


    videolike.append(i.text)
    
    
videolike


# # Answer 5

# In[103]:


import requests
from bs4 import BeautifulSoup

def scrape_house_details(locality):
    url = f"https://www.nobroker.in/property/sale/{locality}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    house_details = []
    for card in soup.find_all('div', class_='card'):
        title = card.find('h2', class_='card-title').text.strip()
        location = card.find('div', class_='card-title-line').text.strip()
        area = card.find('div', class_='card-size').text.strip()
        emi = card.find('div', class_='card-rent').text.strip()
        price = card.find('div', class_='card-price').text.strip()

        house_details.append({
            'Title': title,
            'Location': location,
            'Area': area,
            'EMI': emi,
            'Price': price
        })

    return house_details

if __name__ == "__main__":
    localities = ["indira-nagar", "jayanagar", "rajaji-nagar"]
    
    for locality in localities:
        print(f"Houses in {locality.replace('-', ' ').title()}:")
        houses = scrape_house_details(locality)
        for house in houses:
            print(house)
        print("\n")


# # Answer 6

# In[54]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[55]:


page = requests.get('https://www.bewakoof.com/top-wear-for-men')


# In[56]:


page


# In[57]:


soup = BeautifulSoup(page.content)
soup


# In[59]:


first_name = soup.find('div', class_="productNaming bkf-ellipsis")
first_name


# In[60]:


first_name.text


# In[64]:


price = soup.find('span', class_="sellingPrice mr-1")
price


# In[65]:


price.text


# In[68]:


imageurl = soup.find('img', class_="swiper-lazy swiper-lazy-loaded")


# In[69]:


imageurl


# In[71]:


name = []

for i in soup.find_all('div', class_="productNaming bkf-ellipsis"):

    name.append(i.text)
    
    
    
name  
    


# In[72]:


price = []

for i in soup.find_all('span', class_="sellingPrice mr-1"):


    price.append(i.text)
    
    
    
price  
    


# In[73]:


imageurl = []

for i in soup.find_all('img', class_="swiper-lazy swiper-lazy-loaded") :


    imageurl.append(i.text)
    
    
    
imageurl  
    


# # Answer 7

# In[11]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[12]:


page = requests.get('https://www.cnbc.com/world/?region=world')


# In[13]:


page


# In[14]:


soup = BeautifulSoup(page.content)
soup


# In[15]:


first_head = soup.find('a',class_="LatestNews-headline")
first_head


# In[16]:


first_head.text


# In[24]:


date = soup.find('time',class_="LatestNews-timestamp")
date


# In[25]:


date.text


# In[32]:


newslink = soup.find('a', {"href":"https://www.cnbc.com/2024/03/02/busy-er-doctors-say-these-8-sleep-tips-help-them-wake-up-refreshed-every-day.html"})


# In[33]:


newslink


# In[21]:


heading = []

for i in soup.find_all('a',class_='LatestNews-headline'):
    heading.append(i.text)
    
    
    
heading


# In[26]:


heading = []

for i in soup.find_all('a',class_='LatestNews-headline'):
    heading.append(i.text)
    
    
    
heading  
    



# In[34]:


newslink = []

for i in soup.find_all('a', {"href":"https://www.cnbc.com/2024/03/02/busy-er-doctors-say-these-8-sleep-tips-help-them-wake-up-refreshed-every-day.html"}):
    newslink.append(i.text)
    
    
    
newslink


# In[35]:


datetime = []

for i in soup.find_all('time',class_="LatestNews-timestamp"):
    datetime.append(i.text)
    
    
    
datetime  
    


# # Answer 8

# In[39]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[40]:


page = requests.get('https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/')


# In[41]:


page


# In[42]:


soup = BeautifulSoup(page.content)
soup


# In[43]:


paper_title_first = soup.find('h2',class_="h5 article-title")
paper_title_first


# In[44]:


paper_title_first.text


# In[45]:


date = soup.find('p', class_="article-date")
date


# In[46]:


date.text


# In[47]:


Author = soup.find('p', class_="article-authors")
Author


# In[48]:


Author.text


# In[49]:


papertitle = []

for i in soup.find_all('h2',class_="h5 article-title"):
    papertitle.append(i.text)
    
    
    
papertitle  


# In[51]:


date = []

for i in soup.find_all('p', class_="article-date"):
    date.append(i.text)
    
    
    
date  


# In[52]:


Author = []

for i in soup.find_all('p', class_="article-authors"):
    Author.append(i.text)
    
    
    
Author  


# In[ ]:




