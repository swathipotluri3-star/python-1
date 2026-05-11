#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=15
print(a)
print(type(a))


# In[3]:


x=50
print(x)
print(type(x))


# In[4]:


a=7.8
print(a)
print(type(a))


# In[5]:


x=47.6
print(x)
print(type(x))


# In[6]:


a="swathi"
print(a)
print(type(a))


# In[7]:


x="kavitha"
print(x)
print(type(x))


# In[8]:


a=["mango","banana","apple"]
print(a)
print(type(a))


# In[9]:


x=["car","bike","ship"]
print(x)
print(type(x))


# In[10]:


a=(24,45,67)
print(a)
print(type(a))


# In[11]:


x=(100,1000,10000)
print(x)
print(type(x))


# In[12]:


a={2,4,6,8}
print(a)
print(type(a))


# In[13]:


x={3,5,7,9}
print(x)
print(type(x))


# In[14]:


a={
   "name":"ravi",
   "age":35,
   "qualification":"manager"
   }
print(a)
print(type(a))


# In[15]:


x={
   "name":"pavan",
   "age":20,
   "marks":79
   }
print(x)
print(type(x))


# In[16]:


age=25
print(age>=20)
print(type(age>=20))


# In[17]:


is_running = True
print(is_running)
print(type(is_running))



# In[18]:


name="kiran"
print(name)


# In[19]:


age=45
print(age)


# In[20]:


name="arun"
occupation="regional manager"
salary=60000
print(name,occupation,salary)


# In[22]:


x=56
y=92
print(x+y)


# In[23]:


print(x-y)
print(y-x)


# In[24]:


print(x*y)


# In[25]:


print(x/y)
print(y/x)


# In[26]:


print(x//y)
print(y//x)


# In[27]:


print(x%y)
print(y%x)


# In[28]:


print(x**y)
print(y**x)


# In[29]:


a=400
b=600
print(a==b)
print(b==a)


# In[30]:


print(a!=b)
print(b!=a)


# In[31]:


print(a>b)
print(b>a)


# In[32]:


print(a<b)
print(b<a)


# In[33]:


print(a>=b)
print(b>=a)


# In[34]:


print(a<=b)
print(b<=a)


# In[35]:


x=20
print(x)


# In[36]:


x=60
x+=56
print(x)


# In[37]:


x=90
x-=45
print(x)


# In[38]:


x=56
x*=23
print(x)


# In[39]:


x=99
x/=44
print(x)


# In[40]:


age=55
print(age>45 and age<35)


# In[41]:


marks=87
print(marks>90 or marks>=45)


# In[42]:


is_holiday = True
print(not is_holiday)


# In[43]:


a=["apple","grapes","banana"]
print("grapes" in a)


# In[44]:


x=["car","bike","ship"]
print("boat" not in x)
print("car" not in x)


# In[45]:


x=[40,50]
y=x
print(x is y)
print(y is x)


# In[46]:


a=[99,999]
b=[88,888]
print(a is not b)


# In[48]:


a=45
b=55
print(a&b)


# In[49]:


print(a^b)


# In[50]:


print(a<<b)


# In[51]:


print(a>>b)


# In[52]:


print(a|b)


# In[53]:


print(~b)
print(~a)


# In[54]:


age=34
if age >=18:
    print("eligible for vote")


# In[57]:


age=12
if age <=18:
        print("not eligible for vote")


# In[61]:


age=20
if age >=18:
     print("eligible")
else:
     print("not eligible")


# In[62]:


age=16
if age>=18:
         print("eligible")
else:
         print("not eligible")


# In[63]:


marks=80
if marks >= 90:
    print("A grade")
elif marks >=55:
    print("B grade")
else:
    print("fail")


# In[64]:


marks=34
if marks>=90:
    print("A grade")
elif marks >=55:
    print("B grade")
else:
    print("fail")


# In[65]:


for i in range(10,25):
    print(i)


# In[66]:


for i in range(12,33):
    print(i)


# In[67]:


for i in range(4,16,8):
    print(i)


# In[68]:


for i in range(2,22,4):
       print(i)


# In[69]:


i=2
while  i<=10:
    print(i)
    i+=3    


# In[70]:


i=5
while i<=25:
    print(i)
    i+=6


# In[4]:


import os
print(os.getcwd())


# In[ ]:




