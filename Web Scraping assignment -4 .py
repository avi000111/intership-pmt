#!/usr/bin/env python
# coding: utf-8

# # Answer 1

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


# import liabraries
import selenium
import pandas as pd
import time 
import warnings
warnings.filterwarnings('ignore')

# import selenium webdriver
from selenium import webdriver

# import required Exception which needs to handled
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

# import requests
import requests

from selenium.webdriver.common.by import By


# In[3]:


# connecting to webdriver
driver=webdriver.Chrome()
time.sleep(1)

# Opening Wikipedia webpage
url='https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos'
driver.get(url)
time.sleep(2)


# In[4]:


# Empty list for scraping data
Rank =[]
Name =[]
Artist =[]
Upload_date=[]
Views=[]


# In[5]:


# Extracting Rank Via X path
try:
    rank=driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"][1]/tbody/tr/td[1]')
    for i in rank:
        Rank.append(i.text)
except NoSuchElementException:
    Rank.append('NA')
except StaleElementReferenceException:
    Rank.append('NA')
    
# Extracting Name Via X path
try:
    name=driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"][1]/tbody/tr/td[2]')
    for i in name:
        Name.append(i.text)
except NoSuchElementExceptionhElementException:
    Name.append('NA')
except StaleElementReferenceException:
    Name.append('NA')
    
# Extracting Artist Name Via Xpath
try:
    artist=driver.find_elements(By.XPATH,"//table[@class='sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter'][1]/tbody/tr/td[3]")
    for i in artist:
        Artist.append(i.text)
except NoSuchElementExceptionhElementException:
    Artist.append('NA')
except StaleElementReferenceException:
    Artist.append('NA')

# Extracting Upload date Via Xpath
try:
    upload_date=driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"][1]/tbody/tr/td[5]')
    for i in upload_date:
        Upload_date.append(i.text)
except NoSuchElementExceptionhElementException:
    Upload_date.append('NA')
except StaleElementReferenceException:
    Upload_date.append('NA') 

# Extracting Views via Xpath
try:
    views=driver.find_elements(By.XPATH,"//table[@class='sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter'][1]/tbody/tr/td[4]")
    for i in views:
        Views.append(i.text)
except NoSuchElementExceptionhElementException:
    Views.append('NA')
except StaleElementReferenceException:
    Views.append('NA')
    


# In[6]:


# Dataframe for scrap data
Wiki_YT=pd.DataFrame({'Rank':Rank,'Video Name':Name,'Uploader':Artist,'Views (in Billons)':Views,'Upload Date':Upload_date})
print('\033[1m'+'Most Viewed Video on YouTube from Wikipedia :'+'\033[0m')
Wiki_YT


# # Answer 2

# In[3]:


# import liabraries
import selenium
import pandas as pd
import time 
import warnings
warnings.filterwarnings('ignore')

# import selenium webdriver
from selenium import webdriver

# import required Exception which needs to handled
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

# import requests
import requests

from selenium.webdriver.common.by import By


# In[22]:


# connecting to webdriver
driver=webdriver.Chrome()
time.sleep(1)

# Opening Wikipedia webpage
url="https://www.bcci.tv/"

driver.get(url)
time.sleep(1)


# In[23]:


# Opening fixtures webpage through browser
fixtures=driver.find_element(By.XPATH,"//div[@class='w-100 tab-pane fade  show active ']/ul/div/a[2]")
try:
    fixtures.click()
except ElementNotInteractableException:
    driver.get(fixtures.get_attribute('href'))


# In[26]:


# Scraping URL 
URL= []
link=driver.find_elements(By.XPATH,'//div[@class="match-card match-card-fw match-card-up ng-scope"]')
for i in link:
    URL.append(i.get_attribute('href'))


# In[27]:


# Creating empty list
Title = []

Place = []
Date = []
Time = []


# In[28]:


from tqdm import tqdm
for i in tqdm(URL):
    driver.get(i)
    
    # Scraping Match title
    try:
        title=driver.find_element(By.XPATH,"//span[@class='matchOrderText ng-binding ng-scope t20-tag']")
        Title.append(title.text)
    except NoSuchElementException:
        Title.append('NA')
        
    
        
    # Scraping venue Via Xpath
    try:
        place=driver.find_element(By.XPATH,"//span[@class='ng-binding ng-scope']")
        Place.append(place.text)
    except NoSuchElementException:
        Place.append('NA')
        
    # Scraping date Via Xpath
    try:
        date=driver.find_element(By.XPATH,'//div[@class="match-dates ng-binding"]')
        Date.append(date.text)
    except NoSuchElementException:
        Date.append('NA')
        
    # Scraping Time Via Xpath
    try:
        time=driver.find_element(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
        Time.append(time.text)
    except NoSuchElementException:
        Time.append('NA')
        


# In[29]:


# Dataframe for scrap data
Cricket=pd.DataFrame({'Match Title':Title,'Tournament':Series,'Venue':Place,'Date':Date,'Time':Time})
print('\033[1m'+'Team India’s Upcoming International fixtures :'+'\033[0m')
Cricket


# # Answer 5

# In[39]:


# import liabraries
import selenium
import pandas as pd
import time 
import warnings
warnings.filterwarnings('ignore')

# import selenium webdriver
from selenium import webdriver

# import required Exception which needs to handled
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

# import requests
import requests

from selenium.webdriver.common.by import By


# In[40]:


# connecting to webdriver
driver=webdriver.Chrome()
time.sleep(1)

# Opening Wikipedia webpage
url='https://www.billboard.com/'
driver.get(url)
time.sleep(1)


# In[41]:


# Creating Empty List
Song =[]
Artist =[]
Last_Week_rank=[]
Peak_rank =[]
Weeks =[]


# In[42]:


# Clicking on hot 100 option
hot_100=driver.find_element(By.XPATH,'//ul[@class="o-nav__list lrv-a-unstyle-list lrv-u-flex lrv-u-justify-content-center lrv-a-space-children-horizontal a-space-children--60@custom lrv-u-justify-content-space-evenly@desktop lrv-u-font-size-15 u-letter-spacing-0043 a-font-primary-medium-s u-display-none@mobile-max"]/li[1]/a')
try:
    hot_100.click()
except ElementNotInteractableException:
    driver.get(hot_100.get_attribute('href'))
time.sleep(2)


# In[43]:


# Scraping Song Name
try:
    song=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li/h3')
    for i in song:
        Song.append(i.text)
except NoSuchElementException:
    Song.append('NA')
    

    
# Scraping Song last week rank
try:
    last_rank=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li[4]')
    for i in last_rank:
        Last_Week_rank.append(i.text)
except NoSuchElementException:
    Last_Week_rank.append('NA')

# Scraping Song peak rank
try:
    peak=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li[5]')
    for i in peak:
        Peak_rank.append(i.text)
except NoSuchElementException:
    Peak_rank.append('NA')

# Scraping Song Artist Name
try:
    weeks=driver.find_elements(By.XPATH,'//span[@class="c-label  a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"]')
    for i in weeks:
        Weeks.append(i.text)
except NoSuchElementException:
    Weeks.append('NA')


# In[44]:


Billboard=pd.DataFrame({'Song_Name':Song,
                
                'Last_week_rank':Last_Week_rank,
                'Peak':Peak_rank,
                'Weeks_on_chart':Weeks})
print('\033[1m'+'Billboard Hot 100 Songs :'+'\033[0m')
Billboard


# # Answer 6

# In[43]:


# import liabraries
import selenium
import pandas as pd
import time 
import warnings
warnings.filterwarnings('ignore')

# import selenium webdriver
from selenium import webdriver

# import required Exception which needs to handled
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

# import requests
import requests

from selenium.webdriver.common.by import By


# In[44]:


# connecting to webdriver
driver=webdriver.Chrome()
time.sleep(1)

# Opening Wikipedia webpage
url='https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare'
driver.get(url)
time.sleep(1)


# In[45]:


# Creating Empty Lists
Book =[]
Author =[]
Volumes_sold =[]
Publisher =[]
Genre =[]


# In[46]:


# Scraping Book name
try:
    book=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[2]')
    for i in book:
        Book.append(i.text)
except NoSuchElementException:
    Book.append('NA')
    
# Scraping Book author's via Xpath
try:
    author=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[3]')
    for i in author:
        Author.append(i.text)
except NoSuchElementException:
    Author.append('NA')
    
# Scraping Volumes sold via Xpath
try:
    sold=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[4]')
    for i in sold:
        Volumes_sold.append(i.text)
except NoSuchElementException:
    Volumes_sold.append('NA')
    
# Scraping publisher via xPath
try:
    publisher=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[5]')
    for i in publisher:
        Publisher.append(i.text)
except NoSuchElementException:
    Publisher.append('NA')
    
# Scraping Genre via Xpath
try:
    genre=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[6]')
    for i in genre:
        Genre.append(i.text)
except NoSuchElementException:
    Genre.append('NA')


# In[47]:


#creating dataframe
Top_Books=pd.DataFrame({"Book Title":Book,
                "Author Name":Author,
                'Volumes sold':Volumes_sold,
                'Publisher':Publisher,
                'Genre':Genre})
print('\033[1m'+'Best Selling Books of All Time List by The Guardian  :'+'\033[0m')
Top_Books


# # Answer 8

# In[21]:


# import liabraries
import selenium
import pandas as pd
import time 
import warnings
warnings.filterwarnings('ignore')

# import selenium webdriver
from selenium import webdriver

# import required Exception which needs to handled
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

# import requests
import requests

from selenium.webdriver.common.by import By


# In[22]:


# connecting to webdriver
driver=webdriver.Chrome()
time.sleep(1)

# Opening Wikipedia webpage
url='https://archive.ics.uci.edu/'
driver.get(url)
time.sleep(1)


# In[23]:


# Clicking on all datasets links
dataset=driver.find_element(By.XPATH,"//ul[@class='menu menu-horizontal']/li/a")
dataset.click()
time.sleep(2)



# In[24]:


# Creating empty lists
Dataset =[]
Data_Type =[]
Task =[]

No_of_Instances =[]
No_of_Attribute =[]



# In[25]:


# Scraping DataSet Name via Xpath
from tqdm import tqdm
try:
    dataset=driver.find_elements(By.XPATH,"//h2[@class='truncate text-primary']")
    for i in tqdm(dataset):
        Dataset.append(i.text)
        time.sleep(0.15)
except NoSuchElementException:
    Dataset.append('NA')
    
# Scraping Data Type via Xpath
try:
    Type=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[2]/span')
    for i in Type[1:]:
        Data_Type.append(i.text)
except NoSuchElementException:
    Data_Type.append('NA')
    
# Scraping Task via Xpath
try:
    task=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[1]/span')
    for i in task[1:]:
        Task.append(i.text)
except NoSuchElementException:
    Task.append('NA')
    
    
# Scraping No_of_Instances via Xpath
try:
    no_of_Instances=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[3]/span')
    for i in no_of_Instances[1:]:
        No_of_Instances.append(i.text)
except NoSuchElementException:
    No_of_Instances.append('NA')

# Scraping No_of_Attribute via Xpath
try:
    no_of_Attribute=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[4]/span')
    for i in no_of_Attribute[1:]:
        No_of_Attribute.append(i.text)
except NoSuchElementException:
    No_of_Attribute.append('NA')
    


# In[26]:


# Creating Data Frame for UCI Dataset
UCI_Dataset=pd.DataFrame({'DataSet Title':Dataset,
                'Data Type':Data_Type,
                'Task':Task,
                
                'No of Instances':No_of_Instances,
                'No of Attribute':No_of_Attribute,
                })
print('\033[1m'+' UCI Machine Learning Dataset:'+'\033[0m')
UCI_Dataset


# In[ ]:




