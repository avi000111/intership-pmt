#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# # Answer 1

# In[19]:


# import Liabraies
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# In[20]:


driver = webdriver.Chrome()


# In[21]:


# opening the nukri pageon automated chorome browser
driver.get('https://www.shine.com/')


# In[28]:


#entering title and location as requried in the question:
jobtitle = driver.find_element(By.CLASS_NAME,"form-control  ")
                               
                              
jobtitle.send_keys('Data Analyst')


# In[29]:


location = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')


# In[31]:


search = driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click()


# In[32]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[ ]:


# scraping jobtitle from the given page
title_tags=driver.find_elements(By.XPATH,)
for i in title_tags:
    title=i.text
    job_title.append(title)



# In[33]:


# scraping job location from the given page
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags:
    location=i.text
    job_location.append(location)


# In[34]:


# scraping company_name from the given page
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]/span')
for i in company_tags:
    company=i.text
    company_name.append(company)


# In[35]:


# scraping experience_required from the given page

experience_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags:
    exp = i.text
    experience_required.append(exp)


# In[36]:


print(len(job_location),len(company_name),len(experience_required))


# In[37]:


import pandas as pd
df = pd.DataFrame({'Location':job_location,'Company_name':company_name,'Experience':experience_required})


# In[38]:


df


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


# In[4]:


# opening the nukri pageon automated chorome browser
driver.get('https://www.naukri.com/')


# In[5]:


#entering title and location as requried in the question:
jobtitle = driver.find_element(By.CLASS_NAME,"suggestor-input ")
jobtitle.send_keys('Data Analyst')


# In[7]:


location = driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Bangalore')


# In[8]:


search = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[9]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[13]:


# scraping jobtitle from the given page
title_tags=driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
for i in title_tags:
    title=i.text
    job_title.append(title)



# In[15]:


# scraping job location from the given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')
for i in location_tags:
    location=i.text
    job_location.append(location)


# In[17]:


# scraping company_name from the given page
company_tags=driver.find_elements(By.XPATH,'//div[@class=" row2"]/span/a[1]')
for i in company_tags:
    company=i.text
    company_name.append(company)


# In[18]:


# scraping experience_required from the given page

experience_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience_tags:
    exp = i.text
    experience_required.append(exp)


# In[19]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[20]:


import pandas as pd
df = pd.DataFrame({'Title':job_title,'Location':job_location,'Company_name':company_name,'Experience':experience_required})


# In[21]:


df


#  # Answer 3

# In[62]:


# import Liabraies
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# In[63]:


driver = webdriver.Chrome()


# In[64]:


driver.get('https://www.flipkart.com/')


# In[67]:


search = driver.find_element(By.CLASS_NAME,"Pke_EE")
search.send_keys('100 sunglass')




# In[68]:


search_button = driver.find_element(By.CLASS_NAME,"_2iLD__")
search_button.click()


# In[69]:


Brand=[]
ProductDescription=[]
Price=[]


# In[70]:


Brand_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in Brand_tags:
    Brands=i.text
    Brand.append(Brand)


# In[71]:


Product_Description_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in Product_Description_tags:
    Product=i.text
    ProductDescription.append(Product)


# In[59]:


Price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in Price_tags:
    Prices=i.text
    Price.append(Prices)


# In[72]:


print(len(Brand),len(ProductDescription),len(Price))


# In[73]:


import pandas as pd
df = pd.DataFrame({'Brand':Brand,'ProductDescription':ProductDescription,'Price':Price})


# In[ ]:




