#!/usr/bin/env python
# coding: utf-8

# # wap to check the number is even or odd

# In[ ]:


number = float(input("Enter a number : "))
if number % 2 == 0 :
    print("Your entered number is even")
else :
    print("Your entered number is odd")


# In[ ]:


count = 0
while count < 5 :
    print("Hello")
    count += 1
else :
    print("Loop completed")


# In[ ]:


list(range(5 , 0 , -1))


# In[ ]:


get_ipython().run_line_magic('pinfo2', 'range')


# In[ ]:


for i in range(3) :
    print(i , end=" ")


# In[ ]:


for i in "Python":
    print(i)
else :
    print("Loop completed")    


# In[ ]:


list("Python")


# In[ ]:


a = int(input("Enter a : "))
for i in range(1 , 11) :
    print(a,"*",i,"=",a*i)


# # wap to take 10 values from user and print the avrage the screen

# In[ ]:


sum = 0
i = 10
while i>0 :
    print("Enter number : ")
    num = int(input())
    sum = sum + num
    i-=1
print("Avrage is",sum/10)    


# In[ ]:


for i in range(5) :
    if i==3 :
       continue
    print(i)
else :
    print("Loop cmpleted")


# In[ ]:


for i in range(5) :
    ...


# # wap python program to reverse a given number

# In[ ]:


num = int(input("Enter num : "))
rev = 0
while num != 0 :
    d = num % 10
    rev = rev * 10 + d
    num //= 10
    print(num)


# # wap to find the integer solution of $ x^2 - 2y^2 = 1 $ for the valuea of x and y beetween 1 to 100

# In[4]:


for x in range(1 , 101):
    for y in range(1 , 101):
        if((x**2)-2*(y**2)==1):
            print("(",x,",",y,")")


# # wap to compute the sum of 1-2+3-4...2000

# In[8]:


sum = 0
for i in range(1 , 2001):
    if i % 2 ==0:
        sum -= i
    else:
        sum +=i
print(sum)        


# # wap find the Harshad number
# Harshad number - it is divisible by 10 sum of digit

# In[18]:


num = int(input("Enter a number : "))
if num<0:
    print("Enter Positive")
else:
    ds = 0
    for d in str(num):
        ds += int(d)
    if num%ds==0:
        print("Harshad")
    else:
        print("Not a Harshad")


# In[ ]:




