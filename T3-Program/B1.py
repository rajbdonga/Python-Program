#!/usr/bin/env python
# coding: utf-8

# In[34]:


f = open("Desktop/name.txt",encoding="utf-8")
f.read()
f.mode
f.close()


# In[40]:


get_ipython().run_cell_magic('writefile', 'sample.txt', 'hi\nhello\nwelocme python')


# In[47]:


f = open("sample.txt")
f.read(3)
f.close()
f.closed


# # read line method - read a line from the given text 

# In[49]:


f = open("sample.txt")
f.readline()


# In[51]:


f = open("sample.txt")
f.readline()
f.readline()


# In[52]:


f = open("sample.txt")
f.readline()
f.readline()
f.readline()


# In[53]:


f = open("sample.txt")
f.readline()
f.readline()
f.readline()
f.readline()


# # read lines method - return the list of entire text lines 

# In[72]:


f = open("sample.txt")
f.readlines(3)


# In[80]:


f = open("Desktop/Swami.txt")
for i in f:
    for j in i.split():
        print(j)


# # this method write containt to the file in right moad if the file is present the containt will be over written if the file is not present then the new file will be created 

# In[87]:


f = open("Desktop/name1.txt",'w')
f.write("raj donga")
f.close()


# In[95]:


f = open("Desktop/name1.txt",'w')
f.re
f.writable()
f.name


# # writelines - this method take and input of list of strings and write on the file 

# In[96]:


f = open("new.txt",'w')
f.writelines(["hi\n" , "hello"])
f.close()


# In[105]:


with open("hi.txt") as f:
    for i in f:
        print(f)
f.closed


# # tell method - this method returns the current possition of the read write pointer within a given file

# In[110]:


f = open("sample.txt")
f.read(2)
f.tell()
f.read(3)
f.tell()
f.readlines()


# # seek(offset [whence]) - this method set the file current possition at the offset the whence argument has three value 0 , 1 , 2 /// 0 means default start of stream , 1 means current possition , 2 means end of the stream  

# In[111]:


f = open("sample.txt")
f.read(3)
f.read()
f.seek(0)
f.read()


# # wap to count number of word , space and character 

# In[135]:


space = 0
word = 1
ch = 0
f = open("sample.txt")
data = f.read()
for count in data:
    ch += 1
    if count == '':
        space += 1
    if count == '' or count == '\n':
        word += 1
print("space is:", space)
print("word is:" , word)
print("ch is:" , ch)


# In[145]:


words = [line.strip() for line in open("Desktop/wordlist.txt")]
print(words)

