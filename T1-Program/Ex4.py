#!/usr/bin/env python
# coding: utf-8

# # Create a fibonacci series from 18th number turm - 5768

# In[ ]:


a = 0
b = 0
c = 1
d = 0
for i in range(0 , 17):
    d = a + b + c
    a = b
    b = c
    c = d
    print(a , end=" ")


# # wap that froms the user to enter number and stop when the user enter stop after this print min even number , max even , avg of even , min odd , max odd , avg of odd enter by the user

# In[ ]:


mineven = None
maxeven = None
sumeven = 0
counteven = 0
minodd = None
maxodd = None
sumodd = 0
countodd = 0
while True:
    numbers = input("Enter No : ")
    if numbers == "stop":
        break
    numbers = int(numbers)
    if numbers % 2 == 0:
        if mineven == None or numbers < mineven:
            mineven = numbers
        if maxeven == None or numbers > maxeven:
            maxeven = numbers
            sumeven += numbers
            counteven += 1
            avgeven = sumeven/counteven
print("mineven = " , mineven)
print("maxeven = " , maxeven)
print("sumeven = " , sumeven)
print("avgeven = " , avgeven)
#     if numbers % 2 != 0:
#         if minodd == None or numbers < minodd:
#             minodd = numbers
#         if maxodd == None or numbers > maxodd:
#                 maxodd = numbers
#                 sumodd += numbers
#                 countodd += 1
#                 avgodd = sumodd/countodd
# print("minodd = " , minodd)
# print("maxodd = " , maxodd)
# print("sumodd = " , sumodd)
# print("avgodd = " , avgodd)


# # ask the user to enter 10 scores to do follwing 1. print highest and lowest score 2. print the avg of score 3. print 2nd largest score or if any score is grater than 100 than after all score have been enter print the massage warning the user that a value over 100 is enter 4. drop the to lowest score and print he avg of the rest

# In[ ]:


highest = None
secondlarge = None
lowest = None
secondlowest = None
total = 0
count = 0
has_warning = False
for i in range(10):
    score = float(input("Enter score : "))
    if score > 100:
        has_warning = True
    if count == 0:
        highest = score
        lowest = score
    else:
        if score > highest:
            secondlarge = highest
            highest = score
        elif secondlarge == None or score > secondlarge:
            secondlarge = score
        if score < lowest:
            secondlowest = lowest
            lowest = score
        elif secondlowest == None or score < secondlowest:
            secondlowest = score
total += score
count += 1
average = total/count
print("Highest score = " , highest)
print("secondlarge score = " , secondlarge if countount > 1 else "There is no second large")
print("lowest score = " , lowest)
print("average score = " , average)
if has_warning:
    print("warning more than 100 not allowed")
if count > 2:
    totalafterdrop = total-lowest-secondlowest
    countafterdrop = count-2
    avgafterdrop = totalafterdrop/countafterdrop
    print(avgafterdrop)
else:
    print("There are not enough score")


# # Disarium Number : a number is disarium if the sum of digits rest to the position is the number is self 135 = 1^1 + 3^2 + 5^3 

# In[ ]:




