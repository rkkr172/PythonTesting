#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1.) Constructing Tuples
2.) Basic Tuple Methods
3.) Immutability
4.) When to Use Tuples

Tuples: tuples are very similar to lists. However they have one key difference- immutability. 
Once a element is inside tuples, it can’t be reassigned. 
Tuples are in parenthesis (1,2,3).
"""

#1.) Constructing Tuples
t = (1,2,3,1,5,6)
print(t)
print(type(t))

#number of times a value appears
print(t.count(1))   # gives 2
print(t.count(5))   # gives 1

#Input number and return the index
print(t.index(1))   # gives 0
print(t.index(6))   # gives 5

#3.) Immutability
#t[0] = 'change'        #'tuple' object does not support item assignment
#t = t.append('one')    #'tuple' object has no attribute 'append'

#4.) When to Use Tuples
"""
="Why bother using tuples when they have fewer available methods?"=
To be honest, tuples are not used as often as lists in programming,
but are used when immutability is necessary. If in your program you are 
passing around an object and need to make sure it does not get changed,
then a tuple becomes your solution. 
It provides a convenient source of data integrity.
"""
