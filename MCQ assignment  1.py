#!/usr/bin/env python
# coding: utf-8

# # Answer 1

# In[2]:


def func(a,b):
    return b if a==0 else func(b%a,a)
print(func(30,75))


# # Answer 2

# In[3]:


numbers = (4,7,19,2,89,45,72,22)
sorted_numbers = sorted(numbers)
even = lambda a: a%2==0
even_numbers = filter(even,sorted_numbers)
print(type(even_numbers))


# In[ ]:


(b) filter


# # Answer 3

# In[ ]:


(a)   Tuple


# # Answer 4

# In[20]:


set1 = {14, 3, 55}
set2 = {82, 49, 62}
set3 = {99, 12, 17}


# In[21]:


# combine sets using the union method
combined_set = set1.union(set2, set3)


# In[22]:


# print the length of the combined set
print(len(combined_set))


# In[ ]:


(d) Error


# # Answer 5

# In[ ]:


(a) raise


# # Answer 6

# In[ ]:


(c) datetime


# # Answer 7

# In[23]:


print(4**3 + (7 + 5)**(1 + 1))


# In[ ]:


(c) 208


# # Answer 8

# In[ ]:


(a) stprtime


# # Answer 9

# In[ ]:


(b) immutable


# # Answer 10

# In[ ]:


(a) range()


# # Answer 11

# In[ ]:


(c) Lambda function


# # Answer 12

# In[ ]:


(b)  De-serializing Python object structure


# # Answer 13

# In[ ]:


(b) dump() method


# # Answer 14

# In[ ]:


(a) load()


# # Answer 15

# In[ ]:


(a) Alphabets
(b) Numbers
(c) Special symbols


# # Answer 16

# In[28]:


captains = {
    "Enterprise":"Picard",
    "Voyager":"Janeway",
    "Defiant":"Sisko"
}

for ship,captain in captains.items():
    print(ship,captain)


# In[1]:


captains = {
    "Enterprise":"Picard",
    "Voyager":"Janeway",
    "Defiant":"Sisko",
    
}

for ship in captains:
    print(ship,captains[ship])


# (d) both a and b
# 

# # Answer 17

# In[ ]:


(d) captains = {}


# # Answer 18

# In[9]:


captains{"Enterprise" = "Picard"}
captains{"Voyager" = "Janeway"}
captains{"Defiant" = "Sisko"}



# In[6]:


captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"


# In[5]:


captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",

}


# In[ ]:


d) None of the above


# In[ ]:


# print Answer
(b)and (c) run 


# # Answer 19

# In[10]:


captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",
 "Discovery": "unknown",
}


# In[ ]:


(d) all the correct


# # Answer 20

# In[11]:


captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",
 "Discovery": "unknown",
}


# In[ ]:


d) captains["Discovery"].pop()

