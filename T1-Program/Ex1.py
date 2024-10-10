#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = float(input("Enter a value of a : "))
b = float(input("Enter a value of b : "))
c = float(input("Enter a value of c : "))
s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print("Your area of triangle is = " , f"{area:.2f}")


# In[ ]:


suraface volume oand area of silinder given the height
and radius by the user  


# In[ ]:


radius = float(input("Enter the value of radius : "))
height = float(input("Enter the value of height : "))
PI = 3.14
volume = PI*radius**2*height
print("Your silinder volume is = " , f"{volume:.2f}")
area = 2*PI*radius*height
print("Your silinder area is = " , f"{area:.2f}")


# In[ ]:


to convert to years , months and days


# In[15]:


days = int(input("Enter of days : "))
years = days/365
months = (days%365)/30
days = (days%365)%30
print(f"Your years is : {int(years)} , " , f"Your months is : {int(months)} , " , 
     f"Your days is : {int(days)}")


# In[ ]:


to convert seconds to hours , minites and seconds and days


# In[1]:


seconds = int(input("Enter of seconds : "))
days = seconds//86400
hours = seconds//3600
miniuts = seconds//60
seconds = (seconds%3600)%60
print(f"Your days is : {int(days)} , " , f"Your hours is : {int(hours)} , " , 
     f"Your miniuts is : {int(miniuts)} , " , f"Your seconds is : {int(seconds)} ")


# In[ ]:




