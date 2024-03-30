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


# In[5]:


#connecting to the webdriver
driver=webdriver.Chrome()
time.sleep(2)

# Opening Amazon.in in chrome browser
url='http://www.amazon.in/'
driver.get(url)
time.sleep(2)

# Taking input from user about product search
User_input=input('Enter the title of Product you are interest in search :')


# In[6]:


# Finding search menu by xpath
Search=driver.find_element(By.XPATH,'//input[@id="twotabsearchtextbox"]')
# clearing any previous input in search bar
Search.clear()
# Feeding input specified by user to search menu through send keys
Search.send_keys(User_input)
# Finding Search button for clicking through xpath
Search_button=driver.find_element(By.XPATH,'//input[@id="nav-search-submit-button"]')
# Clicking search button
Search_button.click()


#  # Answer 2

# In[7]:


# Make Empty list to scrap data
Brand =[]
Product = []
Rating =[]
No_of_ratings =[]
Price =[]
Return =[]
Excepted_delivery =[]
Availability =[]
Other_details =[]


# # Scraping url of all product listed on first 3 pages
# 

# In[8]:


URL= []
# range(0,3) used to scrape three pages on website
for page in range(0,3):
    url=driver.find_elements(By.XPATH,'//div[@class="a-section a-spacing-base"]/div/span/a')
    for i in url:
        URL.append(i.get_attribute('href'))
    time.sleep(2)
    # locating next page button and clicking
    Nxt_page=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator"]')
    Nxt_page.click()
    time.sleep(3)


# In[9]:


len(URL)


# In[11]:


from tqdm import tqdm
for i in tqdm(URL):
    driver.get(i)
    time.sleep(2)
    
    # Extracting Brand Name via Xpath
    try:
        brand=driver.find_element(By.XPATH,'//a[@id="bylineInfo"]')
        Brand.append(brand.text) 
    except NoSuchElementException:
        Brand.append('-')
        
    time.sleep(1)
    
    # Extracting product name via Xpath
    try:
        product =driver.find_element(By.XPATH,'//span[@id="productTitle"]')
        Product.append(product.text)
    except NoSuchElementException:
        Product.append('-')
    time.sleep(1)
    
    # Extracting Rating via Xpath
    try:
        rating=driver.find_element(By.XPATH,'//span[@class="a-size-medium a-color-base"]')
        Rating.append(rating.text)
    except NoSuchElementException:
        Rating.append('-')
    time.sleep(1)
    
    # Extracting No of Ratings via Xpath
    try:
        rating_count=driver.find_element(By.XPATH,'//span[@class="a-size-base a-color-secondary"]')
        No_of_ratings.append(rating_count.text)
    except NoSuchElementException:
        No_of_ratings.append('-')
    time.sleep(1)
    
    # Extracting Price via Xpath
    try:
        price=driver.find_element(By.XPATH,'//span[@id="priceblock_dealprice"]')
        Price.append(price.text)
    except NoSuchElementException:
        Price.append('-')
    time.sleep(1)
    
    # Extracting Return or exchange detail via Xpath
    try:
        replacement=driver.find_element(By.XPATH,'//*[@id="RETURNS_POLICY"]/span/div[2]/a')
        Return.append(replacement.text)
    except NoSuchElementException:
        Return.append('-')
    time.sleep(1)
    
    # Extracting Expected Delivery via Xpath
    try:
        delivery=driver.find_element(By.XPATH,'//div[@id="ddmDeliveryMessage"]/b')
        Excepted_delivery.append(delivery.text)
    except NoSuchElementException:
        Excepted_delivery.append('-')
    time.sleep(1)
    
    # Extracting Availability via Xath
    try:
        availability=driver.find_element(By.XPATH,'//span[@class="a-size-medium a-color-success"]')
        Availability.append(availability.text)
    except NoSuchElementException:
        Availability.append('-')
    time.sleep(1)
    
    # Extracting other details via Xpath
    try:
        other=driver.find_element(By.XPATH,'//ul[@class="a-unordered-list a-vertical a-spacing-mini"]')
        Other_details.append(other.text)
    except NoSuchElementException:
        Other_details.append('-')
    time.sleep(1)
    


# In[12]:


Guitar=pd.DataFrame({'Brand':Brand,'Product':Product,'Rating':Rating,'No. of ratings':No_of_ratings,'Price':Price,
                        'Return/Exchange':Return,'Expected Delivery':Excepted_delivery,'Availability':Availability,
                        'Other Details':Other_details,'URL':URL})
print('\033[1m'+'Amazon Festive Sale Guitar with exciting offers :'+'\033[0m')
Guitar


# # Answer 3

# In[49]:


# Connecting to webdriver
driver=webdriver.Chrome()
time.sleep(1)

# Opening url in Chrome browser
url='https://images.google.com/'
driver.get(url)


# # Searching and extracting for Fruits.
# 

# In[41]:


# Finding Search bar website by class
Search=driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]')
# Clearing any previous input in search bar
Search.clear()
# Feeding input 'Fruits' in search bar
Search.send_keys('Fruits')
# Finding Search button for clicking through class name
Search_button=driver.find_element(By.CLASS_NAME,'zgAlFc')
# Clicking search button
Search_button.click()


# In[42]:


# Scrolling window using ScrollBy method from 0 pixel to 25000 pixel
driver.execute_script("window.scrollBy(0,25000)","")


# In[43]:


URL=[]
images= driver.find_elements(By.XPATH,'//img[@class="YQ4gaf"]')
for image in images:
    source= image.get_attribute('src')
    if source is not None:
        if(source[0:4] == 'http'):
            URL.append(source)


# In[44]:


len(URL)


# In[48]:


images = driver.find_elements(By.XPATH,'//img[@class="YQ4gaf"]')

img_urls = []
img_data = []
for image in images:
    source= image.get_attribute('src')
    if source is not None:
        if(source[0:4] == 'http'):
            img_urls.append(source)
            
for i in range(len(img_urls)):
    if i >= 10:
        breakBY.XPATH
    print("Downloading {0} of {1} images" .format(i, 100))
    response= requests.get(img_urls[i])
    file = open(r"C:\Users\HP|Desktop\Fliprobo"+str(i)+".jpg", "wb")
    file.write(response.content)


# # Searching and extracting for Cars.
# 

# In[53]:


# Finding Search bar website by class
Search=driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]')
# Clearing any previous input in search bar
Search.clear()
# Feeding input 'Cars' in search bar
Search.send_keys('Cars')
# Finding Search button for clicking through class name
Search_button=driver.find_element(By.CLASS_NAME,'zgAlFc')
# Clicking search button
Search_button.click()


# In[54]:


# Scrolling window using ScrollBy method from 0 pixel to 25000 pixel
driver.execute_script("window.scrollBy(0,50000)","")


# In[56]:


URL=[]
images= driver.find_elements(By.XPATH,'//div[@class="fR600b islir"]/img')
for image in images:
    source= image.get_attribute('src')
    if source is not None:
        if(source[0:4] == 'http'):
            URL.append(source)


# In[57]:


len(URL)


# In[60]:


images = driver.find_elements(By.XPATH,'//div[@class="fR600b islir"]/img')

img_urls = []
img_data = []
for image in images:
    source= image.get_attribute('src')
    if source is not None:
        if(source[0:4] == 'http'):
            img_urls.append(source)
            
for i in range(len(img_urls)):
    if i >= 100:
        break
    print("Downloading {0} of {1} images" .format(i, 100))
    response= requests.get(img_urls[i])
    file = open(r"C:\Users\Infinity\Fliprobbo\WebScraping Assignment 3 Selenium\Cars" +str(i)+ ".jpg", "wb")
    file.write(response.content)


# # Searching and extracting for Machine Learning.
# 

# In[66]:


# Connecting to webdriver
driver=webdriver.Chrome()
time.sleep(1)

# Opening url in Chrome browser
url='https://images.google.com/'
driver.get(url)


# In[67]:


# Finding Search bar website by class
Search=driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]')
# Clearing any previous input in search bar
Search.clear()
# Feeding input 'Machine Learning' in search bar
Search.send_keys('Machine Learning')
# Finding Search button for clicking through class name
Search_button=driver.find_element(By.CLASS_NAME,'zgAlFc')
# Clicking search button
Search_button.click()


# In[68]:


# Scrolling window using ScrollBy method from 0 pixel to 50000 pixel
driver.execute_script("window.scrollBy(0,50000)","")


# In[70]:


URL=[]
images= driver.find_elements(By.XPATH,'//div[@class="fR600b islir"]/img')
for image in images:
    source= image.get_attribute('src')
    if source is not None:
        if(source[0:4] == 'http'):
            URL.append(source)


# In[71]:


len(URL)


# In[74]:


images = driver.find_elements(By.XPATH,'//div[@class="fR600b islir"]/img')

img_urls = []
img_data = []
for image in images:
    source= image.get_attribute('src')
    if source is not None:
        if(source[0:4] == 'http'):
            img_urls.append(source)
            
for i in range(len(img_urls)):
    if i >= 100:
        break
    print("Downloading {0} of {1} images" .format(i, 100))
    response= requests.get(img_urls[i])
    file = open(r"C:\Users\Infinity\Fliprobbo\WebScraping Assignment 3 Selenium\Machine Learning"+str(i)+".jpg", "wb")
    file.write(response.content)


# # Answer 4

# In[13]:


# Importing require libary
import selenium
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


# In[15]:


# Connecting to webdriver
driver=webdriver.Chrome()
time.sleep(1)

# Opening url in Chrome browser
url='http://www.flipkart.com/'
driver.get(url)
time.sleep(3)


# In[18]:


try:
    login_window = driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _2doB4z"]')
    login_window.click()
except NoSuchElementException:
    print('Login Window is not present')


# In[21]:


# Finding Search bar website by xpath
Search=driver.find_element(By.XPATH,'//div[@class="_2SmNnR"]/input')
# Clearing any previous input in search bar
Search.clear()
# Feeding input 'Oneplus' in search bar
Search.send_keys('Iphone Mobile')
# Finding Search button for clicking through class name
Search_button=driver.find_element(By.XPATH,'//button[@class="_2iLD__"]')
# Clicking search button
Search_button.click()


# In[22]:


# Making empty list to scrape data
Brand =[]
Smartphone =[]
Colour =[]
Storage_Rom =[]
Primary_camera=[]
Secondary_camera=[]
Display_size=[]
Display_resolution=[]
Processor =[]
Processor_cores=[]
Battery_capacity=[]
Price =[]


# In[23]:


URL=[]
url=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in url:
    Href=i.get_attribute('href')
    URL.append(Href)


# In[24]:


len(URL)


# In[28]:


from tqdm import tqdm
for i in tqdm(URL):
    driver.get(i)
    time.sleep(3)
    
    # Expanding specification table by clicking on read more button
    try:
        Read_more=driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
        Read_more.click()
        
    except NoSuchElementException:
        print('NoSuchElementException Occur')
        pass
    
    # Extracting Brand Name via Xpath
    try:
        brand=driver.find_element(By.XPATH,'//span[@class="B_NuCI"]')
        Brand.append(brand.text.split()[0])
    
    except NoSuchElementException:
        Brand.append('-')
        
    # Extracting Smartphone Model via Xpath
    try:
        smartphone=driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][1]/table/tbody/tr[3]/td[2]/ul/li')
        Smartphone.append(smartphone.text)
    
    except NoSuchElementException:
        Smartphone.append('-')
        
    # Extracting Colour via Xpath
    try:
        colour=driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][1]/table/tbody/tr[4]/td[2]/ul/li')
        Colour.append(colour.text)
    
    except NoSuchElementException:
        Colour.append('-')
    
    # Extracting Storage Rom via Xpath
    try:
        Rom=driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][4]/table/tbody/tr[1]/td[2]/ul/li')
        Storage_Rom.append(Rom.text)
        
    except NoSuchElementException:
        Storage_Rom.append('Not Mention')
        
    # Extracting primary camera detail via Xpath
    try:
        primary_camera=driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][5]/table/tbody/tr[2]/td[2]/ul/li')
        Primary_camera.append(primary_camera.text)
    
    except NoSuchElementException:
        Primary_camera.append('Not Mention')
        
    # Extracting Secondary Camera detail via Xpath
    try:
        secondary_cam=driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][5]/table/tbody/tr[5]/td[2]/ul/li')
        Secondary_camera.append(secondary_cam.text)
    
    except NoSuchElementException:
        Secondary_camera.append('Not Mention')
    
    # Extracting Display size via Xpath
    try:
        display=driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][2]/table/tbody/tr[1]/td[2]/ul/li')
        Display_size.append(display.text)
    except NoSuchElementException:
        Display_size.append('-')
    
    # Extracting Display Resolution via Xpath
    try:
        resolution=driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][2]/table/tbody/tr[2]/td[2]/ul/li')
        Display_resolution.append(resolution.text)
    except NoSuchElementException:
        Display_resolution.append('-')
    
    # Extracting processor detail via xpath
    try:
        processor=driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][3]/table/tbody/tr[2]/td[2]/ul/li')
        Processor.append(processor.text)
    
    except NoSuchElementException:
        Processor.append('-')
        
    # Extracting Processor core via xpath
    try:
        core=driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][3]/table/tbody/tr[3]/td[2]/ul/li')
        Processor_cores.append(core.text)
    except NoSuchElementException:
        Processor_cores.append('Not Mention')
    
    #Extracting Price via X path
    try:
        price=driver.find_element(By.XPATH,'//div[@class="_30jeq3 _16Jk6d"]')
        Price.append(price.text)
    except NoSuchElementException:
        Price.append('Not Mention')


# In[29]:


Iphone=pd.DataFrame({'Brand':Brand,'Smartphone':Smartphone,'Colour':Colour,'Price':Price,
                        'Storage Rom':Storage_Rom,'Primary Camera':Primary_camera,'Display Size':Display_size,
                        'Display Resolution':Display_resolution,'Processor':Processor,'Processor Cores':Processor_cores})
print('\033[1m'+'Flipkart Iphone Models :'+'\033[0m')
Iphone.head()


# # Answer 5

# In[30]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


# In[31]:


# Connecting to webdriver
driver=webdriver.Chrome()
time.sleep(1)

# Opening url in chrome browser
url='https://www.google.co.in/maps'
driver.get(url)
time.sleep(3)


# In[32]:


# Finding search menu by xpath
Search=driver.find_element(By.XPATH,'//input[@class="searchboxinput xiQnY"]') 
# clearing any previous input in search bar
Search.clear()
# Feeding input specified by user to search menu through send keys
Search.send_keys('Nashik')
# Finding Search button for clicking through xpath
Search_button=driver.find_element(By.XPATH,'//span[@class="google-symbols"]')  
# Clicking search button
Search_button.click()


# In[33]:


current_url=driver.current_url
print('Current url :',current_url)


# In[34]:


try:
    if "@" in current_url:
        location=current_url.split('@')[1].split(',*/data')[0].split(',')
        location
        print('Latitude of given Location:',location[0])
        print('Longitude of given Location:',location[1])
except:
    print('Location detail not found in url')


# # Answer 6

# In[102]:


driver = webdriver.Chrome()


# In[103]:


url="https://www.digit.in/top-products/best-gaming-laptops-40.html"


# In[104]:


driver.get(url)


# In[106]:


Brands=[]

Specification=[]



# In[107]:


br=driver.find_elements(By.XPATH,"//div[@class='r_offer_details news-community clearfix  product type-product']")
len(br)


# In[108]:


for i in br:
   
    Brands.append(str(i.text).replace("\n",""))
Brands


# In[109]:


sp=driver.find_elements(By.XPATH,"//div[@class='woo_code_zone_loop clearbox']")
len(sp)


# In[110]:


for i in sp:
   
    Specification.append(str(i.text).replace("\n",""))
Specification


# In[111]:


digit_lap=pd.DataFrame([])
digit_lap['Brands']=Brands[0:10]
digit_lap['Specification']=Specification[0:10]



digit_lap


# # Answer 7

# In[63]:


driver = webdriver.Chrome()


# In[64]:


url1="https://trak.in/india-startup-funding-investment-2015/"


# In[65]:


driver.get(url1)


# In[66]:


Dates=[]
Company=[]
Industry=[]
Investor_Name=[]
Investment_Type=[]
Amount=[]


# In[67]:


#scraping the company_name 
companies=driver.find_elements(By.XPATH,"//td[@class='column-3']")
for i in companies:
    if i.text is None :
        Company.append("--") 
    else:
        Company.append(i.text)
print(len(Company),Company)


# In[68]:


#scraping the Industry 
Ind=driver.find_elements(By.XPATH,"//td[@class='column-4']")
for i in Ind:
    if i.text is None :
        Industry.append("--") 
    else:
        Industry.append(i.text)
print(len(Industry),Industry)


# In[69]:


#scraping the Dates 
dt=driver.find_elements(By.XPATH,"//td[@class='column-2']")
for i in dt:
    if i.text is None :
        Dates.append("--") 
    else:
        Dates.append(i.text)
print(len(Dates),Dates)


# In[70]:


#scraping the Investor_Name 
IN=driver.find_elements(By.XPATH,"//td[@class='column-7']")
for i in IN:
    if i.text is None :
        Investor_Name.append("--") 
    else:
        Investor_Name.append(i.text)
print(len(Investor_Name),Investor_Name)


# In[71]:


#scraping the Investment_Type 
IT=driver.find_elements(By.XPATH,"//td[@class='column-8']")
for i in IT:
    if i.text is None :
        Investment_Type.append("--") 
    else:
        Investment_Type.append(i.text)
print(len(Investment_Type),Investment_Type)


# In[72]:


#scraping the Amount 
Price=driver.find_elements(By.XPATH,"//td[@class='column-9']")
for i in Price:
    if i.text is None :
        Amount.append("--") 
    else:
        Amount.append(i.text)
print(len(Amount),Amount)


# In[73]:


Funding=pd.DataFrame([])
Funding['Company']=Company
Funding['Industry']=Industry
Funding['Investor_Name']=Investor_Name
Funding['Amount Invested']=Amount
Funding['Specification']=Investment_Type
Funding['Dates']=Dates
Funding

