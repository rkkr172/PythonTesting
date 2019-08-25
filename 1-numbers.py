#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pros and Cons of Dynamic Typing
Pros of Dynamic Typing
	- very easy to work with
	- faster development time
Cons of Dynamic Typing
	- may result in unexpected bugs!
	- you need to be aware of type()
"""

"""
a=9;b=4
#print("Addition -{}".format(a+b))
#print("Substraction -{}".format(a-b))
#print("Muliplication -{}".format(a*b))
#print("Division -{}".format(a/b))
#print("Floor Division -{}".format(a//b))

#Modulo
#print("Modlus -{}".format(10%2))
#print("Remainder of {} & {} is {}".format(10,3,10%3))
#print("Power -{}".format(2**3))

# int, float, str, list [], tuple (), dict {}, set, bool

w = ['a','b','c']   # List
x = (1,2,3)         # Tuple
y = {'k1','k2'}     # Set
z = {'k1':'v1','k2':'v2'} # Dictionary
print(type(w))
print(type(x))
print(type(y))
print(type(z))
print(type(5))
print(type(5.5))
print(type('hello'))
#print(type(10))
"""

def sal_cal(rate,days):
    per_day_rate=rate
    total_days=days
    wages=per_day_rate*total_days
    return wages

while True:
    try:
        r=float(input("Rate of wages per day -: "));
    #except ValueError:  print("Please, retry rate in number only");
    except:
        print("Please input Ruppes of per Day ");
    else:
        break;
    
while True:
    try:
        d=int(input("Total no. of working days -: "))
    except:
        print("Retry, toatal no. of workings Days");
    else:
        break;
    
sal=float(sal_cal(r,d))
print(f"Total Salary is : {sal}")

#"""

