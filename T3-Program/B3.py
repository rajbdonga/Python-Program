#!/usr/bin/env python
# coding: utf-8

# # wap to count the words to and the present file name python.txt 

# In[ ]:


f = open("Desktop/python.txt")
thecount = 0
tocount = 0
lines = [line.strip() for line in f]
for i in lines:
    if 'the' in i.lower():
        thecount += 1
    if 'to' in i.lower():
        tocount += 1
print("how many 'the' count for python file :",thecount)
print("how many 'to' count for python file :",tocount)
print("how many the 'total count letter' python file :",(thecount+tocount))


# # wap to ask user for the input of name and age and write this details into a file 

# In[ ]:


Name = input("Enter the name :")
Age = input("Enter the age :")
with open("student.txt",'w') as file:
    file.write(Name)
    file.write(Age)


# # wap to read lines from the file1 and file2 and murge them in file3

# In[ ]:


def merge(file1 , file2 , file3):
    with open(file1) as file1 , open(file2) as file2 , open(file3 , 'w') as file3:
        for line in file1:
            file3.write(line)
        for line in file2:
            file3.write(line)
merge("file1.txt","file2.txt","file3.txt")


# # wap to write a pager program lot solution should from for a file name and then display 25 line at a time and asking the user to continue the next 25 line and enter the word stop to the close file

# In[ ]:


def word(file):
    count = 0
    for i in file:
        count += 1
        print(i)
        if count == 25:
            break
    n = input("Enter the Continue or Stop :")
    if n == 'continue':
        word(file)
    else:
        print(n)
word(open("Downloads/wordlist.txt"))


# # wap that read a file and create a new file with all character is capitalized

# In[ ]:


f = open("Downloads/wordlist.txt")
f.read().upper()


# # wap to reverse the content of one file and store and it is second file also covert the content of the second file to upper case and store in third file and count the num of vowels in third file

# In[ ]:


with open("Downloads/wordlist.txt") as file , open("f4.txt" , 'a') as f4 , open("f5.txt" , 'a') as f5:
    s = ""
    count = 0
    for i in file:
        s = i[::-1]
        f4.write(s)
    f4 = open("f4.txt")
    for j in f4:
        f5.write(j.upper())
        if 'a' in j or 'e' in j or 'i' in j or 'o' in  j or 'u':
            count += 1
    print(count)

