#!/usr/bin/env python
# coding: utf-8

# # wap to find the smallest positive integer where whenue put the write most digit to the left most the resulting number is exectly 1.5 times the orignal number

# In[9]:


def smallest():
    n = 1   # (start)
    while True:
        rightmost = n % 10
        restofnumber = n//10
        # no of digit
        k = 0
        temp = n
        while temp > 0:
            temp //= 10
            k += 1
        new = rightmost * (10 ** (k-1)) + restofnumber
        if new == 1.5 * n:
            return
        n += 1
print(smallest())


# # total animal = 10 , 10 heads and 26 legs animal ,  name to how many cows and rabbits

# In[28]:


heads = 10
legs = 26
for i in range(heads + 1):
    cows = i
    rabbits = heads - cows
    if 4 * cows + 2 * rabbits == legs:
        print(f"Cows : {cows} , Rabbits : {rabbits}")


# # Suppose you put 1 rupees in bank on first day(monday) and every day in first day(tuesday to sunday) you putting more than the day before and on every subseqvent for monday you put more than the previus mounday if you have number and amount of money find the total of the end of nth day

# In[35]:


n = int(input("Enter days : "))
mon_amount = 1
amount = 1
ans = 1
for i in range(2 , n+1):
    if i % 7 == 1:
        mon_amount += 1
        amount = mon_amount
        ans = ans + amount
    else:
        amount += 1
        ans += amount
else:
    print(ans)


# # time add program

# In[36]:


user = int(input("Enter hour : "))
day = input("Enter am or pm : ")
hour_ahead = int(input("Enter hour ahead : "))
if user < 1 or user > 12 or(day != 'am' and day != 'pm'):
    print("Enter correct time")
else:
    for i in range(1 , hour_ahead + 1):
        user += 1
        if user > 12:
            user = 1 # (reset)
        if user == 12:
            if day == 'am':
                day = 'pm'
            else:
                day = 'am'
    if day == 'am':
        print(f"Newtime : {user}AM")
    else:
        print(f"Newtime : {user}PM")


# In[42]:


x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func(x)
print('x is now', x)


# In[43]:


car = 20
bike = 10
cycle = 30
def new_Pur():
    global bike, cycle
    car = 30
    bike = 20
    cycle = 50
new_Pur()
print(car + 10, "", bike + 5, "", cycle + 5)

