# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:17:33 2026

@author: swath
"""

1.INTEGER
a=15
print(a)
print(type(a))

x=50
print(x)
print(type(x))

2.FLOAT
a=7.8
print(a)
print(type(a))

x=47.6
print(x)
print(type(x))

3.STRING
a="swathi"
print(a)
print(type(a))

x="kavitha"
print(x)
print(type(x))

4.LIST
a=["mango","banana","apple"]
print(a)
print(type(a))

x=["car","bike","ship"]
print(x)
print(type(x))


5.TUPLE
a=(24,45,67)
print(a)
print(type(a))

x=(100,1000,10000)
print(x)
print(type(x))


6.SET
a={2,4,6,8}
print(a)
print(type(a))

x={3,5,7,9}
print(x)
print(type(x))

7.DICTIONARY
a={
   "name":"ravi",
   "age":35,
   "qualification":"manager"
   }
print(a)
print(type(a))

x={
   "name":"pavan",
   "age":20,
   "marks":79
   }
print(x)
print(type(x))

8.BOOLEAN
age=25
print(age>=20)
print(type(age>=20))

is_running = True
print(is_running)
print(type(is_running))

VARIABLES
name="kiran"
print(name)

age=45
print(age)

name="arun"
occupation="regional manager"
salary=60000
print(name,occupation,salary)

OPERATORS
#ARITHMETIC OPERATORS
ADDITION
x=56
y=92
print(x+y)

SUB
print(x-y)
print(y-x)

MULTI
print(x*y)

DIVISION
print(x/y)
print(y/x)

FLOOR DIVISION
print(x//y)
print(y//x)

MOD
print(x%y)
print(y%x)

EXPO
print(x**y)
print(y**x)


#COMPARISON OPERATORS
a=400
b=600
EQUAL TO
print(a==b)
print(b==a)

NOT EQUAL
print(a!=b)
print(b!=a)

GREATER THAN
print(a>b)
print(b>a)

LESS THAN 
print(a<b)
print(b<a)

GREATER THAN OR EQUAL
print(a>=b)
print(b>=a)

LESS THAN OR EQUAL
print(a<=b)
print(b<=a)


#ASSIGNMENT OPERATORS
x=20
print(x)

x=60
x+=56
print(x)

x=90
x-=45
print(x)

x=56
x*=23
print(x)

x=99
x/=44
print(x)


#LOGICAL OPERATORS
age=55
print(age>45 and age<35)

marks=87
print(marks>90 or marks>=45)

is_holiday = True
print(not is_holiday)


#MEMBERSHIP OPERATORS
a=["apple","grapes","banana"]
print("grapes" in a)

x=["car","bike","ship"]
print("boat" not in x)
print("car" not in x)


#IDENTITY OPERATORS
x=[40,50]
y=x
print(x is y)
print(y is x)

a=[99,999]
b=[88,888]
print(a is not b)


#BITWISE OPERATORS
AND
a=45
b=55
print(a&b)

XOR
print(a^b)

LEFT SHIFT
print(a<<b)

RIGHT SHIFT
print(a>>b)

OR
print(a|b)

NOT
print(~b)
print(~a)
