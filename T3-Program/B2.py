#!/usr/bin/env python
# coding: utf-8

# # wap to read expenses.txt and print out all the expenses > $2000

# In[27]:


f = open(r"C:\Users\LJENG\Downloads\worked_exercises_text_files\expenses.txt")
for i in f:
    if int(i) > 2000:
        print(i , end="")


# # open the secret massage file and print the first letter of the line

# In[25]:


f = open(r"C:\Users\LJENG\Downloads\worked_exercises_text_files\secret_message.txt")
for i in f:
    print(i[0] , end=" ")


# # read the expenses file and add the 10% tax on the amount and write the new amount at the new file

# In[44]:


outputfile = open("newexpenses.txt",'w')
lines = [line.strip() for line in open("Downloads/expenses.txt")]
for item in lines:
    print('{:.2f}'.format(int(item)*1.1),file = outputfile)
print()


# # wap to find a longest word that starts and last character of the same letter wordlist file

# In[61]:


longest = 'a'
words = [line.strip() for line in open("Downloads/wordlist.txt")]
for word in words:
    if word[0] == word[-1] and len(word) > len(longest):
        longest = word
print(longest)


# # wap from the given population txt file print the countries which start with G and have population of 500000

# In[74]:


lines = [line.strip() for line in open("Downloads/population.txt")]
for line in lines:
    l = line.split('\t')
    country = l[0]
    population = int(l[1])
    if country[0] == "G" and population >= 500000:
        print(country,population)

