#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = {1,23, 49, 'abc'}
s


# In[2]:


s.update({"45", 45, 45.6})
s


# In[5]:


x = int(input("Enter a number:"))
if x > 10:
    print("> 10")
    if x > 20:
        print("> 20")
    else:
        print("<= 20")
        


# In[7]:


L = []
for i in range(10):
    L.append(i ** 2)
L


# In[10]:


S = {"apple", 4.9, "cherry"}
for x in S:
    print(x)
else:
    print("Loop completes its iteration")


# In[16]:


D = {"apple": 44, "cherry": "game"}
for x in D:
    print(x, D[x])
print('Done')


# In[18]:


def addAll(*args):
    s = 0
    for x in args:
        s += x
    return s


# In[20]:


addAll(4,5,6,6,7,8,9)


# In[26]:


def addAll2(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum


# In[27]:


addAll2(324,654,3242,5645,4564)


# In[22]:


# the arguments's order can be arbitary
def f(c2, c1, c3):
    print(c1, c2, c3)
f(c1 = "A", c2 = "B", c3 = "C")


# In[24]:


# the name and order of each arugment can be arbitary
def f( **c ):
    for x in c:
        print(x, c[x])
f(c1 = "A", c2 = "B", c3 = "C")
# watch {c1 = "A", c2 = "B", c3 = "C"} as a dictionary


# In[28]:


f(a = "cc", m1 = 45, c = "adv", z =45.6)


# In[29]:


def g(t=0):
    print(t)


# In[31]:


g()


# In[32]:


g(10)


# In[33]:


def printList(L=[]):
    """This function prints the list of elements
       The input is a list and default is empty list."""
    for x in L:
        print(x)


# In[34]:


printList([12,45,"abc", 45.6])


# In[ ]:




