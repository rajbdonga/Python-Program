#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # MAX SCORE IN 3rd MATCH

# In[2]:


scores = np.array([[31,12,15,16],
         [67,63,65,69],
         [52,15,14,15],
         [78,45,45,59],
         [78,45,89,23]])


# In[4]:


max_score = 0
for i in scores[:,2]:
    if i > max_score:
        max_score = i
print(max_score)


# In[ ]:


min_score = [2,0]
for i in scores[2,:]:
    if i < min_score:
        min_score = i
print(min_score)


# In[5]:


batsman_total = []
for i in range(0,5):
    total = 0
    for j in range(0,4):
        total += scores[i,j]
    batsman_total.append(total)
batsman_total = np.array(batsman_total).reshape(5,1)
scores = np.concatenate((scores,batsman_total),axis = 1)
print(scores)


# # sort the array in desending order in total scores of each batsman 

# In[6]:


newlist = list(scores)
sortedarray = sorted(newlist , key=lambda x:x[-1] , reverse=True)
newarray = np.array(sortedarray)
print(newarray)


# In[7]:


match_total = []
for i in range(4):
    total = 0
    for j in range(5):
        total += scores[j,i]
    match_total.append(total)
match_total = np.array(match_total).reshape(1,4)
scores = np.concatenate((scores[:,:-1],match_total),axis = 0)
print(scores)


# # make a new array wich represent if the batsman score is greater then 30 

# In[3]:


print(np.where(scores > 30 , 1 , 0))


# # impliment a python class money to handled rupies and paise it should have following methods 1. __init__ method to initialize rupies and paise 2. add __toaddmoneyobject__ 3. sub __tosubmoneyobject__ 4. ge __ge__ 5. str method to display money object 6. cal total based on quality input

# In[4]:


class Money:
    def __init__(self , rupees , paisa):
        self.rupees = rupees
        self.paisa = paisa
        self.total = rupees + (paisa/100)
    def __add__(self , other):
        return self.total + other.total
    def __sub__(self , other):
        return self.total - other.total
    def __ge__(self , other):
        return self.total > other.total
    def __mul__(self , other):
        return self.total * other
    def __str__(self):
        return f"{self.rupees} Rs and {self.paisa} Paisa"
    def calculatetotal(self , quantity):
        return self.total * quantity
m1 = Money(100,50)
m2 = Money(20,50)
print(m1 + m2)
print(m1 - m2)
print(m1 >= m2)
print(m1 * 5)
print(m2 * 5)
print(m1)
print(m2)
print(m1.calculatetotal(1))
print(m2.calculatetotal(1))


# In[6]:


import numpy as np
import matplotlib.pyplot as plt


# In[25]:


plt.style.use('default')
x = np.linspace(0,10,100)
plt.plot(x,np.sin(x), label = 'sine curve')
plt.xlabel('x lable')
plt.ylabel('y lable')
plt.title('sine curve example plot')
plt.legend()
plt.grid()


# In[36]:


fig = plt.figure(figsize=(5,3), dpi=100)
plt.plot(x,np.sin(x), '-')
plt.plot(x,np.cos(x), '--')


# In[32]:


fig.savefig("plots.png")


# In[39]:


get_ipython().run_line_magic('pinfo2', 'plt.plot')


# In[49]:


plt.subplot(2,2,1)
x = np.linspace(0,10,100)
plt.plot(x,np.sin(x), label = 'sine curve')
plt.xlabel('x lable')
plt.ylabel('y lable')
plt.title('sine curve example plot')
plt.legend()
plt.grid()
plt.tight_layout()
plt.subplot(2,2,2)
x = np.linspace(0,10,100)
plt.plot(x,np.cos(x), label = 'cose curve')
plt.xlabel('x lable')
plt.ylabel('y lable')
plt.title('cose curve example plot')
plt.legend()
plt.grid()
plt.tight_layout()
plt.subplot(2,2,3)
x = np.linspace(0,10,100)
plt.plot(x,np.tan(x), label = 'tan curve')
plt.xlabel('x lable')
plt.ylabel('y lable')
plt.title('tan curve example plot')
plt.legend()
plt.grid()
plt.tight_layout()
plt.subplot(2,2,4)
x = np.linspace(0,10,100)
plt.plot(x,np.exp(x), label = 'exp curve')
plt.xlabel('x lable')
plt.ylabel('y lable')
plt.title('exp curve example plot')
plt.legend()
plt.grid()


# In[62]:


x = [1,2,3]
y = [2,4,1]
plt.plot(x, y , label = 'x vs y curve')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My First Graph')
plt.legend()


# In[61]:


x1 = [1,2,4]
y1 = [2,4,2]
plt.plot(x1, y1 , label = 'line 1')
x2 = [8,5,5]
y2 = [3,4,2]
plt.plot(x2, y2 , label = 'line 2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My First Graph')
plt.legend()


# In[73]:


values = [5,6,4,7,8]
names = ["A" , "B" , "C" , "D" , "E"]
plt.bar(names , values , color="black")


# In[71]:


help(plt.bar)


# In[79]:


x = [1,2,3,4,5,6]
y = [2,3,4,1,5,6]
plt.plot(x,y,color='green' , linestyle='dashed' , linewidth=3 , marker='o' , markerfacecolor='blue' , markersize=12)
plt.ylim(1,8)
plt.xlim(1,8)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Some cool customization')


# In[92]:


ages = [1,11,12,21,22,23,31,32,33,34,41,42,43,44,45,51,52,53,54,61,62,63,71,72,81]
range = (0 , 100)
bins = 10
plt.hist(ages,bins,range,color='green',histtype='bar',rwidth=0.8)
plt.xlabel('age')
plt.ylabel('No. of people')
plt.title('My histogram')


# In[103]:


x = [2,4,2,3.5,3,6,5]
y = [4,6,6,6,4,8,7]
plt.scatter(x,y, label='stars' , color='green' , marker='*' , s=30)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My scatter plots!')


# In[106]:


activities = ['eat' , 'sleep' , 'work' , 'play']
slices = [3,7,8,6]
colors = ['r' , 'y' , 'g' , 'b']
plt.pie(slices , labels=activities , colors=colors , startangle=90 , shadow=True , explode=(0,0,0.1,0) , radius=1.2 , autopct='%1.1f%%')
plt.legend()

