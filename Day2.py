#!/usr/bin/env python
# coding: utf-8

# # DAY 2

# syllabus - input, print, variables , repl it

# # inupt()

# In[1]:


input("Enter anything")


# # Variables

# variables are containers for storing data values

# variable_name = value

# In[11]:


x = 5
print(x)
type(x)


# In[5]:


y = "Hello"


# ## Casting
if you want to specify the data type of a variable
# In[6]:


x = int(5)
y = float(3)
z = str(3)

type() - used to getting data type
# In[7]:


type(x)


# In[8]:


type(y)


# In[9]:


type(z)


# In[10]:


a = 3
type(a)


# ## Case Sensitive

# In[12]:


b = 45
B="Musthafa"

print(b)
print(B)


# ## Assign Multiple Values

# In[13]:


x,y,z = "Apple","Orange","Banana"


# In[15]:


y


# # Output

# print()

# In[17]:


print(x)


# In[19]:


print("I need "+x)


# In[20]:


print("I need "+a)


# In[21]:


print("i need",a)


# # Global Variable

# In[23]:


x = "Good"

def myfun():
    print("Python is "+x)
    
myfun()


# In[24]:


y = "awesome"

def fun1():
    y = "fantastic"
    print("python is "+y)

fun1()

print("python is "+y)


# # Data Types

# Numbers

# int,float & complex

# In[28]:


x = 5
y = 33.5
z = 1+2j


# In[29]:


print(type(x))
print(type(y))
print(type(z))


# Type Conversion

# In[30]:


t = 1

type(t)


# In[35]:


t = float(t)
print(t)
print(type(t))


# Strings 

# string = ''or ""

# In[36]:


x = "Hello"
y = 'World'


# In[37]:


type(x)


# In[38]:


type(y)


# Multi line string

# In[39]:


cucek ='''Cochin University college of engineerig Kuttanad,
         Pulincunnoo
        Alappuzha 673000'''


# In[41]:


print(cucek)


# len() - to find string length

# In[42]:


print(len(x))


# In[44]:


txt = "the best things in life are free"

print("free" in txt)


# Boolean - True, false

# In[45]:


print(10>9)


# In[46]:


print(10<9)


# input() - default data type string

# In[47]:


x = input("Enter anything")


# In[48]:


x


# In[49]:


type(x)


# In[50]:


y = input()


# In[51]:


type(y)


# In[52]:


x = input("Enter 1st")
y = input("Enter 2nd")


# In[53]:


x+y


# In[54]:


type(x+y)


# In[56]:


x = int(input("enter first"))
y = int(input("enter second"))


# In[57]:


x+y


# In[58]:


print(x,y)


# In[59]:


print(x,"is Greater than ",y)


# In[60]:


x = input("Enter 1st")
y = input("Enter 2nd")


# In[62]:


print(x+"is Greater than "+y)


# In[ ]:




