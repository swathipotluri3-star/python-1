# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:04:32 2026

@author: swath
"""

#CONDITIONAL STATEMENTS
IF
age=34
if age >=18:
    print("eligible for vote")
    
    age=12
    if age <=18:
        print("not eligible for vote")
        
        
 IF ELSE
 age=20
 if age >=18:
     print("eligible")
 else:
     print("not eligible")
     
     age=16
     if age>=18:
         print("eligible")
     else:
         print("not eligible")
         
IF ELIF ELSE
marks=80
if marks >= 90:
    print("A grade")
elif marks >=55:
    print("B grade")
else:
    print("fail")
        
marks=34
if marks>=90:
    print("A grade")
elif marks >=55:
    print("B grade")
else:
    print("fail")
    
    
#LOOPING STATEMENTS
FOR LOOP
for i in range(10,25):
    print(i)
    
 for i in range(12,33):
    print(i)
    
for i in range(4,16,8):
    print(i)
    
 for i in range(2,22,4):
        print(i)
        
#WHILE LOOP
i=2
while  i<=10:
    print(i)
    i+=3    
i=5
while i<=25:
    print(i)
    i+=6
    
i=4
while i<=20:
    print(i)
    i-=3
    
i=1
while i<=4:
    print(i)
    i-=2