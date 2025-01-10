#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# single inheritance

class Person:
    def __init__(self , name):
        self.name = name
    def show(self):
        print(f'{self.name} is a python teacher')
class Professor(Person):pass
per = Person("Rossum")
per.show()
pro = Professor("van")
pro.show()


# In[ ]:


# multiple inheritance

class Person:
    def __init__(self , name):
        self.name = name
    def show(self):
        print(f'{self.name} is a python teacher')
class Teacher:
    def credit(self):
        print("he teaches python")
class PythonProgramer(Person,Teacher):pass
p1 = PythonProgramer("van")
p1.show()
p1.credit()


# In[ ]:


# multi-level inheritance

class Human:
    def __init__(self , name):
        self.name = name
    def show(self):
        print(f'{self.name} is a teacher')
class Person(Human):pass
class Professor(Person):pass
p = Professor('james')
p.show()


# In[ ]:


# hierarchical inheritance

class Human:
    def __init__(self , name):
        self.name = name
    def show(self):
        print(f'{self.name} is a teacher')
class PythonProgrammer(Human):pass
class JavaProgrammer(Human):pass
p3 = PythonProgrammer('Rossum')
p3.show()


# In[ ]:


# method overriding

class Father:
    def __init__(self):
        self.money = 1000
        print("father class constructor")
    def show(self):
        print("father instance method")
class Son(Father):
    def show(self):
        print("son instance method")
s = Son()
s.show()


# In[ ]:


# constructor overriding

class Father:
    def __init__(self):
        self.money = 1000
        print("father class constructor")
    def show(self):
        print("father instance method")
class Son(Father):
    def __init__(self):
        self.money = 5000
        self.car = "BMW"
        print("son class constructor")
    def disp(self):
        print("son instance method")
s = Son()
print(s.money)
print(s.car)
s.disp()
s.show()


# In[5]:


# Implement the following hierarchy . The Book class has name, n (number of authors), authors (list of authors),
# publisher, ISBN, and year as its data members and the derived class has course as its data member. The derived class
# method overrides (extends) the methods of the base class.

class Book:
    def __init__(self , name , n_authors , authors , publisher , isbn , year):
        self.name = name
        self.n_authors = n_authors
        self.authors = authors
        self.publisher = publisher
        self.isbn = isbn
        self.year = year
    def disp(self):
        print(f"Name : {self.name}")
        print(f"No of authors : {self.n_authors}")
        print(f"Authors : {','.join(self.authors)}")
        print(f"Publisher : {self.publisher}")
        print(f"ISBN : {self.isbn}")
        print(f"Year : {self.year}")
class DerivedBook(Book):
    def __init__(self , name , n_authors , authors , publisher , isbn , year , course):
        super().__init__(name , n_authors , authors , publisher , isbn , year)
        self.course = course
    def disp(self):
        super().disp()
        print(f"Course : {self.course}")


# In[6]:


bt = DerivedBook("Python" , 1 , ['John'] , "TechPub" , 97832 , 2025 , "CSE")
bt.disp()


# In[7]:


# Implement the following hierarchy . The Staff function has name and salary as its data members, the derived class
# Teaching has subject as its data member and the class NonTeaching has department as its data member. The derived class
# method overrides (extends) the methods of the base class.

class Staff:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
    def disp(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")
class Teaching(Staff):
    def __init__(self , name , salary , subject):
        super().__init__(name , salary)
        self.subject = subject
    def disp(self):
        super().disp()
        print(f"Subject : {self.subject}")
class NonTeaching(Staff):
    def __init__(self , name , salary , dept):
        super().__init__(name , salary)
        self.dept = dept
    def disp(self):
        super().disp()
        print(f"Dept : {self.dept}")


# In[8]:


bt = Teaching("Raj" , 100000 , "Python")
bt.disp()


# In[12]:


# Create a class called Student, having name and email as its data members and _init_(self, name, email) and putdata(self) as
# bound methods. The _init_ function should assign the values passed as parameters to the requisite variables. The putdata
# function should display the data of the student. Create another class called PhDguide having name, email, and students as
# its data members. Here, the students variable is the list of students under the guide. The PhDguide class should have four
# bound methods: _init_, putdata, add, and remove. The _init_ method should initialize the variables, the putdata should
# show the data of the guide, include the list of students, the add method should add a student to the list of students of the
# guide and the remove function should remove the student (if the student exists in the list of students of that guide) from
# the list of students.

class Student:
    def __init__(self , name , email):
        self.name = name
        self.email = email
    def putdata(self):
        print(f"Name : {self.name}")
        print(f"Email : {self.email}")
class Phdguide(Student):
    def __init__(self , name , email):
        self.name = name
        self.email = email
        self.students = []
    def putdata(self):
        print(f"Name : {self.name}")
        print(f"Email : {self.email}")
        print("Students under phdguide")
        for student in self.students:
            student.putdata()
            print("--------")
    def add(self , student):
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} added")
    def remove(self , s):
        if student in self.students:
            self.students.remove(student)
            print(f"{student.name} removed")
        else:
            print("Student not found")


# In[2]:


s1 = Student("raj" , "a@gmail.com")
s2 = Student("rajdonga" , "abcd@gmail.com")
guide = Phdguide("Dr.smit" , "sm@gmail.com")
guide.add(s1)
guide.add(s2)
guide.putdata()
guide.remove(s1)
guide.putdata


# In[7]:


# Method Resolution Order

class A:
    def process(self):
        print('A process')
class B:
    def process(self):
        print('B process')
class C(B,A):
    pass

c = C()
c.process()
C.mro()


# In[10]:


# Method Resolution Order

class A:
    def process(self):
        print('A process')
class B(A):
    pass
class C(A):
    def process(self):
        print('C process')
class D(B,C):
    pass

c = D()
c.process()
D.mro()


# # FROM PYTHON 3 VERSION THE MRO IN CASE OF INHERITANCE IS DECIDED BY C3 LINEARLIZATION ALGORITHAM

# # It defines the mro of any class c as the sum of c and murge of linear of class and the list of parents 

# In[ ]:


# the steps for merge are as follow take the head of first list , if the head is not of any other list then add it to the
# linearlization of c and remove it from the merge otherwise look at the head of the next list and take it based on above 
# condition repeat the process untill all classes are removed


# In[17]:


class F: pass
class E: pass
class D: pass
class C(D,F): pass
class B(D,E): pass
class A(B,C): pass
A.mro()


# In[16]:


class A: pass
class B: pass
class C(A,B): pass
class D(B,A): pass
class X(C,D): pass


# In[ ]:


# a class derive from abc class belongs the abc module is known as abstract class in python
# abc class defines behaviour from author classes
# abstract class can have abstract methods and concrit methods
# abstract class neads to be extended and impliment
# you can not create objects on abstract class


# In[ ]:


Rules : if there in as abstract method in a class that class must be abstract 
    
        if you are in inheriting in abstratct class that have abstract methods you must either provide 
            the implimentation or make this class abstract


# In[1]:


from abc import ABC, abstractmethod
class Defence(ABC):
    def __init__(self):
        self.id = 101
        
    @abstractmethod
    def area(self): pass
    def gun(self): print("GUN-AK47")
class Army(Defence):
    def area(self): print("land area")
class Airlines(Defence):
    def area(self): print("sky area")
class Navy(Defence):
    def area(self): print("sea area")
a = Army()
a.gun()
a.area()


# In[19]:


# overloading

class Fraction:
    def __init__(self , x , y):
        self.num = x
        self.den = y
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __add__(self , other):
        newnum = self.num * other.den + other.num * self.den
        newden = self.den * other.den
        return f"{newnum}/{newden}"
    def __sub__(self , other):
        newnum = self.num * other.den - other.num * self.den
        newden = self.den * other.den
        return f"{newnum}/{newden}"
    def __mul__(self , other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return f"{newnum}/{newden}"
    def __truediv__(self , other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return f"{newnum}/{newden}"
    def convert_decimal(self):
        return f"{self.num}/{self.den}"
f1 = Fraction(1,2)
f2 = Fraction(1,3)
print(f1)
print(f2)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)


# In[20]:


# Create an abstract class named Shape. 
# Create an abstract method named calculate_area for the Shape class.
# Create Two Classes named Rectangle and Circle which inherit Shape class.
# Create calculate_area method in Rectangle class. It should return the area of the rectangle object. (area of rectangle = 
# (length * breadth))
# Create calculate_area method in Circle class. It should return the area of the circle object.
# (area of circle =πr^2))
# Create objects of Rectangle and Circle class.
# The python Program Should also check whether the area of one Rectangle object is greater
# than another rectangle object by overloading > operator.
# Execute the method resolution order of the Circle class. 

from abc import ABC, abstractmethod
class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(shape):
    def __init__(self , l , w):
        self.l = l
        self.w = w
    def calculate_area(self):
        area = self.l * self.w
class Circle(shape):
    def __init__(self , r):
        self.r = r
    def calculate_area(self):
        area = 3.14 * self.r ** 2


# In[3]:


get_ipython().run_line_magic('timeit', 'sum(range(100000))')


# In[6]:


import numpy as np
get_ipython().run_line_magic('timeit', 'np.sum(np.arange(100000))')


# In[6]:


import numpy as np
l = np.array([1,2,3])
print(l)
type(l)


# In[17]:


import numpy as np
b = np.array([[1,2,3],[4,5,6]])
print(b)


# In[21]:


a = np.array([1,2,3],dtype=bool)
print(a)
c = np.array([1,2,3],dtype=float)
print(c)


# In[32]:


s = np.arange(3)
print(s)
t = np.arange(3,11)
print(t)
d = np.arange(3,11,2)
print(d)
n = np.arange(11,3,-1)
print(n)


# In[34]:


np.arange(1,11)


# In[38]:


np.arange(1,11).reshape(2,5)


# In[39]:


np.arange(1,11).reshape(5,2)


# In[44]:


np.arange(1,17).reshape(2,2,2,2)


# In[46]:


np.arange(1,10).reshape(3,3)


# In[47]:


np.arange(1,9).reshape(2,2,2)


# In[49]:


np.ones((3,4),dtype=int)


# In[51]:


np.zeros((3,4),dtype=int)


# In[79]:


a1 = np.arange(10,dtype=np.int32)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)
print(a1)
print(a2)
print(a3)
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)
print(a1.shape)
print(a2.shape)
print(a3.shape)
print(a1.size)
print(a2.size)
print(a3.size)
print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)
print(a1 + 2)
print(a1 - 2)
print(a1 * 2)
print(a1 / 2)
print(a1 // 2)
print(a1 ** 2)
print(a1 == 5)
print(a1 > 5)
print(a1 > a2)


# In[70]:


np.ones((4,3,2))


# In[86]:


a4 = np.arange(1,10).reshape(3,3)
print(a4)
for i in np.nditer(a4):
    print(i,end=" ")


# In[95]:


j = np.arange(6).reshape(2,3)
f = np.arange(6,12).reshape(2,3)
print(j)
print(f)
print(np.concatenate((j,f),axis=0))
print(np.concatenate((j,f),axis=1))


# In[ ]:




