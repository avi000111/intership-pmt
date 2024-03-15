#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[35]:


# import Liabraies
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# In[43]:


driver = webdriver.Chrome()


# In[44]:


# opening the nukri pageon automated chorome browser
driver.get('https://www.naukri.com/')


# In[45]:


#entering title and location as requried in the question:
Designation = driver.find_element(By.CLASS_NAME,"suggestor-input ")
                               
                              
Designation.send_keys('Data Scientist')


# In[46]:


location = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Delhi/NCR')


# In[47]:


search = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[48]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[49]:


# scraping jobtitle from the given page
title_tags=driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a[1]')
for i in title_tags:
    title=i.text
    job_title.append(title)


# In[50]:


# scraping job location from the given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')
for i in location_tags:
    location=i.text
    job_location.append(location)


# In[51]:


# scraping company_name from the given page
company_tags=driver.find_elements(By.XPATH,'//div[@class=" row2"]/span/a[1]')
for i in company_tags:
    company=i.text
    company_name.append(company)


# In[52]:


# scraping experience_required from the given page

experience_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience_tags:
    exp = i.text
    experience_required.append(exp)


# In[53]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[55]:


import pandas as pd
df = pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df.head(10)


# # Answer 2

# In[2]:


# import Liabraies
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# In[3]:


driver = webdriver.Chrome()


# In[28]:


# opening the nukri pageon automated chorome browser
driver.get(' https://www.shine.com/')



# In[29]:


#entering title and location as requried in the question:
Designation = driver.find_element(By.CLASS_NAME,"form-control  ")
                               
                              
Designation.send_keys('Data Scientist')


# In[30]:


location = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Delhi/NCR')


# In[31]:


search = driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click()


# In[32]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[33]:


# scraping jobtitle from the given page
title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]/a')
for i in title_tags:
    title=i.text
    job_title.append(title)



# In[34]:


# scraping job location from the given page
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags:
    location=i.text
    job_location.append(location)


# In[35]:


# scraping company_name from the given page
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags:
    company=i.text
    company_name.append(company)


# In[36]:


# scraping experience_required from the given page

experience_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags:
    exp = i.text
    experience_required.append(exp)


# In[37]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[42]:


import pandas as pd
df = pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})
df.head(10)


# #  Answer 3

# In[2]:


# import Liabraies
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# In[3]:


driver = webdriver.Chrome()


# In[4]:


# opening the nukri pageon automated chorome browser
driver.get('https://www.flipkart.com/')


# In[7]:


Apple_review = driver.find_element(By.CLASS_NAME,"Pke_EE")
                               
                              
Apple_review.send_keys('Apple iPhone 15 (Black, 128 GB)')


# In[8]:


search = driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


# In[51]:


Review_title = []
Review_Ratings = []

Camera = []
Processor = []
Price = []


# In[52]:


review_tags=driver.find_elements(By.XPATH,'//div[@class="col col-7-12"]/div[1]')
for i in review_tags:
    revi=i.text
    Review_title.append(revi)


# In[53]:


review_ratings=driver.find_elements(By.XPATH,'//span[@class="_2_R_DZ"]')
for i in review_ratings:
    revi_rati=i.text
    Review_Ratings.append(revi_rati)


# In[54]:


camera=driver.find_elements(By.XPATH,'//li[3][@class="rgWa7D"]')
for i in camera:
    cam=i.text
    Camera.append(cam)


# In[55]:


processor=driver.find_elements(By.XPATH,'//li[4][@class="rgWa7D"]')
for i in processor:
    pro=i.text
    Processor.append(pro)


# In[56]:


price=driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]')
for i in price:
    pri=i.text
    Price.append(pri)


# In[58]:


print(len(Review_title),len(Review_Ratings),len(Camera),len(Processor),len(Price))


# In[59]:


import pandas as pd
df = pd.DataFrame({'Apple_title':Review_title,'Review_Ratings':Review_Ratings,'Camera':Camera,'Processor':Processor,'Price':Price})
df.head()


# In[ ]:




