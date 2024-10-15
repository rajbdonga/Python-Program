#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def greet(name):
    print(f"Hello {name}")
greet("john")


# In[ ]:


def area(radius : float):
    """
    Description : This function calculate area of circle 
    Parameter : Radius in float
    Return : Area of circle in float
    """
    print(area.__doc__)
    return 3.14*radius**2
area(3.0)


# In[ ]:


help(range)


# In[ ]:


get_ipython().run_line_magic('whos', '')


# In[ ]:


def printline():
    print("Hello")
printline()   


# In[ ]:


def printline(s):
    print(s)
print("Hello")  


# In[ ]:


def printline():
    return "Hello"
printline()  


# In[ ]:


def printline(s):
    return "Hello"
printline("hi")  


# In[ ]:


def cal(a , b):
    return a+b , a-b
cal(5 , 3)


# In[ ]:


x , y = cal(5 , 3)
print(f"x = {x} y = {y}")


# In[ ]:


def cal(a , b):
    return a+b , a-b
m = cal(5 , 3)
type(m)


# In[ ]:


x = 90
def func():
    x = 5
    print(x)
func()
print(x)


# # The variable scope define with in the function is local 
# it's lifetime is one's the function is called and destroy when the function ends

# In[ ]:


x = 90
def func():
    global x
    x = 5
    print(x)
func()
print(x)


# # Waf of celcius and ferenhit tempretures with the use input or choices , c = 5/9 x (f - 32) , f = (c x 9/5) + 32

# In[ ]:


def celcius(f):
    c = 5/9 * (f - 32)
    print(f"c : {c}f")
def ferenhit(c):
    f = (c*9/5) + 32          
    print(f"f : {f}c")
switch = int(input("Enter the value of 1 & 2 :"))
if(switch ==1):
        fer = float(input("Enter the ferenhit temprature : "))
        celcius(fer)
elif(switch == 2):
        cel = float(input("Enter the celcius  temprature : "))
        ferenhit(cel)
else:
        print("Your enter value not match the function plz try again")


# # waf find a factorial

# In[ ]:


def fact(n):
    f = 1
    for i in range(1 , n+1):
        f = f*i
    return f
fact(5)


# In[ ]:


def square(n = 10):
    return n * n
square()
square(20)


# In[ ]:


def wish(name , msg):
    print("hi" , name , msg)
wish(name = "c" , "Good Morning")    


# In[ ]:


def wish(name , msg):
    print("hi" , name , msg)
wish("c" , "Good Morning") 


# # waf to add three number given by the user

# In[5]:


def sum(*n):
    total = 0
    for i in n:
        total = total + i
    print(total)
sum(1 , 2 , 3 , 4)    


# # wap to find a strong number

# In[33]:


def fact(n):
    result = 1
    for i in range(1 , n+1):
        result *= i
    return result
def is_strong(number):
    sum_of_fact = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum_of_fact += fact(digit)
        temp //= 10
    return sum_of_fact == number
is_strong(145)


# # wap to find happy number

# 


def squares(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit * digit
        num //= 10
    return total
def happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = squares(num)
    return num == 1
print("Happy numbers between 1 and 130 are:")
for i in range(1, 131):
    if happy(i):
        print(i, end=" ")
